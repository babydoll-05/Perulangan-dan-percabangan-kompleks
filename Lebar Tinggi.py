t = int(input("Tinggi: "))
l = int(input("Lebar: "))
counter = 1
for i in range(t):
    for j in range(l):
        print(counter, end=' ')
        counter += 1
    print()