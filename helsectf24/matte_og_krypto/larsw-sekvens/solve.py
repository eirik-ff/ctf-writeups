de_bruijn = \
"AAABAACAADAAEAAFAAGAAHAAIAAJAAKAALAAMAANAAOAAPAAQAARAASAATAAUAAVAAWAAXAAYAAZAAaAAbAAcAAdAAeAAfAAgAAhAAiAAjAAkAAlAAmAAnAAoAApAAqAA"

seq_list = [ "AjAA", "AiAA", "kAAl", "AAnA", "AiAA", "hAAi", "AnAA", "iAAj",
            "pAAq", "QAAR", "AAlA", "AYAA", "LAAM", "AgAA", "AgAA", "AAiA",
            "AiAA", "WAAX", "mAAn", "nAAo", "jAAk", "AZAA", "AlAA", "LAAM",
            "AqAA"]

flag = []
for seq in seq_list:
    i = de_bruijn.find(seq)
    flag.append(i)

flag = "".join(chr(i) for i in flag)
print(flag)

