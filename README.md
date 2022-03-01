# Zadanie 1 – SIP Proxy (telefónna ústredňa)

Na vašom počítači (alebo virtuálnom počítači) sprevádzkujte SIP Proxy, ktorá umožní prepájanie a realizáciu hovorov medzi štandardnými SIP klientami.

## Implementácia

### Použitá knižnica

Na implementáciu som použila programátorský jazyk Python, preto som zvolila z Githubu https://github.com/tirfil/PySipFullProxy. 

Z ponúknutých som si vybrala súbor *sipfullproxy.py*, ktorý som upravila.

Úpravy v spomenutom súbore:
* zmenené importované neaktuálny modul za aktuálny
* úpravy na možnosť prevádzky servera lokálne
* komentáre, ktoré som doplnila po prejdení si cudzieho kódu na lepšie pochopenie
* zmenené SIP stavové kódy
* doplnené metódy potrebné pre doplňujúce časti zadania
* zakomentovanie spustenia súboru

## Moje riešenie

Vytvorila som *main.py*, ktorý importuje spomenutý súbor a spúšťa server. Pre user-friendly zážitok som vytvorila spustenie serveru cez terminál, kde je zabezpečené aj bezpečné vypnutie serveru. Okrem toho, je tam nakonfigurované logovanie.

Súbor *sipfullproxy.py* nebolo potrebné veľmi upravovať, lebo trieda obsahovala metódu *handle()*, ktorá správne zabezpečovala chod serveru. Podľa požiadavky (request) volaním metódy *processRequest()*, ktorá prišla na server je zabezpečená adekvátna odpoveď pomocou vybranej metódy:

* *processRegister()* – registrácia
* *processInvite()* – pozvanie do session  (hovor)
* *processnonInvite()* – požiadavka na ukončenie session (hovor) 
* *processAck()* – potvrdenie od klienta
* *processCode()* – požiadavka na informovanie o stave cez SIP stavové kódy

Kvôli zabezpečeniu funkcionality logovania som musela zdrojový kód v súbore *sipfullproxy.py* upraviť. Všetkým pôvodným logovaniam som zmenila typ na *DEBUG* a svojim logovacím správam som nastavila typ *INFO*.

## Funkcionality

### Registrácia účastníka (bez nutnosti autentifikácie)

Ukážka je v súbore *register.pcapng*. V ukážke je zarhnuté aj to, keď ešte z neregistrovaného účtu vykonala operácia. Pri registrácií som zmenila stavový kód, ktorý sa posiela.

### Vytočenie hovoru a zvonenie na druhej strane
Ukážka je v súboroch *ok_call.pcapng*, *declined_call.pcapng* a *canceled_call.pcapng*. Pri ošetrení vytočenia hovoru som zmenila stavové kódy na bližšie pomenovanie chyby.

### Prijatie hovoru druhou stranou, fungujúci hlasový hovor

Ukážka je v súbore *ok_call.pcapng*. Zavolal mobil a ukončil hovor tablet.

### Ukončenie hlasového hovoru (prijatého aj neprijatého)
Ukážka odmietnutého hovoru [tablet -> mobil] je v súbore *declined_call.pcapng*. Ukážka zrušeného hovoru bez prijatia [mobil -> tablet] je v súbore *canceled_call.pcapng*. Ukážka zrušeného hovoru s prijatím [mobil -> tablet] je v súbore *ok_call.pcapng*. Pri ošetrení ukončenia hovoru som zmenila stavové kódy na bližšie pomenovanie chyby.

### Možnosť zrealizovať konferenčný hovor (aspoň 3 účastníci)
Ukážka je v súbore *conference_call.pcapng*. 

### Možnosť presmerovať hovor
Ukážka je v súbore *redirected_call.pcapng*. 

### Možnosť realizovať videohovor
Ukážka je v súbore *video_call.pcapng*. 

### Logovanie “denníka hovorov” 
Bolo potrebné vytvoriť logovacie správy pre tieto aktivity: kto kedy komu volal, kedy bol ktorý hovor prijatý, kedy bol ktorý hovor ukončený.
Súbor *proxy.log* ako ukážka je priložený.

### Úprava SIP stavových kódov z zdrojovom kóde proxy
Vyššie som opísala, ktoré stavové kódy som upravila, ako vidno na obrázku v súbore *register.pcapng*.
 
## Repozitár na zdrojový kód s prislúchajúcimi súbormi

https://github.com/AnettLangova/mtaa_zadanie1

