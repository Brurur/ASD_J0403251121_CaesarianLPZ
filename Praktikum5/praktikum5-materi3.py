# ================================================================
# Nama  : Caesarian Lanang Parizano Zaim
# NIM   : J0403251121
# Kelas : A2
# ================================================================

# ==========================================================
# Contoh Rekursi 3: Menjumlahkan Elemen List
# ==========================================================

def jumlah_list(data, index=0):  # Definisi Fungsi dengan parameter data dan index (default = 0)
    
    # Base case
    if index == len(data):
        return 0  
        # Jika index sudah sama dengan panjang list,
        # artinya tidak ada elemen lagi yang bisa dijumlahkan
        # Mengembalikan 0 karena 0 adalah nilai netral dalam penjumlahan
    
    # Recursive case
    return data[index] + jumlah_list(data, index + 1)
    '''
    "data[index]" adalah elemen yang sedang diproses.
    "jumlah_list(data, index + 1)" adalah pemanggilan fungsi itu sendiri.
    "index + 1" berarti kita maju ke elemen berikutnya.
    Setiap pemanggilan akan menjumlahkan satu elemen sampai mencapai base case.
    '''


# Memanggil dan mencetak hasil fungsi
print(jumlah_list([2, 4, 6, 8]))  # Output: 20

'''
Proses yang terjadi:

2 + jumlah_list([4,6,8])
= 2 + (4 + jumlah_list([6,8]))
= 2 + (4 + (6 + jumlah_list([8])))
= 2 + (4 + (6 + (8 + jumlah_list([]))))
= 2 + 4 + 6 + 8 + 0
= 20
'''