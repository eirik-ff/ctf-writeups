from Crypto.Util.number import bytes_to_long, long_to_bytes
from binascii  import hexlify, unhexlify

e = 0x10001
N = int(input("N (int) = "))
print()

contract = b"Dette er en superviktig kontrakt for veeldig viktige ting med store ord og uforstaaelige kruseduller."
m = bytes_to_long(contract)

e2 = pow(2, e, N)
m2 = (m * e2) % N
print("m' (hex) =", hexlify(long_to_bytes(m2)).decode())
print()
print()

s2 = bytes_to_long(unhexlify(input("signature for m' (hex) = ")))
s = s2 // 2

print()
print("s (hex) =", hexlify(long_to_bytes(s)).decode())

