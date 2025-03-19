n=int(input("Masukkan n = "))

for i in range(1,n+1):

    for j in range(1,i+1):
        print(i," ",end='')
    print()


n=int(input("Masukkan n = "))
for i in range(1,n+1):
    if i%2==1:
        for j in range(1,n+1):
            print(j," ",end='')
    else:
        for j in range(n,0,-1):
            print(j," ",end='')
    print()


n=int(input("Masukkan n = "))
for i in range(0,n+1):
    for j in range(1,n-i+1):
        if j % 2 == 1:
            print("X",end='')
        else:
            print("O",end='')
    print()


hasil = ""

x = int(input("Masukkan jumlah :"))
bar = x
# Looping Baris
while bar >= 0:

# Looping Kolom Spasi Kosong
    kol = bar
    while kol > 0:
        hasil += "   "
        kol -= 1

# Looping Kolom Bintang
    kanan = 1
    while kanan < (x - (bar-1)):
        hasil += " * "
        kanan += 1

    hasil = hasil + "\n"
    bar -= 1

print (hasil)