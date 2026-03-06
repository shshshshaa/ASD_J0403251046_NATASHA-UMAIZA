# ==========================================================
# Nama  : Natasha Umaiza
# NIM   : J0403251046
# Kelas: TPL A1
# Materi: Selection Sort - Descending
# ==========================================================

def selectionSort(angka):
    # Loop utama untuk menentukan posisi terakhir yang akan diisi
    # posisi ini bergerak dari belakang ke depan
    for posisi_akhir in range(len(angka)-1, 0, -1):
        # diasumsikan sementara nilai terkecil ada di index pertama
        index_min = 0
        
        # mencari nilai terkecil dari index 0 sampai posisi_akhir
        for cek in range(1, posisi_akhir+1):
            # jika ditemukan nilai yang lebih kecil
            if angka[cek] < angka[index_min]:
                # simpan index nilai terkecil tersebut
                index_min = cek
        
        # setelah ketemu nilai terkecil, kita tukar dengan elemen di posisi_akhir
        sementara = angka[posisi_akhir]
        angka[posisi_akhir] = angka[index_min]
        angka[index_min] = sementara
        
        # jadi setiap iterasi, nilai terkecil akan dipindahkan ke bagian kanan
        # hasil akhirnya membuat urutan dari besar ke kecil (descending)

# data yang akan diurutkan
nilai = [48, 12, 79, 5, 63, 27, 90, 34, 16]

# memanggil fungsi selection sort
selectionSort(nilai)
print("Descending:", nilai)