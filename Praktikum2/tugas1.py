import os

# ==========================================================
# PATH FILE (AMAN MESKI PINDAH PC / FOLDER)
# ==========================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_STOK = os.path.join(BASE_DIR, "stok_barang.txt")

# ==========================================================
# BACA DATA DARI FILE
# ==========================================================
def baca_stok():
    stok = {}

    if not os.path.exists(FILE_STOK):
        return stok

    with open(FILE_STOK, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            if not baris:
                continue

            kode, nama, jumlah = baris.split(",")
            stok[kode] = {
                "nama": nama,
                "stok": int(jumlah)
            }

    return stok

# ==========================================================
# SIMPAN DATA KE FILE
# ==========================================================
def simpan_stok(stok):
    with open(FILE_STOK, "w", encoding="utf-8") as file:
        for kode, data in stok.items():
            file.write(f"{kode},{data['nama']},{data['stok']}\n")

# ==========================================================
# TAMPILKAN SEMUA BARANG
# ==========================================================
def tampilkan_semua(stok): #fungsi untuk menampilkan semua daftar barang dan stok nya
    if not stok:
        print("Stok barang kosong.")
        return

    print("\n=== DAFTAR STOK BARANG KOPERASI ===")
    print(f"{'Kode':<10} {'Nama Barang':<20} {'Stok':>5}")
    print("-" * 40)

    for kode, data in stok.items():
        print(f"{kode:<10} {data['nama']:<20} {data['stok']:>5}")

# ==========================================================
# CARI BARANG
# ==========================================================
def cari_barang(stok): #fungsi untuk mencari barang berdasarkan kodenya
    kode = input("Masukkan kode barang: ").strip()

    if kode in stok:
        print("\nData Barang")
        print("Kode :", kode)
        print("Nama :", stok[kode]["nama"])
        print("Stok :", stok[kode]["stok"])
    else:
        print("Barang tidak ditemukan")

# ==========================================================
# TAMBAH BARANG
# ==========================================================
def tambah_barang(stok): #fungsi untuk menambah barang
    kode = input("Kode barang baru: ").strip()

    if kode in stok:
        print("Kode sudah ada!")
        return

    nama = input("Nama barang: ").strip()

    try:
        jumlah = int(input("Stok awal: "))
    except ValueError:
        print("Stok harus angka!")
        return

    stok[kode] = {
        "nama": nama,
        "stok": jumlah
    }

    print("Barang berhasil ditambahkan")

# ==========================================================
# UPDATE STOK
# ==========================================================
def update_stok(stok): #fungsi untuk menambah atau mengurangi stok barang 
    kode = input("Kode barang: ").strip()

    if kode not in stok:
        print("Barang tidak ditemukan")
        return

    print("1. Tambah stok")
    print("2. Kurangi stok")
    pilihan = input("Pilih (1/2): ").strip()

    try:
        jumlah = int(input("Jumlah: "))
    except ValueError:
        print("Jumlah harus angka!")
        return

    if pilihan == "1":
        stok[kode]["stok"] += jumlah
        print("Stok berhasil ditambah")

    elif pilihan == "2":
        if stok[kode]["stok"] < jumlah:
            print("Stok tidak cukup")
        else:
            stok[kode]["stok"] -= jumlah
            print("Stok berhasil dikurangi")

    else:
        print("Pilihan tidak valid")

# ==========================================================
# PROGRAM UTAMA 
# ==========================================================
def main(): #fungsi menu utama untuk menjalankan semua fungsi menjadi sebuah program stok barang
    stok_barang = baca_stok()

    while True:
        print("\n=== MENU STOK KOPERASI ===")
        print("1. Tampilkan semua")
        print("2. Cari barang")
        print("3. Tambah barang")
        print("4. Update stok")
        print("5. Simpan data")
        print("0. Keluar")

        menu = input("Pilih menu: ").strip()

        if menu == "1":
            tampilkan_semua(stok_barang)

        elif menu == "2":
            cari_barang(stok_barang)

        elif menu == "3":
            tambah_barang(stok_barang)

        elif menu == "4":
            update_stok(stok_barang)

        elif menu == "5":
            simpan_stok(stok_barang)
            print("Data berhasil disimpan")

        elif menu == "0":
            simpan_stok(stok_barang)
            print("Program selesai")
            break

        else:
            print("Menu tidak valid")

# ==========================================================
# JALANKAN PROGRAM
# ==========================================================
if __name__ == "__main__": 
    main()
