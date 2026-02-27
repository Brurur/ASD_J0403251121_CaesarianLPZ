# ================================================================
# Nama  : Caesarian Lanang Parizano Zaim
# NIM   : J0403251121
# Kelas : A2
# ================================================================

# ========================================================== 
# Latihan 1: Rekursi Pangkat 
# ========================================================== 

def pangkat(a, n): # Definisi Fungsi 
    # Base case 
    if n == 0: 
        return 1 # Mengembalikan nilai 1 jika n sama dengan 0
    # Karena dalam matematika, berapa pun angkanya jika dipangkatkan 0 hasilnya 1
    
    # Recursive case 
    return a * pangkat(a, n - 1) 
    ''' 
    "return" mengembalikan hasil perhitungan.
    "a *" berarti nilai dasar dikalikan dengan hasil fungsi berikutnya.
    "pangkat(a, n - 1)" adalah pemanggilan fungsi itu sendiri.
    "n - 1" berarti pangkatnya dikurangi 1 setiap kali fungsi dipanggil.
    '''
    
# Memanggil dan sekaligus print fungsi pangkat
print(pangkat(2, 4))  # Output: 16a