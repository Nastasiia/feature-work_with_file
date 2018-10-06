# Wrong gcd find 5 mistakes

def gcd(a, b):
    assert a >= 0 and b >= 0
    while a!=0 and b!=0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return (a+b)

# Examples

gcd(10, 0)
gcd(123, 3)
gcd(1000000, 64)
gcd(0, 0)
