from base64 import b64decode

b64_str = "DAEIFwEHEAIfDQI7DRA7FQUPFzsIDQ8BOwU7BgsQO1IBBgBTAVxSAgVRBVxWAgZUUlZcVFQCXVFWXQIBAAFQVFYFBlAGU1FcUFFXAQFVUFFSVV1TU1FQBwVUUVVVUFEZ"

decoded = bytearray(b64decode(b64_str))
num = 5
num = (num * 2686 + 1432990190) % 256

for i in range(len(decoded)):
    decoded[i] ^= num

print(bytes(decoded).decode())

