# Import library yang dibutuhkan
import pandas as pd
from google_play_scraper import reviews, Sort

# ID aplikasi untuk LINE di Play Store
app_id = 'jp.naver.line.android'

# Fungsi untuk mengambil ulasan dari Play Store
def get_reviews_from_playstore(app_id, total_reviews=30000, language='id', region='ID'):
    # List untuk menyimpan hasil ulasan
    all_reviews = []

    # Mengambil ulasan menggunakan google-play-scraper
    fetched_reviews, _ = reviews(
        app_id,
        lang=language,    # Bahasa Indonesia
        country=region,   # Lokasi Indonesia
        count=total_reviews,
        sort=Sort.RATING  # Urutkan berdasarkan rating
    )

    # Memproses hasil ulasan
    for item in fetched_reviews:
        all_reviews.append({
            'review': item['content'],   # Isi ulasan
            'rating': item['score'],     # Rating (1-5)
            'date': item['at'],        # Tanggal ulasan
            'username': item['userName'],     # Nama pengguna
        })

    # Mengubah list ulasan menjadi DataFrame
    df_reviews = pd.DataFrame(all_reviews)
    return df_reviews

# Bagian utama program
if __name__ == "__main__":
    # Jumlah ulasan yang ingin diambil
    review_count = 30000

    # Memanggil fungsi untuk scraping ulasan
    reviews_df = get_reviews_from_playstore(app_id, total_reviews=review_count)

    # Menyimpan hasil ulasan ke dalam file CSV
    reviews_df.to_csv('line_reviews.csv', index=False)
    print(f"Berhasil mengambil {len(reviews_df)} ulasan dan menyimpannya dalam file line_reviews.csv")