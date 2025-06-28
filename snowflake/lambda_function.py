from connection import get_snowflake_connection

def lambda_handler(event, context):    
    conn = get_snowflake_connection()
    
    if not conn:
        return {
            'statusCode': 500,
            'body': 'Failed to connect to Snowflake'
        }
    
    try:
        cursor = conn.cursor()
        
        cursor.execute("SELECT CURRENT_VERSION()")
        result = cursor.fetchone()
        
        return {
            'statusCode': 200,
            'body': f'Connected to Snowflake successfully. Version: {result[0]}'
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error executing query: {str(e)}'
        }
    
    finally:
        if conn:
            conn.close()