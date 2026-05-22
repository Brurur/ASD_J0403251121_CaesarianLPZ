# Nama  : Caesarian Lanang Parizano Zaim
# NIM : J0403251121
# Kelas : A2
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
# ==========================================================
import heapq
# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}


def dijkstra(graph, start):

    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances


hasil = dijkstra(graph, 'Gerbang')
print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")

# Jawaban Analisis:
# 1. Pertanyaan: Lokasi mana yang paling dekat dari Gerbang?
#    Jawaban: Lokasi yang paling dekat dari Gerbang adalah Gerbang sendiri
#    dengan jarak 0 menit. Jika tidak menghitung node awal, lokasi terdekat
#    adalah Kantin dengan jarak 3 menit.
# 2. Pertanyaan: Berapa waktu tempuh terpendek dari Gerbang ke Aula?
#    Jawaban: Waktu tempuh terpendek dari Gerbang ke Aula adalah 6 menit,
#    yaitu melalui Gerbang -> Kantin -> Aula.
# 3. Pertanyaan: Apakah jalur langsung selalu menghasilkan jarak paling kecil?
#    Jelaskan.
#    Jawaban: Jalur langsung tidak selalu menghasilkan jarak paling kecil.
#    Contohnya, Gerbang -> Aula secara langsung berbobot 7, tetapi melalui
#    Kantin hanya 3 + 3 = 6 menit.
# 4. Pertanyaan: Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?
#    Jawaban: Dijkstra cocok digunakan pada kasus lokasi kampus ini karena
#    semua bobot bernilai positif dan algoritma dapat memilih rute dengan total
#    waktu tempuh paling kecil dari Gerbang ke semua lokasi.
