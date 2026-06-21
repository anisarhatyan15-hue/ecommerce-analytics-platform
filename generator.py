import random
import time
import sqlite3
from datetime import datetime

USERS = ["Աննա", "Արամ", "Գոռ", "Մանե", "Դավիթ", "Լուիզա", "Հայկ", "Էլեն"]
PRODUCTS = [
    {"name": "Laptop", "price": 1200, "category": "Electronics"},
    {"name": "Smartphone", "price": 800, "category": "Electronics"},
    {"name": "Book", "price": 25, "category": "Books"},
    {"name": "Coffee Maker", "price": 150, "category": "Home"},
    {"name": "Backpack", "price": 60, "category": "Fashion"},
    {"name": "Headphones", "price": 100, "category": "Electronics"}
]
ACTIONS = ["view", "add_to_cart", "purchase", "cancel"]

def generate_event():
    user = random.choice(USERS)
    product = random.choice(PRODUCTS)
    action = random.choice(ACTIONS)
    timestamp = datetime.now().isoformat()
    
    return {
        "timestamp": timestamp,
        "user": user,
        "product_name": product["name"],
        "price": product["price"],
        "category": product["category"],
        "action": action
    }
def insert_to_db(event):
    conn = sqlite3.connect("ecommerce.db")
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO events (timestamp, user, product_name, price, category, action)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (event["timestamp"], event["user"], event["product_name"], event["price"], event["category"], event["action"]))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    print("Սիմուլյացիան սկսված է... (Անջատելու համար սեղմիր Ctrl+C)")
    try:
      while True:
            current_event = generate_event()
            insert_to_db(current_event)

            print(f"Գրանցվեց՝ {current_event['user']} -> {current_event['action']} -> {current_event['product_name']}")

            time.sleep(1)
    except KeyboardInterrupt:
        print("Սիմուլյացիան դադարեցվեց։")
