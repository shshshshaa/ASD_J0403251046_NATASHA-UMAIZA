#=====================================================
#Nama   : Natasha Umaiza
#NIM    : J0403251046
#Kelas  : TPL A/P1
#=====================================================

#=====================================================
#Implementasi Dasar : Node pada linked list
#=====================================================

class Node:
    #Konstruktor adalah fungsi yang dijalankan secara otomatis ketika class node dipanggil/diinstantiasi
    def __init__(self, data):
        self.data= data #Menyimpan nilai atau data pada list
        self.next = None #Pointer ini menunjuk ke note berikutnya 

#1) Membuat node dengan instantiasi class node
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

#2) Mendefinisikan head dan Menghubungkan Node : A => B => C => None
head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC

#3) Traversal : Menelusuri node dari head sampai ke None
current = head
while current is not None:
    print(current.data) #menampilkan data pada node saat ini
    current = current.next #pindah ke node berikutnya

