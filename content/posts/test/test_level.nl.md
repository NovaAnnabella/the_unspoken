---
title: "Testniveaus: De juiste balans vinden"
date: 2023-05-31
author: "Nova Annabella"
slug: test_level
tags: [ Testing, Software Testing, Test Levels, Mock Tests, Unit Tests, Integration Tests, Component Tests, Contract Tests, End-to-End Tests ]
categories: [ Technology, Software Development, Quality Assurance ]
description: "De juiste balans vinden bij het selecteren van de juiste testniveaus voor het testen van software."
draft: false
images:
  - "/images/content/martin_fowler_testing.png"
card: "summary_large_image"
---


# Testniveaus: De juiste balans vinden

[testebenen](/images/content/martin_fowler_testing.png)](https://martinfowler.com/articles/microservice-testing/)

### Introductie

Het onderwerp testen lijkt nog steeds onbekend terrein met veel ruimte voor interpretatie. De traditionele testpiramide
is in twijfel getrokken en er zijn nieuwe testpiramides ontstaan. Naar mijn mening is er geen behoefte aan een
testpiramide, maar een duidelijk begrip van wat er getest moet worden. De toetsen op lagere niveaus zijn vaak minder
zinvol. De focus moet vooral liggen op het testen van gedrag om ervoor te zorgen dat de API of UI werkt zoals gewenst.
Een uitgebreid overzicht van mogelijke testtypen is hier te vinden: [Martinfowler
Testing](https://martinfowler.com/articles/microservice-testing/).

### Niveau 1 - Tests & Tests per eenheid

Doel: De kleinste testbare softwareonderdelen in de applicatie oefenen om te zien of ze werken zoals verwacht. werken.
Mocktests en unit tests kunnen contraproductief zijn en vaak het ontwikkelproces belemmeren. Deze tests zijn vaak los
van de context en hebben weinig relatie met de werkelijkheid. Ze dienen vaak alleen om onnodige functies in stand te
houden via bestaande unit tests. Zodra mocks worden toegevoegd, wordt het een oefening die zichzelf in de weg staat. De
verwachte resultaten van mock tests zijn beperkt tot wat gedefinieerd is in de oorspronkelijke mock. De eindgebruikers
zijn niet geïnteresseerd in interne functies. Bijvoorbeeld, in een login scenario `loginUser(naam, wachtwoord,
beveiligingsalgoritme)`. Als de unit test een null check doet op de `securityAlgorithm` parameter, wordt er teveel
getest omdat gebruikers de `securityAlgorithm` parameter niet kunnen instellen. de parameter `securityAlgorithm`
instellen.

### Level 2 - Integration Test

Doel: De communicatiepaden en interacties tussen componenten controleren om interfacedefecten te detecteren.
Integratietesten geven waardevolle inzichten in de prestaties en onafhankelijkheid van verschillende onderdelen van de
applicatie. toepassing. Met minder mocks worden de tests begrijpelijker. Ze missen echter nog steeds context en het
gevaar bestaat dat Het gevaar bestaat dat integratietests met minder mocks gewoon verkapte unit tests zijn.

### Level 3 - Compontent Test

Doel: de reikwijdte van de te testen software beperken tot een deel van het te testen systeem, het systeem manipuleren
via interne code-interfaces en het gebruik van testdubbels om de te testen code te isoleren van andere componenten.
systeem via interne code-interfaces en het gebruik van testdubbels om de te testen code te isoleren van andere
componenten. componenten. Het testen van componenten levert veel informatie op over de kwaliteit en prestaties van de
applicatie. In plaats van mocks test je uiteindelijk je applicatie. De grens tussen component testen en end-to-end
testen is niet belangrijk. Met een goede testomgeving vervagen de grenzen tussen beide vaak, zodat het testen van echt
gedrag in plaats van geïsoleerde en contextloze functies. Het maken van extra Het maken van extra testklassen zoals
component stubs, fakes en mocks in productiecode kan echter onderhoudsoverhead toevoegen.

### Niveau 4 - Contracttest

Het doel van dit codeblok is om de interacties op de grens van een externe service te controleren en te ervoor te zorgen
dat het voldoet aan de contractuele vereisten van een consumerende service. Contracttesten lijken vaak op unit testen
en het verschil tussen beide is minimaal. Sommige ontwikkelaars associëren deze tests met Pact tests, die in wezen
werken als unit tests met een server ertussen. De moeite van het onderhouden van deze tests kan echter niet de moeite
waard zijn. Een Pact-test zou bijvoorbeeld de REST API `loginUser?name=aa&password=bb)` gebruiken en een JSON schema
respons verwachten die eerder is geüpload naar de Pact server. server. Dit schema is statisch en gevoelig voor fouten
zoals onjuiste datumformaten of tijdzones in het API-respons. De negatieve effecten kunnen enorm zijn.

### Niveau 5 - End-to-end tests (ook wel black box tests genoemd)

Doel: Controleren of een systeem aan de externe eisen voldoet en zijn doelen bereikt door het hele systeem van begin tot
eind te testen. van begin tot eind. End-to-end testen is betrouwbaar en robuust. Zodra de hindernissen voor het
opzetten van de testomgeving zijn overwonnen, loont de inspanning. loont de inspanning. Deze tests simuleren echt gedrag
en maken mocks overbodig. Fouten komen minder vaak voor en zijn eenvoudiger lokaal te reproduceren. Tijdrovend debuggen
en loggen in productie wordt grotendeels voorkomen, net als zelden voorkomende fouten. en zeldzame incidenten worden
grotendeels vermeden. Ontwikkelaars werken minder vaak of helemaal niet met productiegegevens, waardoor de
verantwoordelijkheid afneemt en de focus toeneemt. Bovendien maken automatiseringen zoals automatische software-updates
de implementatie eenvoudiger, omdat het gedrag al is getest. Er zijn nog meer voordelen! Eenmaal Als de tests eenmaal in
herbruikbare vorm zijn geschreven, kunnen ze worden geïntegreerd in belastingtests om een uitgebreid uitgebreid beeld
van de functionaliteit te krijgen. Deze tests kunnen ook continu worden uitgevoerd in de productieomgeving en realtime
inzicht geven in de status van verschillende workflows. Wanneer een subsysteem, zoals REST service bijvoorbeeld offline
gaat, is het mogelijk om direct te identificeren welke gebruikersworkflows beïnvloed worden. worden beïnvloed.

### Fazit

Samengevat is testen een essentieel aspect van softwareontwikkeling en de keuze van de testniveaus hangt af van de
specifieke eisen en doelen van de applicatie. Terwijl schijntesten en unit tests beperkt kunnen zijn in hun
effectiviteit, bieden integratietesten en De effectiviteit van integratietests en unit tests is beperkt, maar
integratietests en unit tests geven een waardevol inzicht in het gedrag en de prestaties van de applicatie. prestaties
van de applicatie. Contracttesten helpen om interacties met externe diensten te verifiëren, maar hun onderscheid met
unit tests kan minimaal zijn. Uiteindelijk bieden end-to-end tests het hoogste niveau van vertrouwen in de
functionaliteit van het systeem en maken ze uitgebreide tests mogelijk. end-to-end testen geeft het hoogste niveau van
vertrouwen in de functionaliteit van het systeem en maakt uitgebreid testen van de hele applicatie mogelijk. Door de
juiste testniveaus te testniveaus te kiezen en ze effectief te combineren, kunnen ontwikkelaars de kwaliteit,
betrouwbaarheid en robuustheid van uw software.

### Contact

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
