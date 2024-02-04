from binascii import unhexlify

def to_bytes(with_spaces: str) -> bytes:
    return unhexlify("".join(with_spaces.split(" ")))

with open("flag-smaller.bz2", "wb") as fp:
    fp.write(to_bytes("42 5a 68 39"))

    fp.write(to_bytes("31 41 59 26  53 59 89 0d 70 a4 00 5d be 5b 80 c0 10 04 "
                      "00 4c  00 00 00 bb c7 1e 2a 00 08 20 00 54 36 a8 9b 48 "
                      "d0 19 18 20 8a a6 80 0d 00 d3 6a 40 2a a2 8a 92  92 a2 "
                      "a0 82 81 16 69 5a 4b bf 2b c5 2b d4 61 5d  f0 d1 af b7 "
                      "d7 36 6b ad a7 de 23 09 66 c9 00 08  10 0b f1 77 24 53 "
                      "85 09 02 24 32 7f 80"))
