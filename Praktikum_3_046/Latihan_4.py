# ==========================
# DEFINISI NODE UNTUK SINGLE LINKED LIST
# ==========================
class Node:
    def __init__(self, data):
        self.data = data      # Menyimpan nilai/data node
        self.next = None      # Penunjuk ke node berikutnya (default None)


# ==========================
# DEFINISI SINGLE LINKED LIST
# ==========================
class single_Linked_List:
    def __init__(self):
        self.head = None      # Menunjuk ke node pertama (head), default kosong

    # ======================
    # MENAMBAHKAN NODE BARU
    # ======================
    def append(self, data):
        new_node = Node(data)  # Membuat node baru dengan data

        # Jika list kosong, node baru menjadi head
        if not self.head:
            self.head = new_node
            return
        
        # Jika list tidak kosong, cari node terakhir
        temp = self.head
        while temp.next:      # Loop sampai node terakhir (next = None)
            temp = temp.next

        # Sambungkan node terakhir ke node baru
        temp.next = new_node

    # ======================
    # MENAMPILKAN ELEMEN LINKED LIST
    # ======================
    def display(self):
        # Jika list kosong
        if not self.head:
            print("kosong")
            return
        
        temp = self.head  # Mulai dari head
        while temp:       # Loop sampai node terakhir
            print(temp.data, end=" -> ")  # Tampilkan data node
            temp = temp.next
        print("null")     # Tanda akhir linked list

    # ======================
    # MENGGABUNGKAN DUA SINGLE LINKED LIST
    # ======================
    def merge(self, list2):
        # Jika list pertama kosong, langsung ambil list2
        if not self.head:
            self.head = list2.head
            return

        # Cari node terakhir list1
        temp = self.head
        while temp.next:
            temp = temp.next

        # Sambungkan node terakhir list1 ke head list2
        temp.next = list2.head


# ==========================
# PROGRAM UTAMA
# ==========================

list1 = single_Linked_List()  # Membuat Linked List 1
list2 = single_Linked_List()  # Membuat Linked List 2

# Input elemen untuk Linked List 1
data1 = input("Masukkan elemen untuk Linked List 1 (pisahkan dengan koma): ")

if data1.strip() != "":  # Jika input tidak kosong
    for item in data1.split(","):   # Pisahkan input berdasarkan koma
        list1.append(int(item.strip()))  # Convert ke integer lalu masukkan ke list1

# Input elemen untuk Linked List 2
data2 = input("Masukkan elemen untuk Linked List 2 (pisahkan dengan koma): ")

if data2.strip() != "":  # Jika input tidak kosong
    for item in data2.split(","):
        list2.append(int(item.strip()))  # Convert ke integer lalu masukkan ke list2

# Tampilkan isi Linked List 1
print("\nLinked List 1:")
list1.display()

# Tampilkan isi Linked List 2
print("Linked List 2:")
list2.display()

# Menggabungkan list1 dan list2
list1.merge(list2)

# Tampilkan hasil penggabungan
print("Linked List setelah digabungkan:")
list1.display()
