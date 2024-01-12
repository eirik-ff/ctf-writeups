from pathlib import Path

input_file = Path("./random_text.bin")

data = input_file.read_bytes()
data = [d for d in data.split(b"\x00") if len(d) > 0]
data = sorted(data, key=lambda x: len(x))
flag = ""
for d in data:
    f = chr(d[0])
    flag += f
    if f == "}":
        break

print(flag)

