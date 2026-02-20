#=====================================================
#Nama   : Natasha Umaiza
#NIM    : J0403251046
#Kelas  : TPL A/P1
#=====================================================


#=====================================================
#Implementasi Dasar : Queue
#=====================================================

class Node:
    #Konstruktor adalah fungsi yang dijalankan secara otomatis ketika class node dipanggil/diinstantiasi
    def __init__(self, data):
        self.data= data #Menyimpan nilai atau data pada list
        self.next = None #Pointer ini menunjuk ke note berikutnya 
        
class queue:
    #buat konstruktor untuk instantiasi variabel front dan rear
    def __init__(self):
        self.front = None #node paling depan
        self.rear = None #node paling belakang
        
    def is_empty(self):
        return self.front is None
        
    #Membuat fungsi untuk menambahkan data baru
    def enqueue(self,data):
        nodeBaru = Node(data)
        
        #jika queue kosong, front dan rear menunjuk ke node yang sama 
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return 
        
        #jika queue tidak kosong, maka letakkan data baru ke setelah rear, dan jadikan data baru sebagai rear
        self.rear.next = nodeBaru #letakkan data baru pada setelahnya rear
        self.rear = nodeBaru #jadikan data baru sebagai rear
        
    def dequeue(self):
        #menghapus data dari depan / front #lihat data paling depan
        data_terhapus = self.front.data
        
        #geser front ke node berikutnya
        self.front = self.front.next 
        
        #jika setelah geser front menjadi none, maka queue kosong
        #rear juga harus jadi None
        if self.front is None:
            self.rear = None
            
        return data_terhapus
    
    
    def tampilkan(self):
        current = self.front
        print("front -> ", end=" ")
        while current is not None:
            print(current.data, end="->")
            current = current.next 
        print("Rear")
        
#Instantiasi class queue
q = queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
q.dequeue
q.tampilkan()