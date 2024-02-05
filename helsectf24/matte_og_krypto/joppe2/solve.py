# Assuming always 5 parts and knowing 3 shares is enough
from Crypto.Util.number import long_to_bytes

def reconstruct(secret0: tuple[int, int], 
                secret1: tuple[int, int], 
                secret2: tuple[int, int]):
    x0, y0 = secret0
    x1, y1 = secret1
    x2, y2 = secret2

    # We can't use floating points as we lose precision, but ints in Python
    # have arbitrary precision, so we do all calculations using ints.
    # The formulas has been manually manipulated on paper to end up at the ones
    # below. 
    prod = (x0 - x1) * (x0 - x2) * (x1 - x2)

    f_prod = lambda x: y0 * (x - x1) * (x - x2) * (x1 - x2) -\
                       y1 * (x - x0) * (x - x2) * (x0 - x2) +\
                       y2 * (x - x0) * (x - x1) * (x0 - x1)

    eval0 = f_prod(0)
    assert eval0 % prod == 0, "Modulo test failed"
    f0 = eval0 // prod
    return f0
    

# joppe2
secret2 = (2588682506107567, 655305480793967733879479427128553132958736140573542016023878)
secret4 = (4359708773407619, 655305480794013934214261797861718778141983069985929089695418)
secret5 = (6634057562378419, 655305480794107806938926839990618969191800755240410150653418)
joppe2 = reconstruct(secret2, secret4, secret5)
print(long_to_bytes(joppe2).decode())

