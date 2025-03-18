def piramida(n):
    for i in range(1, n+1):
        # Membuat spasi agar bintang berada di tengah
        spasi = " " * (n - i)
        # Membuat bintang sesuai pola (2i - 1)
        bintang = "*" * (2*i - 1)
        # Menampilkan hasil
        print(spasi + bintang)

# Contoh pemanggilan fungsi
piramida(5)
