# ================================================================
# Nama  : Caesarian Lanang Parizano Zaim
# NIM   : J0403251121
# Kelas : A2
# ================================================================

# ================================================================
# Implementasi Dasar : Node pada Linked List
# ================================================================


class Node:
    # Konstruktor yang dijalankan secara otomatis ketika class Node dipanggil / diinstansiasi
    def __init__(self, data):
        # Menyimpan nilai atau data pada list
        self.data = data
        # Pointer ini menunjuk ke note berikutnya (awal = None)
        self.next = None


# 1) Membuat node dengan instansiasi class Node
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

# 2) Mendefinisikan head dan menghubungkan Node o A -> B -> C -> None

head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC

# 3) Traversal : Menulusuri Node dari head sampai ke None
current = head
while current is not None:
    print(current.data)  # Menampilkan data pada Node saat ini
    current = current.next  # Pindah ke Node berikutnya
