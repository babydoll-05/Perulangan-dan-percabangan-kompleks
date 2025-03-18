def filter_ganjil(angka_list):
    return " ".join(str(angka) for angka in angka_list if angka % 2 == 1)

# Contoh penggunaan
angka_list = [1, 2, 3, 4, 5, 6, 7]
print(filter_ganjil(angka_list))  # Output: "1 3 5 7"
