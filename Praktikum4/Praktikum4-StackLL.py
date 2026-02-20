# ================================================================
# Nama  : Caesarian Lanang Parizano Zaim
# NIM   : J0403251121
# Kelas : A2
# ================================================================

# ================================================================
# Implementasi Dasar : Stack
# ================================================================


class Node:
    # Konstruktor yang dijalankan secara otomatis ketika class Node dipanggil / diinstansiasi
    def __init__(self, data):
        # Menyimpan nilai atau data pada list
        self.data = data
        # Pointer ini menunjuk ke note berikutnya (awal = None)
        self.next = None

# Stack ada operasi push (memasukkan head baru) dan pop (menghapus head)


class Stack:
    def __init__(self):
        self.top = None  # Top menunjuk ke node paling atas (awalnya kosong)

    def is_empty(self):
        return self.top is None  # Stack kosong jika top = None

    def push(self, data):  # Memasukkan data baru pada Stack
        # 1 Membuat Node baru
        # Instansiasi/memanggil konstruktor pada class Node
        nodeBaru = Node(data)

        # 2 Node baru menunjuk ke top yang lama (head lama)
        nodeBaru.next = self.top

        # 3 Geser top pindah ke Node baru
        self.top = nodeBaru

    def pop(self):  # Mengambil/Menghapus Node paling atas (top/head)

        if self.is_empty():
            print("Stack kosong, tidak bisa pop")
            return

        data_terhapus = self.top.data  # Sototi bagian top dan simpan di variabel
        self.top = self.top.next  # Geser top ke Node berikutnya
        return data_terhapus

    def peek(self):
        # Melihat data yang paling atas tanpa menghapus
        if self.is_empty():
            return None
        return self.top.data

    def tampilkan(self):
        current = self.top
        print("Top", end=" -> ")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Instansiasi Class Stack
s = Stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()
print(f"Peek (Lihat Top): {s.peek()}")
s.pop()
s.tampilkan()
print(f"Peek (Lihat Top): {s.peek()}")
