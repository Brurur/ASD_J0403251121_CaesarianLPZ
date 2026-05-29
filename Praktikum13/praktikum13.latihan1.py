# Nama : Caesarian Lanang Parizano Zaim
# NIM : J0403251121
# Kelas : A2
# Praktikum 13 - Graph III: Spanning Tree

# Daftar semua edge pada graph awal
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Dipilih 3 edge (jumlah node - 1 = 4 - 1 = 3) yang menghubungkan semua node tanpa membentuk cycle.
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

print("Edge pada graph:")
for edge in edges:
    print(edge)

print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

print("\nJumlah edge graph       =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

# ==========================================================
# Jawaban Analisis:
#
# 1. Apa perbedaan graph awal dan spanning tree?
#    Graph awal memiliki 5 edge dan mengandung cycle (misal A-C-D-A).
#    Spanning tree hanya memiliki 3 edge (n-1), menghubungkan semua
#    node tanpa cycle sama sekali.
#
# 2. Mengapa spanning tree tidak boleh memiliki cycle?
#    Cycle berarti ada jalur redundan. Jika tujuannya menghubungkan
#    semua node dengan edge seminimal mungkin, cycle hanya menambah
#    edge tanpa manfaat koneksi baru dan pada kasus berbobot,
#    cycle meningkatkan total biaya.
#
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
#    Untuk menghubungkan N node tanpa cycle, dibutuhkan tepat N-1
#    edge. Lebih dari itu pasti membentuk cycle; kurang dari itu
#    ada node yang tidak terhubung. Graph awal biasanya punya
#    lebih dari N-1 edge karena memiliki banyak jalur alternatif.
# ==========================================================
