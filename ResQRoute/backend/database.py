import mysql.connector
from mysql.connector import Error

# Replace these with your actual MySQL credentials
DB_CONFIG = {
    "host": "localhost",
    "user": "root",   # e.g., 'root'
    "password": "Tanmay1@lol",
    "database": "ResQRoute"
}

def get_connection():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"[ERROR] Database connection failed: {e}")
        return None

def fetch_all(query, params=None):
    conn = get_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, params or ())
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return results
    return []

def execute_query(query, params=None):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute(query, params or ())
        conn.commit()
        cursor.close()
        conn.close()
        return True
    return False
