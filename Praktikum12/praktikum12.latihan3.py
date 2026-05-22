# ====================================================
# Nama  : Natasha Umaiza
# NIM   : J0403251046
# Kelas : A/P1
#=====================================================

# ==========================================================
# Latihan 3: Implementasi Bellman-Ford
# ==========================================================

# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    # Fungsi untuk mencari jarak terpendek dari node start
    # ke seluruh node lain menggunakan algoritma Bellman-Ford.
    
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}
    # Jarak dari start ke start adalah 0
    distances[start] = 0

    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):
        # Periksa semua edge
        for node in graph:
            for neighbor, weight in graph[node].items():
                # Jika jarak ke node saat ini sudah diketahui,
                # dan ditemukan jarak yang lebih kecil ke neighbor,
                # maka lakukan update jarak
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    
    return distances

hasil = bellman_ford(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)


# ==========================================================
# Jawaban Analisis:
# 1. Berapa bobot langsung dari A ke B?
#    Jawab: 5
# 2. Berapa total bobot jalur A->C->B?
#    Jawab: 2 (didapat dari 4 + (-2))
# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
#    Jawab: Jalur memutar dari A -> C -> B.
# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
#    Jawab: Karena algoritma ini melakukan iterasi "relaksasi" mengevaluasi seluruh sisi/edge berulang kali. Sehingga, apabila terdapat jalur yang menjadi lebih murah akibat penambahan bobot negatif, sistem tetap akan mendeteksi dan memperbarui jarak terkecilnya dengan benar.
# 5. Apa yang dimaksud dengan proses relaksasi edge?
#    Jawab: Proses perbandingan untuk mengecek apakah biaya perjalanan ke suatu node tetangga dapat diubah menjadi lebih murah jika melalui node perantara (node saat ini). Jika lebih murah, maka nilai jarak tetangga tersebut akan di-update (direlaksasi).
# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
#    Jawab: Dijkstra menggunakan antrean prioritas (greedy) sehingga berjalan sangat cepat tetapi gagal pada graph yang memiliki bobot negatif. Sedangkan Bellman-Ford merelaksasi seluruh sisi secara berulang (dynamic programming) sehingga berjalan lebih lambat, tetapi akurat pada graph berbobot positif maupun negatif.
# ==========================================================