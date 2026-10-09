# Weather Data Engineering Pipeline

A data engineering project that uses Apache Airflow to orchestrate scheduled batch extraction of weather data from a weather API, transform the incoming data, and load it into PostgreSQL for visualization and business intelligence reporting.

## Problem Statement

Organizations and analysts often need timely, reliable, and structured weather data for reporting, forecasting, trend analysis, and operational decision-making. Weather data provided by external APIs is often returned in formats that are difficult to query and analyze directly. This project addresses that challenge by building a robust data pipeline that:

- Extracts weather data from a weather API.
- Handles API requests reliably using retry and backoff mechanisms.
- Transforms raw data into a clean, consistent, and analysis-ready structure.
- Loads the processed data into PostgreSQL for storage and downstream use.
- Enables reporting and business intelligence workflows using centralized, queryable data.

## Project Overview

The pipeline is orchestrated with Apache Airflow and designed to run scheduled batch jobs. Airflow manages task dependencies, execution timing, retries, monitoring, and failure handling across the data workflow.

The process follows a standard data engineering flow:

1. Extract weather data from the API.
2. Validate and normalize the incoming data.
3. Transform the data into a ready-to-store format.
4. Load the data into PostgreSQL.
5. Make the data available for visualization and BI reporting.

## Architecture

```text
Weather API
    |
    |  HTTP requests
    v
Apache Airflow
    |
    |  Extract -> Transform -> Load
    v
PostgreSQL Database
    |
    |  Reporting and BI
    v
Dashboards and Business Intelligence Tools
```

<img width="753" height="197" alt="open_weather_pipe_architecture" src="https://github.com/user-attachments/assets/badd0794-3e49-4ca7-ba54-b43d56076cc6" />


## Technologies

- **Apache Airflow** — workflow orchestration and scheduled batch execution.
- **Python** — data extraction, transformation, and loading logic.
- **Requests** — HTTP requests to the weather API.
- **Tenacity** — retry and backoff handling for unreliable API calls.
- **SQLAlchemy** — database connection management and schema definition.
- **PostgreSQL** — durable storage for processed weather data.
- **Pandas** — data manipulation and transformation.
- **Docker** — containerized deployment of the application and services.
- **Business Intelligence Tools** — visualization and reporting on the stored data.

## Pipeline Workflow

### 1. Data Extraction

Airflow triggers a scheduled job that makes requests to the weather API. The extractor retrieves current weather, forecasts, or other required weather fields and captures the raw response.

### 2. Data Transformation

The raw API response is cleaned and transformed into a structured format. This includes:

- Handling missing or invalid values.
- Converting data types.
- Normalizing field names and timestamps.
- Enriching the data where needed.
- Preparing the data for storage and analysis.

### 3. Data Loading

The transformed data is written to PostgreSQL using SQLAlchemy. The database schema defines tables and relationships for efficient querying and reporting.

### 4. Reporting and BI

Once the data is stored in PostgreSQL, analysts and BI tools can query it to build dashboards, generate reports, and perform trend and performance analysis.

## Key Features

- Scheduled batch fetching of weather data with Apache Airflow.
- Reliable API interactions using retries and backoff.
- Automated data extraction, transformation, and loading.
- Database schema definition using SQLAlchemy.
- PostgreSQL storage for analytics and reporting.
- Scalable and maintainable data pipeline architecture.

## Project Goals

The main objective of this project is to automate the collection and preparation of weather data so that it can be stored in a structured database and used effectively by business intelligence and reporting systems.

## Getting Started

1. Install the required Python dependencies.
2. Configure the weather API credentials and PostgreSQL connection settings.
3. Start Apache Airflow and the PostgreSQL database.
4. Create and run the Airflow DAGs.
5. Query the processed data in PostgreSQL for reporting and analysis.

## License

This project is licensed under the MIT License.
