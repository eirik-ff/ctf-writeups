# NPST julen 2023

Dette var PSTs julekalender-CTF for julen 2023. I år var det i også i samarbeid
med NSM og Kripos. 


## Dag 1

### Flagg

`PST{SYSTEM INFISERT GRUNKER INCOMING}`


### Oppgave

> Mobil-detektiven 📱
> 
> ---
> 
> Her får du den første oppgaven!
> 
> Under etterforskningen av hendelsen på jule-verkstedet har vi oppdaget noe
> rart. Et av meldingssystemene som sender varslinger til beredskapsvaktene for
> verkstedet har sendt en SMS til et ukjent nummer. Meldingen er dessverre helt
> uleselig for oss, så vi trenger dine mobildetektiv-egenskaper. Når du finner
> ut av det, send meg svar på formatet PST{ditt svar her}.
> 
> ```
> 7-4 9-3 7-4 8-1 3-2 6-1 0-1
> 4-3 6-2 3-3 4-3 7-4 3-2 7-3
> 8-1 0-1 4-1 7-3 8-2 6-2 5-2
> 3-2 7-3 0-1 4-3 6-2 2-3 6-3
> 6-1 4-3 6-2 4-1
> ```
> 
> \- Tastefinger


### Løsning

Det var ikke umiddelbart åpenbart for meg hva tallene betydde. Etter å ha
stirret på dem en stund kan vi se at det første tallet er alltid i intervallet
0-9 og det andre tallet er maks 4. For de som husker tastaturet på gamle 
mobiltelefoner er dette kjent. Det er nemlig hvor mange ganger man må trykke på
hver tast for å få rett tall. `7-4` betyr altså "Trykk på knapp 7 fire ganger".
Dette kan løses med dette solve scriptet: 

[`solve.py`](./dag1/solve.py):

```python
sequence = "7-4 9-3 7-4 8-1 3-2 6-1 0-1 4-3 6-2 3-3 4-3 7-4 3-2 7-3 8-1 0-1 4-1 7-3 8-2 6-2 5-2 3-2 7-3 0-1 4-3 6-2 2-3 6-3 6-1 4-3 6-2 4-1"
sequence = sequence.split(" ")

keypad = {
    1: "", 2: "ABC", 3: "DEF",
    4: "GHI", 5: "JKL", 6: "MNO",
    7: "PQRS", 8: "TUV", 9: "WXYZ",
    0: " "
}

flag = "PST{"
for seq in sequence:
    num, idx = (int(i) for i in seq.split("-"))
    idx -= 1
    flag += keypad[num][idx]

flag += "}"
print(flag)
```


### Svar

> 🤦🏻
> \- Tastefinger


## Dag 2

### Flagg

`PST{LØSTE_DU_DENNE_SOM_PUSLESPILL_ELLER_KUBE?:)}`


### Oppgave

> Scrambled
> 
> ---
> 
> Over natten har det vært store utfordringer knyttet til en av maskinene i
> verkstedet. En serie feilproduserte leker har kommet på rullende bånd. Vi
> prøver å finne ut hva som har skjedd. Graver du ned i det her?
>
> \- Mellomleder

Vedlegg:

![dag2-vedlegg](./dag2/oedelagte_leker_fix.png)


### Løsning

Fra vedlegget ser vi at vi har alle sidene til en Rubiks kube som er brettet ut
flatt, hvor hver firkant har en bokstav. Måten å løse oppgaven på er da å løse
Rubiks kuben slik at vi kan lese flagget på kuben. Det er flere måter å løse den
på. 

