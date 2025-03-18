def elevator(n):
    lantai_prima = []  
    for i in range(2, n+1):  # Mengecek setiap lantai dari 2 hingga N
        is_prima = True  
        for j in range(2, int(i**0.5) + 1):  # Cek apakah angka prima
            if i % j == 0:
                is_prima = False
                break  
        if is_prima:
            lantai_prima.append(i)

    print("Elevator berhenti di lantai:", ", ".join(map(str, lantai_prima)))

# Contoh penggunaan dengan while untuk memastikan input valid
while True:
    try:
        n = int(input("Masukkan jumlah lantai: "))
        if n < 2:
            print("Jumlah lantai minimal harus 2.")
            continue
        elevator(n)
        break
    except ValueError:
        print("Harap masukkan angka yang valid.")
