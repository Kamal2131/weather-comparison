# --- utils/s3_utils.py ---
import os
import boto3
import pandas as pd
from io import StringIO
from dotenv import load_dotenv

load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_DEFAULT_REGION")
BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

FOLDER_PREFIX = "weather"  # All files will go inside this 'folder'

s3 = boto3.client(
    "s3",
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)

def save_df_to_s3(df: pd.DataFrame, filename: str):
    if df.empty:
        print("⚠️ Not saving empty dataframe to S3.")
        return

    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)

    key = f"{FOLDER_PREFIX}/{filename}"
    s3.put_object(Bucket=BUCKET_NAME, Key=key, Body=csv_buffer.getvalue())
    print(f"✅ Uploaded '{key}' to bucket '{BUCKET_NAME}'")


def read_df_from_s3(filename: str) -> pd.DataFrame:
    key = f"{FOLDER_PREFIX}/{filename}"
    try:
        obj = s3.get_object(Bucket=BUCKET_NAME, Key=key)
        df = pd.read_csv(obj['Body'])
        if df.empty:
            print("⚠️ S3 file exists but is empty.")
            return None  # type: ignore
        return df
    except Exception as e:
        print("❌ Error reading from S3:", e)
        return None  # type: ignore


def list_weather_keys():
    try:
        objects = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix=FOLDER_PREFIX + "/")
        contents = objects.get("Contents", [])
        # Only return filenames (not full S3 keys)
        keys = [obj["Key"].replace(FOLDER_PREFIX + "/", "") for obj in contents if obj["Key"].endswith(".csv")]
        return keys
    except Exception as e:
        print(f"❌ Failed to list keys from S3: {e}")
        return []
