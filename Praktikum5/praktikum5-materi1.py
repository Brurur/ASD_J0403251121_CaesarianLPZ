# ================================================================
# Nama  : Caesarian Lanang Parizano Zaim
# NIM   : J0403251121
# Kelas : A2
# ================================================================

# ========================================================== 
# Contoh Rekursi 1: Faktorial 
# ========================================================== 

def faktorial(n):  # Definisi Fungsi
    
    # Base case
    if n == 0:
        return 1  
        # Mengembalikan 1 jika n sama dengan 0
        # Karena secara matematika, 0! bernilai 1
    
    # Recursive case
    return n * faktorial(n - 1)  
    '''
    "n *" berarti nilai n saat ini dikalikan.
    "faktorial(n - 1)" adalah pemanggilan fungsi itu sendiri.
    "n - 1" berarti masalah diperkecil satu langkah.
    Proses ini akan terus berjalan sampai mencapai base case (n == 0).
    '''


# Memanggil dan mencetak hasil fungsi faktorial
print(faktorial(5))  # Output: 120
'''
Proses yang terjadi:

5 * faktorial(4)
= 5 * (4 * faktorial(3))
= 5 * (4 * (3 * faktorial(2)))
= 5 * (4 * (3 * (2 * faktorial(1))))
= 5 * (4 * (3 * (2 * (1 * faktorial(0)))))
= 5 * 4 * 3 * 2 * 1 * 1
= 120
'''