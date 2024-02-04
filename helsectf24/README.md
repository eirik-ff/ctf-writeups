# HelseCTF 2024

# Innholdsfortegnelse

TODO


# matte og krypto

## alder

### Oppgave

> Kari og Ola er to gamle vampyrer.
> 
> I dag er Kari 3133713 år eldre enn Ola. Om 5 år vil Kari være 4 ganger eldre
> enn Ola. Hvor gammel er Kari og Ola i dag?
> 
> Flaggformat: `helsectf{<alder kari>_<alder ola>}`
> 
> Som eksempel, hvis Kari er 1 år og Ola er 3 år så ville svaret vært
> `helsectf{1_3}`. Merk at dette bare var et eksempel for å vise deg hvordan du
> leverer når du har riktig svar.

### Løsning


## reisetid

### Oppgave

> Kari og Ola bor 150km fra hverandre og skal møtes for å ta en kaffe. Kari
> kjører kl 1200, og ville brukt 3 timer om hun måtte kjøre hele lengden på
> 150km. Ola kjører kl 1300, og ville brukt 5 timer om han måtte kjøre hele
> lengden på 150km.
> 
> Hva er klokka når de møtes, og hvor langt i meter har Kari kjørt?
> 
> Flaggformat: `helsectf{<tid 4tall>_<lengde i meter>}`
> 
> Som eksempel, hvis de møtes kl 1201 og Kari har kjørt 11km så vil svaret være
> `1201_11000`. Merk at dette bare var et eksempel for å vise deg hvordan du
> leverer når du har riktig svar.

### Løsning


## Larsw sekvens

### Oppgave

> Vi har fanget opp en spesiell sekvens
> `AAABAACAADAAEAAFAAGAAHAAIAAJAAKAALAAMAANAAOAAPAAQAARAASAATAAUAAVAAWAAXAAYAAZAAaAAbAAcAAdAAeAAfAAgAAhAAiAAjAAkAAlAAmAAnAAoAApAAqAA`
> med en liste av korte tegn:
> 
>     AjAA
>     AiAA
>     kAAl
>     AAnA
>     AiAA
>     hAAi
>     AnAA
>     iAAj
>     pAAq
>     QAAR
>     AAlA
>     AYAA
>     LAAM
>     AgAA
>     AgAA
>     AAiA
>     AiAA
>     WAAX
>     mAAn
>     nAAo
>     jAAk
>     AZAA
>     AlAA
>     LAAM
>     AqAA
> 
> Kameraten til Lars sier at han kan ha brukt dette til å kryptere flagget. Lars
> har muligens en overdreven interesse i sekvenser laget av Nicolaas Govert.

### Løsning


## joppe1

### Oppgave

> Redd Joppe, død eller levende!
> 
> Ola har en lei tendens til å miste muldvarpen sin, Joppe. Denne gangen er den
> blitt kidnappet av Adi Shamir og hans venner. Adi har låst den inn i safen med
> en kode som ingen helt vet.
> 
> De tre vennene har delt koden mellom seg på en slik måte at du trenger to av
> bitene for å kunne rekonstruere koden til safen.
> 
> De går med på å gi deg sin bit hvis du kan løse deres gåte.
> 
> Bruk endepunktet under for å prøve deg på gåtene.
> 
> Om du bruker du Adis metode eller ikke så finner du koden på null.

### Løsning


## joppe2

### Oppgave

> Redd Joppe, død eller levende!
> 
> Joppe er igjen låst inn av Adis venner.
> 
> Denne gangen er koden delt slik at du trenger 3 av bitene fra gjengen på 5 for
> å finne koden til safen der Joppe ligger. Koden inneholder også flagget.
> 
> Det er ganske store tall, presisjonen må opp og Adi kan ha glemt å bruke
> modulo her.

### Løsning


## joppe3

### Oppgave

> Redd Joppe, død eller levende!
> 
> Koden blir igjen delt opp mellom de 5 og man må løse minst 3 oppgaver for å
> finne koden til låsen.
> 
> Men denne gangen hadde Adi sovet dårlig, og noe gikk galt. Presisjonen på
> tallflytsoperasjonene ble noe unøyaktig, også mumlet Adi noe om at "finner du
> x, finner du koden".
> 
> Igjen er det ganske store tall, presisjonen må opp og Adi har igjen glemt å
> bruke modulo her.

