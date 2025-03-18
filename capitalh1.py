def capitalH(baris, kolom):
    if baris >= 3 and kolom >= 3:  # Cek apakah dimensi minimal 3x3
        if baris % 2 == 1:  # Baris harus ganjil agar ada tengahnya
            for i in range(baris):
                if i != (baris // 2):  
                    print("#" + " " * (kolom - 2) + "#")  # Baris atas dan bawah
                else:
                    print("#" * kolom)  # Baris tengah penuh dengan '#'
        else:
            print("dimensi tidak sesuai")  # Jika baris genap
    else:
        print("dimensi tidak sesuai")  # Jika dimensi terlalu kecil

# Contoh pemanggilan fungsi
capitalH(5, 5)
