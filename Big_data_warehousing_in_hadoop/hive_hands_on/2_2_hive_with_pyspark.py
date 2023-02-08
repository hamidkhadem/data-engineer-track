#####
# Remove "warn" logs from spark
#####

from os.path import abspath
from pyspark.sql import SparkSession

# warehouse_location points to the default location for managed databases and tables
warehouse_location = abspath('spark-warehouse')

spark = SparkSession \
    .builder \
    .appName("Pyspark integration with Hive") \
    .config("spark.sql.warehouse.dir", warehouse_location) \
    .enableHiveSupport() \
    .getOrCreate()
# enableHiveSupport() option in spark session supports the connection with Hive

# Queries are expressed in HiveQL
spark.sql("SELECT * FROM company.employees").show()


employees_df = spark.sql("SELECT id, first_name, last_name, age, gender \
                    FROM company.employees \
                    WHERE age < 30 \
                    ORDER BY first_name")

employees_df.show(50)
