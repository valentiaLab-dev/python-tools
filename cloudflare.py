import boto3
from botocore.config import Config
from app import app

def s3_client():
    return boto3.client(
        's3',
        endpoint_url=app.config["R2_ENDPOINT_URL"],
        aws_access_key_id=app.config["R2_ACCESS_KEY_ID"],
        aws_secret_access_key=app.config["R2_SECRET_ACCESS_KEY"],
        config=Config(signature_version='s3v4'),
        region_name='auto'  # R2 uses 'auto' for region
    )