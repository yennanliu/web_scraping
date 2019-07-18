
-- 1. Duration period 
-- get duration period (minute) per booking per car 

SELECT id,
       end_reservation,
       start_reservation,
       EXTRACT (epoch
                FROM (end_reservation - start_reservation))::integer/60 AS duration_min
FROM
  (SELECT DISTINCT id,
                   end_reservation,
                   start_reservation
   FROM <table_name>
   WHERE end_reservation IS NOT NULL
     AND start_reservation IS NOT NULL ) sub
ORDER BY id,
         end_reservation


-- 2. utilization   (day)
-- get utilization per day 



WITH booking AS
  (SELECT date(start_reservation) AS date,
          count(DISTINCT id) AS booked_car
   FROM <table_name>
   GROUP BY 1),
     all_ AS
  (SELECT date(date_of_insert) AS date,
          count(DISTINCT id) AS all_car
   FROM <table_name>
   GROUP BY 1)
SELECT booking.*,
       all_.all_car,
       booking.booked_car::NUMERIC/all_.all_car::NUMERIC AS utilization
FROM booking
INNER JOIN all_ ON booking.date = all_.date
ORDER BY booking.date



-- 3. utilization   (hour)
-- get utilization per hour 


WITH booking AS
  (SELECT TO_TIMESTAMP(cast(start_reservation AS TEXT),'yyyy-mm-dd HH24') AS date,
          count(DISTINCT id) AS booked_car
   FROM <table_name>
   GROUP BY 1),
     all_ AS
  (SELECT TO_TIMESTAMP(cast(date_of_insert AS TEXT),'yyyy-mm-dd HH24') AS date,
          count(DISTINCT id) AS all_car
   FROM <table_name>
   GROUP BY 1)
SELECT booking.*,
       all_.all_car,
       booking.booked_car::NUMERIC/all_.all_car::NUMERIC AS utilization
FROM booking
INNER JOIN all_ ON booking.date = all_.date
ORDER BY booking.date



-- 4.  utilization  (using hour / 24 hour)
### fix the "duration across day problem"
### e.g. start : 2017-01-01 23:00, end : 2017-01-02 07:00 
# hour of using / 24 hour for each car  (V1)


WITH dates AS
  ( SELECT DISTINCT generate_series(min(b.start_reservation::date) OVER (PARTITION BY b.id)::TIMESTAMP, now()::date - '1 day'::interval, '1 day'::interval)::date AS date,
                    b.id,
                    24 AS capacity_hours,
                    1 AS capacity_days
   FROM rw.blue_move b
   WHERE date(b.start_reservation) >= '2018-01-12' ),
     get_last_log AS
  (SELECT b.*,
          ROW_NUMBER() OVER (PARTITION BY id,
                                          date(date_of_insert)
                             ORDER BY date(date_of_insert),
                                      date_of_insert DESC) AS row_id,
                            ROW_NUMBER() OVER (PARTITION BY id,
                                                            start_reservation
                                               ORDER BY date_of_insert DESC) AS row_id_
   FROM rw.blue_move b
   WHERE start_reservation IS NOT NULL
     AND end_reservation IS NOT NULL )
SELECT d_1.date,
       last_log.id,
       last_log.start_reservation,
       last_log.end_reservation,
       CASE
           WHEN last_log.start_reservation < d_1.date
                AND last_log.end_reservation::date > d_1.date THEN 24::double precision
           WHEN last_log.start_reservation < d_1.date THEN date_part('hour'::text, last_log.end_reservation) + date_part('minute'::text, last_log.end_reservation) / 60::double precision
           WHEN last_log.start_reservation::date = d_1.date
                AND last_log.end_reservation::date > d_1.date THEN date_part('epoch'::text, d_1.date + '1 day'::interval - last_log.start_reservation) / 3600::double precision
           WHEN last_log.start_reservation::date = d_1.date
                AND last_log.end_reservation::date = d_1.date THEN date_part('epoch'::text, last_log.end_reservation - last_log.start_reservation) / 3600::double precision
           ELSE 0::double precision
       END AS service_hours
FROM get_last_log last_log
RIGHT JOIN dates d_1 ON (last_log.start_reservation::date <= d_1.date
                         AND last_log.end_reservation::date >= d_1.date
                         OR last_log.start_reservation::date = d_1.date)
AND d_1.id::text = last_log.id::text
WHERE row_id = 1
  AND row_id_ = 1
ORDER BY id,
         start_reservation, date















