import streamlit as st
from datetime import date

from database.db import tambah_data

def input_page():

    st.title("📝 Input Data Pemupukan")

    st.divider()

    with st.form("form_input"):

        col1, col2 = st.columns(2)

        with col1:

            tanggal = st.date_input(
                "Tanggal Aplikasi",
                date.today()
            )

            unit = st.selectbox(
                "Unit",
                [
                    "SKGE",
                    "SKLE",
                    "SKTE"
                ]
            )

            blok = st.text_input(
                "Blok",
                placeholder="Contoh : A01"
            )

            jenis_pupuk = st.selectbox(
                "Jenis Pupuk",
                [
                    "NPK",
                    "MOP",
                    "Urea",
                    "Dolomite",
                    "Rock Phosphate"
                ]
            )

        with col2:

            jumlah = st.number_input(
                "Jumlah Pupuk (Kg)",
                min_value=0.0,
                step=50.0
            )

            hk = st.number_input(
                "Jumlah HK",
                min_value=0,
                step=1
            )

            aplikasi = st.selectbox(
                "Jenis Aplikasi",
                [
                    "Manual",
                    "Broadcast",
                    "Pocket"
                ]
            )

        simpan = st.form_submit_button("💾 Simpan Data")

    if simpan:

        data = (
            str(tanggal),
            unit,
            blok,
            jenis_pupuk,
            jumlah,
            hk,
            aplikasi
        )

        tambah_data(data)

        st.success("✅ Data berhasil disimpan.")