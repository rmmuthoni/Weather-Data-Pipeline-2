import sys
import os 
import json 
import pandas as pd 
from pathlib import Path 

# HOME Path 
current_folder = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_folder) 
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from settings import DATABASE_ENGINE


def load_silver_data_to_warehouse(**context) -> None:
    """Loads the transformed silver data layer into the remote postgresql warehouse"""

    # Pull the silver file path from XCOM 
    silver_file_path = context["ti"].xcom_pull(task_ids="silver_weather_transform", key="silver_weather_data_file")

    # If the filepath was not found, Raise an error 
    if not silver_file_path:
        raise ValueError(f"{silver_file_path} was not found in XCOM context") 

    # Load the file 
    with open(silver_file_path) as f:
        silver_weather_data = json.load(f) 

    # Ccreate a dataframe from this json data 
    weather_data_df = pd.DataFrame([silver_weather_data])


print(DATABASE_ENGINE)