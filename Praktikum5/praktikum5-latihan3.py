# ================================================================
# Nama  : Caesarian Lanang Parizano Zaim
# NIM   : J0403251121
# Kelas : A2
# ================================================================

# ========================================================== 
# Latihan 3: Mencari Nilai Maksimum 
# ========================================================== 
 
def cari_maks(data, index=0):  # Definisi Fungsi dengan parameter data dan index (default = 0)
    
    # Base case
    if index == len(data) - 1:
        return data[index]  
        # Mengembalikan elemen terakhir jika index sudah berada di posisi akhir list
        # len(data) - 1 digunakan karena index list dimulai dari 0
    
    # Recursive case
    maks_sisa = cari_maks(data, index + 1)  
    '''
    "cari_maks(data, index + 1)" adalah pemanggilan fungsi itu sendiri.
    "index + 1" berarti kita maju ke elemen berikutnya.
    Fungsi akan terus berjalan sampai mencapai elemen terakhir (base case).
    Nilai maksimum dari sisa elemen akan disimpan di variabel "maks_sisa".
    '''
    
    # Membandingkan elemen sekarang dengan maksimum dari sisa elemen
    if data[index] > maks_sisa:
        return data[index]  
        # Jika elemen sekarang lebih besar, kembalikan elemen sekarang
    else:
        return maks_sisa  
        # Jika tidak, kembalikan nilai maksimum dari sisa elemen


# Membuat list angka
angka = [3, 7, 2, 9, 5]

# Memanggil dan mencetak hasil fungsi
print("Nilai maksimum:", cari_maks(angka))
'''
Proses yang terjadi:
Membandingkan 3 dengan maksimum dari [7,2,9,5]
Membandingkan 7 dengan maksimum dari [2,9,5]
Membandingkan 2 dengan maksimum dari [9,5]
Membandingkan 9 dengan maksimum dari [5]
Elemen terakhir 5 menjadi base case awal
Hasil akhirnya adalah 9
'''