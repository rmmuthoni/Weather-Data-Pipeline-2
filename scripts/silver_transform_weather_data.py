import json 
from pathlib import Path 
from datetime import datetime


def run_silver_transformation(**context) -> None:
    """Runs transformations on the extracted weather data""" 

    # PUll the execution date of the DAG 
    dag_execution_date = context["ds_nodash"]

    # Pull the bronze file from Xcom 
    bronze_file_path = context["ti"].xcom_pull(key="bronze_weather_data_file", task_ids="bronze_weather_ingest")

    # If the file is not in Xcom, Raise an Error 
    if not bronze_file_path:
        raise ValueError("Bronze file path not found in XCom context") 

    # Define where to send the transformed file
    silver_file_path = Path("/opt/airflow/data/silver")
    silver_file_path.mkdir(parents=True, exist_ok=True) # Create the folder "silver" if not exists 

    with open(bronze_file_path) as f:
        raw_data = json.load(f)

    # TRansformations 
    cleaned_weather_data = {
        "created_at": datetime.now().isoformat(),
        "temperature": raw_data.get("main", {}).get("temp"),
        "temperature_feels_like": raw_data.get("main", {}).get("feels_like"),
        "temperature_min": raw_data.get("main", {}).get("temp_min"),
        "temperature_max": raw_data.get("main", {}).get("temp_max"),
        "pressure": raw_data.get("main", {}).get("pressure"),
        "humidity": raw_data.get("main", {}).get("humidity"),
        "wind_speed": raw_data.get("wind", {}).get("speed"),
        "wind_direction": raw_data.get("wind", {}).get("deg"),
        "city": raw_data.get("name"),
        "country": raw_data.get("sys", {}).get("country"),
    }

    # Save the data to silver layer 
    output_file = silver_file_path / f"weather_data_{dag_execution_date}.json"
    with open(output_file, "w") as f:
        json.dump(cleaned_weather_data, f)

    # PUsh the silver transformed data file path to XCom context 
    context["ti"].xcom_push(key="silver_weather_data_file", value=str(output_file))