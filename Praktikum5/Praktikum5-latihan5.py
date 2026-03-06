#====================================
# Nama: Natasha Umaiza
# NIM: J0403251046
# Kelas: TPL A/P1
#====================================

# ==========================================================
#Latihan 5: Studi Kasus Generator PIN
# ==========================================================

def buat_pin(panjang, hasil=""):
    # Base case
    # kondisi berhenti dari rekursi
    # Kalau panjang hasil sudah sama dengan n, maka fungsi akan mencetak hasil dan berhenti
    if len(hasil) == panjang:
        print("PIN:",hasil)
        return
    
    # Recursive call
    # fungsi memanggil dirinya sendiri dengan menambahkan angka dari 0 hingga 9 ke hasil
    for angka in ["0", "1", "2"]:
        buat_pin(panjang, hasil + angka)

#contoh penggunaan
buat_pin(3) # Output: Semua kombinasi PIN 3 digit dari 000 hingga 222

# ==========================================================
# Penjelasan: bagaimana cara mencegah angka yang sama muncul berulang?
# ==========================================================

# pada program di atas, angka boleh muncul berulang
# karena setiap rekursi selalu mencoba semua angka
# tanpa mengecek apakah angka tersebut sudah pernah dipakai.

# untuk mencegah angka yang sama muncul berulang,
# kita bisa menambahkan pengecekan sebelum memanggil rekursi,
# misalnya hanya menambahkan angka jika angka tersebut
# belum ada di dalam variabel "hasil".