import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    ENV = os.environ.get('ENV') or ''
    LOCAL_DIR = os.environ.get('LOCAL_DIR') or ''
    ROOT_DIR_NAME = os.environ.get('ROOT_DIR_NAME') or ''
    OUTPUT_DIR_NAME = os.environ.get('OUTPUT_DIR_NAME') or ''
    R2_ACCESS_KEY_ID = os.environ.get('R2_ACCESS_KEY_ID') or ''
    R2_SECRET_ACCESS_KEY = os.environ.get('R2_SECRET_ACCESS_KEY') or ''
    R2_ENDPOINT_URL = os.environ.get('R2_ENDPOINT_URL') or ''
    BUCKET_NAME = os.environ.get('BUCKET_NAME') or ''