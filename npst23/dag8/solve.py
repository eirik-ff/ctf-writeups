from binascii import unhexlify

modulus = unhexlify(open("modulus.hex", "r").read())
modulus_int = int.from_bytes(modulus, "big")
ciphertext = open("ciphertext.bin", "rb").read()
ciphertext_int = int.from_bytes(ciphertext, "big")

e = 2**16 + 1
p = modulus_int
d = pow(e, -1, p - 1)

c = ciphertext_int
message_int = pow(c, d, p)
length = (message_int.bit_length() + 7 ) // 8
message = message_int.to_bytes(length, "big")
print(message.decode())

