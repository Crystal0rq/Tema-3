import random

def jacobi(a, n):
    if n <= 0 or n % 2 == 0:
        return 0

    a = a % n
    result = 1

    while a != 0:
        while a % 2 == 0:
            a //= 2
            if n % 8 in [3, 5]:
                result = -result

        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result

        a = a % n

    return result if n == 1 else 0


def solovay_strassen(n, k):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = jacobi(a, n)

        if x == 0:
            return False

        mod_exp = pow(a, (n - 1) // 2, n)

        if x == -1:
            x = n - 1

        if mod_exp != x:
            return False

    return True


n = 7
if solovay_strassen(n, 10):
    print(f"{n} este probabil prim.")
else:
    print(f"{n} este compus.")
