import boto3
from botocore.exceptions import NoCredentialsError
import os
from dotenv import load_dotenv

# This loads the variables from .env
load_dotenv()

s3_client = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('AWS_REGION')
)

BUCKET_NAME = os.getenv('BUCKET_NAME')


def download_file(file_name, local_path):
    try:
        s3_client.download_file(BUCKET_NAME, file_name, local_path)
    except NoCredentialsError:
        print('Credentials not available')


def upload_file(file_name, object_name=None):
    try:
        s3_client.upload_file(file_name, BUCKET_NAME, object_name or file_name)
    except NoCredentialsError:
        print('Credentials not available')


def fetch_metadata(object_name):
    """
    Fetch the metadata for a specific object in the given S3 bucket.
    
    Parameters:
    object_name (str): The name of the object for which to fetch the metadata.

    Returns:
    dict: The metadata of the object.
    """
    try:
        response = s3_client.head_object(Bucket=BUCKET_NAME, Key=object_name)
        return response['Metadata']
    except NoCredentialsError:
        print('Credentials not available')
