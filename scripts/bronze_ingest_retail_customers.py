import json 
import requests 
from datetime import datetime 
from pathlib import Path  


def run_bronze_ingest_retail_customers(**context) -> None:
    """Ingests Retail CUstomers from the Ecomerce ENdpoint"""

    CUSTOMER_DATA_ENDPOINT = "https://dummyjson.com/users?limit=0"
    CUSTOMER_DATA_FOLDER = Path("/opt/airflow/data/bronze/retail_store/")
    CUSTOMER_DATA_FOLDER.mkdir(parents=True, exist_ok=True) 

    response = requests.get(CUSTOMER_DATA_ENDPOINT, timeout=5)
    response.raise_for_status()

    raw_customer_data = response.json()

    raw_customer_data_file_path = CUSTOMER_DATA_FOLDER / f"raw_customer_data_{datetime.now().strftime("%Y%m%d%H%M%S")}.json"

    with open(raw_customer_data_file_path, "w") as f:
        json.dump(raw_customer_data, f)

    context["ti"].xcom_push(key="raw_customer_data_file_path", value=str(raw_customer_data_file_path))