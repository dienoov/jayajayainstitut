# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Permasalahan Bisnis
- Tingginya angka dropout di berbagai program studi yang dimiliki institusi.
- Kurangnya informasi awal untuk mengidentifikasi siswa yang berisiko tidak lulus.
- Perlunya ada sistem preventif untuk meningkatkan kelulusan siswa.

### Cakupan Proyek
- Menganalisis data historis siswa untuk menemukan pola yang berhubungan dengan status akademik: Dropout, Enrolled (aktif), dan Graduate (lulus).
- Membangun dashboard untuk memvisualisasikan informasi siswa.
- Mengembangkan model machine learning untuk memprediksi status siswa di akhir masa studi.
- Menyediakan prototipe sistem prediksi berbasis web (Streamlit) yang memungkinkan pengguna untuk mendapatkan prediksi risiko dropout atau lulus

### Persiapan

Sumber data: [Jaya Jaya Institut](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md)

Setup environment:

- Jalankan perintah berikut di terminal.
```bash
python -m venv venv
```

- Aktifkan environment.
Windows
```bash
venv\Scripts\Activate
```
Mac/Linux
```bash
source venv/bin/activate
```

- Instal dependensi.
```bash
pip install -r requirements.txt
```

## Business Dashboard
Dashboard ini dibuat menggunakan Streamlit dan menampilkan beberapa visualisasi berikut.
- Distribusi Status Siswa: Dropout, Enrolled, Graduate.
- Distribusi Usia dan Gender: Visualisasi histogram dan pie chart.
- Rata-rata Nilai dan SKS: Boxplot nilai dan SKS semester 1 dan 2.
- Status Ekonomi & Beasiswa: Visualisasi Debtor dan Scholarship Holder.

Dashboard ini dapat diakses di
[https://jayajayainstitut-dashboard.streamlit.app/](https://jayajayainstitut-dashboard.streamlit.app/).

## Menjalankan Sistem Machine Learning
Prototype sistem prediksi dibangun dengan Streamlit dan model machine learning yang disimpan menggunakan Joblib.

Langkah menjalankan:
```bash
streamlit run prediction.py
```

Prototype kemudian akan berjalan di [http://localhost:8501](http://localhost:8501) dan menampilkan form input untuk fitur-fitur yang diperlukan untuk prediksi.

Prototype ini dapat diakses di
[https://jayajayainstitut-prediction.streamlit.app/](https://jayajayainstitut-prediction.streamlit.app/).

## Conclusion
- Berdasarkan hasil analisis data melalui exploratory data analysis (EDA) dan visualisasi pada dashboard, ditemukan bahwa faktor utama yang berkaitan dengan risiko dropout mahasiswa adalah performa akademik, yaitu jumlah mata kuliah yang disetujui (approved)dan nilai rata-rata semester. Di sisi lain, mahasiswa yang menerima beasiswa memiliki tingkat kelulusan yang lebih tinggi.
- Dari sisi pemodelan machine learning, model yang dikembangkan menunjukkan performa yang sangat baik dengan tingkat akurasi sebesar 92%, serta nilai precision, recall, dan F1-score yang tinggi di sekitar 90–94%. Hal ini menunjukkan bahwa model mampu mengklasifikasikan status siswa dengan cukup akurat dan konsisten.

### Rekomendasi Action Items
Beberapa tindakan yang bisa dilakukan Jaya Jaya Institut.
- Memberikan bimbingan khusus bagi siswa dengan prediksi risiko dropout tinggi.
- Memantau tren nilai dan SKS untuk mendeteksi penurunan performa akademik lebih awal.
- Mengintegrasikan dashboard ini ke sistem administrasi kampus untuk pemantauan real-time.