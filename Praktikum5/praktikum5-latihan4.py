# ================================================================
# Nama  : Caesarian Lanang Parizano Zaim
# NIM   : J0403251121
# Kelas : A2
# ================================================================

# ========================================================== 
# Latihan 4: Kombinasi Huruf 
# ========================================================== 
 
def kombinasi(n, hasil=""):  # Definisi Fungsi dengan parameter n dan hasil (default string kosong)
    
    # Base case
    if len(hasil) == n:
        print(hasil)  
        return  
        # Jika panjang string "hasil" sudah sama dengan n,
        # maka kombinasi sudah lengkap dan langsung dicetak
        # return digunakan untuk menghentikan cabang rekursi ini
    
    # Recursive case 1
    kombinasi(n, hasil + "A")  
    '''
    "hasil + 'A'" berarti menambahkan huruf A ke string sebelumnya.
    Fungsi memanggil dirinya sendiri untuk melanjutkan pembentukan kombinasi.
    Cabang ini akan terus berkembang sampai panjangnya mencapai n.
    '''
    
    # Recursive case 2
    kombinasi(n, hasil + "B")  
    '''
    "hasil + 'B'" berarti menambahkan huruf B ke string sebelumnya.
    Ini adalah cabang kedua dari rekursi.
    Setiap level akan bercabang menjadi dua kemungkinan: A atau B.
    '''


# Memanggil fungsi kombinasi
kombinasi(2)
'''
Proses yang terjadi untuk n = 2:

Awal: hasil = ""
Cabang menjadi:
"A"
"AA"
"AB"
"B"
"BA"
"BB"

Output akhirnya:
AA
AB
BA
BB
'''