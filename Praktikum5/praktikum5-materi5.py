# ================================================================
# Nama  : Caesarian Lanang Parizano Zaim
# NIM   : J0403251121
# Kelas : A2
# ================================================================

# ==========================================================
# Contoh Backtracking 2: Kombinasi Biner dengan Batas '1' (Pruning)
# ==========================================================

def biner_batas(n, batas, hasil="", jumlah_1=0):  
    # Definisi Fungsi dengan:
    # n        = panjang kombinasi
    # batas    = jumlah maksimal karakter '1'
    # hasil    = string sementara (default kosong)
    # jumlah_1 = menghitung berapa banyak '1' yang sudah dipakai
    
    # Pruning
    if jumlah_1 > batas:
        return  
        # Jika jumlah '1' sudah melebihi batas,
        # maka cabang ini dihentikan lebih awal
        # Inilah yang disebut pruning (memotong cabang yang tidak valid)
    
    # Base case
    if len(hasil) == n:
        print(hasil)
        return
        # Jika panjang string sudah sama dengan n,
        # maka kombinasi valid dan langsung dicetak
    
    # Pilih '0'
    biner_batas(n, batas, hasil + "0", jumlah_1)
    '''
    Menambahkan karakter '0' ke hasil.
    jumlah_1 tidak bertambah karena kita tidak menambah '1'.
    Fungsi dipanggil kembali untuk melanjutkan pembentukan kombinasi.
    '''
    
    # Pilih '1'
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)
    '''
    Menambahkan karakter '1' ke hasil.
    jumlah_1 ditambah 1 karena kita menambahkan satu '1'.
    Jika jumlah_1 melebihi batas, cabang ini akan otomatis berhenti (pruning).
    '''


# Memanggil fungsi
biner_batas(4, 2)

'''
Artinya:
Membuat kombinasi biner sepanjang 4 digit
dengan maksimal 2 angka '1'

Contoh output:
0000
0001
0010
0011
0100
0101
0110
1000
1001
1010
1100

Semua kombinasi yang memiliki lebih dari 2 angka '1' tidak akan muncul
karena sudah dipotong oleh pruning.
'''