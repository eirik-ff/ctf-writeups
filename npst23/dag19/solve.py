
nissetekst = open("part2/nissetekst").read()
code = eval(open("part3/hemmelig/code").read())  # eval FYFY!

flag = ""
for c in code:
    flag += nissetekst[c]

print(flag)

