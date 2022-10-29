def gcd(a, b):
    if a == 0:
        return b

    return gcd(b%a, a)

assert gcd(35,10) == 5
assert gcd(10,35) == 5

print("ok")