# ====================================================
# Nama  : Natasha Umaiza
# NIM   : J0403251046
# Kelas : A/P1
#=====================================================

# ==========================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
# ==========================================================

import heapq
# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances

hasil = dijkstra(graph, 'Gerbang')

print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")


# ==========================================================
# Jawaban Analisis:
# 1. Lokasi mana yang paling dekat dari Gerbang?
#    Jawab: Kantin, dengan waktu tempuh 2 menit.
# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
#    Jawab: 7 menit (melalui rute Gerbang -> Kantin -> Lab -> Aula, yaitu 2 + 4 + 1).
# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
#    Jawab: Tidak selalu. Sebagai buktinya, jika dari Kantin ingin ke Aula, rute langsung butuh waktu 7 menit. Tetapi jika mengambil rute memutar (Kantin -> Lab -> Aula), waktu tempuh total justru lebih singkat yaitu 5 menit (4 + 1).
# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?
#    Jawab: Karena kasus perjalanan lokasi dengan bobot "waktu tempuh" memiliki jaminan bahwa nilainya selalu positif (tidak mungkin ada waktu tempuh yang bernilai minus/negatif). Sehingga algoritma Dijkstra sangat efisien dan optimal untuk kasus nyata semacam ini.
# ==========================================================