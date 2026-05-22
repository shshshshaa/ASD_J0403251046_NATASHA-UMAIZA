# ====================================================
# Nama  : Natasha Umaiza
# NIM   : J0403251046
# Kelas : A/P1
#=====================================================

# ==========================================================
# Latihan 2: Implementasi Dijkstra
# ==========================================================

import heapq
# Weighted graph dengan bobot positif
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):
    # Fungsi untuk mencari jarak terpendek dari node start
    # ke seluruh node lain menggunakan algoritma Dijkstra.
    
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}
    # Jarak dari start ke start adalah 0
    distances[start] = 0
    # Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat, maka proses dilewati
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances

hasil = dijkstra(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)


# ==========================================================
# Jawaban Analisis:
# 1. Berapa jarak terpendek dari A ke B?
#    Jawab: 4
# 2. Berapa jarak terpendek dari A ke C?
#    Jawab: 2
# 3. Berapa jarak terpendek dari A ke D?
#    Jawab: 3
# 4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B?
#    Jawab: Karena total nilai bobot akumulatif edge A->C->D adalah 2 + 1 = 3, yang mana nilainya jauh lebih kecil dibanding total akumulatif A->B->D yaitu 4 + 5 = 9.
# 5. Apa fungsi priority_queue dalam algoritma Dijkstra?
#    Jawab: Berfungsi untuk menyimpan pasangan nilai (jarak, node) dengan mengurutkannya secara otomatis agar node dengan jarak terpendek sementara selalu diambil (diproses) lebih dulu (memenuhi prinsip greedy).
# 6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif?
#    Jawab: Dijkstra mengasumsikan bahwa setelah jarak ke suatu node divalidasi sebagai nilai terkecil (dikeluarkan dari queue), nilai tersebut sudah final dan tidak akan dievaluasi lagi. Jika terdapat bobot negatif, jarak tersebut masih bisa berkurang, sehingga asumsi greedy Dijkstra membuat perhitungan menjadi tidak akurat.
# ==========================================================