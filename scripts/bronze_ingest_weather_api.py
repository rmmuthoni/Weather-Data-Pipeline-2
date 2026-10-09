import requests 
import json 
from datetime import datetime 
from pathlib import Path 


# URL to the data sources
API_URL="https://api.openweathermap.org/data/2.5/weather?lat=-1.2921&lon=36.8219&appid=0fbbe1672b62e7ed642cdc4c59cf5d71"

def run_bronze_ingestion(**context): 
    """THis function will be used to extract the Weather data from the Weathermap API""" 

    response = requests.get(API_URL, timeout=5) 

    # Raise Errors for >= 500 Server Errors
    response.raise_for_status() 

    # Extract Json data payload 
    data = response.json() 

    # current timestamp 
    current_timestamp = datetime.now().strftime("%Y%m%d%H%M%S") 

    # Path to the file store
    file_path = Path(f"/opt/airflow/data/bronze/weather_data_{current_timestamp}.json")

    # Write to the file 
    with open(file_path, "w") as f:
        json.dump(data, f)

    # Push the path to the / four use by downstream task instances
    context["ti"].xcom_push(key="bronze_weather_data_file", value=str(file_path))