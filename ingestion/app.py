import os
import boto3
from botocore.client import Config
from dotenv import load_dotenv
from generate_data import generate_csv

load_dotenv()

S3_ENDPOINT = os.getenv("S3_ENDPOINT", "http://minio:9000")
S3_ACCESS_KEY = os.getenv("S3_ACCESS_KEY")
S3_SECRET_KEY = os.getenv("S3_SECRET_KEY")
S3_BUCKET = os.getenv("S3_BUCKET", "data-bucket")

def ensure_bucket(s3):
    try:
        s3.create_bucket(Bucket=S3_BUCKET)
    except Exception:
        pass

def upload_file(filename, key):
    s3 = boto3.client('s3',
                      endpoint_url=S3_ENDPOINT,
                      aws_access_key_id=S3_ACCESS_KEY,
                      aws_secret_access_key=S3_SECRET_KEY,
                      config=Config(signature_version='s3v4'),
                      region_name='us-east-1')
    ensure_bucket(s3)
    s3.upload_file(filename, S3_BUCKET, key)
    print("Uploaded", filename, "to", S3_BUCKET+"/"+key)

if __name__ == "__main__":
    generate_csv(path="sample_data/transactions.csv", n=int(os.getenv("SAMPLE_ROWS", 200000)))
    upload_file("sample_data/transactions.csv", "raw/transactions.csv")
    print("Ingestion complete.")
