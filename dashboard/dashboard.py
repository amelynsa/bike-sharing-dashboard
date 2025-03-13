import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi halaman Streamlit
st.set_page_config(page_title="Dashboard Peminjaman Sepeda", layout="wide")

# Load dataset
df = pd.read_csv("dashboard/main_data.csv", delimiter=",")

# Judul utama
st.title("Dashboard Analisis Peminjaman Sepeda")
st.markdown("""
Dashboard ini menyajikan analisis tentang pola peminjaman sepeda berdasarkan:
- **Kondisi cuaca**
- **Hari kerja vs akhir pekan**
""")

# Fungsi untuk visualisasi pengaruh cuaca terhadap peminjaman
def plot_weather_impact(df):
    weather_avg = df.groupby('weathersit')['cnt'].mean().reset_index()
    
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(x='weathersit', y='cnt', data=weather_avg, ax=ax)
    ax.set_title("Pengaruh Cuaca terhadap Peminjaman Sepeda")
    ax.set_xlabel("Cuaca (1=Cerah, 2=Mendung, 3=Hujan ringan, 4=Hujan lebat)")
    ax.set_ylabel("Rata-rata Peminjaman")
    st.pyplot(fig)

    # Menambahkan penjelasan setelah visualisasi
    st.markdown("""
    ### **📊 Analisis Pengaruh Cuaca terhadap Peminjaman Sepeda**
    - Cuaca memiliki dampak signifikan terhadap peminjaman sepeda.
    - Saat **cuaca buruk (hujan ringan atau hujan lebat)**, jumlah peminjaman sepeda cenderung menurun drastis.
    - Saat **cuaca cerah**, jumlah peminjaman meningkat.

    **Kesimpulan:**  
    - Perusahaan dapat **menyediakan jas hujan atau diskon** saat cuaca buruk untuk menarik pengguna.  
    - Pada hari dengan cuaca cerah, stok sepeda dapat ditingkatkan untuk memenuhi permintaan.  
    """)

# Fungsi untuk visualisasi pola peminjaman antara hari kerja dan akhir pekan
def plot_workday_pattern(df):
    workday_avg = df.groupby('workingday')['cnt'].mean().reset_index()
    
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(x='workingday', y='cnt', data=workday_avg, ax=ax)
    ax.set_title("Pola Peminjaman Sepeda: Hari Kerja vs Akhir Pekan")
    ax.set_xlabel("0 = Akhir Pekan, 1 = Hari Kerja")
    ax.set_ylabel("Rata-rata Peminjaman")
    st.pyplot(fig)

    # Menambahkan penjelasan setelah visualisasi
    st.markdown("""
    ### **📊 Analisis Peminjaman Sepeda: Hari Kerja vs Akhir Pekan**
    - Peminjaman sepeda lebih tinggi pada **hari kerja**, menunjukkan bahwa sepeda lebih banyak digunakan sebagai transportasi ke tempat kerja atau sekolah.
    - Pada **akhir pekan**, jumlah peminjaman sedikit menurun, kemungkinan lebih banyak digunakan untuk rekreasi.

    **Kesimpulan:**  
    - Perusahaan dapat **menyesuaikan stok sepeda berdasarkan hari** untuk menghindari kekurangan sepeda saat jam sibuk.  
    - Strategi promosi dapat dibuat untuk meningkatkan pemakaian sepeda di akhir pekan, seperti diskon atau event bersepeda.  
    """)

# Sidebar untuk memilih visualisasi
st.sidebar.header("Pilih Visualisasi")
viz_choice = st.sidebar.radio("Pilih Analisis:", 
                              ("Pengaruh Cuaca", "Hari Kerja vs Akhir Pekan"))

if viz_choice == "Pengaruh Cuaca":
    plot_weather_impact(df)
elif viz_choice == "Hari Kerja vs Akhir Pekan":
    plot_workday_pattern(df)
elif viz_choice == "Peminjaman per Jam":
    plot_hourly_pattern(df)
