import json 
import requests 
from datetime import datetime 
from pathlib import Path 


def run_bronze_ingest_retail_customers(**context):
    """Extracts return customers data from the customres endpoint"""

    PRODUCTS_ENDPOINT = "https://dummyjson.com/products?limit=0" 
    BRONZE_FOLDER = Path("/opt/airflow/data/bronze/retail_store/")
    BRONZE_FOLDER.mkdir(parents=True, exist_ok=True) # Create the folder "retail_store" if not exists

    # Fetch Retail customers 
    response = requests.get(PRODUCTS_ENDPOINT, timeout=5)

    # Raise SErver Errors -> status >= 500
    response.raise_for_status()

    # Raw Customers Data 
    raw_product_data = response.json()

    # Bronze File Path 
    raw_products_file_path = BRONZE_FOLDER / f"raw_retail_products_{datetime.now().strftime("%Y%m%d%H%M%S")}.json"

    # Save the JSON
    with open(raw_products_file_path, "w") as f:
        json.dump(raw_product_data, f)

    # Push the file path to XCOM context for downsteam tasks 
    context["ti"].xcom_push(key="raw_retail_products_file_path", value=str(raw_products_file_path))

