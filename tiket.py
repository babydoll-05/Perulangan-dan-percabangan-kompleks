def tiket(daftar_tiket):
    ganjil = sum(1 for tiket in daftar_tiket if tiket % 2 == 1)
    genap = sum(1 for tiket in daftar_tiket if tiket % 2 == 0)

    if genap > ganjil:
        return 'Lebih banyak tiket genap'
    elif ganjil > genap:
        return 'Lebih banyak tiket ganjil'
    else:
        return 'Jumlah tiket ganjil dan genap sama banyak'

# Contoh penggunaan
print(tiket([120, 225, 310, 455, 600, 715]))
