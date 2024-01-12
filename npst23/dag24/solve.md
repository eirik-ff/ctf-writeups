# Day 24

Etter mye om og men gikk det til slutt. Cluet var å lese hele hjelp-siden og så
lete etter rett delay. 

Vi vet fra databladet at alle instruksjonene tar _nøyaktig_ 2 klokkesykluser å
gjennomføre. Siden prosessorklokken kjører på 100 MHz, betyr det altså at en
instruksjon tar 20 ns for å kjøre. Litt prøving og feiling ga 27 ns glitch og
basert på hjelpen så kan man bruke samme bredde hele tiden, så da ble det med
det. 

For å finne delayen måtte vi først finne stedet i koden vi ønsker å glitche.
Ved å sammenlikne den gode .elf filen og den onde .bin filen finner vi de
forskjellige funksjonene og tilhørende adresser. Det er tydelig at vi skal 
kjøre `dump_flash HoHoHo123!` der `HoHoHo123!` er det opprinnelige passordet. 
Usikker på om det er viktig å ha med eller ikke, men det burde jo endre antall
instruksjoner til strcmp og gjengen, så greit å ta med kanskje. kommandoen og glitche i sjekken om passordet er rett. Ved å
legge inn at vi skal glitche `20 * N` ns der `N` er antall instruksjoner finner
vi med mye prøving og feiling at etter 9525 (pluss minus 2-3 instruksjoner) instruksjoner glitcher vi på rett 
sted. Denne offsetten ble funnet ved å kjøre en form for binærsøk på antall 
instruksjoner til vi ser at vi glitcher midt i "Wrong override password!" i
FØR output boksen. Da er det bare å backtrace til vi får at den glitcher på den
ønskede instruksjonen. Da får vi flagget. 


## Egg

EGG: `EGG{3rr0r! Unr34ch4bl3 c0d3 d373c73d!}`

I stedet for å glitche i `dump_egg` stedet hvor det ikke går an å glitche to 
sjekker, ser vi i stedet for at `get_egg` ligger bak `flash_write` i assembly.
Når vi nå har flagget som også er override passordet, kan vi kjøre en factory
reset, og glitche return i `flash_write` for å også kjøre `get_egg`. Finner med
samme prøve og feile-metode som før at `20 * 10514` fungerer bra. 

