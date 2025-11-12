from pyspark.sql import SparkSession

def run_etl():
    spark = SparkSession.builder \
        .appName("BatchETL") \
        .config("spark.hadoop.fs.s3a.endpoint", "http://minio:9000") \
        .config("spark.hadoop.fs.s3a.access.key", "minioadmin") \
        .config("spark.hadoop.fs.s3a.secret.key", "minioadmin") \
        .config("spark.hadoop.fs.s3a.path.style.access", "true") \
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
        .getOrCreate()

    input_path = "s3a://data-bucket/raw/transactions.csv"
    output_path = "s3a://data-bucket/curated/cleaned_transactions.csv"

    df = spark.read.option("header", True).option("inferSchema", True).csv(input_path)
    cleaned_df = df.dropna(subset=["amount"])
    cleaned_df.write.mode("overwrite").option("header", True).csv(output_path)

    spark.stop()

if __name__ == "__main__":
    run_etl()
