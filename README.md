## **Analisis Sentimen Review Aplikasi LINE di Play Store**  

Repository ini berisi **proses Analisis Sentimen** terhadap **30.000 data review aplikasi LINE** di Play Store menggunakan teknik **Machine Learning dan Deep Learning**. Tujuan utama dari analisis ini adalah untuk **mengklasifikasikan review** ke dalam **3 kategori sentimen**: **positif, netral, dan negatif**.  

Proses analisis dilakukan dalam **3 skema pelatihan berbeda**, dengan kombinasi algoritma, metode ekstraksi fitur, dan pembagian data yang bervariasi.  

---

## **Metodologi**
### 📌 **1. Menyiapkan Data**
Dataset yang digunakan terdiri dari **30.000 review aplikasi LINE**, dengan atribut:  
- **review** → Teks ulasan pengguna.  
- **rating** → Skor yang diberikan pengguna (1-5).  
- **date** → Tanggal dan waktu review dibuat.  
- **username** → Nama pengguna yang memberikan review.  

📌 **Preprocessing Data:**  
- Menghapus nilai kosong.  
- Konversi teks ke huruf kecil.  
- Pembersihan teks (penghapusan karakter khusus, simbol, dan emoji).  
- Labeling sentimen berdasarkan **rating dan kata kunci dalam review**.  

---

### 📌 **2. Eksperimen dengan 3 Skema Pelatihan**  

#### 🟢 **Skema 1: CNN + Tokenisasi & Padding (80/20)**  
- **Model**: **Convolutional Neural Network (CNN)**  
- **Ekstraksi Fitur**: **Tokenisasi & Padding**  
- **Pembagian Data**: **80% training, 20% testing**  
- **Penjelasan**:  
  - Data dikonversi ke **angka menggunakan tokenisasi**.  
  - Panjang teks diseragamkan dengan **padding**.  
  - CNN digunakan untuk menangkap pola dalam teks menggunakan **Conv1D, BatchNormalization, GlobalMaxPooling1D**.  

#### 🟡 **Skema 2: SVM + TF-IDF (70/30)**  
- **Model**: **Support Vector Machine (SVM) dengan kernel linear**  
- **Ekstraksi Fitur**: **TF-IDF (Term Frequency - Inverse Document Frequency)**  
- **Pembagian Data**: **70% training, 30% testing**  
- **Penjelasan**:  
  - Data dikonversi ke **vektor numerik menggunakan TF-IDF**.  
  - Model **SVM digunakan untuk klasifikasi berbasis margin maksimal**, yang bekerja baik pada teks.  

#### 🔵 **Skema 3: Random Forest + TF-IDF (80/20)**  
- **Model**: **Random Forest Classifier**  
- **Ekstraksi Fitur**: **TF-IDF**  
- **Pembagian Data**: **80% training, 20% testing**  
- **Penjelasan**:  
  - Data dikonversi ke **vektor numerik menggunakan TF-IDF**.  
  - Model **Random Forest dengan 100 pohon keputusan** digunakan untuk meningkatkan akurasi melalui **ensemble learning**.  

---

## 📊 **Evaluasi Model**
📌 Setiap model dievaluasi berdasarkan **akurasi pada training set dan testing set** dengan **target akurasi ≥ 92%**.  
📌 Jika model gagal mencapai target, dilakukan **penyesuaian parameter atau metode ekstraksi fitur**.  

📌 **Hasil Akurasi Model:**  
| Model  | Training Accuracy | Testing Accuracy |
|--------|------------------|------------------|
| **CNN (80/20)**  | 98.12% | 96.50% |
| **SVM (70/30)**  | 99.88% | 99.39% |
| **Random Forest (80/20)**  | 100% | 98.50% |

📌 **Analisis Hasil**:  
- Model **SVM** memberikan **hasil terbaik** dengan akurasi **99.39% pada testing set**.  
- Model **CNN** cukup baik tetapi memerlukan waktu komputasi lebih lama.  
- Model **Random Forest** memiliki **overfitting** pada training set tetapi tetap berkinerja baik.  

---

## 🚀 **Testing & Inference**
Setelah pelatihan selesai, model diuji dengan **review baru** untuk memprediksi sentimen (**negatif, netral, atau positif**).  

**🔹 Contoh Input Review:**  
> "Aplikasi ini sangat membantu saya dalam berkomunikasi dengan teman-teman. Fitur-fiturnya keren!"  

**🔹 Output Model:**  
✅ **Prediksi Sentimen: Positif**  

---

## 🛠 **Instalasi & Cara Menjalankan**
1️⃣ **Clone Repository Ini**  
```bash
git clone https://github.com/noviantisafitri/LINE-App-Review-Sentiment-Analysis.git
cd LINE-App-Review-Sentiment-Analysis
```
2️⃣ **Install Library yang Diperlukan**  
```bash
pip install -r requirements.txt
```
3️⃣ **Jalankan Notebook di Jupyter atau Colab**  
```bash
jupyter notebook
```
4️⃣ **Buka file `Sentimen Analysis.ipynb` dan jalankan semua sel kode**  

---
