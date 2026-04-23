import sqlite3
import os

DATABASE_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'instance', 'database.db')
SCHEMA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'database', 'schema.sql')

def get_db_connection():
    """建立並回傳資料庫連線，並設定 row_factory 讓結果可以像 dict 一樣存取"""
    # 確保 instance 目錄存在
    os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)
    
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """初始化資料庫，如果資料表不存在則建立"""
    if not os.path.exists(SCHEMA_PATH):
        print(f"Schema file not found at {SCHEMA_PATH}")
        return
        
    conn = get_db_connection()
    with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
        schema_script = f.read()
    
    try:
        conn.executescript(schema_script)
        conn.commit()
        print("Database initialized successfully.")
    except Exception as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()
