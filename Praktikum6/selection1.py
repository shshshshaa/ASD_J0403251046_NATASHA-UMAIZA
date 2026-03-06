# ==========================================================
# Nama  : Natasha Umaiza
# NIM   : J0403251046
# Kelas: TPL A1
# Materi: Selection Sort - Ascending
# ==========================================================

def selectionSort(angka):
    # Loop utama untuk menentukan posisi terakhir yang akan diisi
    # fillslot bergerak dari belakang ke depan
    for posisi_akhir in range(len(angka)-1, 0, -1):
        # diasumsikan sementara nilai terbesar ada di index pertama
        index_maks = 0
        
        # mencari nilai terbesar dari index 0 sampai posisi_akhir
        for cek in range(1, posisi_akhir+1):
            # jika ditemukan nilai yang lebih besar
            if angka[cek] > angka[index_maks]:
                # maka simpan index nilai terbesar tersebut
                index_maks = cek
        
        # setelah ketemu nilai terbesar,  tukar dengan elemen di posisi_akhir
        
        sementara = angka[posisi_akhir]
        angka[posisi_akhir] = angka[index_maks]
        angka[index_maks] = sementara
        
        # jadi setiap iterasi, angka terbesar akan pindah ke bagian paling kanan

# data yang akan diurutkan
nilai = [48, 12, 79, 5, 63, 27, 90, 34, 16]

# memanggil fungsi selection sort
selectionSort(nilai)
print("Ascending:", nilai)
