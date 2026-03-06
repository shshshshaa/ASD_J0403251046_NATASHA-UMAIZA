# ==========================================================
# Nama  : Natasha Umaiza
# NIM   : J0403251046
# Kelas: TPL A1
# Materi: Bubble Sort - Descending
# ==========================================================

def bubble_sort_desc(daftar_angka):
    # Loop luar untuk menentukan batas iterasi
    # setiap iterasi, elemen terbesar akan "naik" ke bagian kiri
    for batas_iterasi in range(len(daftar_angka)-1, 0, -1):
        # Loop dalam untuk membandingkan dua angka yang bersebelahan
        for posisi in range(batas_iterasi):
            # Jika angka kiri lebih kecil dari angka kanan
            # maka ditukar agar angka besar berada di depan
            if daftar_angka[posisi] < daftar_angka[posisi+1]:
                
                # proses pertukaran nilai
                sementara = daftar_angka[posisi]
                daftar_angka[posisi] = daftar_angka[posisi+1]
                daftar_angka[posisi+1] = sementara
                
# data yang akan diurutkan
nilai = [63, 15, 88, 29, 4, 71, 36, 92, 10]

# menjalankan fungsi bubble sort
bubble_sort_desc(nilai)
print("Descending:", nilai)
