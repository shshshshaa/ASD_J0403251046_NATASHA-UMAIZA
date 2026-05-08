#==============================================================
# Praktikum 3: Konversi Adjacency Matrix ke Adjacency List
# Nama: Natasha Umaiza
# NIM: J0403251046
# Kelas: A/A1
#==============================================================

def matrix_to_list(matrix):
    # Menghitung jumlah node berdasarkan jumlah baris di matriks
    V = len(matrix) 
    
    #dictionary kosong untuk menyimpan hasil konversi
    adj_list = {}
    
    # Perulangan luar: Mengecek setiap baris (sebagai Node asal)
    for i in range(V):
        # Membuat list kosong untuk menampung tetangga dari node i
        adj_list[i] = [] 
        
        # Perulangan dalam: Mengecek setiap kolom pada baris i (sebagai Node Tujuan)
        for j in range(V):
            # Jika nilainya 1, berarti ada garis/koneksi antara node i dan node j
            if matrix[i][j] == 1:
                # Tambahkan node j ke dalam daftar tetangga node i
                adj_list[i].append(j)
                
    return adj_list

if __name__ == "__main__":
    # Matriks yang diberikan di soal Praktikum 3
    matrix = [
        [0, 1, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [0, 0, 1, 0]
    ]
    
    hasil_konversi = matrix_to_list(matrix)
    
    print("Hasil Konversi ke Adjacency List:")
    for node, neighbors in hasil_konversi.items():
        print(f"Node {node} -> {neighbors}")