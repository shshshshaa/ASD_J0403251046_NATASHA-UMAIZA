# ==========================================================
# Nama  : Natasha Umaiza
# NIM   : J0403251046
# Kelas: TPL A1
# Materi: Quick Sort - Ascending
# ==========================================================

def quickSort(angka):
    # mulai proses quick sort dari index pertama sampai terakhir
    quickSortHelper(angka, 0, len(angka)-1)

def quickSortHelper(angka, awal, akhir):
    # kalau index awal masih lebih kecil dari akhir berarti masih ada yang harus diurutkan
    if awal < akhir:
        # cari posisi pivot setelah proses partition
        titik_bagi = partition(angka, awal, akhir)
        # urutkan bagian kiri pivot
        quickSortHelper(angka, awal, titik_bagi-1)
        # urutkan bagian kanan pivot
        quickSortHelper(angka, titik_bagi+1, akhir)

def partition(angka, awal, akhir):
    # pivot diambil dari elemen pertama
    pivot = angka[awal]
    # penanda kiri mulai dari setelah pivot
    kiri = awal + 1
    # penanda kanan dari elemen terakhir
    kanan = akhir
    
    selesai = False
    
    while not selesai:
        # geser penanda kiri selama nilainya masih lebih kecil/sama dengan pivot
        while kiri <= kanan and angka[kiri] <= pivot:
            kiri = kiri + 1
        
        # geser penanda kanan selama nilainya masih lebih besar/sama dengan pivot
        while angka[kanan] >= pivot and kanan >= kiri:
            kanan = kanan - 1
        
        # kalau kanan sudah melewati kiri berarti proses berhenti
        if kanan < kiri:
            selesai = True
        else:
            # tukar elemen kiri dan kanan karena posisinya salah
            sementara = angka[kiri]
            angka[kiri] = angka[kanan]
            angka[kanan] = sementara
            
    # tukar pivot dengan posisi kanan supaya pivot ada di posisi yang benar
    sementara = angka[awal]
    angka[awal] = angka[kanan]
    angka[kanan] = sementara
    
    return kanan


# data yang akan diurutkan
nilai = [42, 18, 73, 9, 65, 27, 50, 31, 14]

# menjalankan fungsi quick sort
quickSort(nilai)
print("Ascending:", nilai)