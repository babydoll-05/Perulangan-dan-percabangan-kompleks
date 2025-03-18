def primaterdekat(prima):
    for p in range(2, prima):
        if prima % p == 0:
            return False 
    return True

def bil_prima_terdekat(user):
    while user > 0:
        user -= 1
        if primaterdekat(user):
            return user
    return None

user = int(input("Masukkan angka:) : "))
prima_paling_dekat = bil_prima_terdekat(user)

if prima_paling_dekat:
    print(f"Bilangan prima paling dekat dari {user} adalah {prima_paling_dekat}")
