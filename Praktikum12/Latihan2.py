# Nama  : Caesarian Lanang Parizano Zaim
# NIM : J0403251121
# Kelas : A2
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 2: Implementasi Dijkstra
# ==========================================================
import heapq
# Weighted graph dengan bobot positif
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}


def dijkstra(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Dijkstra.
    """
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}
    # Jarak dari start ke start adalah 0
    distances[start] = 0
    # Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat,
        # maka proses dilewati
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

        return distances


hasil = dijkstra(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

# Jawaban Analisis:
# 1. Pertanyaan: Berapa jarak terpendek dari A ke B?
#    Jawaban: Jarak terpendek dari A ke B adalah 4.
# 2. Pertanyaan: Berapa jarak terpendek dari A ke C?
#    Jawaban: Jarak terpendek dari A ke C adalah 2.
# 3. Pertanyaan: Berapa jarak terpendek dari A ke D?
#    Jawaban: Jarak terpendek dari A ke D adalah 3.
# 4. Pertanyaan: Mengapa jarak A ke D lebih kecil melalui C dibandingkan
#    melalui B?
#    Jawaban: Jarak A ke D lebih kecil melalui C karena bobot A -> C -> D
#    adalah 2 + 1 = 3, sedangkan melalui B bobotnya 4 + 5 = 9.
# 5. Pertanyaan: Apa fungsi priority_queue dalam algoritma Dijkstra?
#    Jawaban: priority_queue berfungsi menyimpan node yang akan diproses
#    berdasarkan jarak terkecil, sehingga node dengan jarak paling dekat
#    diproses lebih dulu.
# 6. Pertanyaan: Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif?
#    Jawaban: Dijkstra tidak cocok untuk graph dengan bobot negatif karena
#    keputusan jarak terpendek yang sudah dipilih dapat berubah jika ada edge
#    berbobot negatif, sehingga hasilnya bisa tidak akurat.
