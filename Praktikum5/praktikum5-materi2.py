# ================================================================
# Nama  : Caesarian Lanang Parizano Zaim
# NIM   : J0403251121
# Kelas : A2
# ================================================================

# ==========================================================
# Contoh Rekursi 2: Tracing Masuk/Keluar
# ==========================================================

def hitung(n):  # Definisi Fungsi
    
    # Base case
    if n == 0:
        print("Selesai")  
        return  
        # Jika n sudah 0, tampilkan "Selesai"
        # return digunakan untuk menghentikan rekursi agar tidak terus berjalan
    
    # Proses sebelum rekursi (saat fungsi turun)
    print("Masuk:", n)  
    # Menampilkan nilai n saat pertama kali masuk ke level rekursi
    
    # Recursive call
    hitung(n - 1)  
    '''
    "hitung(n - 1)" adalah pemanggilan fungsi itu sendiri.
    "n - 1" berarti nilai n dikurangi 1 setiap kali dipanggil.
    Fungsi akan terus berjalan sampai mencapai base case (n == 0).
    '''
    
    # Proses setelah rekursi (saat fungsi naik kembali)
    print("Keluar:", n)  
    # Bagian ini dijalankan setelah proses rekursif selesai
    # Menunjukkan urutan saat fungsi kembali ke atas (stack unwinding)


# Memanggil fungsi hitung
hitung(3)

'''
Urutan output:

Masuk: 3
Masuk: 2
Masuk: 1
Selesai
Keluar: 1
Keluar: 2
Keluar: 3
'''