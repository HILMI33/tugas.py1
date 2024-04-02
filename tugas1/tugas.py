def pesan_sambutan():
    # Meminta pengguna untuk memasukkan nama dan usia
    nama = input("Masukkan nama Anda: ")
    usia = int(input("Masukkan usia Anda: "))
    
    # Menentukan pesan sambutan berdasarkan usia
    if usia < 18:
        pesan = "Halo, " + nama + "! Anda masih muda, nikmati masa remaja Anda."
    elif usia >= 18 and usia < 60:
        pesan = "Halo, " + nama + "! Selamat datang di usia dewasa."
    else:
        pesan = "Halo, " + nama + "! Selamat menikmati hari tua Anda."
    
    # Menampilkan pesan sambutan
    print(pesan)

# Memanggil fungsi untuk menjalankan program
pesan_sambutan()
