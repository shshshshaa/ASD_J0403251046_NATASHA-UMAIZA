# ====================================================
# Nama  : Natasha Umaiza
# NIM   : J0403251046
# Kelas : A/P1
#=====================================================

# ==========================================================
# Latihan 5: Studi Kasus Program Shortest Path (Antar Kota)
# ==========================================================

import heapq
# 1. Representasi graph berbobot menggunakan dictionary
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}

# 2. Fungsi Dijkstra
def dijkstra(graph, start):
    # Inisialisasi jarak setiap node dengan tak terhingga
    distances = {node: float('inf') for node in graph}
    # Jarak menuju node awal adalah 0
    distances[start] = 0
    # Masukkan node awal ke dalam priority queue
    pq = [(0, start)]

    while pq:
        # Ambil node dengan jarak paling kecil
        current_distance, current_node = heapq.heappop(pq)

        # Hindari memproses ulang node jika sudah ada rute yang lebih singkat
        if current_distance > distances[current_node]:
            continue

        # Proses iterasi seluruh tetangga
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # Proses relaksasi dan penambahan antrean jika ada rute lebih pendek
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                
    return distances

# 3. Input penentuan node awal
node_awal = 'Bogor'

# 4. Memanggil algoritma untuk output
hasil = dijkstra(graph, node_awal)

# Format Output Yang Diharapkan Sesuai Modul
print(f"Jarak terpendek dari {node_awal}:")
for kota, jarak in hasil.items():
    print(f"{node_awal} -> {kota} = {jarak}")


# ==========================================================
# Jawaban Analisis:
# 1. Node awal yang digunakan apa?
#    Jawab: Node 'Bogor'.
# 2. Node mana yang memiliki jarak paling kecil dari node awal?
#    Jawab: Node 'Depok' dengan total jarak = 2.
# 3. Node mana yang memiliki jarak paling besar dari node awal?
#    Jawab: Node 'Bandung' dengan total jarak = 8.
# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.
#    Jawab: 
#    - Algoritma dimulai di node Bogor (jarak = 0). Priority queue mengecek tetangga Bogor yaitu Jakarta (5) dan Depok (2).
#    - Karena Depok memiliki jarak terkecil, algoritma mengunjungi Depok.
#    - Dari Depok, dicek tetangganya: rute baru ke Jakarta menjadi 2(Depok) + 2(Bobot Depok->Jkt) = 4 (Lebih kecil dari 5, maka jarak Jakarta diperbarui menjadi 4). Lalu dicek rute ke Bandung menjadi 2(Depok) + 6(Bobot Depok->Bdg) = 8.
#    - Kemudian algoritma beralih memproses Jakarta yang saat ini bernilai (4). Dicek rute ke Bandung melalui Jakarta yaitu 4(Jakarta) + 7(Bobot Jkt->Bdg) = 11.
#    - Karena jarak baru ke Bandung (11) lebih besar dibanding jarak yang sudah tercatat (8), nilai ditolak.
#    - Program berakhir dan jarak minimum ditemukan.
# ==========================================================