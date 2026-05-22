# Nama  : Caesarian Lanang Parizano Zaim
# NIM : J0403251121
# Kelas : A2
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 1: Weighted Graph dan Perhitungan Jalur
# ==========================================================
# Representasi weighted graph menggunakan dictionary bersarang
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}
# Menghitung dua kemungkinan jalur dari A ke D
jalur_1 = graph['A']['B'] + graph['B']['D']
jalur_2 = graph['A']['C'] + graph['C']['D']
print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)
# A -> B -> D
# A -> C -> D
if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")

# Jawaban Analisis:
# 1. Pertanyaan: Berapa total bobot jalur A -> B -> D?
#    Jawaban: Total bobot jalur A -> B -> D adalah 4 + 5 = 9.
# 2. Pertanyaan: Berapa total bobot jalur A -> C -> D?
#    Jawaban: Total bobot jalur A -> C -> D adalah 2 + 1 = 3.
# 3. Pertanyaan: Jalur mana yang dipilih sebagai jalur terpendek?
#    Jawaban: Jalur yang dipilih sebagai jalur terpendek adalah A -> C -> D.
# 4. Pertanyaan: Mengapa jalur terpendek tidak selalu ditentukan dari jumlah
#    edge yang paling sedikit?
#    Jawaban: Jalur terpendek tidak selalu ditentukan dari jumlah edge paling
#    sedikit, tetapi dari jumlah bobot terkecil. Jumlah edge sedikit belum tentu
#    lebih pendek jika bobot pada edge tersebut besar.
