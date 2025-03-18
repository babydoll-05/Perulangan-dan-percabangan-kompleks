def faktor(a):
    if a == 0 or a == 1:
        return 1
    else:
        return a * faktor(a - 1)

def din(b):
    for f in range(b, 0, -1):
        print(faktor(f), end=" ")
        for a in range(f, 0, -1):
            print(a, end=" ")
        print()

fakto = int(input("Masukkan nilai n: "))
din(fakto)