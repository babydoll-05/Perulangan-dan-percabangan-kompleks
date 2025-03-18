def is_prime(bilangan):
    if bilangan < 2:
        return "bukan prima"
    for i in range(2, int(bilangan**0.5) + 1):
        if bilangan % i == 0:
            return "bukan prima"
    return "prima"

# Contoh penggunaan
print(is_prime(1))   # Output: bukan prima
print(is_prime(2))   # Output: prima
print(is_prime(100)) # Output: bukan prima
print(is_prime(23))  # Output: prima
