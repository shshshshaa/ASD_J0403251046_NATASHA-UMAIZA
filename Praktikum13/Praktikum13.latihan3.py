# =============================================
# Nama : Natasha Umaiza 
# NIM : J0403251046
# Kelas : A/A1
# Latihan 3. Implementasi Algoritma Prim
# =============================================



import heapq # Menggunakan Priority Queue untuk mempermudah pencarian bobot terkecil

# Graph direpresentasikan menggunakan dictionary (Adjacency List)
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):
    visited = set([start]) # Menandai node awal sebagai node yang sudah dikunjungi
    edges = []
    
    # Memasukkan semua edge dari node awal ke dalam antrean (heap)
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))
        
    mst = []
    total_weight = 0
    
    # Melakukan perulangan selama Priority Queue masih memiliki elemen
    while edges:
        # Mengambil edge dengan bobot terkecil dari heap
        weight, u, v = heapq.heappop(edges)
        
        # Jika node tujuan (v) belum dikunjungi, tambahkan ke dalam MST
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight
            
            # Memasukkan tetangga dari node tujuan ke dalam antrean jika belum dikunjungi
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))
                    
    return mst, total_weight

mst, total = prim(graph, 'A')

print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
print("Total bobot =", total)


# ==========================================
# Jawaban Analisis:
# 1. Node awal apa yang digunakan?
#    Dimulai dari node 'A'.

# 2. Edge mana yang dipilih pertama kali?
#    Edge dari 'A' ke 'C' dengan bobot 2.
# 
# 3. Bagaimana Prim menentukan edge berikutnya?
#    Algoritma Prim mengevaluasi semua edge yang terhubung dengan node-node yang sudah dikunjungi kemudian memilih edge dengan bobot terkecil yang menghubungkan ke node baru.
# 
# 4. Berapa total bobot MST yang dihasilkan?
#    Total bobot MST adalah 6.
# 
# 5. Apa perbedaan pendekatan Prim dan Kruskal?
#    Kruskal menggunakan pendekatan global dengan mengurutkan seluruh edge dan memilih dari yang terkecil. Sebaliknya, Prim menggunakan pendekatan lokal dengan memperluas tree secara bertahap dari satu node awal ke node tetangga terdekatnya.
