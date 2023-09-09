---
title: "Testniveaus: Het juiste evenwicht vinden"
date: 2023-05-31
author: "Nova Annabella"
slug: test_level
tags: [ Testing, Software Testing, Test Levels, Mock Tests, Unit Tests, Integration Tests, Component Tests, Contract Tests, End-to-End Tests ]
categories: [ Technology, Software Development, Quality Assurance ]
description: "Het juiste evenwicht vinden bij het kiezen van de geschikte testniveaus voor softwaretests"
draft: false
images:
  - "/images/content/martin_fowler_testing.png"
card: "summary_large_image"
---


# Testniveaus: Het juiste evenwicht vinden

[![testebenen](/images/content/martin_fowler_testing.png)](https://martinfowler.com/articles/microservice-testing/)

### Inleiding

Het onderwerp testen lijkt tot op de dag van vandaag nog onbekend terrein met veel ruimte voor interpretatie. De traditionele
testpiramide werd in twijfel getrokken en nieuwe testpiramides zijn ontstaan. Naar mijn mening is er geen
testpiramide nodig, maar een duidelijk begrip van wat getest moet worden. De tests op lagere niveaus zijn vaak
minder betekenisvol. De focus moet vooral liggen op het testen van gedrag, om te verzekeren dat de
API
of UI functioneert zoals gewenst. Een uitgebreid overzicht van mogelijke testmethoden is hier te vinden:
[Martinfowler Testing](https://martinfowler.com/articles/microservice-testing/).


### Niveau 1 - Proeftoetsen & Unit Tests

Doel: Het uitoefenen van de kleinste testbare softwareonderdelen in de toepassing om te bepalen of ze functioneren zoals verwacht.

Mock-tests en unit-tests kunnen contraproductief zijn en het ontwikkelingsproces vaak belemmeren. Deze tests zijn vaak
losgekoppeld van de context en hebben weinig betrekking tot de realiteit. Ze dienen vaak alleen om overbodige functionaliteiten over bestaande
unit-tests te behouden. Zodra mocks worden toegevoegd, wordt het een zelfbezinning. De verwachte
resultaten van mock-tests zijn beperkt tot wat in de oorspronkelijke mock werd gedefinieerd. De eindgebruikers
zijn niet geïnteresseerd in interne functies. Bijvoorbeeld, in een
login-scenario `loginUser(name, password, securityAlgorithmus)`. Als de unit-test een nullcontrole op
de `securityAlgorithm`-parameter uitvoert, wordt er te veel getest, omdat gebruikers de `securityAlgorithm`-parameter niet
kunnen instellen.

### Niveau 2 - Integratietest

Doel: Controleer de communicatiepaden en interacties tussen componenten om interfacefouten te detecteren.
Integratietests leveren waardevolle inzichten op over de prestaties en onafhankelijkheid van verschillende onderdelen
van de applicatie. Met minder mocks worden de tests begrijpelijker. Er ontbreekt echter nog steeds context en er is een
risico dat integratietests gewoon vermomde unit tests zijn met minder mocks.

### Niveau 3 - Component Test

Doel: Beperking van de omvang van de geteste software tot een deel van het te testen systeem, manipulatie van het systeem
via interne code-interfaces en gebruik van test-dubbels om de te testen code te isoleren van andere
componenten.

Componenttests leveren een schat aan informatie op over de kwaliteit en prestaties van de toepassing. In plaats van
Mocks, test je uiteindelijk je toepassing. De grens tussen componenttests en end-to-end tests is niet
significant. Met een goede testomgeving vervagen de grenzen tussen hen vaak, zodat het testen van het echte
gedrag in plaats van geïsoleerde en contextloze functies mogelijk wordt. Echter, het creëren van extra
testklassen zoals component-stubs, neppe en mocks in de productiecode kan extra onderhoud met zich meebrengen.

### Niveau 4 - Contract Test

Het doel van deze codeblok is om de interacties aan de grens van een externe dienst te controleren en
ervoor te zorgen dat deze voldoet aan de contractvereisten van een consumerende dienst.

Contracttests lijken vaak op componententests, en het verschil tussen hen is minimaal. Sommige ontwikkelaars
associëren deze tests met Pact-tests, die in essentie fungeren als unittests met een server ertussen. De
inspanning om deze tests te onderhouden, is echter mogelijk niet de moeite waard. Bijvoorbeeld, een Pact-test zou de
REST-API `loginUser?name=aa&password=bb)` kunnen testen en een JSON-schema-antwoord verwachten dat eerder was geüpload naar de Pact-server.
Dit schema is statisch en vatbaar voor fouten, zoals verkeerde datumformaten of tijdzones in de
API-antwoord. De negatieve effecten kunnen enorm zijn.

### Niveau 5 - End-to-End Tests (ook wel Black-Box-Tests genoemd)

Doel: Controle of een systeem externe eisen naleeft en zijn doelen bereikt door het hele systeem te testen
van begin tot eind.

End-to-End-tests zijn betrouwbaar en robuust. Zodra de obstakels van het opzetten van de testomgeving zijn overwonnen, betaalt de
inspanning zich uit. Deze tests simuleren echt gedrag en elimineren de noodzaak van mocks. Fouten komen minder vaak voor
op en zijn lokaal gemakkelijker te reproduceren. Gecompliceerde debugging en het bijhouden van logboeken in productie 
worden grotendeels vermeden, evenals zeldzame incidenten. Ontwikkelaars werken minder vaak, zo niet, met 
productiegegevens, wat de verantwoordelijkheid vermindert en de focus verhoogt. Bovendien vergemakkelijken automatiseringen zoals
automatische software-updates de uitvoering, omdat het gedrag al is getest. Er zijn nog meer voordelen! Zodra
de tests zijn geschreven in een herbruikbare vorm, kunnen ze worden geïntegreerd in belastingtests om een ​​
compleet beeld van de functionaliteit te krijgen. Deze tests kunnen ook continu worden uitgevoerd in de productieomgeving
en bieden realtime inzicht in de status van verschillende workflows. Als een subsysteem, zoals 
bijvoorbeeld een externe REST-service, offline gaat, kan onmiddellijk worden geïdentificeerd welke gebruikersworkflows
zijn getroffen.

### Conclusie

Samenvattend is testen een essentieel aspect van softwareontwikkeling, en de keuze van de testniveaus hangt af van
de specifieke eisen en doelen van de applicatie. Hoewel mock-tests en unit-tests in hun effectiviteit
beperkt kunnen zijn, bieden integratietests en componenttests waardevolle inzichten in het gedrag en de
prestaties van de applicatie. Contracttests helpen bij het verifiëren van interacties met externe diensten, maar hun
afbakening ten opzichte van componenttests kan minimaal zijn. Uiteindelijk bieden end-to-end tests het hoogste niveau van vertrouwen in
de functionaliteit van het systeem en maken ze uitgebreide tests van de gehele applicatie mogelijk. Door de juiste
testniveaus te kiezen en ze effectief te combineren, kunnen ontwikkelaars de kwaliteit, betrouwbaarheid en robuustheid van je
software garanderen.

### Contact

[GitHub-problemen](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
