# Nama : Caesarian Lanang Parizano Zaim
# NIM : J0403251121
# Kelas : A2
# Praktikum 13 - Graph III: Spanning Tree

import heapq

# Representasi graph sebagai adjacency dictionary
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}


def prim(graph, start):
    visited = set([start])

    # Min-heap berisi tuple (bobot, node_asal, node_tujuan).
    # heapq selalu mengeluarkan elemen dengan bobot terkecil lebih dulu.
    edges = []
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    while edges:
        weight, u, v = heapq.heappop(edges)

        # Lewati edge ini jika node tujuan sudah dikunjungi
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight

            # Tambahkan semua edge dari node baru ke heap
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight


mst, total = prim(graph, 'A')

print("Minimum Spanning Tree (Prim, mulai dari A):")
for edge in mst:
    print(f"  {edge[0]} - {edge[1]}, bobot = {edge[2]}")

print("Total bobot =", total)

# ==========================================================
# Jawaban Analisis:
#
# 1. Node awal apa yang digunakan?
#    Node 'A'.
#
# 2. Edge mana yang dipilih pertama kali?
#    A-C dengan bobot 2, karena dari A edge terkecilnya adalah A-C.
#
# 3. Bagaimana Prim menentukan edge berikutnya?
#    Setiap kali node baru ditambahkan, semua edge dari node itu
#    dimasukkan ke min-heap. Prim lalu mengambil edge berbobot
#    terkecil dari heap yang belum membentuk cycle.
#    Urutan yang terjadi: A-C(2) → C-D(1) → D-B(3).
#
# 4. Berapa total bobot MST yang dihasilkan?
#    A-C(2) + C-D(1) + D-B(3) = 6
#
# 5. Apa perbedaan pendekatan Prim dan Kruskal?
#    Kruskal: memilih edge terkecil secara GLOBAL dari seluruh graph.
#    Prim   : tumbuh dari satu node, selalu memilih edge terkecil
#             yang menghubungkan tree yang sudah ada ke node baru.
#    Hasilnya bisa sama, tapi cara berpikirnya berbeda:
#    Kruskal fokus pada edge, Prim fokus pada node.
# ==========================================================
