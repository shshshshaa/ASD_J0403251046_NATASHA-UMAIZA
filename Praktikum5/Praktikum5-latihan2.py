#====================================
# Nama: Natasha Umaiza
# NIM: J0403251046
# Kelas: TPL A/P1
#====================================

# ==========================================================
#Latihan 2: Tracing Rekursi
# ==========================================================

def countdown(n):
    # Base case
    # kondisi berhenti dari rekursi
    # Kalau n = 0, maka fungsi akan mencetak "Selesai" dan berhenti
    if n == 0:
        print("Selesai")
        return
   
    #bagian ini dijalankan saat fungsi pertama kali masuk
    print("Masuk:", n)      
    
    # Recursive call
    # fungsi memanggil dirinya sendiri dengan n-1
    countdown(n - 1)        
   
    #bagian ini dijalankan setelah fungsi rekursi selesai dan mulai kembali ke fungsi sebelumnya
    print("Keluar:", n)     

# ==========================================================
# Mengapa output "Keluar" muncul terbalik?
# ==========================================================

# karena pada rekursi, pemanggilan fungsi disimpan di dalam stack.
# stack bekerja dengan prinsip LIFO (Last In First Out),
# artinya yang terakhir masuk akan keluar lebih dulu.