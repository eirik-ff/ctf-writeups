
def scytale_decrypt(ciphertext: str, turns: int) -> str:
    assert len(ciphertext) % turns == 0, \
        f"Turns ({turns}) must divide ciphertext length ({len(ciphertext)})"

    letters_per_turn = len(ciphertext) // turns
    plaintext = ""
    for t in range(letters_per_turn):
        row = ciphertext[t::letters_per_turn]
        plaintext += row

    return plaintext


def scytale_encrypt(plaintext: str, turns: int) -> str:
    assert len(plaintext) % turns == 0, \
        f"Turns ({turns}) must divide plaintext length ({len(plaintext)})"

    ciphertext = ""
    for t in range(turns):
        column = plaintext[t::turns]
        ciphertext += column

    return ciphertext


def divisors(n: int) -> list[int]:
    div = []
    for d in range(1, n // 2 + 1):
        if n % d == 0:
            div.append(d)

    div.append(n)
    return div


def scytale_decrypt_bruteforce(ciphertext: str, 
                               known_plaintext: str, 
                               ignore_case: bool = False) -> list[int]:
    all_turns = divisors(len(ciphertext))

    possible_turns = []
    for turns in all_turns:
        plaintext = scytale_decrypt(ciphertext, turns)

        if ignore_case:
            known = known_plaintext.lower()
            plaintext = plaintext.lower()
        else:
            known = known_plaintext

        if known in plaintext:
            possible_turns.append(turns)

    return possible_turns


ciphertext = open("melding.txt", "rb").read().decode("utf-8")
for turns in scytale_decrypt_bruteforce(ciphertext, "pst{"):
    print(scytale_decrypt(ciphertext, turns))

