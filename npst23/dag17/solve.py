
melding1 = open("melding_1.txt").read()
numbers = [int(n) for n in open("melding_2.txt").read().split(", ")]

unique = ""
for c in melding1:
    if c not in unique:
        unique += c

flag = ""
for n in numbers:
    flag += unique[n]

print(flag)

