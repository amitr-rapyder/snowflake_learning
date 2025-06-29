from connection import get_snowflake_connection
from cortex_functions import CORTEX_OPERATIONS, get_available_operations

def test_connection():
    print("Testing Snowflake connection...")
    
    conn = get_snowflake_connection()
    
    if not conn:
        print("Failed to connect to Snowflake")
        return False
    
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT CURRENT_VERSION()")
        result = cursor.fetchone()
        print(f"Connected successfully! Snowflake version: {result[0]}")
        return True
        
    except Exception as e:
        print(f"Error executing query: {e}")
        return False
    
    finally:
        if conn:
            conn.close()

def test_cortex_functions():
    
    test_data = {
        "complete": ("What is artificial intelligence?",),
        "summarize": ("Artificial intelligence is a branch of computer science that aims to create intelligent machines that work and react like humans. It involves machine learning, natural language processing, and robotics.",),
        "sentiment": ("I love using Snowflake for data analytics!",)
    }
    
    results = {}
    
    for operation in get_available_operations():
        print(f"\nTesting {operation}...")
        try:
            func = CORTEX_OPERATIONS[operation]
            args = test_data.get(operation, ())
            result = func(*args)
            
            if result:
                print(f"[SUCCESS] {operation}: {result[:100]}..." if len(str(result)) > 100 else f"[SUCCESS] {operation}: {result}")
                results[operation] = True
            else:
                print(f"[FAIL] {operation}: No result returned")
                results[operation] = False
                
        except Exception as e:
            print(f"[ERROR] {operation}: {e}")
            results[operation] = False
    
    return results

def run_all_tests():
    
    connection_ok = test_connection()
    
    if connection_ok:
        cortex_results = test_cortex_functions()
        
        print(f"Connection: {'PASS' if connection_ok else 'FAIL'}")
        
        for operation, success in cortex_results.items():
            print(f"Cortex {operation}: {'PASS' if success else 'FAIL'}")
    else:
        print("connection failure")

run_all_tests()

