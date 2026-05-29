# =============================================
# Nama : Natasha Umaiza 
# NIM : J0403251046
# Kelas : A/A1
# Latihan 1. Memahami Konsep Spanning Tree
# =============================================

# Mendefinisikan daftar seluruh edge pada graph awal yang masih mengandung cycle
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Mendefinisikan contoh spanning tree yang valid
# Semua node saling terhubung tanpa membentuk cycle
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

print("Edge pada graph:")
for edge in edges:
    print(edge)

print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

# Membuktikan bahwa spanning tree selalu memiliki jumlah edge yang lebih sedikit
print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))


# ==========================================
# Jawaban Analisis:
# 1. Apa perbedaan graph awal dan spanning tree?
#    Graph awal dapat memiliki lebih banyak edge dan mengandung cycle, sedangkan spanning tree adalah subgraph atau bagian dari graph yang menghubungkan seluruh node tanpa membentuk cycle.
# 
# 2. Mengapa spanning tree tidak boleh memiliki cycle?
#    Karena untuk memastikan efisiensi. Cycle menunjukkan adanya edge tambahan yang tidak diperlukan untuk menghubungkan node, sehingga hal itu hanya akan menambah biaya atau kompleksitas.
#
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
#    Karena spanning tree hanya menggunakan edge secukupnya untuk memastikan semua node terhubung. Jumlah edge pada spanning tree selalu sama dengan jumlah node dikurangi satu.
