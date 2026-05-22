# Nama  : Caesarian Lanang Parizano Zaim
# NIM : J0403251121
# Kelas : A2
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 3: Implementasi Bellman-Ford
# ==========================================================

# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}


def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    """

    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke start adalah 0
    distances[start] = 0

    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):

        # Periksa semua edge
        for node in graph:
            for neighbor, weight in graph[node].items():

                # Jika jarak ke node saat ini sudah diketahui,
                # dan ditemukan jarak yang lebih kecil ke neighbor,
                # maka lakukan update jarak
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
        return distances


hasil = bellman_ford(graph, 'A')

print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

# Jawaban Analisis:
# 1. Pertanyaan: Berapa jarak terpendek dari A ke B?
#    Jawaban: Jarak terpendek dari A ke B adalah 2.
# 2. Pertanyaan: Berapa jarak terpendek dari A ke C?
#    Jawaban: Jarak terpendek dari A ke C adalah 4.
# 3. Pertanyaan: Mengapa jarak A ke B lebih kecil melalui C dibandingkan
#    jalur langsung?
#    Jawaban: Jarak A ke B menjadi lebih kecil melalui C karena jalur
#    A -> C -> B memiliki bobot 4 + (-2) = 2, lebih kecil daripada jalur
#    langsung A -> B yang berbobot 5.
# 4. Pertanyaan: Mengapa Bellman-Ford dapat digunakan untuk graph dengan
#    bobot negatif?
#    Jawaban: Bellman-Ford dapat menangani bobot negatif karena algoritma ini
#    melakukan relaksasi berulang pada semua edge, sehingga perubahan jarak
#    akibat edge negatif masih dapat diperhitungkan.
