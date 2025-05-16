# ✒️ Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

---

## 🚀 Business Understanding

Jaya Jaya Maju adalah perusahaan multinasional dengan lebih dari 1000 karyawan. Saat ini, perusahaan menghadapi tantangan serius berupa tingginya attrition rate (lebih dari 10%), yang berdampak pada efisiensi kerja dan biaya operasional. Untuk mengatasi hal ini, tim HR membutuhkan analisis data yang mampu mengidentifikasi penyebab attrition rate (lebih dari 10%), sebuah dashboard untuk memantau kondisi tersebut, serta pendekatan prediktif untuk mengantisipasinya.

### 🔍 Permasalahan Bisnis

1. Tingginya attrition rate yang berpengaruh pada stabilitas dan biaya perusahaan.
2. Kurangnya pemahaman berbasis data terkait alasan karyawan keluar.
3. Tidak adanya dashboard yang memudahkan pemantauan faktor-faktor attrition.
4. Belum ada rekomendasi konkret untuk mengurangi attrition rate berdasarkan data.

### 📋 Cakupan Proyek

1. Eksplorasi dan pembersihan data karyawan yang tersedia.
2. Analisis eksploratif untuk menemukan pola dan hubungan antara attrition dan variabel lain.
3. Pembuatan model prediktif untuk mengestimasi kemungkinan karyawan keluar di masa depan dengan algoritma **XGBoost**.
4. Pembuatan business dashboard analisis attrition rate menggunakan **Metabase**
5. Penyusunan rekomendasi berbasis data untuk membantu tim HR menurunkan attrition rate.

---

## ⚙️ Persiapan

📂 Sumber data: [Dataset Jaya jaya maju](https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv)

Setup environment:

```bash
# Membuat virtual environment
python -m venv venv

# Aktivasi environment
# Windows
venv\Scripts\activate

# MacOS/Linux
source venv/bin/activate

# Install dependensi
pip install -r requirements.txt

```

---

## 📊 Business Dashboard

### Fitur Dashboard
- Summary: berisi **Total-karyawan**, **Total-Resign**, dan **Persen-Resign**

