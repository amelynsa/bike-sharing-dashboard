
# **🚴‍♂️ Bike Sharing Index (Hourly Data) ⏳**  

Dashboard ini menyajikan analisis data peminjaman sepeda berdasarkan data per jam menggunakan Streamlit.  

---

## **🛠 Setup Environment**  
### **1️⃣ Buat Folder dan Virtual Environment**  
```bash
mkdir bike_sharing_analysis
cd bike_sharing_analysis
python -m venv venv
```

### **2️⃣ Aktifkan Virtual Environment**  
- **Windows:**  
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux:**  
  ```bash
  source venv/bin/activate
  ```

### **3️⃣ Install Dependencies**  
Pastikan file `requirements.txt` tersedia, lalu jalankan:  
```bash
pip install -r requirements.txt
```

---

## **🚀 Menjalankan Aplikasi Streamlit**  
Jalankan perintah berikut untuk membuka dashboard analisis:  
```bash
streamlit run dashboard.py
```

---

## **📂 Struktur Folder Proyek**  
```plaintext
submission/
│── dashboard        
    ├── main_data.csv 
    ├── dashboard.py 
│── data/               
│   ├── hour.csv        
│── notebook.ipynb
│── README.md
│── requirements.txt
│── url.txt

```

---

## **📌 Dependencies (requirements.txt minimal)**  
Pastikan file `requirements.txt` berisi library yang diperlukan:
```
streamlit
pandas
matplotlib
seaborn
```

---
