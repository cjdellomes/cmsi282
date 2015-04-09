import math

def extended_euclidean(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = extended_euclidean(b % a, a)
    return g, x - math.floor(b / a) * y, y

def modular_inverse(a, mod):
    g, x, y = extended_euclidean(a, mod)
    if g != 1:
        return False
    return x % mod

def is_square(n):
    if math.sqrt(n) == int(math.sqrt(n)):
        return True
    return False

def factor(n):
    a = math.ceil(math.sqrt(n))
    b = (a ** 2) - n
    while is_square(b) == False:
        a += 1
        b = (a ** 2) - n
    b = math.floor(math.sqrt(b))
    p = a - b
    q = a + b
    return p, q

def private_key(e, primes):
    return modular_inverse(e, (primes[0] - 1) * (primes[1] - 1))

print(private_key(5, factor(729880581317)))