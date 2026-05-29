# Nama : Caesarian Lanang Parizano Zaim
# NIM : J0403251121
# Kelas : A2
# Praktikum 13 - Graph III: Spanning Tree

# Daftar edge dalam format (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Urutkan edge dari bobot terkecil ke terbesar (inti Kruskal)
edges.sort()

mst = []
total_weight = 0

# Set ini menyimpan node-node yang sudah masuk ke dalam MST.
# Digunakan untuk deteksi cycle sederhana: jika KEDUA ujung edge sudah ada di 'connected', menambahkan edge itu akan membentuk cycle.
connected = set()

for weight, u, v in edges:
    # Edge aman ditambahkan jika minimal satu ujungnya belum terhubung,
    # sehingga tidak menutup lingkaran (cycle).
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)

print("Minimum Spanning Tree (Kruskal):")
for edge in mst:
    print(f"  {edge[0]} - {edge[1]}, bobot = {edge[2]}")

print("Total bobot =", total_weight)

# ==========================================================
# Jawaban Analisis:
#
# 1. Edge mana yang dipilih pertama kali?
#    C-D dengan bobot 1, karena setelah diurutkan ia adalah
#    edge berbobot paling kecil.
#
# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
#    Strategi greedy Kruskal: dengan selalu memilih edge terkecil
#    yang aman, akumulasi bobot dijamin minimum di akhir proses.
#
# 3. Berapa total bobot MST yang dihasilkan?
#    C-D(1) + A-C(2) + B-D(3) = 6
#
# 4. Mengapa edge tertentu tidak dipilih?
#    Edge A-B(4) dan A-D(5) tidak dipilih karena saat gilirannya
#    tiba, semua node (A, B, C, D) sudah masuk ke 'connected',
#    sehingga menambahkan edge tersebut akan membentuk cycle.
# ==========================================================
