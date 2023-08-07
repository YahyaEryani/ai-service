import boto3
from botocore.exceptions import NoCredentialsError
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the S3 client with credentials and region information
s3_client = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name=os.getenv('AWS_REGION')
)

# Get the bucket name from environment variable
BUCKET_NAME = os.getenv('BUCKET_NAME')


def download_file(file_name, local_path):
    """
    Download a file from an S3 bucket to a local path.
    
    Parameters:
    - file_name (str): Name of the file in the S3 bucket.
    - local_path (str): Local path where the file should be saved.

    Raises:
    - NoCredentialsError: If credentials are not available.
    """
    try:
        s3_client.download_file(BUCKET_NAME, file_name, local_path)
    except NoCredentialsError:
        print('Credentials not available')


def upload_file(file_name, object_name=None):
    """
    Upload a local file to an S3 bucket.

    Parameters:
    - file_name (str): Name of the local file to upload.
    - object_name (str, optional): Desired object name in S3. If not provided, the local file name is used.

    Raises:
    - NoCredentialsError: If credentials are not available.
    """
    try:
        s3_client.upload_file(file_name, BUCKET_NAME, object_name or file_name)
    except NoCredentialsError:
        print('Credentials not available')


def fetch_metadata(object_name):
    """
    Fetch the metadata for a specific object in the given S3 bucket.
    
    Parameters:
    - object_name (str): The name of the object for which to fetch the metadata.

    Returns:
    - dict: The metadata of the object.

    Raises:
    - NoCredentialsError: If credentials are not available.
    """
    try:
        response = s3_client.head_object(Bucket=BUCKET_NAME, Key=object_name)
        return response['Metadata']
    except NoCredentialsError:
        print('Credentials not available')