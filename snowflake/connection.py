import os
import snowflake.connector
from dotenv import load_dotenv

load_dotenv()

def get_snowflake_connection():
    try:
        conn = snowflake.connector.connect(
            user=os.getenv('SNOWSQL_USER'),
            password=os.getenv('SNOWSQL_PWD'),
            account=os.getenv('SNOWFLAKE_ACCOUNT'),
            warehouse=os.getenv('WAREHOUSE'),
            database=os.getenv('DATABASE'),
            schema=os.getenv('SCHEMA')
        )
        return conn
    except Exception as e:
        print(f"Error connecting to Snowflake: {e}")
        return None