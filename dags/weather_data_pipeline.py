import sys 
from pathlib import Path
from airflow.providers.standard.operators.python import PythonOperator 
from datetime import datetime, timedelta 
from airflow import DAG

# HOME Path 
AIRFLOW_HOME = Path("/opt/airflow") 
if str(AIRFLOW_HOME) not in sys.path:
    sys.path.insert(0, str(AIRFLOW_HOME))

from scripts.bronze_ingest_weather_api import run_bronze_ingestion
from scripts.silver_transform_weather_data import run_silver_transformation
from scripts.load_silver_to_warehouse import load_silver_data_to_warehouse




# Setting up the default arguments 
default_args = {
    "owner": "rogers",
    "retries": 3,
    "retry_delay": timedelta(minutes=1)
} 


# Defines the DAGS 
with DAG(
    dag_id="weather_data_pipeline",
    default_args=default_args,
    description="Weather Data Pipeline - Move Data from OPen Weather Map API's to a Postgres Warehouse",
    schedule=timedelta(hours=1),
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=["etl", "weather etl"]
) as dag:

    bronze = PythonOperator(
        task_id="bronze_weather_ingest",
        python_callable=run_bronze_ingestion
    )

    silver = PythonOperator(
        task_id="silver_weather_transform",
        python_callable=run_silver_transformation
    )

    load = PythonOperator(
        task_id="load_to_warehouse",
        python_callable=load_silver_data_to_warehouse
    )

    # Execution Order
    bronze >> silver >> load

    



