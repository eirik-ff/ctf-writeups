from Crypto.Cipher import AES
from base64 import b64decode
import json

from binascii import unhexlify


# from hemmeligheter.txt
hexstrs = ["a3c5a5a81ebc62c6144a9dc1ae5cce11",
           "980daad49738f76b80c8fafb0673ff1b",
           "fc78e6fee2138b798e1e51ed15e0a109"]

key = 0
for k in hexstrs:
    key ^= int.from_bytes(unhexlify(k), "big")

key = key.to_bytes((key.bit_length() + 7 ) // 8, "big")

with open("melding.enc", "rb") as f:
    data = json.loads(f.read())
    nonce = b64decode(data["nonce"])
    ciphertext = b64decode(data["ciphertext"])
    tag = b64decode(data["tag"])
    cipher = AES.new(key, AES.MODE_GCM, nonce = nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    print("Dekryptert melding: " + plaintext.decode('utf-8'))

