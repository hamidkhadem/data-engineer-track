-- Includes:
--  External Tables
--  Loading data
--  Storing Formats

-- External Table
CREATE EXTERNAL TABLE company.employees_external (
 id int,
 first_name string,
 last_name string,
 age int,
 gender string )
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION '/user/zaka/employees_data';

-- select data
SELECT * FROM company.employees_external;

-- drop the table, and notice
DROP TABLE company.employees_external;


-------------Storing Formats---------
-- Specify storing format
CREATE TABLE company.employees_prq (
 id int,
 first_name string,
 last_name string,
 age int,
 gender string )
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS PARQUET;

-- Insert into table
INSERT INTO company.employees values(200,'Zaka','student',23,'M');

-- check HDFS path


-------------LOADING DATA---------
-- Load File into table
LOAD DATA INPATH '/user/zaka/employees_data/employess_data.csv' INTO TABLE company.employees;

-- check hdfs path
-- $ hdfs dfs -ls /user/hive/warehouse/emp.db/employee/

-- LOAD CSV File from the LOCAL filesystem
LOAD DATA LOCAL INPATH '/home/<local_path>/employess_data.csv' INTO TABLE company.employees;

-- using OVERWRITE
LOAD DATA INPATH '/user/zaka/employees_data/employess_data.csv' OVERWRITE INTO TABLE company.employees;
