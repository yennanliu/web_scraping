# http://www.codedata.com.tw/database/mysql-tutorial-13-stored-routines/

# https://www.a2hosting.co.uk/kb/developer-corner/mysql/mysql-stored-functions-and-procedures

#  stored function
DELIMITER $$
CREATE FUNCTION plus(temp_max FLOAT, temp_min FLOAT) RETURNS DECIMAL(9,2)
BEGIN
  DECLARE tem__ DECIMAL(9,2);
  SET tem__ = temp_max + temp_min;
  RETURN tem__;
END$$
DELIMITER ;


# sql 
SELECT *, plus(temp_max,temp_min) AS tem_test FROM weather_data;


#  stored function
DELIMITER $$
CREATE PROCEDURE procedureTest()
BEGIN
  SELECT CET FROM weather_data;
END$$
DELIMITER ;

# execute 
CALL procedureTest() \G
