#==============================================================
# Praktikum 2: MembuatAdjacency List
# Nama: Natasha Umaiza
# NIM: J0403251046
# Kelas: A/A1
#==============================================================

def printAdjacencyList(graph):
    print("Adjacency List Representation:")
    
    # .items() digunakan untuk mengambil pasangan 'kunci' (node) dan 'nilai' (tetangganya)
    for node, neighbors in graph.items():
        print(f"{node} -> {neighbors}")

if __name__ == "__main__":
    # Key adalah node asal, Value adalah list node yang terhubung langsung  
    graph = {
        'A': ['B', 'C'], # Node A terhubung langsung dengan Node B dan C
        'B': ['A', 'D'], # Node B terhubung langsung dengan Node A dan D
        'C': ['A', 'D'], # Node C terhubung langsung dengan Node A dan D
        'D': ['B', 'C']  # Node D terhubung langsung dengan Node B dan C
    }

    printAdjacencyList(graph)