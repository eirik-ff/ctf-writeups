from pathlib import Path

otp = [23, 2, 0, 5, 13, 16, 22, 7, 9, 4, 19, 21, 18, 10, 20, 11, 12, 14, 6, 1, 3, 8, 17, 15]
pinneved = Path("./pinneved.txt").read_text()

def explode(input, antall):
    størrelse = len(input) // antall
    fragmenter = []
    
    for i in range(0, len(input), størrelse):
        fragment = input[i:i+størrelse]
        fragmenter.append(fragment)
    
    return fragmenter

pinneved = explode(pinneved, 24)
pinneved_reversed = [""] * 24
for n, i in enumerate(reversed(otp)):
    pinneved_reversed[i] = pinneved[n]
eksplosjon = [
        ''.join([
            chr(ord(c) - 2) for c in fragment
        ]) 
        for fragment in pinneved_reversed
]
bang = "".join(eksplosjon)

Path("./slede.txt").write_text(bang)
print("Wrote answer to file slede.txt")

