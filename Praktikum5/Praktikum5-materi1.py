#====================================
# Nama: Natasha Umaiza
# NIM: J0403251046
# Kelas: TPL A/P1
#====================================

# ========================================================== 
# Contoh Rekursi 1: Faktorial 
# ========================================================== 

def faktorial(n): # Base case: berhenti ketika n = 0 
    if n == 0: 
        return 1 # Recursive case: masalah diperkecil menjadi faktorial(n-1) 
    return n * faktorial(n - 1) 
print(faktorial(5)) 

# Penjelasan:
# fungsi faktorial digunakan untuk menghitung nilai n!
# dimana rumus faktorial adalah:
# n! = n × (n-1) × (n-2) × ... × 1

# ketika faktorial(5) dijalankan,
# fungsi akan terus memanggil dirinya sendiri
# sampai mencapai base case.
