# ==========================================================
# Nama  : Natasha Umaiza
# NIM   : J0403251046
# Kelas: TPL A1
# Materi: Quick Sort - Descending
# ==========================================================

def quickSort(angka):
    # Memanggil fungsi helper untuk memulai proses quick sort
    quickSortHelper(angka, 0, len(angka)-1)

def quickSortHelper(angka, awal, akhir):
    # Jika posisi awal masih lebih kecil dari akhir,
    # berarti masih ada bagian list yang perlu diurutkan
    if awal < akhir:
        # Menentukan titik pivot setelah proses partition
        titik = partition(angka, awal, akhir)
        # Mengurutkan bagian kiri pivot secara rekursif
        quickSortHelper(angka, awal, titik-1)
        # Mengurutkan bagian kanan pivot secara rekursif
        quickSortHelper(angka, titik+1, akhir)

def partition(angka, awal, akhir):
    # Pivot diambil dari elemen pertama
    pivot = angka[awal]
    # Penanda kiri dimulai dari setelah pivot
    kiri = awal + 1
    # Penanda kanan dimulai dari elemen terakhir
    kanan = akhir
    
    selesai = False
    
    # Proses pengaturan posisi elemen terhadap pivot
    while not selesai:
        
        # Geser penanda kiri selama nilai masih >= pivot
        # karena kita ingin urutan descending
        while kiri <= kanan and angka[kiri] >= pivot:
            kiri = kiri + 1
        
        # Geser penanda kanan selama nilai masih <= pivot
        while angka[kanan] <= pivot and kanan >= kiri:
            kanan = kanan - 1
        
        # Jika penanda kanan sudah melewati kiri maka berhenti
        if kanan < kiri:
            selesai = True
        else:
            # Tukar elemen kiri dan kanan karena posisinya salah
            sementara = angka[kiri]
            angka[kiri] = angka[kanan]
            angka[kanan] = sementara
    
    # Tukar posisi pivot dengan elemen pada posisi kanan
    sementara = angka[awal]
    angka[awal] = angka[kanan]
    angka[kanan] = sementara
    
    # Mengembalikan posisi pivot yang baru
    return kanan


# Data yang akan diurutkan
nilai = [48, 12, 79, 5, 63, 27, 90, 34, 16]

# Memanggil fungsi quick sort
quickSort(nilai)
print("Descending:", nilai)
