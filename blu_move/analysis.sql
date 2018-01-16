
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



-- 4. dev utilization   (hour)
# hour of using / 24 hour for each car 


WITH get_last_log AS
  (SELECT b.start_reservation AS start_reservation_,
          b.end_reservation,
          b.*,
          ROW_NUMBER() OVER (PARTITION BY id,
                                          date(date_of_insert)
                             ORDER BY date(date_of_insert),
                                      date_of_insert DESC) AS row_id,
                            ROW_NUMBER() OVER (PARTITION BY id,
                                                            start_reservation
                                               ORDER BY date_of_insert DESC) AS row_id_
   FROM <table_name> b
   WHERE start_reservation IS NOT NULL
     AND end_reservation IS NOT NULL )
SELECT *
FROM get_last_log
WHERE row_id = 1
  AND row_id_ = 1
ORDER BY id,
         start_reservation_,
         row_id_


