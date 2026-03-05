import math

def fermat_factor(n):
    if n % 2 == 0:
        return 2, n // 2

    t = math.isqrt(n)
    if t * t < n:
        t += 1

    while True:
        s2 = t * t - n
        s = int(math.isqrt(s2))

        if s * s == s2:
            a = t - s
            b = t + s
            return a, b

        t += 1
        
n = 40723
a, b = fermat_factor(n)
print(a, b)

