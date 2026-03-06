# ==========================================================
# Nama  : Natasha Umaiza
# NIM   : J0403251046
# Kelas: TPL A1
# Materi: Bubble Sort - Ascending
# ==========================================================

def bubble_sort_asc(angka_list):
    # perulangan utama untuk menentukan berapa kali proses sorting dilakukan
    # setiap iterasi akan "mengamankan" satu elemen terbesar di bagian akhir list
    for batas in range(len(angka_list)-1,0,-1):
         # perulangan untuk membandingkan elemen yang bersebelahan
        for indeks in range(batas):
            # jika elemen sekarang lebih besar dari elemen setelahnya
            # berarti urutannya salah untuk ascending
            if angka_list[indeks] > angka_list[indeks+1]:
                 # proses menukar posisi dua elemen tersebut
                sementara = angka_list[indeks]
                angka_list[indeks] = angka_list[indeks+1]
                angka_list[indeks+1] = sementara

# data yang akan diurutkan
data_angka = [45, 12, 89, 33, 7, 56, 21, 90, 18]
# menjalankan fungsi bubble sort
bubble_sort_asc(data_angka)
print(data_angka)
