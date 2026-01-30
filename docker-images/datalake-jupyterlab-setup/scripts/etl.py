from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("ETL Pipeline") \
    .getOrCreate()

print("spark session created successfully")