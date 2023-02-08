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
LOCATION '/user/hive/data/employess_data_external';

-- select data
SELECT * FROM company.employees;

-- drop the table, and notice


-------------LOADING DATA---------
-- Load File into table
LOAD DATA INPATH '/user/hive/data/employess_data.csv' INTO TABLE company.employees;

-- check hdfs path
-- $ hdfs dfs -ls /user/hive/warehouse/emp.db/employee/

-- LOAD CSV File from the LOCAL filesystem
LOAD DATA LOCAL INPATH '/home/<local_path>/employess_data.csv' INTO TABLE company.employees;

-- using OVERWRITE
LOAD DATA INPATH '/user/hive/data/employess_data.csv' OVERWRITE INTO TABLE company.employees;



-------------Storing Formats---------
-- Specify storing format
CREATE EXTERNAL TABLE students(
    id int,
    first_name string,
    last_name string,
    class string)
STORED AS PARQUET;

-- check HDFS path

