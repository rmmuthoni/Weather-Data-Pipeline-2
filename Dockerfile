FROM apache/airflow:3.3.2 

ENV PYTHONPATH="${PYTHONPATH}:/opt/airflow"

COPY requirements.txt . 

RUN pip install --no-cache-dir -r requirements.txt