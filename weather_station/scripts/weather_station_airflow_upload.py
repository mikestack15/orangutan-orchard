from weather_station_utilities import upload_most_recent_data

def main():
    """Check if a data file exists, upload the most recent data file as a blob to cloud bucket,
    and remove the file once successfully uploaded."""
    
    if not upload_most_recent_data():
        raise ConnectionRefusedError("Could not upload blob to GCP!")

if __name__ == "__main__":
    main()