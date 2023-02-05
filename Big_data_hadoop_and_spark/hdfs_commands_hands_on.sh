# Checking hdfs health
hdfs fsck /

# hdfs listing help commands
hdfs dfs -help

# hdfs listing files with parameters
hdfs dfs -ls -t -r /user/zaka/

# Make new directory
hdfs dfs -mkdir /user/zaka/first_data

# Remove empty directory
hdfs dfs -rmdir /user/zaka/first_data

# Copy files from local to hdfs
hdfs dfs -put Desktop/file* /user/zaka/
#or
hdfs dfs -copyFromLocal Desktop/file* /user/zaka/

# Copy from hdfs to local
hdfs dfs -get /user/zaka/file* Desktop/test_data/
#or
hdfs dfs -copyToLocal /user/zaka/file* Desktop/test_data/

# Copy files inside hdfs
hdfs dfs -mkdir /user/zaka/test_data/
hdfs dfs -cp /user/zaka/file* /user/zaka/test_data/

# Delet directory and its content
hdfs dfs -rm -r /user/zaka/test_data

# Move inside hdfs
hdfs dfs -mkdir /user/zaka/test_data/
hdfs dfs -mv /user/zaka/file* /user/zaka/test_data/

# View file content on hdfs
hdfs dfs -cat /user/zaka/file_1.txt

# Information about a specific file
hdfs fsck /user/zaka/file_1.txt -files -blocks -locations

# hdfs storage usage
hdfs dfs -df -h  #(-h for human readable)

# hdfs storage information for files
hdfs dfs -du -h /user/zaka/

# hdfs storage information for a folder
hdfs dfs -du -s -h /user/zaka/ #(is for sum)