Den mest åpenbare måten er å løse den fysisk. Jeg gjorde opprinnelig dette,
men glemte å ta bilder av prosessen. Måten jeg gjorde det på var å først
overføre den flate kuben i en kube-løser nettside som f.eks.
[denne](https://rubiks-cube-solver.com/) hvor man kan tegne den flate kuben.
Deretter tok jeg å kjørte løsningen i revers for å få den rette kuben. Så var
det å klippe opp flere post-it-lapper og skrive bokstaver på dem, for så å løse
kuben og lese av.

En annen måte er å gjøre det manuelt i f.eks. Excel. Dette er mulig fordi hver
sub-kube i Rubiks kuben har kun én mulig plassering i en løst kube. F.eks. har
en hjørnebrikke med rød, blå og hvit kun ett rett sted i den løste kuben. Vi tar
derfor bokstavene fra den uløste kuben og overfører til de eneste stedene de
passer i en løst kube. Dette krever en del visualisering og hjernetrim, men det
går til slutt. Se [`solve.xlsx`](./dag2/solve.xlsx) for løsning. 

Etter å ha løst kuben ser vi at den rød siden sier hvilken rekkefølge vi skal
lese svaret i: `RBWGOY` = `red, blue, white, green, orange, yellow`. Dette gir
oss da flagget. 


### Svar

> Her var det mye røre! Bra du klarte å finne ut av det!
> 
> \- Mellomleder


## Dag 3

### Flagg

`KRIPOS{Husk å se etter spor i snøen!}`


### Oppgave

> 📃Redacted
> 
> ---
> 
> Det er krise! Filene på alvemaskinene har blitt kryptert, og vi har ingen
> backups tilgjengelig!
> 
> På nissens skrivebord fant vi det vedlagte brevet, sammen med en kryptert fil.
> 
> Det er ubeskrivelig viktig at vi får åpnet denne filen igjen umiddelbart, da
> Jule NISSEN ikke klarer å huske innholdet!
> 
> \- Mellomleder

Vedlegg:

* [Mitt utpressingsbrev.docx](<./dag3/Mitt utpressingsbrev.docx>)
* [huskeliste.txt.enc](./dag3/huskeliste.txt.enc)

### Løsning

Vi får utdelt et Word-dokument med en ransom-note:

![Ransom note original](./dag3/figures/ransom-note-original.png)

Det er tilsynelatende "REDACTED", men dette er kun en svart boks vi lett kan
flytte. Det samme gjelder bildet midt på siden som viser krypto-metoden. Etter å
fikse disse figurene ser dokumentet slik ut:

![Ransom note solved](./dag3/figures/ransom-note-solved.png)

Vi har dermed fått nøkkelen og krypteringsmetoden. Det modifiserte
Word-dokumentet får du [her](<./dag3/Mitt utpressingsbrev løst.docx>). 

For å dekryptere huskelisten lager vi et script som leser inn ciphertexten,
kjører ROT13 på IVen og dekrypterer med AES-CTR:

[`solve.py`](./dag3/solve.py):
```python
from pathlib import Path
from binascii import unhexlify
from Crypto.Cipher import AES
from Crypto.Util import Counter

def rot13(text):
    result = []
    for char in text:
        if "a" <= char <= "z":
            result.append(chr((ord(char) - ord("a") + 13) % 26 + ord("a")))
        elif "A" <= char <= "Z":
            result.append(chr((ord(char) - ord("A") + 13) % 26 + ord("A")))
        else:
            result.append(char)
    return "".join(result)


# 24 bytes = 192 bit key
key = unhexlify("dda2846b010a6185b5e76aca4144069f88dc7a6ba49bf128")

# IV is ROT13 encoded before use
iv = "UtgangsVektor123"
iv_rot13 = rot13(iv)

iv = iv_rot13.encode()

enc = Path("./huskeliste.txt.enc").read_bytes()

cipher = AES.new(
    key,
    AES.MODE_CTR,
    counter=Counter.new(128, initial_value=int.from_bytes(iv, byteorder="big"))
)

dec = cipher.decrypt(enc)

print(dec.decode("latin-1"))
```


### Svar

> Flott!
> 
> Jeg kaller inn til et møte med Jule NISSEN og de andre påvirkede så vi kan få
> delt ut informasjonen igjen.
> 
> \- Mellomleder


## Dag 4

### Flagg

`PST{ASCII_art_er_kult}`


### Oppgave

> Pinneved
>
> ---
> 
> Alvebetjentene på Jule NISSEN sitt verksted våknet i dag til et fryktelig syn;
> Julenissens slede er sprengt i fillebiter. Vi har satt folk på saken for å
> finne ut av hvem som er ansvarlig for ødeleggelsen, men det er kritisk at
> sleden blir reparert slik at vi får testet den før Jule NISSEN skal levere
> pakkene.
> 
> Alvebetjentene har samlet vrakrestene, samt verktøyet de mistenker at
> sabotørene har brukt.
> 
> Vi trenger at du rekonstruerer sleden så fort som mulig!
>
> \- Tastefinger

Vedlegg:

* [pinneved.py](./dag4/pinneved.py)
* [pinneved.txt](./dag4/pinneved.txt)


### Løsning

Dette er en reversing-oppgave hvor vi skal reversere `pinneved.py`-scriptet for
å rekonstruere sleden. Kort fortalt tar `pinneved.py`-scriptet den sammensatte
sleden og deler opp i 24 fragmenter med `explode()` funksjonen som lagres i
`bang`. Hvert tegn i hvert fragment blir så gjort om til det tegnet som kommer 2
etter som blir lagret i `eksplosjon`. Disse omgjorte fragmentene blir så satt
sammen ved å bruke indeksene i `otp` arrayet. Solve-scriptet under gjor denne
prosessen baklengs. 

[`solve.py`](./dag4/solve.py):
```python
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
```

Den sammensatte sleden kan sees i [`slede.txt`](./dag4/slede.txt).


### Svar

> Et faktisk kunstverk! Godt jobbet!
> 
> Vi setter i gang testingen sporenstreks.
> 
> \- Tastefinger

