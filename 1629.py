def modular_pow(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent >>= 1
        base = (base * base) % modulus
    return result

a, b, c = map(int, input().split())
print(modular_pow(a, b, c))
