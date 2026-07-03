import sqlite3
import os
import json

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mdm_mock.db')

def get_db_connection():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def setup_database():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS customers (id INTEGER PRIMARY KEY, name TEXT, churn_risk TEXT, lifetime_value INTEGER)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS suppliers (id INTEGER PRIMARY KEY, name TEXT, reliability_score INTEGER, active_contracts INTEGER)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, sku TEXT, category TEXT, stock_level INTEGER)''')
    
    cursor.execute("DELETE FROM customers")
    cursor.execute("DELETE FROM suppliers")
    cursor.execute("DELETE FROM items")
    
    customers = [
        (1, "Acme Corp", "Low", 150000), (2, "Global Tech", "High", 45000), 
        (3, "Stark Ind", "Low", 980000), (4, "Wayne Ent", "Medium", 200000), (5, "LexCorp", "High", 10000)
    ]
    suppliers = [
        (1, "PartsCo", 95, 3), (2, "FastShip", 78, 1), 
        (3, "Prime Mat", 99, 5), (4, "Global Log", 88, 4), (5, "QuickSend", 92, 2)
    ]
    items = [
        (1, "SKU-100", "Electronics", 450), (2, "SKU-205", "Hardware", 12), 
        (3, "SKU-399", "Software", 9999), (4, "SKU-400", "Services", 50), (5, "SKU-500", "Storage", 200)
    ]
    
    cursor.executemany("INSERT INTO customers VALUES (?, ?, ?, ?)", customers)
    cursor.executemany("INSERT INTO suppliers VALUES (?, ?, ?, ?)", suppliers)
    cursor.executemany("INSERT INTO items VALUES (?, ?, ?, ?)", items)
    
    conn.commit()
    conn.close()

def execute_sql_query(query: str) -> str:
    """Executes query and returns stringified JSON to the agent."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        results = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return json.dumps(results)
    except Exception as e:
        return json.dumps({"error": str(e)})