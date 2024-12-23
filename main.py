from dotenv import load_dotenv
import os
import psycopg2
import psycopg2.extras

# Load environment variables from .env file
load_dotenv()

# Retrieve database configuration from environment variables
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

# Establish the connection
database_session = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASS,
    host=DB_HOST,
    port=DB_PORT
)

# Create a cursor
cursor = database_session.cursor(cursor_factory=psycopg2.extras.DictCursor)
