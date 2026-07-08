import streamlit as st
from database.db import load_data

def monitoring_page():

    st.title("📊 Monitoring Data Pemupukan")

    df = load_data()

    if df.empty:
        st.warning("Belum ada data.")
        return

    st.subheader("Data Pemupukan")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )