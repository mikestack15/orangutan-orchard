import os
import glob
from google.cloud import storage
from datetime import datetime
from weather_station_secrets import CREDS_PATH, BUCKET_NAME, DESTINATION_BLOB_NAME, DATA_PATH, SERVICE_KEY_NAME

# Change environmental variable for Google.
def setup_creds() -> None:
    os.chdir(CREDS_PATH)
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = CREDS_PATH + SERVICE_KEY_NAME

def get_date_string() -> str:
    today = datetime.now()
    today = today.strftime("%d-%m-%Y-%H-%M")
    return today

def get_most_recent_data_file() -> str:
    list_of_files = glob.glob(f'{DATA_PATH}*.csv')
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file

"""Uploads a file to the bucket.

    The ID of your GCS bucket:
    bucket_name = "your-bucket-name"
    The path to your file to upload:
    source_file_name = "local/path/to/file"
    The ID of your GCS object:
    DESTINATION_BLOB_NAME = "storage-object-name"   
"""
def upload_most_recent_data() -> bool:
    setup_creds()
    storage_client = storage.Client()
    bucket = storage_client.bucket(BUCKET_NAME)
    blob = bucket.blob(DESTINATION_BLOB_NAME)
    source_file_name = get_most_recent_data_file()
    blob.upload_from_filename(source_file_name)
    return True