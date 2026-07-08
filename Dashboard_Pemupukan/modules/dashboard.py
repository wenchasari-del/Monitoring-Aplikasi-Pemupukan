import streamlit as st
import plotly.express as px

from database.db import load_data


def dashboard_page():

    st.title("🌱 Dashboard Monitoring Pemupukan")
    st.image(
    "Pupuk.png",
    use_container_width=True
)
    st.markdown(
    """
    <h1 style='text-align:center;color:#1B5E20;'>
    🌱 Dashboard Monitoring Pemupukan
    </h1>

    <p style='text-align:center;font-size:18px;color:gray;'>
    Monitoring Operasional Pemupukan Kelapa Sawit
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

    df = load_data()

    if df.empty:
        st.warning("Belum ada data pemupukan.")
        return
        # ==========================
# FILTER
# ==========================

st.subheader("🔍 Filter Data")

col1, col2 = st.columns(2)

with col1:
    daftar_unit = ["Semua"] + sorted(df["unit"].unique().tolist())
    pilih_unit = st.selectbox("Unit", daftar_unit)

with col2:
    daftar_pupuk = ["Semua"] + sorted(df["jenis_pupuk"].unique().tolist())
    pilih_pupuk = st.selectbox("Jenis Pupuk", daftar_pupuk)

if pilih_unit != "Semua":
    df = df[df["unit"] == pilih_unit]

if pilih_pupuk != "Semua":
    df = df[df["jenis_pupuk"] == pilih_pupuk]

    # ==========================
    # KPI
    # ==========================

    total_pupuk = df["jumlah_pupuk"].sum()
    total_hk = df["hk"].sum()
    total_aplikasi = len(df)
    blok_aktif = df["blok"].nunique()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
    "🌱 Total Pupuk",
    f"{total_pupuk:,.0f} Kg"
)

c2.metric(
    "👷 Total HK",
    f"{total_hk}"
)

c3.metric(
    "📄 Total Aplikasi",
    total_aplikasi
)

c4.metric(
    "🌴 Blok Aktif",
    blok_aktif
)

    st.divider()

    # ==========================
    # GRAFIK
    # ==========================

    kiri, kanan = st.columns(2)

    with kiri:

        fig1 = px.bar(
            df,
            x="unit",
            y="jumlah_pupuk",
            color="unit",
            title="Jumlah Pupuk per Unit"
        )

        st.plotly_chart(fig1, use_container_width=True)

    with kanan:

        fig2 = px.pie(
            df,
            names="jenis_pupuk",
            values="jumlah_pupuk",
            hole=0.45,
            title="Komposisi Jenis Pupuk"
        )

        st.plotly_chart(fig2, use_container_width=True)

    st.divider()

    st.subheader("📋 Data Terbaru")

    st.dataframe(
        df.sort_values("tanggal", ascending=False),
        use_container_width=True,
        hide_index=True
    )