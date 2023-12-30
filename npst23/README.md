# NPST julen 2023

Dette var PSTs julekalender-CTF for julen 2023. I år var det i også i samarbeid
med NSM og Kripos. 


## Dag 1

### Flagg

```
PST{SYSTEM INFISERT GRUNKER INCOMING}
```


### Oppgave

Mobil-detektiven 📱

---

Her får du den første oppgaven!

Under etterforskningen av hendelsen på jule-verkstedet har vi oppdaget noe rart.
Et av meldingssystemene som sender varslinger til beredskapsvaktene for
verkstedet har sendt en SMS til et ukjent nummer. Meldingen er dessverre helt
uleselig for oss, så vi trenger dine mobildetektiv-egenskaper. Når du finner ut
av det, send meg svar på formatet PST{ditt svar her}.

> 7-4 9-3 7-4 8-1 3-2 6-1 0-1
> 4-3 6-2 3-3 4-3 7-4 3-2 7-3
> 8-1 0-1 4-1 7-3 8-2 6-2 5-2
> 3-2 7-3 0-1 4-3 6-2 2-3 6-3
> 6-1 4-3 6-2 4-1

\- Tastefinger


### Løsning

Det var ikke umiddelbart åpenbart for meg hva tallene betydde. Etter å ha
stirret på dem en stund kan vi se at det første tallet er alltid i intervallet
0-9 og det andre tallet er maks 4. For de som husker tastaturet på gamle 
mobiltelefoner er dette kjent. Det er nemlig hvor mange ganger man må trykke på
hver tast for å få rett tall. `7-4` betyr altså "Trykk på knapp 7 fire ganger".
Jeg laget et script [`solve.py`](./dag1/solve.py) som leser inn alle tallene og
setter sammen flagget. 


### Svar

🤦🏻
- Tastefinger

