from pyspark.sql import SparkSession
from pyspark.sql.functions import lit, concat, col

# Create spartSession
spark = SparkSession.builder \
   .master("yarn") \
   .appName("zaka retail data") \
   .config("spark.executor.memory", '4g') \
   .config('spark.executor.cores', '1') \
   .config('spark.cores.max', '1') \
   .config("spark.driver.memory",'4g') \
   .getOrCreate()

# Read orders csv file
ordersDF = spark.read.csv("/user/zaka/retail_data/orders.csv")

# Print the schema
ordersDF.printSchema()

# Using inferSchema for auto schema inferring
ordersDF = spark.read.csv("/user/zaka/retail_data/orders.csv", inferSchema=True)
ordersDF.printSchema()

# Give Schema as parameter
ordersDF = spark.read.csv("/user/zaka/retail_data/orders.csv", \
        schema='''
            order_id INT, 
            order_date STRING, 
            order_customer_id INT, 
            order_status STRING''')
ordersDF.printSchema()

# Find the count
ordersDF.count()

# Select columns
ordersDF.select("order_id", "order_status").show()

# Employees collection
employees = [(1, "Ahmad", "Ali", 1000.0, "Jordanian"),
             (2, "Osama", "Mohammad", 1250.0, "Lebanese"),
             (3, "Omar", "Jack", 750.0, "Qatari"),
             (4, "Amanda", "Ali", 1500.0, "Lebanese")]

# Create DF from collection
employeesDF = spark. \
    createDataFrame(employees,
                    schema="""employee_id INT,first_name STRING, 
                    last_name STRING, salary FLOAT, nationality STRING""")
employeesDF.printSchema()
employeesDF.show()

employeesDF. \
    select("first_name", "last_name"). \
    show()

# Dropping a column
employeesDF. \
    drop("nationality"). \
    show()

# Using concat and lit to concnt columns
# lit() is to add a new constant column to DataFrame 
# by assigning a literal or constant
employeesDF. \
    select("employee_id",
           concat("first_name", lit(", "), "last_name").alias("full_name"),
           "salary",
           "nationality"
          ). \
    show()

# Writing dataframes
employeesDF. \
    write. \
    mode('overwrite'). \
    option('compression', 'none'). \
    format('json'). \
    save('/user/zaka/retail_data/employees.json')

####
# Dataframes processing
employeesDF. \
    orderBy("nationality"). \
    groupBy("nationality"). \
    count(). \
    show()

# Filtering columns
ordersDF. \
    filter((ordersDF["order_status"] == "COMPLETE")). \
    show()

ordersDF. \
    filter((col("order_status") == "COMPLETE")). \
    show()