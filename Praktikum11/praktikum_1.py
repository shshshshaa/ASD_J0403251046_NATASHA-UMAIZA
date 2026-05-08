#==============================================================
# Praktikum 1: Membuat Adjacency Matrix
# Nama: Natasha Umaiza
# NIM: J0403251046
# Kelas: A/A1
#==============================================================

def createGraph(V, edges):
    # Membuat list 2 dimensi (matriks) ukuran V x V yang semuanya diisi angka 0
    mat = [[0 for _ in range(V)] for _ in range(V)]

    for it in edges:
        u = it[0] # Menyimpan angka node pertama ke dalam variabel u
        v = it[1] # Menyimpan angka node kedua (tujuan) ke dalam variabel v
        mat[u][v] = 1 # Menandai koordinat matriks [u][v] dengan angka 1 (tanda terhubung)
        mat[v][u] = 1 # Menandai koordinat sebaliknya [v][u] dengan 1 (karena undirected graph)

    return mat # Mengembalikan hasil matriks yang sudah terisi angka 1 dan 0

if __name__ == "__main__":
    V = 4 # Mendefinisikan total node, karena ada node 0, 1, 2, dan 3 (total 4)

    # Mendefinisikan daftar sisi/garis. 
    # Array [0, 1] artinya ada garis yang menghubungkan node 0 dan node 1.
    edges = [[0, 1], [0, 2], [1, 2], [2, 3]]

    # Memanggil fungsi createGraph lalu menyimpannya ke dalam variabel 'mat'
    mat = createGraph(V, edges)

    print("Adjacency Matrix Representation:")
    
    # Perulangan luar: untuk mencetak Baris ke-0 s/d ke-3
    for i in range(V):
        # Perulangan dalam: mencetak setiap Kolom pada baris tersebut
        for j in range(V):
            # Mencetak angka 0 atau 1 ke layar. 
            print(mat[i][j], end=" ")
        
        print()