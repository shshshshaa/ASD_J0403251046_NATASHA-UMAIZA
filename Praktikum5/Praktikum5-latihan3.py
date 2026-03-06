#====================================
# Nama: Natasha Umaiza
# NIM: J0403251046
# Kelas: TPL A/P1
#====================================

# ==========================================================
#Latihan 3: Mencari Nilai Maksimum
# ==========================================================

def cari_maks(data, indeks=0):
    # Base case
    # kondisi berhenti dari rekursi
    # Kalau indeks sudah mencapai panjang data, maka fungsi akan mengembalikan nilai negatif tak hingga sebagai pembanding
    if indeks == len(data):
        return data[indeks]  
    
    # Recursive call
    # fungsi memanggil dirinya sendiri dengan indeks + 1 untuk mencari maksimum dari sisa data
    # nilai maksimum dari sisa data disimpan dalam variabel maks_sisa
    maks_sisa = cari_maks(data, indeks + 1)
    
    # Setelah mendapatkan nilai maksimum dari sisa data, fungsi membandingkan elemen saat ini (data[indeks]) dengan nilai maksimum tersebut (maks_sisa)
    if data[indeks] > maks_sisa:
        return data[indeks]
    else:
        return maks_sisa
    
    #data yang akan dicari nilai maksimumnya disimpan dalam list angka, kemudian fungsi cari_maks dipanggil dengan list tersebut sebagai argumen. Hasilnya akan mencetak nilai maksimum dari list angka.
    angka = [3, 7, 2, 9, 5]
    
    #menjalankan fungsi cari_maks dengan list angka sebagai argumen dan mencetak hasilnya
    print("Nilai maksimum:", cari_maks(angka))

# ==========================================================
# Penjelasan: bagaimana jumlah kombinasi yang dihasilkan?
# ==========================================================

# setiap posisi memiliki 2 kemungkinan huruf,
# yaitu A atau B.

# karena setiap langkah bercabang menjadi 2 kemungkinan,
# maka jumlah total kombinasi adalah:
# 2^n

# contoh:
# n = 1 → 2 kombinasi (A, B)
# n = 2 → 4 kombinasi (AA, AB, BA, BB)
# n = 3 → 8 kombinasi

# jadi semakin besar nilai n,
# jumlah kombinasi akan bertambah secara eksponensial.