import boto3
from config import Config

def client:
    # Initialize S3 client for R2
    return  boto3.client(
        's3',
        endpoint_url=R2_ENDPOINT_URL,
        aws_access_key_id=R2_ACCESS_KEY_ID,
        aws_secret_access_key=R2_SECRET_ACCESS_KEY,
        config=Config(signature_version='s3v4'),
        region_name='auto'  # R2 uses 'auto' for region
    )
    
    
    