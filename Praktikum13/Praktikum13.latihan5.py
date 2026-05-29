# =============================================
# Nama : Natasha Umaiza 
# NIM : J0403251046
# Kelas : A/A1
# Latihan 5. Tugas Mandiri: Buat Program MST dengan Kasus Baru
# Pilihan: Kasus 2. Jaringan Komputer
# =============================================


# Daftar koneksi antar router beserta nilai bobotnya (misal: latency/biaya)
# Format: (Bobot, 'Router_Asal', 'Router_Tujuan')
edges_jaringan = [
    (3, 'RouterA', 'RouterB'),
    (2, 'RouterA', 'RouterC'),
    (5, 'RouterB', 'RouterD'),
    (1, 'RouterC', 'RouterD'),
    (4, 'RouterB', 'RouterC')
]

# Mengurutkan rute dari bobot terkecil sesuai syarat Kruskal
edges_jaringan.sort()

mst_jaringan = [] 
total_bobot = 0 
connected_router = set() 

# Mengevaluasi setiap jalur koneksi mulai dari yang teringan/termurah
for bobot, u, v in edges_jaringan:
    if u not in connected_router or v not in connected_router:
        mst_jaringan.append((u, v, bobot))
        total_bobot += bobot
        # Mencatat router ke dalam jaringan aktif
        connected_router.add(u)
        connected_router.add(v)

print("Topologi Jaringan Komputer Terpilih (MST):")
for edge in mst_jaringan:
    print(f"{edge[1]} - {edge[2]} (Bobot: {edge[0]})")
print("Total Bobot Minimum =", total_bobot)


# ==========================================
# Jawaban Analisis:
# 1. Kasus apa yang dipilih?
#    Kasus 2, yaitu Jaringan Komputer.
# 
# 2. Algoritma apa yang digunakan?
#    Algoritma Kruskal. Pendekatan ini dipilih karena sangat cocok untuk memilah nilai latency/biaya rute antar router dari yang terkecil.
# 
# 3. Edge mana saja yang dipilih dalam MST?
#    RouterC - RouterD (bobot 1), RouterA - RouterC (bobot 2), dan RouterA - RouterB (bobot 3).
# 
# 4. Berapa total bobot MST?
#    Total bobot minimum dari topologi jaringan ini adalah 6.
# 
# 5. Mengapa edge tertentu tidak dipilih?
#    Koneksi RouterB - RouterC (bobot 4) dan RouterB - RouterD (bobot 5) tidak dipilih. Jika ditambahkan, akan terjadi routing loop (cycle) karena semua router sebenarnya sudah saling berkomunikasi melalui jalur utama yang lebih efisien.
