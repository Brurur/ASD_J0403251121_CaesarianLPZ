# Nama  : Caesarian Lanang Parizano Zaim
# NIM : J0403251121
# Kelas : A2
# Praktikum 12 - Graph II: Shortest Path

# ============================================================
# Latihan 5: Studi Kasus dengan Program Shortest Path
# ============================================================

import heapq

# Representasi graph berbobot menggunakan dictionary bersarang.
# Bobot menunjukkan jarak antar kota.
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Jakarta': {'Bandung': 7},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Bandung': {}
}


def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node awal
    ke semua node lain menggunakan algoritma Dijkstra.
    """

    # Semua jarak awal dibuat tak hingga, lalu jarak node awal dibuat 0.
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Priority queue digunakan agar node dengan jarak terkecil diproses dahulu.
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika data jarak yang keluar dari queue sudah tidak terbaru, lewati.
        if current_distance > distances[current_node]:
            continue

        # Periksa semua kota tetangga dari kota saat ini.
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Jika ditemukan jarak yang lebih pendek, simpan jarak baru.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


node_awal = 'Bogor'
hasil = dijkstra(graph, node_awal)

print("Jarak terpendek dari Bogor:")
for kota, jarak in hasil.items():
    print("Bogor ->", kota, "=", jarak)

# Jawaban Analisis:
# 1. Pertanyaan: Node awal yang digunakan apa?
#    Jawaban: Node awal yang digunakan adalah Bogor.
# 2. Pertanyaan: Node mana yang memiliki jarak paling kecil dari node awal?
#    Jawaban: Node yang memiliki jarak paling kecil dari node awal adalah Bogor
#    sendiri dengan jarak 0. Jika node awal tidak dihitung, node paling dekat
#    adalah Depok dengan jarak 2.
# 3. Pertanyaan: Node mana yang memiliki jarak paling besar dari node awal?
#    Jawaban: Node yang memiliki jarak paling besar dari node awal adalah
#    Bandung dengan jarak 8.
# 4. Pertanyaan: Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus
#    yang Anda buat.
#    Jawaban: Algoritma Dijkstra bekerja dengan memberi jarak awal 0 pada
#    Bogor dan tak hingga pada node lain. Setelah itu, algoritma memilih node
#    dengan jarak sementara paling kecil, memeriksa semua tetangganya, lalu
#    memperbarui jarak jika ditemukan rute yang lebih pendek. Pada kasus ini,
#    rute ke Jakarta menjadi lebih pendek melalui Depok, sehingga jarak Bogor
#    ke Jakarta adalah 4 dan jarak Bogor ke Bandung adalah 8.
