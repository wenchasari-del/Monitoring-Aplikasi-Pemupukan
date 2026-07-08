import streamlit as st
from streamlit_option_menu import option_menu

from database.db import create_table

from modules.dashboard import dashboard_page
from modules.input import input_page
from modules.monitoring import monitoring_page
from modules.laporan import laporan_page

create_table()

st.set_page_config(
    page_title="Dashboard Monitoring Pemupukan",
    page_icon="🌱",
    layout="wide"
)

selected = option_menu(
    None,
    ["Dashboard", "Input Data", "Monitoring", "Laporan"],
    icons=[
        "speedometer2",
        "clipboard-plus",
        "bar-chart",
        "file-earmark-excel"
    ],
    orientation="horizontal"
)

if selected == "Dashboard":
    dashboard_page()

elif selected == "Input Data":
    input_page()

elif selected == "Monitoring":
    monitoring_page()

elif selected == "Laporan":
    laporan_page()