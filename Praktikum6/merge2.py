# ==========================================================
# Nama  : Natasha Umaiza
# NIM   : J0403251046
# Kelas: TPL A1
# Materi: Merge Sort - Descending
# ==========================================================


def merge_sort_desc(daftar_data):
    # jika jumlah elemen lebih dari 1 maka list akan dibagi
    # ini bagian dari konsep divide and conquer
    if len(daftar_data) > 1:
        # menentukan titik tengah list
        tengah = len(daftar_data) // 2
        # membagi list menjadi dua bagian
        bagian_kiri = daftar_data[:tengah]
        bagian_kanan = daftar_data[tengah:]

        # memanggil fungsi yang sama untuk mengurutkan bagian kiri dan kanan
        merge_sort_desc(bagian_kiri)
        merge_sort_desc(bagian_kanan)

        # indeks untuk masing-masing bagian
        i = 0  # indeks bagian kiri
        j = 0  # indeks bagian kanan
        k = 0  # indeks list utama

        # membandingkan elemen dari dua bagian
        while i < len(bagian_kiri) and j < len(bagian_kanan):
            # karena ingin descending, angka yang lebih besar
            # akan dimasukkan terlebih dahulu
            if bagian_kiri[i] >= bagian_kanan[j]:
                daftar_data[k] = bagian_kiri[i]
                i = i + 1
            else:
                daftar_data[k] = bagian_kanan[j]
                j = j + 1

            # pindah ke posisi berikutnya di list utama
            k = k + 1

        # jika masih ada sisa elemen di bagian kiri
        # maka langsung dipindahkan ke list utama
        while i < len(bagian_kiri):
            daftar_data[k] = bagian_kiri[i]
            i = i + 1
            k = k + 1

        # jika masih ada sisa elemen di bagian kanan
        # maka langsung dipindahkan ke list utama
        while j < len(bagian_kanan):
            daftar_data[k] = bagian_kanan[j]
            j = j + 1
            k = k + 1


# data yang akan diurutkan
nilai_data = [61, 14, 87, 32, 9, 55, 28, 90, 17]

# menjalankan fungsi merge sort
merge_sort_desc(nilai_data)
print("Descending:", nilai_data)