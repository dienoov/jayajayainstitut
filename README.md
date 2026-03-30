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
Dashboard ini dibuat menggunakan Streamlit. Berikut adalah beberapa insight yang dapat diperoleh dari dashboard ini.
- Approved Units (1st & 2nd Semester): Visualisasi box plot untuk jumlah unit yang disetujui di semester pertama dan kedua.
  - Dropout memiliki median unit yang disetujui sangat rendah, dengan distribusi yang sangat lebar, artinya banyak mahasiswa dropout yang hampir tidak menyelesaikan unit sama sekali.
  - Graduate memiliki median sekitar 6 unit per semester dengan distribusi yang lebih rapat dan konsisten.
  - Pola ini menunjukkan bahwa jumlah unit yang berhasil diselesaikan bisa menjadi prediktor kuat.
- Grades (1st & 2nd Semester): Visualisasi box plot untuk nilai rata-rata di semester pertama dan kedua.
  - Dropout memiliki IQR yang sangat lebar (dari 0 hingga 12), dengan median sekitar 10–11. Hal ini menandakan variasi nilai yang ekstrem sebagian mendapat nilai baik, sebagian jelek.
  - Graduate memiliki distribusi lebih sempit dengan median sekitar 12–13, menunjukkan performa yang lebih stabil dan konsisten.
  - Nilai dropout tidak selalu rendah, namun variabilitasnya yang tinggi menunjukkan bahwa nilai bisa menjadi indikator risiko, terutama jika nilainya sangat rendah.
- Gender: Visualisasi bar chart untuk jenis kelamin mahasiswa.
  - Mahasiswa perempuan mendominasi kelompok Graduate secara signifikan.
  - Mahasiswa laki-laki menunjukkan rasio dropout yang lebih tinggi relatif terhadap jumlahnya.
  - Pola ini menunjukkan bahwa jenis kelamin bisa menjadi faktor yang mempengaruhi risiko dropout, dengan mahasiswa laki-laki lebih rentan terhadap risiko tersebut.
- Age at Enrollment: Visualisasi box plot untuk usia saat mendaftar.
  - Mayoritas mahasiswa mendaftar di usia 17–22 tahun.
  Mahasiswa yang lebih muda saat mendaftar cenderung lebih banyak yang lulus.
  - Mahasiswa berusia di atas 25 tahun memiliki proporsi dropout yang lebih tinggi.
  - Usia saat mendaftar bisa menjadi indikator risiko, dengan mahasiswa yang lebih tua cenderung memiliki risiko dropout yang lebih tinggi.
- Debtor Status: Visualisasi bar chart untuk status debitur mahasiswa.
  - Mahasiswa yang berstatus debitur (Yes) memiliki proporsi dropout yang jauh lebih tinggi dibanding graduate, menunjukkan tekanan finansial berhubungan kuat dengan dropout.
- Scholarship Holder: Visualisasi bar chart untuk status pemegang beasiswa mahasiswa.
  - Pemegang beasiswa mayoritas berada di kelompok Graduate, beasiswa tampaknya memberikan dukungan finansial yang signifikan untuk membantu mahasiswa menyelesaikan studi mereka.
- Tuition Fees Up to Date: Visualisasi bar chart untuk status pembayaran uang kuliah.
  - Mahasiswa yang tidak membayar uang kuliah tepat waktu sangat dominan di kelompok Dropout.
  - Sebaliknya, Graduate hampir semuanya membayar tepat waktu, menunjukkan fitur ini sebagai sinyal peringatan dini yang kuat.

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