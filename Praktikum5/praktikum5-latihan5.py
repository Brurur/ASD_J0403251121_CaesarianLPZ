# ================================================================
# Nama  : Caesarian Lanang Parizano Zaim
# NIM   : J0403251121
# Kelas : A2
# ================================================================

# ========================================================== 
# Studi Kasus: Generator PIN 
# ========================================================== 
 
def buat_pin(panjang, hasil=""):  # Definisi Fungsi dengan parameter panjang dan hasil (default string kosong)
    
    # Base case
    if len(hasil) == panjang:
        print("PIN:", hasil)  
        return  
        # Jika panjang string "hasil" sudah sama dengan panjang yang ditentukan,
        # maka kombinasi PIN sudah lengkap dan langsung dicetak
        # return digunakan untuk menghentikan cabang rekursi ini
    
    # Recursive case dengan perulangan
    for angka in ["0", "1", "2"]:
        '''
        Perulangan ini akan mengambil setiap elemen dalam list:
        "0", "1", dan "2".
        Setiap angka akan ditambahkan ke string "hasil".
        '''
        
        buat_pin(panjang, hasil + angka)
        '''
        "hasil + angka" berarti menambahkan satu digit ke PIN sebelumnya.
        Fungsi memanggil dirinya sendiri untuk melanjutkan pembentukan PIN.
        Proses ini akan terus berjalan sampai panjangnya mencapai batas yang ditentukan.
        '''


# Memanggil fungsi buat_pin
buat_pin(3)
'''
Proses yang terjadi untuk panjang = 3:

Awal: hasil = ""
Cabang pertama mulai dari "0", lalu berkembang menjadi:
000
001
002

Lalu cabang dari "1":
100
101
102

Lalu cabang dari "2":
200
201
202

Total kombinasi: 3^3 = 27 kemungkinan PIN
'''