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

