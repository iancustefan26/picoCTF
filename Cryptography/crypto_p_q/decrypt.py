n = 1422450808944701344261903748621562998784243662042303391362692043823716783771691667
c = 843044897663847841476319711639772861390329326681532977209935413827620909782846667
e = 65537

p = 2159947535959146091116171018558446546179
q = 658558036833541874645521278345168572231473

totient = (p - 1) * (q - 1)

def extended_gcd(a, b):
    """
    Extended Euclidean Algorithm to find the greatest common divisor of a and b.
    It returns a tuple (g, x, y) where g is the gcd of a and b, and x and y are
    the coefficients of Bézout's identity (ax + by = g).
    """
    if a == 0:
        return b, 0, 1
    else:
        g, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return g, x, y

def modular_inverse(e, phi):
    """
    Finds the modular inverse of e modulo phi using the Extended Euclidean Algorithm.
    """
    g, x, y = extended_gcd(e, phi)
    if g != 1:
        raise ValueError('Modular inverse does not exist')
    else:
        return x % phi


d = modular_inverse(e,totient)

message = pow(c, d, n)

#print(bytearray.fromhex(hex(message)).decode())
print(bytearray.fromhex(hex(message)[2:]))