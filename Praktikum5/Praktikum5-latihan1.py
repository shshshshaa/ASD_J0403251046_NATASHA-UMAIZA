#====================================
# Nama: Natasha Umaiza
# NIM: J0403251046
# Kelas: TPL A/P1
#====================================

# ==========================================================
#Latihan 1: Rekursi Pangkat
# ==========================================================

def pangkat (a,n):
    # Base Case
    # Kondisi berhenti dari rekursi
    # Kalau pangkatnya 0, maka hasilnya 1
    # Jadi, jika n = 0, maka fungsi akan mengembalikan nilai 1
    if n == 0:
        return 1
    # Recursive Case
    # Kalau n bukan 0, fungsi akan memanggil dirinya sendiri dengan n-1
    # Setiap kali fungsi memanggil dirinya sendiri, nilai a akan dikalikan dengan hasil dari pangkat(a, n-1)
    # hasilnya adalah a dikalikan dengan hasil dari pangkat(a, n-1), yang pada akhirnya akan menghasilkan a^n
    return a * pangkat(a, n-1)
print(pangkat(2,4)) # Output: 16

# Penjelasan:
# fungsi pangkat(a, n) menghitung a^n menggunakan rekursi. Base case terjadi ketika n = 0, di mana fungsi mengembalikan 1. Untuk nilai n > 0, fungsi memanggil dirinya sendiri dengan n-1 dan mengalikan hasilnya dengan a, sehingga menghasilkan a^n.
# Contoh: pangkat(2, 4) akan menghitung 2^4 dengan cara 2 * pangkat(2, 3), kemudian 2 * (2 * pangkat(2, 2)), dan seterusnya hingga mencapai base case.
# Output dari pangkat(2, 4) adalah 16, karena 2^4 = 16.
