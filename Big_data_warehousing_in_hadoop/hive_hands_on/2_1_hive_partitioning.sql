-- Includes:
--  Partitioning
--  Spark Integration

-- Use Database
USE company;

-- Create table with partitioning
CREATE TABLE company.employees_part (
 id int,
 first_name string,
 last_name string,
 age int)
PARTITIONED BY(gender string)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ',';

LOAD DATA INPATH '/<hdfs_path>/employees_data.csv' INTO TABLE company.employees_part;

-- Show partitions
SHOW PARTITIONS company.employees_part;

-- See partitions in HDFS

-- Drop Hive Partition
ALTER TABLE company.employees_part DROP IF EXISTS PARTITION (gender='M');

-- Bucketing
CREATE TABLE company.employees_part (
 id int,
 first_name string,
 last_name string,
 age int)
PARTITIONED BY(gender string)
CLUSTERED BY (last_name) INTO 32 BUCKETS
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ',';