# ==========================================================
# Nama  : Natasha Umaiza
# NIM   : J0403251046
# Kelas: TPL A1
# Materi: Insertion Sort - Descending
# ==========================================================


def insertion_sort_desc(daftar_nilai):
    # perulangan dimulai dari indeks ke-1
    # karena elemen pertama dianggap sudah terurut
    for i in range(1, len(daftar_nilai)):
        # nilai yang sedang diproses
        nilai_sekarang = daftar_nilai[i]
        # posisi awal untuk melakukan perbandingan
        posisi = i
        # selama posisi masih lebih dari 0
        # dan nilai sebelumnya lebih kecil dari nilai_sekarang
        # maka elemen tersebut digeser ke kanan
        while posisi > 0 and daftar_nilai[posisi - 1] < nilai_sekarang:
            daftar_nilai[posisi] = daftar_nilai[posisi - 1]
            posisi = posisi - 1
        # setelah posisi yang tepat ditemukan,
        # nilai_sekarang dimasukkan ke posisi tersebut
        daftar_nilai[posisi] = nilai_sekarang


# data yang akan diurutkan
angka_data = [62, 14, 88, 29, 7, 51, 33, 95, 18]

# menjalankan fungsi insertion sort
insertion_sort_desc(angka_data)
print("Descending:", angka_data)
