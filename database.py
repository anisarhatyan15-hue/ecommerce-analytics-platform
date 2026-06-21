import sqlite3

DB_NAME = "ecommerce.db"

def init_db():
    conn =sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            user TEXT,
            product_name TEXT,
            price REAL,
            category TEXT,
            action TEXT
        )
    ''')
    conn.commit()
    conn.close()
    print(f"Տվյալների բազան՝ '{DB_NAME}', հաջողությամբ պատրաստ է:")

if __name__ == "__main__":
    init_db()