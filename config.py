import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    R2_ACCESS_KEY_ID = os.environ.get('R2_ACCESS_KEY_ID') or 'xxxxx'
    R2_SECRET_ACCESS_KEY = os.environ.get('R2_SECRET_ACCESS_KEY') or ''
    R2_ENDPOINT_URL = os.environ.get('R2_ENDPOINT_URL') or ''
    BUCKET_NAME = os.environ.get('BUCKET_NAME') or ''