![](https://github.com/7z1x/Belajar-Penerapan-Data-Science/blob/60630c1f308820c24cb27521f6c2dde8f5f5b66e/image/summary.jpg)

- Struktur Organisasi: Distribusi karyawan berdasarkan **departemen**, **joblevel**, dan **jobrole**.

![](https://github.com/7z1x/Belajar-Penerapan-Data-Science/blob/60630c1f308820c24cb27521f6c2dde8f5f5b66e/image/organization%20review.jpg)

- Kepuasan dan Keterlibatan: Perbandingan **EnvironmentSatisfaction**, **JobInvolvement**, dan **JobSatisfaction** antara karyawan yang resign dan tidak resign.

![](https://github.com/7z1x/Belajar-Penerapan-Data-Science/blob/60630c1f308820c24cb27521f6c2dde8f5f5b66e/image/satisfaction.jpg)

- Faktor Demografis: Analisis attrition berdasarkan **Gender** dan **MarritalStatus**.

![](https://github.com/7z1x/Belajar-Penerapan-Data-Science/blob/60630c1f308820c24cb27521f6c2dde8f5f5b66e/image/gender%20dan%20status.jpg)

- Kondisi Kerja: Dampak lembur **OverTime** dan frekuensi perjalanan dinas **BusinessTravel**terhadap attrition rate.

![](https://github.com/7z1x/Belajar-Penerapan-Data-Science/blob/60630c1f308820c24cb27521f6c2dde8f5f5b66e/image/workload%20impact.jpg)

### ✅ Insight

- Summary: Dari total 1,470 karyawan, 179 telah mengundurkan diri (12.18% tingkat resign).
- Satisfaction Insight: Karyawan yang tidak resign memiliki kepuasan lingkungan, keterlibatan pekerjaan, dan kepuasan kerja yang lebih tinggi (sekitar 2.5-3) dibandingkan yang resign (sekitar 2.5).
- Gender & Status: Tingkat resign tertinggi pada karyawan lajang (30%), sedangkan perbedaan gender menunjukkan tingkat resign serupa (12.07% wanita, 12.24% pria).
- Organizational Overview: Departemen Sales memiliki tingkat resign tertinggi (14.8%), diikuti Human Resources (12%). Tingkat resign juga bervariasi berdasarkan peran pekerjaan, dengan Sales Representative dan Research Director menonjol.
- Workload Impact: Karyawan dengan overtime memiliki tingkat resign yang jauh lebih tinggi (23.56%) dibandingkan yang tidak (7.69%). Frequent business travel juga meningkatkan tingkat resign (sekitar 20%) dibandingkan non-travel atau travel rarely

### 🎥 Video
- [Link Video](https://drive.google.com/drive/folders/1mX5Y9gvlK_skZWqvj-7X08D04j3LlFDA?usp=sharing)

### 🔐 Akses Metabase (setup lokal)

Gunakan login berikut saat pertama kali setup:

- **Email**: `root@mail.com`
- **Password**: `root123`

  
---

## 🌟 Conclusion
Berdasarkan analisis data dan model prediksi yang dilakukan, ditemukan beberapa faktor utama yang memengaruhi keputusan karyawan untuk resign, antara lain: 
- status lembur (OverTime)
- level stock option (StockOptionLevel)
- jabatan (JobRole dan JobLevel)
- kepuasan terhadap lingkungan kerja (EnvironmentSatisfaction) dan
- keterlibatan kerja (JobInvolvement)
  
Karyawan yang tidak lembur, memiliki stock option lebih tinggi, serta job level yang lebih tinggi cenderung memiliki tingkat resign yang lebih rendah. Selain itu, karyawan yang sering melakukan perjalanan bisnis dan yang masih lajang menunjukkan kecenderungan berbeda dalam tingkat resign. Dengan demikian, perusahaan dapat lebih fokus pada faktor-faktor tersebut untuk menurunkan tingkat turnover dan meningkatkan retensi karyawan.

---

## 🎯 Rekomendasi Action Items

- Optimalkan Kebijakan Karyawan untuk Meningkatkan Retensi
  - Perusahaan perlu meninjau dan mengembangkan kebijakan terkait lembur, benefit (seperti stock option), serta kesejahteraan karyawan secara menyeluruh. Hal ini meliputi pemberian insentif yang adil bagi yang lembur, program stock option untuk meningkatkan loyalitas, serta upaya meningkatkan kepuasan dan keterlibatan karyawan melalui survei dan budaya kerja positif. Selain itu, perhatian khusus juga perlu diberikan kepada karyawan yang sering melakukan perjalanan bisnis, dengan menyediakan fleksibilitas jadwal dan dukungan logistik guna mengurangi stres dan risiko resign.
- Evaluasi dan Monitoring rutin melalui dashboard
  - Manfaatkan dashboard yang sudah ada untuk terus memantau kondisi karyawan dan mengidentifikasi risiko resign lebih awal.
- Integrasi Model Prediksi ke dalam Sistem HRIS untuk Deteksi Dini Risiko Attrition
  - Pasang model ini di sistem HRIS agar bisa mendeteksi karyawan yang berisiko resign dan cepat diatasi.
 
---
 
## 🗂️ Struktur Folder Proyek

```
submission/
│
├── dataset/
│   └── employee_data.csv
│
├── image/
│   └── gender dan status.jpg
│   └── organization review.jpg
│   └── satisfaction.jpg
│   └── summary.jpg
│   └── workload impact.jpg
│ 
├── model/
│   └── model_attrition_xgboost.pkl
│
├── metabase.db.mv.db (belum tau)
├── notebook.ipynb
├── notebook.py
├── requirements.txt
└── README.md
```

---

