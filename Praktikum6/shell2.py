# ==========================================================
# Nama  : Natasha Umaiza
# NIM   : J0403251046
# Kelas: TPL A1
# Materi: Shell Sort - Descending
# ==========================================================
def shellSort(angka):
    # Menentukan jarak awal (gap)
    # gap dimulai dari setengah panjang list
    jarak = len(angka) // 2
    # Selama gap masih lebih dari 0 maka proses sorting dilakukan
    while jarak > 0:   
        # Mengurutkan setiap kelompok data berdasarkan gap
        for awal in range(jarak):
            gapInsertionSort(angka, awal, jarak)
        # Setelah satu tahap selesai, gap diperkecil
        jarak = jarak // 2


def gapInsertionSort(angka, mulai, jarak):
    # Menelusuri elemen dengan interval gap
    for i in range(mulai + jarak, len(angka), jarak):
        # Menyimpan nilai yang sedang dicek
        nilai_sekarang = angka[i]
        # Menyimpan posisi awal
        posisi = i
        
        # Untuk descending:
        # jika elemen sebelumnya lebih kecil, maka digeser ke kanan
        while posisi >= jarak and angka[posisi-jarak] < nilai_sekarang:
            angka[posisi] = angka[posisi-jarak]
            posisi = posisi - jarak
        # Menempatkan nilai pada posisi yang benar
        angka[posisi] = nilai_sekarang

# Data yang akan diurutkan
nilai = [48, 12, 79, 5, 63, 27, 90, 34, 16]

# Memanggil fungsi shell sort
shellSort(nilai)
print("Descending:", nilai)