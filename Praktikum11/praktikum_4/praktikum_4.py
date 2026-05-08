#==============================================================
# Praktikum 4: Studi Kasus Peta Kota di Korea Selatan
# Nama: Natasha Umaiza
# NIM: J0403251046
# Kelas: A/A1
#==============================================================

def main():
    # ---------------------------------------------------------
    # 1. ADJACENCY LIST (DENGAN BOBOT/JARAK)
    # ---------------------------------------------------------
    print("=== REPRESENTASI ADJACENCY LIST ===")
    
    # Format: "Kota Asal": [("Kota Tujuan", Jarak)]
    graph_list = {
        "Seoul": [("Incheon", 30), ("Suwon", 35), ("Daejeon", 160)],
        "Incheon": [("Seoul", 30), ("Suwon", 40)],
        "Suwon": [("Seoul", 35), ("Incheon", 40), ("Daejeon", 130)],
        "Daejeon": [("Seoul", 160), ("Suwon", 130), ("Busan", 260)],
        "Busan": [("Daejeon", 260)]
    }
    
    for kota, koneksi in graph_list.items():
        print(f"Node {kota:<7} rute -> {koneksi}")
        
    print("\n" + "="*60 + "\n")

    # ---------------------------------------------------------
    # 2. ADJACENCY MATRIX (DENGAN BOBOT/JARAK)
    # ---------------------------------------------------------
    print("=== REPRESENTASI ADJACENCY MATRIX ===")
    
    cities = ["Seoul", "Incheon", "Suwon", "Daejeon", "Busan"]
    V = len(cities)
    
    # Inisialisasi matriks dengan angka 0 (0 berarti tidak ada jalur langsung)
    matrix = [[0 for _ in range(V)] for _ in range(V)]
    
    # Update fungsi add_edge agar bisa menerima parameter 'jarak'
    def add_edge(kota1, kota2, jarak):
        u = cities.index(kota1)
        v = cities.index(kota2)
        
        matrix[u][v] = jarak # Mengganti angka 1 menjadi angka jarak (km)
        matrix[v][u] = jarak # Jalur dua arah
        
    # Memasukkan rute beserta jarak aslinya (dalam km)
    add_edge("Seoul", "Incheon", 30)
    add_edge("Seoul", "Suwon", 35)
    add_edge("Seoul", "Daejeon", 160)
    add_edge("Incheon", "Suwon", 40)
    add_edge("Suwon", "Daejeon", 130)
    add_edge("Daejeon", "Busan", 260)
    
    # Menampilkan Matriks
    print("      Se    In    Su    Da    Bu") 
    for i in range(V):
        print(f"{cities[i][:2]:<4}", end="  ")
        for j in range(V):
            # Mencetak angka jarak (ditambah spasi biar rata tabelnya)
            print(f"{matrix[i][j]:<4}", end="  ") 
        print()

    # ---------------------------------------------------------
    # 3. PRINT DAFTAR NODE
    # ---------------------------------------------------------
    print("\n" + "="*60)
    print("=== DAFTAR NODE (VERTEX) ===")
    print("Berikut adalah daftar kota yang bertindak sebagai node:")
    for i, city in enumerate(cities):
        print(f"{i+1}. {city}")

    # ---------------------------------------------------------
    # 4. PRINT HUBUNGAN ANTAR NODE (EDGE)
    # ---------------------------------------------------------
    print("\n" + "="*60)
    print("=== HUBUNGAN ANTAR NODE (EDGE) ===")
    print("Berikut adalah daftar rute/koneksi antar kota beserta jaraknya:")
    
    # Menggunakan set untuk menghindari duplikasi print rute bolak-balik
    printed_edges = set()
    
    for kota_asal, koneksi_list in graph_list.items():
        for kota_tujuan, jarak in koneksi_list:
            # Mengurutkan nama kota agar rute A-B dan B-A dianggap edge yang sama
            edge = tuple(sorted([kota_asal, kota_tujuan]))
            
            if edge not in printed_edges:
                print(f"- {kota_asal} <---> {kota_tujuan} (Jarak: {jarak} km)")
                printed_edges.add(edge)
                
    print("="*60)

if __name__ == "__main__":
    main()