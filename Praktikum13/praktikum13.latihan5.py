# Nama : Caesarian Lanang Parizano Zaim
# NIM : J0403251121
# Kelas : A2
# Praktikum 13 - Graph III: Spanning Tree

# Daftar edge dalam format (bobot, kota1, kota2)
# Bobot merepresentasikan jarak/biaya pembangunan jalan (satuan: km atau unit biaya)
edges = [
    (5, 'Bogor',   'Jakarta'),
    (2, 'Bogor',   'Depok'),
    (3, 'Depok',   'Jakarta'),
    (6, 'Jakarta', 'Bandung'),
    (4, 'Depok',   'Bandung')
]

# ---- Implementasi Kruskal ----
# Kruskal dipilih di sini untuk kasus sparse graph (sedikit edge relatif ke node)

# Union-Find (Disjoint Set) untuk deteksi cycle yang benar
parent = {}


def find(node):
    # Cari root dari node; path compression untuk efisiensi
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(u, v):
    # Gabungkan dua komponen; kembalikan False jika sudah satu komponen (cycle)
    root_u = find(u)
    root_v = find(v)
    if root_u == root_v:
        return False   # u dan v sudah terhubung → menambahkan edge ini = cycle
    parent[root_u] = root_v
    return True


# Inisialisasi setiap kota sebagai komponen tersendiri
all_nodes = set()
for w, u, v in edges:
    all_nodes.add(u)
    all_nodes.add(v)

for node in all_nodes:
    parent[node] = node

# Urutkan semua edge dari bobot terkecil
edges.sort()

mst = []
total_weight = 0

for weight, u, v in edges:
    # Tambahkan edge hanya jika tidak membentuk cycle (union berhasil)
    if union(u, v):
        mst.append((u, v, weight))
        total_weight += weight

# Tampilkan hasil
print("=" * 55)
print("  MST Jaringan Jalan Antar Kota - Algoritma Kruskal")
print("=" * 55)
print("\nSemua edge (diurutkan dari terkecil):")
for w, u, v in edges:
    print(f"  {u} - {v}: {w}")

print("\nEdge yang dipilih untuk MST:")
for u, v, w in mst:
    print(f"  {u} <---> {v}  |  Jarak/Biaya: {w}")

print(f"\nTotal bobot MST minimum: {total_weight}")
print("=" * 55)

# ==========================================================
# Jawaban Analisis:
#
# 1. Kasus apa yang dipilih?
#    Kasus 1.
#
# 2. Algoritma apa yang digunakan?
#    Algoritma Kruskal dengan struktur Union-Find untuk deteksi cycle
#    yang akurat (lebih andal dibanding cek set sederhana di latihan 2).
#
# 3. Edge mana saja yang dipilih dalam MST?
#    Bogor   - Depok   (bobot 2)  ← terkecil, aman
#    Depok   - Jakarta (bobot 3)  ← aman, Bandung belum terhubung
#    Depok   - Bandung (bobot 4)  ← aman, Bandung masuk MST
#    (total 3 edge = 4 kota - 1)
#
# 4. Berapa total bobot MST?
#    2 + 3 + 4 = 9
#
# 5. Mengapa edge tertentu tidak dipilih?
#    Bogor-Jakarta (5): saat gilirannya tiba, Bogor dan Jakarta sudah
#    terhubung melalui Bogor→Depok→Jakarta, sehingga menambahkannya
#    akan membentuk cycle → dilewati.
#    Jakarta-Bandung (6): saat gilirannya tiba, Jakarta dan Bandung
#    sudah terhubung melalui Depok→Bandung, sehingga juga membentuk
#    cycle → dilewati.
# ==========================================================
