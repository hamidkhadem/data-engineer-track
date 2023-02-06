from pyspark.sql import SparkSession
from pyspark.sql.functions import lit, concat, col


def create_spark_session():
    spark = SparkSession.builder \
        .master("yarn") \
        .appName("zaka retail data") \
        .config("spark.executor.memory", '4g') \
        .config('spark.executor.cores', '1') \
        .config('spark.cores.max', '1') \
        .config("spark.driver.memory",'4g') \
        .getOrCreate()

    return spark


def read_process_df(spark):
    ordersDF = spark.read.csv("/user/zaka/retail_data/orders.csv", \
        schema='''
            order_id INT, 
            order_date STRING, 
            order_customer_id INT, 
            order_status STRING''')
    
    ordersDF. \
        filter((ordersDF["order_status"] == "COMPLETE"))

    return ordersDF


def save_df(df):
    df.write \
        .mode("overwrite") \
        .option("compression", "none") \
        .format("json") \
        .save("/user/zaka/retail_data/orders_spark_submit.json")


def main():
    spark = create_spark_session()
    df = read_process_df(spark)
    save_df(df)


if __name__ == "__main__":
    main()