### Løsning


## Kontraktsignering

## Oppgave

> Signaturtjenesten 2OpphøydIe signerer alle dine meldinger, bortsett fra den
> superviktige kontrakten.
> 
> Alle som har riktig signatur på kontrakten får flagget!

## Løsning


# rev

## babyrev_fortran

Flagg: `helsectf{l3nGe_s1D3n_f01k_progaMMeR7e_i_Fortran_90}`

### Oppgave

> En babyrev husker gamle fortellinger fra sin bestefar som programmerte i et
> litt utdatert programmeringsspråk. Heldigvis kom det en senere revisjon på
> 90-tallet som er noe enklere å bruke.
> 
> Greier du å printet ut flagget i klartekst?

### Løsning

Jeg åpner binærfilen i Ghidra og går til `main`-funksjonen:

![](./rev/babyrev_fortran/figures/main.png)

Funksjoner med prefiksen `_gfortran` er innebygde funksjoner for
standard-funksjoner i Fortran (f.eks. `WRITE`). Fra det jeg klarte å forstå må
Fortran først starte skriving (`st_write`) for så å overføre bytene som skal
skrives til skjermen (`transfer_character_write`), for å til slutt stoppes
(`st_write_done`). 

Går vi inn i funksjonen jeg har døpt `load_flag_into_buffer_and_maybe_decrypt`
ser vi:

![](./rev/babyrev_fortran/figures/load_flag_into_buffer_and_maybe_decrypt.png)

Den kopierer flagget fra en global variabel `__a_MOD_flag`, og basert på siste
argument kjører den noe mer kode. Går vi videre inn i `decrypt_flag_buffer` ser
vi:

![](./rev/babyrev_fortran/figures/decrypt_flag_buffer.png)

Funksjonen looper gjennom flagget og dekoder/dekrypterer det på linje 26-28. Jeg
prøvde først å lage en Python-script som gjorde samme dekoding, men fikk det
ikke til å fungere. 

Derfor løste jeg oppgaven dynamisk. Jeg åpnet binæren i GDB og satt en
breakpoint på if-setningen i `load_flag_info_buffer_any_maybe_decrypt`. Ved å
manuelt skippe instruskjonen for if-setningen fikk jeg kjørt
`decrypt_flag_buffer`, men her hang programmet seg. 

Min teori for hvorfor dette skjer er at `st_write` ble først kjørt i `main`, og
deretter igjen i `decrypt_flag_buffer` *uten* at `st_write_done` blir kjørt
først. I GDB så jeg at programmet henger fordi det venter på en mutex. 

Løsningen min ble å patche binæren med `hexedit` til å ikke kjøre `st_write` i
`main` ved å erstatte `call` instruksjonen med `nop` (`0x90`). Assembly-koden
gikk fra

![](./rev/babyrev_fortran/figures/before_patch.png)

til

![](./rev/babyrev_fortran/figures/after_patch.png)

Merk at adressene er de samme. Jeg gjorde samme patch med if-setningen. 

Når jeg nå kjører binærfilen blir flagget skrevet ut. Programmet får segfault,
men det skjer etter at flagget blir skrevet ut så det betyr ikke noe her. 


## babyrev_rust 

Flagg: `helsectf{rask_rust_rimer_relativt_riktig!}`

### Oppgave

> En babyrev er litt Rust(en) i programmering. Hen har programmet inn et flagg i
> kildekoden, kompilert det til en binærfil (se vedlagt fil) men har så greid å
> mistet kildekoden. Om hen bare hadde skrevet ned argumentet. Kan du finne
> flagget og levere det inn?
> 
> Reven har noen vage minner om at det kan være et par hint i filen som kan
> hjelpe en ivrig REverser i å finne flagget.

### Løsning

