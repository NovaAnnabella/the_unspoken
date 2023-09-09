---
title: "Illusie Serverloos & Cloud"
date: 2023-05-24
author: "Nova Annabella"
slug: illusion_serverless_cloud
tags: [ Development, Serverless, Cloud, Microservices, Scalability, Architecture, Infrastructure ]
categories: [ Technology, Software, Cloud ]
description: "Uitdagingen en realiteiten van serverloze functies in de cloud. Waardevolle inzichten voor bedrijven die overwegen om naar de cloud te migreren."
draft: false
images:
  - "/images/content/onprem_vs_cloud.png"
card: "summary_large_image"
---


# De Illusie van Serverloze Functies in de Cloud

![aws_costs_twitter_1](/images/content/onprem_vs_cloud.png)

### Inleiding

Ik ben teleurgesteld over hoe vaak marketing het wint van gezond verstand. Veel managers negeren hun eigen experts - de ontwikkelaars. Dit geldt ook voor de migratie naar de cloud. Spoiler: Wie geld moet besparen, zou de cloud moeten vermijden. Want de nieuwe buzzword "Serverless" in de cloud betekent: Jij zorgt voor de software, wij zorgen voor de hardware. Maar wie een capabele, gemotiveerde en nieuwsgierige beheerder heeft, kan ook zelf serverloos werken (bijvoorbeeld [KNative](https://knative.dev)).

![aws_costs_twitter_1](/images/content/aws_costs_twitter_1.png)

### Serverless Functies vs Microservices:



#### Microservices

Een typische stateless microservice zorgt voor een specifieke functie/domein en wordt ingezet in een 
container orchestratieomgeving. Deze omgeving zorgt voor infrastructuur, beveiliging, firewall, 
logboekregistratie, metrieken, geheimen, netwerk, back-ups en nog veel meer. Een groot voordeel is dat een microservice lokaal met 
weinig 
middelen geïntegreerd getest kan worden en Cloud-/Server-agnostisch (overal inzetbaar) is.

#### Serverless Functies

Een klein grapje vooraf: Paradoxaal, maar waar - Serverloze functies zijn sterk afhankelijk van de serveromgeving. :)
Een typische Serverless functie zorgt ook alleen voor een specifieke functie/domein en wordt zonder frameworks
in
pure code geschreven om sneller te zijn dan een microservice (ook een goede oefening voor microdiensten). Een groot
voordeel is dat Serverless functies automatisch worden geschaald. Elk serverloos functie heeft echter een
aanzienlijke hoeveelheid GlueCode nodig om de infrastructuur te definiëren - beveiliging, firewall, netwerk, logboekregistratie, statistieken,
geheimen, caching, back-ups en nog veel meer.
Daarom kan een eenvoudige functie zoals het kopiëren van een bestand met inbegrip van API snel 1500 regels code (incl. IaC)
omvatten.
De beheerskosten verschuiven van beheer naar ontwikkeling in een verhouding van 1:N (1 naar Serverloze
Functies). De kennis en implementatie zijn dus niet langer
gebundeld en kunnen snel instabiel worden. Dit leidt tot verhoogde onderhoudskosten.
Ook echte integratieve tests zijn met Serverless zeldzaam of alleen met grote moeite verbonden.
Uiteindelijk is de complexiteit van serverloze functies aanzienlijk hoger dan die van een enkele microservice.
Hogere complexiteit betekent ook een lagere onderhoudbaarheid. Nieuwe teamleden hebben het moeilijker en hebben aanzienlijk
meer voorkennis nodig.

### Serverless en de Cloud in het algemeen

De meeste cloud-technologieën zijn niet up-to-date. Bijvoorbeeld, Node.js, Java, Python en andere
talen of technologieën zijn vaak niet makkelijk bij te werken, meestal is het enige dat helpt, wachten.
Zelfs moderne en standaard technologieën, zoals MongoDB, MySQL, Kafka, NATS, RabbitMQ, Redis, Prometheus, InfluxDB, Grafana,
Kibana, Elastic Search etc. zijn vaak niet beschikbaar of overprijsd.
Zonder zulke standaarddiensten bevindt men zich vaak in het virtuele stenen tijdperk en maakt gebruik van verouderde oplossingen, zoals
Webhooks voor externe communicatie.
Daar komt bij dat de manoeuvreerruimte bij zaken als regulatie,
compliance, privacy en uitvalbeveiliging sterk beperkt is.

De cloud moet daarom agnostisch worden bedreven, om snel te kunnen wisselen tussen AWS, Azure, Google, On-Premise, etc. en
kosten te kunnen vergelijken.
Grenzen zijn aanwezig in de cloud, wat vaak leidt tot creatieve omwegen die de complexiteit
verhogen. Ook integraal testen kan duur worden, want elke ontwikkelaar heeft een eigen ontwikkelomgeving in de cloud
nodig, omdat veel clouddiensten nauwelijks of niet lokaal testbaar zijn.
Zelfs zonder tests is de cloud duur. Terwijl op On-Premise systemen voornamelijk
hardwarekosten nodig zijn, moet in de cloud extra betaald worden voor het verkeer, sommige standaarddiensten en vaak zelfs voor de
meervoudige belasting. Daarbij is het makkelijk om het overzicht in de cloud te verliezen, het gaat niet over
gebruiksgemak, maar om geld. De kosten zijn zo verborgen dat je ze pas opmerkt als het te laat
is.

De basisprincipes van de architectuur en infrastructuur moeten in de cloud en vooral op het gebied van serverloze
nieuwe concepten worden gerealiseerd omdat de implementatie sterk afhankelijk is van de beschikbare functies.
Telkens als ik de architectuur heb ontworpen, komt de gedachte bij me op: "Dit had ook een enkele service kunnen zijn."

Voor mij is serverloos een interessant idee en het is goed schaalbaar, maar het verlaagt niet de kosten. Integendeel,
het vereist veel meer kennis en tijd in ontwikkeling. Serverloosheid en de cloud vereisen discipline en
voorkennis.
Als de kennis voor On-Premise-systemen ontbreekt, wordt het met de cloud niet eenvoudiger.
Hoe moeten ontwikkelaars daarnaast infrastructuurkennis opdoen?

Ik zou een goed beheerde Kubernetes-cluster verkiezen boven de Cloud-architectuur.
Medewerkers schalen niet. Veel ontwikkelaars hebben geen discipline in het schrijven van code.
Helaas geldt dit voor 80 procent van de ontwikkelaars. Hoe zullen deze ontwikkelaars dan nog de cloud kunnen beheren?

Het is belangrijk dat bedrijven de uitdagingen en implicaties van serverloze architectuur en de cloud grondig begrijpen.
Dit vereist niet alleen technische kennis, maar ook een strategische aanpak. Een ondoordachte migratie naar de cloud kan leiden tot complexiteit, hogere kosten en overweldiging van de ontwikkelaars.

Samenvatting, serverloos in de cloud is een veelbelovend concept dat echter zorgvuldig overwogen moet worden.
Kosten, complexiteit, onderhoudbaarheid en de vaardigheden van het ontwikkelteam moeten in aanmerking worden genomen.
Elk bedrijf heeft andere eisen en prioriteiten. Men moet een weloverwogen beslissing nemen of
Serverloos in de Cloud is de juiste oplossing, of dat alternatieve benaderingen, zoals
bijv. een goed Kubernetes-cluster een betere keuze zijn.

Het succesvolle gebruik van serverloos en cloud computing vereist een combinatie van technische expertise,
strategische planning en een duidelijk begrip van de bedrijfsbehoeften. Op deze manier kan men de illusie van serverloosheid zien en de juiste beslissing nemen voor de eigen softwareontwikkeling.

### Conclusie

De introductie van serverloze functies in de cloud belooft flexibiliteit, schaalbaarheid en ontlasting van
ontwikkelaars van infrastructuurtaken. Men moet zich echter niet laten verblinden door deze illusie. De
overstap naar de cloud en het gebruik van serverloze functies brengt een aantal uitdagingen met zich mee.

Ontwikkelaars moeten naast de eigenlijke ontwikkeling een nieuwe "taal" leren en zonder de juiste ondersteuning
meer verantwoordelijkheid nemen.
De complexiteit van serverloze functies is vaak hoger dan die van microservices, omdat ontwikkelaars veel extra
taken zoals infrastructuurdefinitie, beveiliging en schalen moeten overnemen. Echte integratieve tests zijn
moeilijk en voorkennis en ervaring voor de bediening zijn in de cloud nog belangrijker.

De cloud zelf brengt ook verdere uitdagingen met zich mee. Veel cloudtechnologieën zijn niet up-to-date
en het gebruik van moderne standaardservices kan duur of zelfs onmogelijk zijn. Regelgevende eisen, naleving en
gegevensbescherming beperken de bewegingsvrijheid. Daarnaast lopen de kosten in de cloud gemakkelijk uit de hand,
en het overzicht van de uitgaven raakt snel verloren.

Over het geheel genomen dient men zorgvuldig de voor- en nadelen van serverloos en cloud af te wegen.
Bedrijven zouden hun specifieke eisen, de bestaande kennis in het team en de lange-termijn effecten
van de migratie naar de cloud in overweging moeten nemen.
Een weloverwogen beslissing op basis van een uitgebreide analyse is cruciaal voor het succes en de rentabiliteit
van het project.

Uiteindelijk is het aan de bedrijven om hun ontwikkelaars adequaat te ondersteunen, de kosten en complexiteit van de
cloud realistisch in te schatten en alternatieve oplossingen zoals goed beheerde Kubernetes-clusters te overwegen.
Met een duidelijke strategie en een gedegen begrip van de eigen behoeften, kunnen bedrijven de voordelen van de
cloud en serverloze functies optimaal benutten en de illusie doorzien.

### Contact

[GitHub-problemen](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
