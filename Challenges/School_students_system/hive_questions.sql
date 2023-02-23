-- Create "school" database


-- Create a table "students" without partition stored in textfile


-- Check database and table created in hdfs

-- Upload data files into hdfs://users/<your_user>/students_data/


-- Load students_data.csv into the table


-- select the first 10 rows to observe the loaded data


-- find the total records count, and observe the map-reduce process info in Hive


-- create a new table "students_part" partitioned by column gender and state.


-- set your hive to accept dynamic partitions


-- Load data into students_part by reading data from students table


-- Notice the partitioned data in hdfs in path


-- Do two counting queries for Females who live in 'AZ' state from both tables (students, students_part)


-- Notice the big time differece from the unpartitioned and partitioned tables
-- and write down the time calculated by hive for each query
--  unpartitioned:  
--  partitioned:    


-- Create and store partitioned data as PARQUET format in a new table "students_prq"


-- Load data into students_prq by reading data from students table


-- Notice the difference in size in the stored data in hdfs
--  36988 /user/hive/warehouse/school.db/students_part/gender=F/state=AZ/000000_0
--  19984 /user/hive/warehouse/school.db/students_prq/gender=F/state=AZ/000000_0


-- Create a new table "voting_eligibile"


-- Load LOCAL "voting_eligibile_students.csv" file into the table


-- join tables students_prq and voting_eligibile on the name column, 
-- and select the distinct names from the students_prq, and the registration from the voting_eligibile
-- to see if any matches and show the first 10 rows


-- BONUS: find every state's students who keep the highest GPA among their state's students.