Jeg installerer Ghidra pluginen [GhidRust](https://github.com/DMaroo/GhidRust)
og åpner binærfilen i Ghidra. Der blir jeg møtt med klønete dekopilert
"Rust"/pseudo-C-kode som er vanskelig å forstå. Etter mye stirring, lesing om
reversing av Rust
([CheckPoint Research sin
artikkel](https://research.checkpoint.com/2023/rust-binary-analysis-feature-by-feature/)
synes jeg var hjelpsom), hjelp fra ChatGPT, og dekompilere små Rust-programmer
for å skjønne flyten, kom jeg frem til at programmet leser inn en streng fra
`argv` og tester om den strengen er lik flagget. Det er en del funksjoner som
kjøres som `reverse`, `join`, og `rev`, men jeg skjønner ikke hvordan disse
henger sammen. 

Problemet er her måten strenger lagres på i Rust. Alle strenger lagres som en
kontinuerlig blokk i minne som gjør at Ghidra ikke forstår hvor en streng
slutter og en annen starter. Pseudokoden ser også ganske uforståelig ut:

![](./rev/babyrev_rust/figures/flag_string_weird.png)

Jeg kom frem til at strengen sikkert er definert som et array av `char`, og at
dette blir oversatt til en variabel med en `char`/`string` og variabelen som
ligger rett etter i minne er lengden. F.eks. `local_3b0 = "h"` og `local_3a8 =
1` (etter betyr her lavere minneadresse). 

Her er det da to måter å gå frem. Enten manuelt sette sammen alle `local_XXX`
variabelene i rett rekkefølge basert på minneadressen, eller dynamisk. Jeg gir
for dynamisk. Etter flagget er definert kommer det en skjekk:

![](./rev/babyrev_rust/figures/eq_after_flag.png)

`local_a8` er resultatet av `join` og `local_90` er det vi skrev inn som
argument. Jeg åpner derfor binæren i GDB og setter et breakpoint på
`call`-instruksjonen til `_<>::eq`. Siden `local_a8` er andre argument til
funksjonen, vet vi at det lastes inn i `RSI`-registeret. Derfor kan vi skrive ut
innholdet i minnet der `RSI` peker, og dermed får vi flagget. 


## StateOfGo

### Oppgave

> Mitt Go-program kompilerer fint, men viser ikke flagget? Jeg som trodde Go
> aldri kunne gjøre noe feil!? Se om det hjelper å overskrive en byte på
> vilkårlig offset.

### Løsning


## Seksjoneringsavdelingsdirektør Gustavsen

### Oppgave

> De jobber i feil seksjon, hr. Gustavsen!

### Løsning


## debug_rat

### Oppgave

> En god RAT går aldri av moten! Vi har deployet en test, men glemte å slå av
> feilsøkingsgrensesnittet og andre skjulte kommandoer.
> 
> Kan du ta kontrollen på råtta og se om det er mulig å få ut flagget som ligger
> lagret på `/flag.txt`?
> 
> Oppdatering: Obs! Noen kan finne flagget på en måte som inneholder en feil -
> det har doble underscores '__'. Korrekt flagg er uten doble underscores.
> 
> PS! Binarien er en fult fungerende Remote Access Trojan som gir Remote Code
> Execution. I god stil er derfor oppgavefilen pakket i en kryptert zip.
> (passord: infected)

### Løsning


# maldoc

## easy_flag

### Oppgave

> Du har fått i oppgave å analysere et Excel-ark for å se om det kan inneholde
> en skjult melding.
> 
> I god stil er oppgavefilen pakket i en kryptert zip. (passord infected)

### Løsning


## hidden

### Oppgave

> Enda et Excel-ark! Men denne gangen fant vi ingen macroer... Men hvor er
> flagget?
> 
> I god stil er oppgavefilen pakket i en kryptert zip. (passord infected)

### Løsning


## Claim_in_mail

### Oppgave

> Du har fått en e-post med et html-vedlegg. Det er vel bare å åpne det?
> 
> Tips: Nøst opp i angrepskjeden. Finn ut hva den forsøker å kjøre. Målet er å
> finne siste tilgjengelig steg i kjeden.
> 
> I god stil er oppgavefilen pakket i en kryptert zip. (passord infected)

### Løsning


## Pass or fail?

### Oppgave

> .bat - filer kan gjøre ganske mye. Denne bat-filen vil ikke kjøre noe skummelt
> om du kjører den. Finn ut hva den gjør. Evt hva du kan mate den med (input)
> for å få ønsket resultat.
> 
> Flagget gjemmer seg i en pass, ikke en fail.
> 
> Passord for zip-fil er standard (infected).

### Løsning


# misc

## Skalerbar vektorgrafikk

### Oppgave

> Flagget finnes i den vedlagte SVG-fila.

### Løsning


## tetris1

### Oppgave

> I denne runden av HelseCTF har vi laget vårt eget tetris-spill. Spill tetris
> til du har fått rydda bort totalt fem linjer.

### Løsning


## tetris2

### Oppgave

> Før du starter spillet står det hvilke taster som kan brukes for å styre
> spillet. Én av tastene er ikke listet og gir uante muligheter. Bruk tasten mye
> og få et flagg.

### Løsning


## tetris3 

### Oppgave

> Nede i horisonten, under fjell, snø og terreng ligger det et flagg.

### Løsning


## tetris4

### Oppgave

> Spill til du har fått renska 5000 linjer på brettet.

### Løsning


## bombzip2

### Oppgave

> Vi har en bzip2-fil som inneholder et komprimert flagg, men den utpakka fila
> er kjempestor. Mange, mange terabyte, og flagget ligger helt på slutten. Hvis
> du prøver å pakke den ut fyller du sannsynligvis harddiskene dine. Derfor er
> oppgaven uløselig.

### Løsning


## null pointer

### Oppgave

> Utvikler Per Ointer trenger av og til å kjøre python-programmer på webserveren
> sin. Derfor har han laget en veldig enkel webtjeneste for å sende inn
> python-programmer og returnere output:
> 
> Eksempelkjøring av program: `curl 'http://server/?program=print(repr(repr))'`
> 
> For å hindre misbruk er kun 10 forskjellige tegn tillatt i python-programmet:
> `pointer(*)`
> 
> Dessverre viser det seg at dette ikke er godt nok. Hent ut flagget i fila `0`
> i current directory.

### Løsning


## not cipher

### Oppgave

> Utvikler Carl I. Pher trenger av og til å kjøre python-programmer på
> webserveren sin. Derfor har han laget en veldig enkel webtjeneste for å sende
> inn python-programmer og returnere output:
> 
> Eksempelkjøring av program: `curl 'http://server/?program=print(repr(repr))'`
> 
> For å hindre misbruk er kun 13 forskjellige tegn tillatt i python-programmet:
> `not+cipher(*)`
> 
> Dessverre viser det seg at dette ikke er godt nok. Hent ut flagget i
> `/lol/hemmeligmappe/flagg.txt`

### Løsning


# stego

## image processing 1 

### Oppgave

> fourier-transformasjoner kan brukes til mye innenfor bildeprosessering. man
> kan lett beregne en diskret fourier-transformasjon til et bilde i python:
> 
>     ft = numpy.fft.fft2(img_data)
> 
> en vanlig måte å visualisere en kompleks fourier transformasjon på er å skyve
> den slik at origo, og de laveste frekvensene havner i midten av
> visualiseringen. for å visualisere komplekse tall i vanlige grå-farger tar man
> gjerne normen / absoluttverdien til de komplekse verdiene. det er også vanlig
> å visualisere det med en logaritmisk skala, siden endringene i
> frekvens-intensiteten ofte er numerisk liten:
> 
>     fshift = numpy.fft.fftshift(ft)
>     spectrum = numpy.log(numpy.abs(fshift))
> 
> hva skjuler seg i dette bildet av et ekorn?

### Løsning


## image processing 2 

### Oppgave

> fourier-transformasjonen til et bilde kan brukes til mye nyttig, blant annet
> til edge-detection. et high-pass filter vil slippe gjennom høye frekvenser,
> men stoppe lave frekvenser. de lave frekvensene beskriver de store og grove
> detaljene i bildet, mens de høye frekvensene beskriver små detaljer og harde
> linjer, teksturer og hår f.eks.
> 
> ved å fjerne de lave frekvensene kan vi lettere se de høye frekvensene og
> kanter og detaljer kommer bedre fram.
> 
> jeg har lagt ved et bilde av et blåbær, men det er dessverre nokså skadet og
> ting har glidd litt sammen, så det er umulig å se detaljene i bildet. se om du
> klarer å få frem noen detaljer!
> 
> tips! prøv gjerne litt forskjellige masker med forskjellige verdier.

### Løsning


## prikker

### Oppgave

> En TV skjerm har klikket helt og viser bare prikker i ulike farger. Hvis man
> ser godt etter kan man kanskje se en hemmelig melding, spesielt hvis man
> finner den riktige fargen!

### Løsning


