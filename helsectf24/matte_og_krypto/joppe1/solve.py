def lagrange2(x: int, 
              x0: int, 
              x1: int):
    return (x - x1) / (x0 - x1)

def polynomial2(secret0: tuple[int, int], secret1: tuple[int, int]):
    x0, y0 = secret0
    x1, y1 = secret1

    l0 = lambda x: lagrange2(x, x0, x1)
    l1 = lambda x: lagrange2(x, x1, x0)
    f = lambda x: y0 * l0(x) + y1 * l1(x)

    return int(f(0))


# joppe1
secret1 = (-500, 1229)
secret3 = (1000, 2729)
joppe1 = polynomial2(secret1, secret3)
print(joppe1)

