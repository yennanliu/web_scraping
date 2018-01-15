
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


-- 1. utilization  
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



