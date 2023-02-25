
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, FloatType
from pyspark.ml.feature import VectorAssembler, StandardScaler
from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator

# Spark session
spark = SparkSession.builder \
    .master("yarn") \
    .appName("Linear-Regression-Example") \
    .getOrCreate()

# Data file
HOUSING_DATA = "/user/zaka/spark_mllib/housing_data.csv"

schema = StructType([
    StructField("median_house_value", FloatType(), nullable=True),
    StructField("total_bedrooms", FloatType(), nullable=True),
    StructField("population", FloatType(), nullable=True),
    StructField("house_holds", FloatType(), nullable=True),
    StructField("median_income", FloatType(), nullable=True),
    StructField("rooms_per_househole", FloatType(), nullable=True),
    StructField("population_per_househole", FloatType(), nullable=True),
    StructField("bedrooms_ratio", FloatType(), nullable=True)]
)

# Load housing data
housing_df = spark.read.csv(path=HOUSING_DATA, header=True, schema=schema)

housing_df.printSchema()
housing_df.show(5)

## Feature Extraction
# Features Columns
featureCols = ["total_bedrooms", "population", "house_holds", "median_income", "rooms_per_househole", "population_per_househole", "bedrooms_ratio"]

# put features into a feature vector column
assembler = VectorAssembler(inputCols=featureCols, outputCol="features") 
assembled_df = assembler.transform(housing_df)
assembled_df.show(10, truncate=False)

## Standardization
# Initialize the `standardScaler`
standardScaler = StandardScaler(inputCol="features", outputCol="features_scaled")
scaled_df = standardScaler.fit(assembled_df).transform(assembled_df)
scaled_df.select("features", "features_scaled").show(10, truncate=False)

# Building A Machine Learning Model With Spark ML
# Split the data into train and test sets
train_data, test_data = scaled_df.randomSplit([.8,.2])  # , seed=rnd_seed

# Initialize `lr`
lr = LinearRegression(
    featuresCol='features_scaled',
    labelCol="median_house_value",
    predictionCol='pred_median_house_value',
    maxIter=10,
    regParam=0.3,
    elasticNetParam=0.8,
    standardization=False
)

# Fit the data to the model
linearModel = lr.fit(train_data)

# Coefficients for the model
linearModel.coefficients

# Intercept for the model
linearModel.intercept

# Generate predictions
predictions = linearModel.transform(test_data)

# Extract the predictions and the "known" correct labels
predictions_and_labels = predictions.select("pred_median_house_value", "median_house_value")
predictions_and_labels.show()

## Inspect the Metrics
evaluator = RegressionEvaluator(
    predictionCol="pred_median_house_value",
    labelCol='median_house_value',
    metricName='rmse'
)
print(f"RMSE: {evaluator.evaluate(predictions_and_labels)}")
