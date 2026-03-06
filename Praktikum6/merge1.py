# ==========================================================
# Nama  : Natasha Umaiza
# NIM   : J0403251046
# Kelas: TPL A1
# Materi: Merge Sort - Ascending
# ==========================================================

def merge_sort_ascending(list_angka):

    # jika jumlah data lebih dari 1 maka list akan dibagi
    # ini adalah bagian dari konsep divide and conquer
    if len(list_angka) > 1:
        # menentukan titik tengah list
        tengah = len(list_angka) // 2
        # membagi list menjadi dua bagian
        bagian_kiri = list_angka[:tengah]
        bagian_kanan = list_angka[tengah:]
        # memanggil fungsi rekursif untuk mengurutkan bagian kiri dan kanan
        merge_sort_ascending(bagian_kiri)
        merge_sort_ascending(bagian_kanan)

        # variabel penanda indeks
        i = 0  # indeks bagian kiri
        j = 0  # indeks bagian kanan
        k = 0  # indeks list utama

        # membandingkan elemen dari dua bagian yang sudah dipecah
        while i < len(bagian_kiri) and j < len(bagian_kanan):

            # jika nilai kiri lebih kecil atau sama dengan kanan
            # maka dimasukkan ke list utama terlebih dahulu
            if bagian_kiri[i] <= bagian_kanan[j]:
                list_angka[k] = bagian_kiri[i]
                i = i + 1
            else:
                list_angka[k] = bagian_kanan[j]
                j = j + 1

            # pindah ke posisi berikutnya di list utama
            k = k + 1

        # jika masih ada sisa elemen di bagian kiri
        # maka langsung dipindahkan ke list utama
        while i < len(bagian_kiri):
            list_angka[k] = bagian_kiri[i]
            i = i + 1
            k = k + 1

        # jika masih ada sisa elemen di bagian kanan
        # maka langsung dipindahkan ke list utama
        while j < len(bagian_kanan):
            list_angka[k] = bagian_kanan[j]
            j = j + 1
            k = k + 1


# data yang akan diurutkan
data_nilai = [48, 15, 92, 33, 7, 61, 29, 80, 14]

# menjalankan fungsi merge sort
merge_sort_ascending(data_nilai)
print("Ascending:", data_nilai)