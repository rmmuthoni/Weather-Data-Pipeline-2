# from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator 
from datetime import datetime, timedelta 
from airflow import DAG



def extract_job():
    print("Extraction Job")

def transformation_job():
    print("Transformation JOb") 

def loading_job():
    print("Loading Job") 



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
    schedule=timedelta(minutes=1),
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=["etl", "weather etl"]
) as dag:

    extraction_task = PythonOperator(
        task_id="extraction_job",
        python_callable=extract_job
    )

    transformation_task = PythonOperator(
        task_id="transformation_job",
        python_callable=transformation_job
    )

    loading_task = PythonOperator(
        task_id="loading_job",
        python_callable=loading_job
    )


    extraction_task >> transformation_task >> loading_task 
