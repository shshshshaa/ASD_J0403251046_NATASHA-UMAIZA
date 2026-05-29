# =============================================
# Nama : Natasha Umaiza 
# NIM : J0403251046
# Kelas : A/A1
# Latihan 2. Implementasi Algoritma Kruskal
# =============================================

# Daftar edge direpresentasikan dengan format tuple: (bobot, node_awal, node_tujuan)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge dari bobot terkecil, yang merupakan syarat utama algoritma Kruskal
edges.sort()

mst = [] # Menyimpan hasil akhir rute Minimum Spanning Tree
total_weight = 0
connected = set() # Melacak node yang sudah terhubung untuk mencegah cycle

# Melakukan iterasi pada setiap edge yang telah diurutkan
for weight, u, v in edges:
    # Jika salah satu node belum terhubung, berarti aman untuk ditambahkan (tidak membentuk cycle)
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        # Menandai bahwa kedua node tersebut sudah masuk ke dalam jaringan
        connected.add(u)
        connected.add(v)

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
print("Total bobot =", total_weight)


# ==========================================
# Jawaban Analisis:
# 1. Edge mana yang dipilih pertama kali?
#    Edge (1, 'C', 'D') karena memiliki bobot terkecil.
# 
# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
#    Karena algoritma Kruskal memilih edge dengan bobot terkecil secara bertahap untuk meminimalkan total bobot pada hasil akhir.
# 
# 3. Berapa total bobot MST yang dihasilkan?
#    Total bobot yang dihasilkan adalah 6 (dari 1 + 2 + 3).
# 
# 4. Mengapa edge tertentu tidak dipilih?
#    Karena jika edge tersebut ditambahkan, maka akan membentuk cycle pada node-node yang sebelumnya sudah terhubung.
