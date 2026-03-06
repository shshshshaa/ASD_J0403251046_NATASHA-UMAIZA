# ==========================================================
# Nama  : Natasha Umaiza
# NIM   : J0403251046
# Kelas: TPL A1
# Materi: Latihan Soal- Kandidat
# Metode: Selection Sort - Descending
# ==========================================================

def selection_sort(nilai):
    # Loop untuk menggeser posisi pengurutan dari belakang ke depan
    for posisi_akhir in range(len(nilai)-1, 0, -1):
        # diasumsikan sementara nilai terkecil ada di index pertama
        index_min = 0
        # mencari nilai terkecil dari bagian list yang belum terurut
        for cek in range(1, posisi_akhir+1):
            if nilai[cek] < nilai[index_min]:
                index_min = cek
        
        # tukar nilai terkecil dengan elemen di posisi_akhir
        sementara = nilai[posisi_akhir]
        nilai[posisi_akhir] = nilai[index_min]
        nilai[index_min] = sementara
        
        # karena nilai terkecil selalu dipindah ke kanan,
        # maka nilai terbesar akan berada di kiri
        # hasil akhirnya urutan descending

# Data skor tes potensi akademik
skor_tes = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]
# Mengurutkan skor dari tertinggi ke terendah
selection_sort(skor_tes)
print("Skor setelah diurutkan (Descending):", skor_tes)

# Mengambil 5 skor tertinggi
lima_terbaik = skor_tes[:5]
print("5 skor kandidat terbaik:", lima_terbaik)

# ==========================================================
# Jawaban soal
# ==========================================================

# 1. Lima skor tertinggi dari yang paling besar ke kecil
#    diambil dari 5 elemen pertama setelah data diurutkan

# 2. Menampilkan kandidat yang lolos
print("\nKandidat yang lolos:")

for i in range(5):
    print("Kandidat", i+1, "dengan skor:", lima_terbaik[i])


# ==========================================================
# Penjelasan singkat:
#
# Program ini mengurutkan skor tes menggunakan Selection Sort
# secara descending (dari nilai terbesar ke terkecil).
#
# Setelah semua data diurutkan, program mengambil 5 skor
# pertama karena itu adalah nilai tertinggi.
#
# Dari data:
# [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]
#
# Setelah diurutkan menjadi:
# [98, 89, 76, 68, 57, 43, 33, 22, 12, 9]
#
# Maka 5 kandidat terbaik adalah:
# 98, 89, 76, 68, 57
# ==========================================================