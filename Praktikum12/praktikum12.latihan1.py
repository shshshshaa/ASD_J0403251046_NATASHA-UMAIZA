# ====================================================
# Nama  : Natasha Umaiza
# NIM   : J0403251046
# Kelas : A/P1
#=====================================================

# ==========================================================
# Latihan 1: Weighted Graph dan Perhitungan Jalur
# ==========================================================

# Representasi weighted graph menggunakan dictionary bersarang
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

# Menghitung dua kemungkinan jalur dari A ke D
jalur_1 = graph['A']['B'] + graph['B']['D']
jalur_2 = graph['A']['C'] + graph['C']['D']

print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)

if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")


# ==========================================================
# Jawaban Analisis:
# 1. Berapa total bobot jalur A->B->D?
#    Jawab: Total bobotnya adalah 9 (4 + 5).
# 2. Berapa total bobot jalur A->C->D?
#    Jawab: Total bobotnya adalah 3 (2 + 1).
# 3. Jalur mana yang dipilih sebagai jalur terpendek?
#    Jawab: Jalur A -> C -> D.
# 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit?
#    Jawab: Karena pada weighted graph, yang menjadi faktor penentu (biaya/waktu) adalah total akumulasi bobot (weight) dari setiap edge yang dilalui, bukan jumlah langkah atau edge-nya. Sebuah rute yang memutar dengan banyak edge bisa saja lebih murah biayanya dibanding rute langsung jika total bobotnya lebih kecil.
# ==========================================================