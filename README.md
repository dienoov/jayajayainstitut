# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Permasalahan Bisnis
- Tingginya angka dropout di berbagai program studi yang dimiliki institusi.
- Kurangnya informasi awal untuk mengidentifikasi siswa yang berisiko tidak lulus.
- Perlunya ada sistem preventif untuk meningkatkan kelulusan siswa.

### Cakupan Proyek
- Menganalisis data historis siswa untuk menemukan pola yang berhubungan dengan status akademik: Dropout dan Graduate.
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
- Berdasarkan hasil analisis data melalui exploratory data analysis (EDA) dan visualisasi pada dashboard, ditemukan bahwa beberapa fitur seperti jumlah unit yang disetujui di semester pertama dan kedua, nilai rata-rata, status debitur, status pemegang beasiswa, dan pembayaran uang kuliah tepat waktu memiliki korelasi yang kuat dengan status akademik mahasiswa. Mahasiswa yang memiliki approved units rendah, nilai yang sangat bervariasi, berstatus debitur, tidak memegang beasiswa, dan tidak membayar uang kuliah tepat waktu cenderung memiliki risiko lebih tinggi untuk melakukan dropout.
- Dari sisi pemodelan machine learning, model yang dikembangkan menunjukkan performa yang sangat baik dengan tingkat akurasi sebesar 92%, serta nilai precision, recall, dan F1-score yang tinggi di sekitar 90–94%. Model ini mampu memprediksi dengan baik mahasiswa yang berisiko untuk melakukan dropout maupun yang kemungkinan besar akan lulus, sehingga dapat menjadi alat yang efektif untuk institusi dalam mengidentifikasi dan memberikan intervensi kepada mahasiswa yang membutuhkan dukungan tambahan.

### Rekomendasi Action Items
Beberapa tindakan yang bisa dilakukan Jaya Jaya Institut.
- Approved units 1st & 2nd semester adalah prediktor paling dominan dalam model. Dari visualisasi box plot, mahasiswa Dropout memiliki median approved units mendekati 0–2 per semester, sedangkan Graduate konsisten di 6 unit. Artinya mahasiswa dengan approved units rendah berisiko sangat tinggi untuk dropout. 
  - Rekomendasi: Institusi membangun sistem dashboard early warning yang secara otomatis menandai mahasiswa dengan approved units rendah (misalnya di bawah 3 unit) pada semester pertama dan kedua. Mahasiswa yang teridentifikasi dapat segera diberikan intervensi seperti bimbingan akademik, konseling, atau dukungan tambahan untuk membantu mereka meningkatkan performa akademik.
- Tuition fees up to date memiliki korelasi kuat dengan status akademik. Mahasiswa yang tidak membayar tepat waktu sangat dominan di kelompok Dropout, sementara Graduate hampir semuanya membayar tepat waktu. Hal ini menunjukkan bahwa masalah finansial bisa menjadi faktor risiko utama untuk dropout.
  - Rekomendasi: Institusi perlu membuat skema cicilan atau penundaan pembayaran bagi mahasiswa yang memiliki tunggakan UKT, terutama bagi mereka yang menunjukkan tanda-tanda risiko akademik. Selain itu, institusi dapat meningkatkan komunikasi dengan mahasiswa mengenai pentingnya pembayaran tepat waktu dan menyediakan bantuan keuangan atau beasiswa tambahan bagi mereka yang mengalami kesulitan finansial.
- Scholarship holder menunjukkan bahwa pemegang beasiswa sangat dominan di kelompok Graduate. Beasiswa tampaknya memberikan dukungan finansial yang signifikan untuk membantu mahasiswa menyelesaikan studi mereka, sehingga menjadi faktor penting dalam meningkatkan tingkat kelulusan.
  - Rekomendasi: Institusi memperluas kriteria penerima beasiswa tidak hanya berbasis prestasi, tetapi juga berbasis risiko dropout (berdasarkan approved units, pembayaran UKT, dll). Dengan memberikan beasiswa kepada mahasiswa yang berisiko tinggi untuk dropout, institusi dapat memberikan dukungan finansial yang mereka butuhkan untuk tetap melanjutkan studi dan meningkatkan tingkat kelulusan secara keseluruhan.