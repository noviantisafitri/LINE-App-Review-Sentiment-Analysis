# **Analisis Sentimen Review Aplikasi LINE menggunakan Deep Learning**

Proyek ini bertujuan untuk melakukan analisis sentimen pada review aplikasi LINE menggunakan deep learning. Model yang dikembangkan bertujuan untuk mengklasifikasikan sentimen ke dalam tiga kategori: **negatif, netral, dan positif**.

## **1. Dataset**
- Dataset terdiri dari **30.000 data** review aplikasi LINE.  
- Setiap review dikategorikan ke dalam **tiga kelas**:  
  - **Negatif** (0)  
  - **Netral** (1)  
  - **Positif** (2)  

- Dataset ini telah melalui proses **preprocessing** yang mencakup:
  - **Case folding** (mengubah teks menjadi huruf kecil)
  - **Tokenization** (memisahkan kata-kata dalam teks)
  - **Stopword removal** (menghapus kata-kata umum yang tidak memiliki makna signifikan)
  - **Stemming** (mengubah kata ke bentuk dasar)
  - **Ekstraksi fitur** menggunakan **TF-IDF / Word2Vec**.

## **2. Model Deep Learning**
Terdapat tiga skema pelatihan model yang telah diuji, dengan kombinasi metode ekstraksi fitur, algoritma, dan pembagian data:

| Percobaan | Algoritma | Ekstraksi Fitur | Pembagian Data | Akurasi Training | Akurasi Testing |
|-----------|-----------|----------------|----------------|------------------|----------------|
| 1 | LSTM | TF-IDF | 80/20 | XX% | XX% |
| 2 | BiLSTM | Word2Vec | 80/20 | XX% | XX% |
| 3 | CNN + LSTM | TF-IDF | 70/30 | XX% | XX% |

> **Catatan**: Hasil akurasi pada training dan testing akan diupdate setelah model mendapatkan hasil terbaik.

## **3. Model Training**
Model dilatih dengan kombinasi berbagai teknik optimasi:
- **Optimizer**: Adam
- **Loss Function**: Categorical Crossentropy
- **Batch Size**: 32 / 64 (tergantung eksperimen)
- **Epochs**: 10 - 50
- **Embedding**: Word2Vec / Glove (jika diterapkan)
- **Dropout**: Untuk menghindari overfitting

## **4. Cara Menjalankan Proyek**
### **a. Clone Repository**
```bash
git clone https://github.com/username/repository-name.git
cd repository-name
```

### **b. Install Dependencies**
Pastikan Python sudah terinstall, lalu jalankan:
```bash
pip install -r requirements.txt
```

### **c. Jalankan Training Model**
Buka Jupyter Notebook atau jalankan script berikut untuk training:
```bash
python train.py
```

### **d. Testing Model**
Untuk melakukan prediksi pada review baru:
```bash
python inference.py --text "Aplikasi ini sangat bagus dan membantu!"
```
Output:
```
Predicted Sentiment: Positif
```

## **5. Hasil dan Evaluasi**
- Model diuji dengan **akurasi minimum 85% pada testing set**.  
- Target utama: **Mencapai akurasi di atas 92% pada training dan testing set**.  
- Jika belum mencapai target, akan dilakukan **tuning hyperparameter dan eksperimen lebih lanjut**.
