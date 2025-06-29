from connection import get_snowflake_connection

def cortex_complete(prompt, model='snowflake-arctic'):
    conn = get_snowflake_connection()
    if not conn:
        return None
    
    try:
        cursor = conn.cursor()
        query = f"SELECT SNOWFLAKE.CORTEX.COMPLETE('{model}', '{prompt}')"
        cursor.execute(query)
        result = cursor.fetchone()
        return result[0] if result else None
    except Exception as e:
        print(f"Error in cortex_complete: {e}")
        return None
    finally:
        conn.close()

def cortex_summarize(text):
    conn = get_snowflake_connection()
    if not conn:
        return None
    
    try:
        cursor = conn.cursor()
        query = f"SELECT SNOWFLAKE.CORTEX.SUMMARIZE('{text}')"
        cursor.execute(query)
        result = cursor.fetchone()
        return result[0] if result else None
    except Exception as e:
        print(f"Error in cortex_summarize: {e}")
        return None
    finally:
        conn.close()

def cortex_sentiment(text):
    conn = get_snowflake_connection()
    if not conn:
        return None
    
    try:
        cursor = conn.cursor()
        query = f"SELECT SNOWFLAKE.CORTEX.SENTIMENT('{text}')"
        cursor.execute(query)
        result = cursor.fetchone()
        return result[0] if result else None
    except Exception as e:
        print(f"Error in cortex_sentiment: {e}")
        return None
    finally:
        conn.close()



CORTEX_OPERATIONS = {
    "complete": cortex_complete,
    "summarize": cortex_summarize,
    "sentiment": cortex_sentiment
}

def get_available_operations():
    return list(CORTEX_OPERATIONS.keys())