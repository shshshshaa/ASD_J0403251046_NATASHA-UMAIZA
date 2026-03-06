#====================================
# Nama: Natasha Umaiza
# NIM: J0403251046
# Kelas: TPL A/P1
#====================================

# ==========================================================
# Contoh Rekursi 3:: Menjumlahkan Elemen List
# ==========================================================

def jumlah_list(data, index=0):
    # Base case
    # kondisi berhenti dari rekursi
    # Jika index sudah mencapai panjang data, maka fungsi akan mengembalikan 0
    if index == len(data):
        return 0
    
    # Recursive case
    # fungsi memanggil dirinya sendiri dengan index + 1
    # Setiap kali fungsi memanggil dirinya sendiri, nilai data[index] akan ditambahkan dengan hasil dari jumlah_list(data, index + 1)
    return data[index] + jumlah_list(data, index + 1)
# contoh pemanggilan fungsi
print(jumlah_list([2, 4, 6, 8]))  # Output: 20
