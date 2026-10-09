from dotenv import load_dotenv 
import os 
from sqlalchemy import create_engine
import psycopg2

load_dotenv() 

# Database Settings
DATABASE_URL = os.getenv("DATABASE_URL").format(
    DATABASE_PASSWORD=os.getenv("DATABASE_PASSWORD"),
    DATABASE_HOST = os.getenv("DATABASE_HOST"),
    DATABASE_PORT = os.getenv("DATABASE_PORT"),
    DATABASE_NAME = os.getenv("DATABASE_NAME")
)

DATABASE_ENGINE = create_engine(DATABASE_URL)

