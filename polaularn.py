def polaular(n):
    set_angka = ([f"{i:02d}" for i in range(1, (n**2) + 1)])
    print(set_angka)
    
    start = 0
    stop = n
    step = 1

    for i in range(n):
        for j in range(start, stop, step):
            print(set_angka[j], end=" ")
        print()

        if step == 1:
            step = -1
            start = stop + n - 1
            stop -= 1
        else:
            step = 1
            stop = start + n - 1
            start += 1

polaular(5)
