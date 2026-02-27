# ================================================================
# Nama  : Caesarian Lanang Parizano Zaim
# NIM   : J0403251121
# Kelas : A2
# ================================================================

# ========================================================== 
# Latihan 2: Tracing Rekursi 
# ==========================================================

def countdown(n):  # Definisi Fungsi
    
    # Base case
    if n == 0:
        print("Selesai")  # Menampilkan "Selesai" jika n sudah 0
        return  # Menghentikan fungsi agar tidak terus memanggil dirinya sendiri
        # Tanpa return, rekursi akan terus berjalan dan bisa menyebabkan error
    
    # Proses sebelum rekursi (saat fungsi "turun")
    print("Masuk:", n)  
    # Menampilkan nilai n saat pertama kali masuk ke fungsi
    
    # Recursive case
    countdown(n - 1)  
    '''
    "countdown(n - 1)" adalah pemanggilan fungsi itu sendiri.
    "n - 1" berarti nilai n dikurangi 1 setiap kali fungsi dipanggil.
    Fungsi akan terus dipanggil sampai mencapai base case (n == 0).
    '''
    
    # Proses setelah rekursi (saat fungsi "naik kembali")
    print("Keluar:", n)
    # Bagian ini dijalankan setelah proses rekursif selesai
    # Ini menunjukkan urutan saat fungsi kembali ke atas (stack unwinding)


# Memanggil fungsi countdown
countdown(3)
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