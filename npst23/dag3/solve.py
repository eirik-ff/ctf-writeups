from pathlib import Path
from binascii import unhexlify
from Crypto.Cipher import AES
from Crypto.Util import Counter

def rot13(text):
    result = []
    for char in text:
        if "a" <= char <= "z":
            result.append(chr((ord(char) - ord("a") + 13) % 26 + ord("a")))
        elif "A" <= char <= "Z":
            result.append(chr((ord(char) - ord("A") + 13) % 26 + ord("A")))
        else:
            result.append(char)
    return "".join(result)


# 24 bytes = 192 bit key
key = unhexlify("dda2846b010a6185b5e76aca4144069f88dc7a6ba49bf128")

# IV is ROT13 encoded before use
iv = "UtgangsVektor123"
iv_rot13 = rot13(iv)

iv = iv_rot13.encode()

enc = Path("./huskeliste.txt.enc").read_bytes()

cipher = AES.new(
    key,
    AES.MODE_CTR,
    counter=Counter.new(128, initial_value=int.from_bytes(iv, byteorder="big"))
)

dec = cipher.decrypt(enc)

print(dec.decode("latin-1"))

