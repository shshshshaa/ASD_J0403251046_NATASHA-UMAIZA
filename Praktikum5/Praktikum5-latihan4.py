#====================================
# Nama: Natasha Umaiza
# NIM: J0403251046
# Kelas: TPL A/P1
#====================================

# ==========================================================
#Latihan 4: Kombinasi Huruf
# ==========================================================

def kombinasi(n, hasil=""):
    # Base case
    # kondisi berhenti dari rekursi
    # Kalau panjang hasil sudah sama dengan n, maka fungsi akan mencetak hasil dan berhenti
    if len(hasil) == n:
        print(hasil)
        return
    
    # Recursive call
    # fungsi memanggil dirinya sendiri dengan menambahkan 'A' dan 'B' ke hasil
    kombinasi(n, hasil + "A")
    kombinasi(n, hasil + "B")

    #contoh penggunaan
kombinasi(2) # Output: AA, AB, BA, BB

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

