from connection import get_snowflake_connection

def test_connection():
    print("Testing Snowflake connection...")
    
    conn = get_snowflake_connection()
    
    if not conn:
        print("[FAIL] Failed to connect to Snowflake")
        return False
    
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT CURRENT_VERSION()")
        result = cursor.fetchone()
        print(f"[SUCCESS] Connected successfully! Snowflake version: {result[0]}")
        return True
        
    except Exception as e:
        print(f"[ERROR] Error executing query: {e}")
        return False
    
    finally:
        if conn:
            conn.close()

test_connection()