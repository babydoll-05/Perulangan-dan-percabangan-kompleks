def polaular(angka):
    if angka <= 0:  # Menangani kasus angka <= 0
        print("tidak terdefiniskan")
        return
    
    matriks = [[0] * angka for _ in range(angka)]
    num = 1

    for i in range(angka):
        if i % 2 == 0:
            for j in range(angka):
                matriks[i][j] = num
                num += 1
        else:
            for j in range(angka - 1, -1, -1):
                matriks[i][j] = num
                num += 1

    for row in matriks:
        print(" ".join(f"{x:02}" for x in row))

# Contoh penggunaan
polaular(4)
polaular(0)  # Akan mengeluarkan "tidak terdefinisi"
