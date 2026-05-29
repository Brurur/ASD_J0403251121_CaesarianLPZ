# Nama : Caesarian Lanang Parizano Zaim
# NIM : J0403251121
# Kelas : A2
# Praktikum 13 - Graph III: Spanning Tree

import heapq

# Representasi weighted graph antar gedung kampus
graph = {
    'GedungA': {'GedungB': 4, 'GedungC': 2, 'GedungD': 5},
    'GedungB': {'GedungA': 4, 'GedungD': 3},
    'GedungC': {'GedungA': 2, 'GedungD': 1},
    'GedungD': {'GedungA': 5, 'GedungB': 3, 'GedungC': 1}
}


def prim(graph, start):
    visited = set([start])
    edges = []

    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    while edges:
        weight, u, v = heapq.heappop(edges)

        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight

            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight


# Jalankan Prim mulai dari GedungA sebagai titik awal pemasangan kabel
mst, total_cost = prim(graph, 'GedungA')

print("=" * 50)
print("  Jaringan Kabel Minimum Antar Gedung Kampus")
print("=" * 50)
print("\nKoneksi kabel yang dipasang:")
for u, v, w in mst:
    print(f"  {u} <---> {v}  |  Biaya: {w}")

print(f"\nTotal biaya minimum pemasangan kabel: {total_cost}")
print("=" * 50)

# ==========================================================
# Jawaban Analisis:
#
# 1. Algoritma apa yang digunakan?
#    Algoritma Prim, karena graph ini tergolong dense (setiap
#    gedung punya banyak koneksi), sehingga Prim lebih efisien.
#
# 2. Edge mana saja yang dipilih?
#    GedungA - GedungC (biaya 2)
#    GedungC - GedungD (biaya 1)
#    GedungD - GedungB (biaya 3)
#
# 3. Berapa total biaya minimum?
#    2 + 1 + 3 = 6
#
# 4. Mengapa MST cocok digunakan pada kasus ini?
#    Tujuannya adalah menghubungkan SEMUA gedung (bukan mencari
#    jalur tercepat antar dua gedung). MST menjamin semua gedung
#    terhubung dengan total panjang/biaya kabel paling sedikit,
#    tanpa jalur redundan yang membuang anggaran.
# ==========================================================
