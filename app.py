from fastapi import FastAPI
import sqlite3
import psutil

app = FastAPI(title="E-Commerce Analytics API")

@app.get("/")
def home():
    return {"message": "Բարի գալուստ E-Commerce Analytics API: Օգտագործեք /revenue կամ /metrics հասցեները:"}
@app.get("/revenue")
def get_revenue():
    conn = sqlite3.connect("ecommerce.db")
    cursor = conn.cursor()
    cursor.execute("SELECT price FROM events WHERE action = 'purchase'")
    rows = cursor.fetchall()
    conn.close()
    total_revenue = sum([row[0] for row in rows])

    return {
        "status": "success",
        "total_revenue_usd": total_revenue,
        "total_sales_count": len(rows)
    }
@app.get("/metrics")
def get_system_metrics():
    cpu_usage = psutil.cpu_percent()  # Չափում է CPU-ի (պրոցեսորի) ծանրաբեռնվածությունը %-ով
    ram_usage = psutil.virtual_memory().percent  # Չափում է RAM-ի (օպերատիվ հիշողության) ծանրաբեռնվածությունը %-ով
    
    return {
        "cpu_usage_percent": cpu_usage,
        "ram_usage_percent": ram_usage,
        "system_status": "OK" if cpu_usage < 80 else "HIGH_LOAD"
    }