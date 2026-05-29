# =============================================
# Nama : Natasha Umaiza 
# NIM : J0403251046
# Kelas : A/A1
# Latihan 4. Studi Kasus: Jaringan Kabel Antar Gedung
# =============================================


# Mendefinisikan daftar biaya pemasangan kabel antar gedung
# Format data: (Biaya_Pemasangan, 'Gedung_Asal', 'Gedung_Tujuan')
edges_gedung = [
    (1, 'GedungC', 'GedungD'),
    (2, 'GedungA', 'GedungC'),
    (3, 'GedungB', 'GedungD'),
    (4, 'GedungA', 'GedungB'),
    (5, 'GedungA', 'GedungD')
]

# Mengurutkan rute dari biaya termurah ke biaya termahal
edges_gedung.sort()

mst_gedung = [] 
total_biaya = 0 
connected_gedung = set() 

# Mengevaluasi setiap jalur berdasarkan urutan biaya termurah (Algoritma Kruskal)
for biaya, u, v in edges_gedung:
    # Memastikan penambahan jalur tidak membuat siklus/cycle antar gedung
    if u not in connected_gedung or v not in connected_gedung:
        mst_gedung.append((u, v, biaya))
        total_biaya += biaya
        # Mencatat gedung tersebut sebagai bagian dari jaringan
        connected_gedung.add(u)
        connected_gedung.add(v)

print("Jalur Kabel Minimum Terpilih (MST):")
for edge in mst_gedung:
    print(f"{edge[1]} - {edge[2]} (Biaya: {edge[0]})")
print("Total Biaya Minimum =", total_biaya)


# ==========================================
# Jawaban Analisis:
# 1. Algoritma apa yang digunakan?
#    Algoritma Kruskal. Karena struktur datanya menggunakan representasi list of edges, sehingga proses sorting bobot  dapat diimplementasikan dengan lebih mudah, efisien, dan langsung tanpa perlu membangun adjacency list.
# 
# 2. Edge mana saja yang dipilih?
#    GedungC - GedungD (biaya 1), GedungA - GedungC (biaya 2), dan GedungB - GedungD (biaya 3).
# 
# 3. Berapa total biaya minimum?
#    Total biaya minimumnya adalah 6.
# 
# 4. Mengapa MST cocok digunakan pada kasus ini?
#    Karena tujuan utamanya adalah menghubungkan seluruh gedung ke dalam satu jaringan dengan biaya instalasi kabel seminimal mungkin, tanpa memerlukan jalur memutar (cycle) yang hanya akan menambah biaya.
