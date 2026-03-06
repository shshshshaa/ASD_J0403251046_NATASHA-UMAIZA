# ==========================================================
# Nama  : Natasha Umaiza
# NIM   : J0403251046
# Kelas: TPL A1
# Materi: Insertion Sort - Ascending
# ==========================================================

def insertion_sort_ascending(angka):
    # perulangan dimulai dari indeks ke-1
    # karena elemen pertama dianggap sudah terurut
    for i in range(1, len(angka)):
      # nilai yang sedang diproses
        nilai_sekarang = angka[i]
        # posisi awal untuk membandingkan dengan elemen sebelumnya
        posisi = i
        # selama posisi masih lebih dari 0
        # dan nilai sebelumnya lebih besar dari nilai_sekarang
        # maka elemen tersebut digeser ke kanan
        while posisi > 0 and angka[posisi - 1] > nilai_sekarang:
            angka[posisi] = angka[posisi - 1]
            posisi = posisi - 1
        # setelah posisi yang tepat ditemukan,
        # nilai_sekarang dimasukkan ke posisi tersebut
        angka[posisi] = nilai_sekarang


# data yang akan diurutkan
data_angka = [41, 12, 85, 23, 7, 66, 39, 90, 14]

# menjalankan fungsi insertion sort
insertion_sort_ascending(data_angka)
print("Ascending:", data_angka)
