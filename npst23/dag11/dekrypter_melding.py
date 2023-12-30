from Crypto.Cipher import AES
from base64 import b64decode
import json

key = ???

with open("melding.enc", "rb") as f:
    try:
        data = json.loads(f.read())
        nonce = b64decode(data["nonce"])
        ciphertext = b64decode(data["ciphertext"])
        tag = b64decode(data["tag"])
        cipher = AES.new(key, AES.MODE_GCM, nonce = nonce)
        plaintext = cipher.decrypt_and_verify(ciphertext, tag)
        print("Dekryptert melding: " + plaintext.decode('utf-8'))
    except (ValueError, KeyError):
        print("Oisann, noe gikk galt!")