-- Create databse
CREATE DATABASE IF NOT EXISTS company;

-- Show databases
SHOW DATABASES;

-- Use Database
USE company;

-- Describe database
DESCRIBE DATABASE company;
DESCRIBE SCHEMA company; 
DESCRIBE DATABASE EXTENDED company;
DESCRIBE SCHEMA EXTENDED company;

-- Create Tables
CREATE TABLE IF NOT EXISTS company.employees (
 id int,
 first_name string,
 last_name string,
 age int,
 gender string )
COMMENT 'Employees Table'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ',';

-- Show Tables
SHOW TABLES;

-- Describe Tables
DESCRIBE FORMATTED employees;
DESCRIBE EXTENDED employees;

-- select data
SELECT * FROM company.employees;

-- Insert into table
INSERT INTO company.employees values(200,'Zaka','student',23,'M');

-- select data
SELECT * FROM company.employees;

