import sys 
from pathlib import Path
from airflow.providers.standard.operators.python import PythonOperator 
from datetime import datetime, timedelta 
from airflow import DAG

# HOME Path 
AIRFLOW_HOME = Path("/opt/airflow") 
if str(AIRFLOW_HOME) not in sys.path:
    sys.path.insert(0, str(AIRFLOW_HOME))

from scripts.bronze_ingest_retail_products import run_bronze_ingest_retail_products 
from scripts.bronze_ingest_retail_customers import run_bronze_ingest_retail_customers


# Define DAG
default_args = {
    "owner": "rogers",
    "retries": 3,
    "retry_delay": timedelta(seconds=10)
} 

with DAG(
    dag_id="retail_store_data_pipeline",
    default_args=default_args,
    description="Moves the data from the E-commerce endpoints to the EDW for analytics",
    schedule=timedelta(minutes=10),
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=["etl", "ecomerce etl", "retail", "retail store"]
) as dag:

    bronze_extract_products = PythonOperator(
        task_id="bronze_extract_products",
        python_callable=run_bronze_ingest_retail_products
    )

    bronze_extract_customers = PythonOperator(
        task_id="bronze_extract_customers",
        python_callable=run_bronze_ingest_retail_customers
    )

    [bronze_extract_products, bronze_extract_customers]