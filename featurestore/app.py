import os
from fastapi import FastAPI, HTTPException
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

S3_BUCKET = os.getenv("S3_BUCKET")
S3_ENDPOINT = os.getenv("S3_ENDPOINT")
S3_ACCESS_KEY = os.getenv("S3_ACCESS_KEY")
S3_SECRET_KEY = os.getenv("S3_SECRET_KEY")

storage_options = {
    "key": S3_ACCESS_KEY,
    "secret": S3_SECRET_KEY,
    "client_kwargs": {"endpoint_url": S3_ENDPOINT},
}

app = FastAPI(title="Feature Store API")

@app.get("/features/daily")
def get_daily_features():
    try:
        path = f"s3://{S3_BUCKET}/processed/features/"
        df = pd.read_parquet(path, storage_options=storage_options)
        return {"rows": df.head(50).to_dict(orient="records")}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
