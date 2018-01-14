
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