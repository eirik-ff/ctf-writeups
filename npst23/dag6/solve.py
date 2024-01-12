import re
from pathlib import Path

text = Path("./input.txt").read_text().encode("utf-8")
special = b"\xE2\x80\x8d"  # https://www.compart.com/en/unicode/U+200D

flag = ""
for match in re.finditer(special, text):
    i = match.span()[1]
    flag += chr(text[i])

print(flag)

