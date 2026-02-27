# ================================================================
# Nama  : Caesarian Lanang Parizano Zaim
# NIM   : J0403251121
# Kelas : A2
# ================================================================

# ==========================================================
# Contoh Backtracking 1: Kombinasi Biner (n)
# ==========================================================

def biner(n, hasil=""):  # Definisi Fungsi dengan parameter n dan hasil (default string kosong)
    
    # Base case
    if len(hasil) == n:
        print(hasil)  
        return  
        # Jika panjang string "hasil" sudah sama dengan n,
        # maka kombinasi biner sudah lengkap dan langsung dicetak
        # return digunakan untuk menghentikan cabang rekursi ini
    
    # Choose + Explore: tambah '0'
    biner(n, hasil + "0")  
    '''
    "hasil + '0'" berarti menambahkan karakter 0 ke string sebelumnya.
    Fungsi memanggil dirinya sendiri untuk melanjutkan pembentukan kombinasi.
    Cabang ini akan terus berkembang sampai panjangnya mencapai n.
    '''
    
    # Choose + Explore: tambah '1'
    biner(n, hasil + "1")  
    '''
    "hasil + '1'" berarti menambahkan karakter 1 ke string sebelumnya.
    Ini adalah cabang kedua dari rekursi.
    Setiap level akan bercabang menjadi dua kemungkinan: 0 atau 1.
    '''


# Memanggil fungsi biner
biner(3)

'''
Output untuk n = 3:

000
001
010
011
100
101
110
111

Total kombinasi: 2^3 = 8 kemungkinan
'''