import math

def capitalH(baris, kolom):
    if baris < 3 or baris % 2 == 0 or kolom < 3:
        print("dimensi tidak sesuai")
    else:
        for i in range(1, baris + 1):
            for j in range(1, kolom + 1):
                if i == math.ceil(baris / 2):
                    print("#", end="")  # Baris tengah penuh dengan '#'
                else:
                    if j == 1 or j == kolom:
                        print("#", end="")  # Cetak '#' di awal dan akhir
                    else:
                        print(" ", end="")  # Cetak spasi di tengah
            print()  # Pindah ke baris baru setelah satu baris selesai dicetak

# Contoh pemanggilan fungsi
capitalH(5, 4)
