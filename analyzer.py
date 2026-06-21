import sqlite3
import pandas as pd

def analyze_data():

    conn = sqlite3.connect("ecommerce.db")

    query = "SELECT * FROM events"

    df = pd.read_sql_query(query,conn)
    conn.close()

    if df.empty:
        print("Բազան դատարկ է: Սկզբում միացրու generator.py-ն:")
        return

    print("--- 📊 ՏՎՅԱԼՆԵՐԻ ՎԵՐԼՈՒԾՈՒԹՅՈՒՆ ---")

    print(f"Ընդհանուր գրանցված գործողությունների քանակը՝ {len(df)}\n")
    
    print("1. Գործողությունների բաշխվածությունը՝")
    print(df['action'].value_counts())
    print("-" * 30)

    purchases = df[df['action'] == 'purchase']

    total_revenue = purchases['price'].sum()
    print(f"2. Ընդհանուր ստացված եկամուտը՝ ${total_revenue}")
    print("-" * 30)

    print("3. Ամենաշատ վաճառված 3 ապրանքները՝")
    top_products = purchases['product_name'].value_counts().head(3)
    print(top_products)

if __name__ == "__main__":
    analyze_data()
    