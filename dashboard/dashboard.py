import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("dashboard/main_data.csv", delimiter=",")

# Konversi kolom tanggal ke format datetime
df["dteday"] = pd.to_datetime(df["dteday"])

# Sidebar untuk filter interaktif
st.sidebar.header("Filter Data")
start_date = st.sidebar.date_input("Pilih tanggal mulai", df["dteday"].min())
end_date = st.sidebar.date_input("Pilih tanggal akhir", df["dteday"].max())

# Filter berdasarkan tanggal
filtered_df = df[(df["dteday"] >= pd.to_datetime(start_date)) & (df["dteday"] <= pd.to_datetime(end_date))]

# Pilihan filter cuaca
weather_options = df["weathersit"].unique()
selected_weather = st.sidebar.multiselect("Filter berdasarkan cuaca", weather_options, default=weather_options)

# Terapkan filter cuaca
filtered_df = filtered_df[filtered_df["weathersit"].isin(selected_weather)]

# Judul Dashboard
st.title("DASHBOARD PEMINJAMAN SEPEDA")
st.markdown("Dashboard ini menampilkan hasil analisis data terkait jumlah peminjaman sepeda berdasarkan berbagai faktor seperti cuaca dan tipe hari. Silakan gunakan panel samping untuk menampilkan data sesuai kebutuhan.")

# Pilihan halaman visualisasi
st.sidebar.header("Pilih Visualisasi")
visualization_type = st.sidebar.radio("Pilih tipe visualisasi", ["Cuaca", "Hari Kerja vs Akhir Pekan"])

if visualization_type == "Cuaca":
    # Visualisasi pengaruh cuaca terhadap peminjaman sepeda
    st.subheader("Pengaruh Cuaca terhadap Peminjaman Sepeda")
    weather_avg = filtered_df.groupby("weathersit")["cnt"].mean().reset_index()
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(x="weathersit", y="cnt", data=weather_avg, ax=ax)
    ax.set_xlabel("Cuaca (1=Cerah, 2=Mendung, 3=Hujan ringan, 4=Hujan lebat)")
    ax.set_ylabel("Rata-rata Peminjaman")
    st.pyplot(fig)

elif visualization_type == "Hari Kerja vs Akhir Pekan":
    # Halaman Hari Kerja vs Akhir Pekan
    st.subheader("Peminjaman Sepeda: Hari Kerja vs Akhir Pekan")

    # Filter hari kerja dan akhir pekan
    st.sidebar.header("Filter Hari")
    day_type = st.sidebar.radio("Pilih tipe hari", ["Hari Kerja", "Akhir Pekan"])

    if day_type == "Hari Kerja":
        filtered_df = filtered_df[filtered_df["workingday"] == 1]
    else:
        filtered_df = filtered_df[filtered_df["workingday"] == 0]

    # Visualisasi hasil setelah filter
  
    avg_rentals = filtered_df.groupby("workingday")["cnt"].mean().reset_index()
    avg_rentals["workingday"] = avg_rentals["workingday"].map({0: "Akhir Pekan", 1: "Hari Kerja"})
    
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(x="workingday", y="cnt", data=avg_rentals, ax=ax)
    ax.set_xlabel("Tipe Hari")
    ax.set_ylabel("Rata-rata Peminjaman Sepeda")
    st.pyplot(fig)
