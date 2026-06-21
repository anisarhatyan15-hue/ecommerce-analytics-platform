import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="E-Commerce Dashboard", layout="wide")
st.title("📊 Իրական Ժամանակի Վաճառքների Վահանակ")
st.write("Այս էջը ցույց է տալիս մեր խանութի ստատիստիկան ուղիղ տվյալների բազայից:")

def load_date():
    conn = sqlite3.connect("ecommerce.db")
    df = pd.read_sql_query("Select * FROM events",conn)
    conn.close()
    return df
df =  load_date()

if df.empty:
    st.warning("Տվյալների բազան դատարկ է: Սկզբում միացրեք generator.py-ն:")
else:
    purchases = df[df['action'] == 'purchase']
    total_revenue = purchases['price'].sum()
    total_orders = len(purchases)
    unique_users = df['user'].nunique()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Ընդհանուր Եկամուտը", value=f"${total_revenue:.2f}")
    with col2:
        st.metric(label="Ընհանուր Պատվերներ", value=total_orders)
    with col3:
        st.metric(label="Ակտիվ ՀաՃախորդներ", value=unique_users)
    # ՃԻՇՏ ՏԱՐԲԵՐԱԿԸ ԳԾԻ ՀԱՄԱՐ՝
    st.markdown("---")

    left_col,right_col = st.columns(2)

    with left_col:
        st.subheader("📦 Ամենաշատ վաճառված ապրանքները")
        prod_counts = purchases['product_name'].value_counts()
        st.bar_chart(prod_counts)

    with right_col:
        st.subheader("📈 Գործողությունների բաշխվածությունը")
        action_counts = df['action'].value_counts()
        st.bar_chart(action_counts)
        

    if st.button("🔄 Թարմացնել Տվյալները"):
        st.rerun()
