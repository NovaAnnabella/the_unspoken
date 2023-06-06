---
title: "Illusion Serverless & Cloud
date: 2023-05-24
author: "Nova Annabella"
slug: illusion_serverless_cloud
tags: [ Development, Serverless, Cloud, Microservices, Scalability, Architecture, Infrastructure ]
categories: [ Technology, Software, Cloud ]
description: "Uitdagingen en realiteiten van serverloze mogelijkheden in de cloud. Waardevolle inzichten voor bedrijven die een migratie naar de cloud overwegen".
draft: false
images:
  - "/images/content/onprem_vs_cloud.png"
card: "summary_large_image"
---



# De illusie van serverloze functies in de cloud

aws_costs_twitter_1](/images/content/onprem_vs_cloud.png)

### Introductie

Ik ben teleurgesteld hoe vaak marketing het wint van gezond verstand. Veel managers plaatsen zichzelf boven hun eigen
experts - de ontwikkelaars. Dit geldt ook voor migratie naar de cloud. Spoiler: Als u geld moet besparen geld moet
besparen, moet u de cloud vermijden. Want het nieuwe modewoord "serverloos" in de cloud betekent: U zorgt voor de
software, wij zorgen voor de hardware. U zorgt voor de software, wij zorgen voor de hardware. Als je echter een bekwame,
gemotiveerde en leergierige beheerder hebt, kun je ook zelf serverloos werken (bijv. [KNative](https://knative.dev)).
aws_costs_twitter_1](/images/content/aws_costs_twitter_1.png)

### Serverloze functies vs microservices:



#### Microservices

Een typische stateless microservice zorgt voor een specifieke functie/domein en wordt ingezet in een container
orkestratie omgeving. Deze omgeving zorgt voor infrastructuur, beveiliging, firewall, logging, metrieken, geheimen,
netwerken, back-ups en meer. Een groot voordeel is dat een microservice lokaal kan worden ingezet met weinig resources
en cloud/server agnostisch is (kan overal worden ingezet).

#### Serverloze functies

Een grapje vooraf: Paradoxaal, maar waar - serverloze functies zijn sterk afhankelijk van de serveromgeving. :) Een
typische serverless functie zorgt ook voor slechts één specifieke functie/domein en is geschreven in pure code zonder
frameworks om sneller te zijn dan een microservice. code om sneller te zijn dan een microservice (ook een goede oefening
voor MicroServices). Een groot voordeel is dat Serverless functies automatisch schalen. Elke serverless functie vereist
echter een aanzienlijke hoeveelheid GlueCode nodig om de infrastructuur te definiëren - beveiliging, firewall, netwerk,
logging, metriek, geheimen, caching, back-ups en nog veel meer. Daarom kan een eenvoudige functie zoals het kopiëren van
een bestand inclusief API al snel 1500 regels code (incl. IaC). betrokken kunnen zijn. De beheerkosten verschuiven van
beheer naar ontwikkeling in een verhouding van 1:N (1 tot Serverless functies). De kennis en implementatie zijn dus niet
meer gebundeld en kunnen snel instabiel worden. Daarnaast zijn er hogere onderhoudskosten. Echt integratief testen is
ook zeldzaam bij serverless, of alleen mogelijk met grote inspanning. Uiteindelijk is de complexiteit van serverless
functies aanzienlijk hoger dan die van een enkele microservice. Hogere complexiteit betekent ook lagere
onderhoudbaarheid. Nieuwe teamleden hebben het moeilijker en hebben aanzienlijk meer voorkennis nodig.

### Serverless en de cloud in het algemeen

De meeste cloudtechnologieën zijn niet up-to-date. Bijvoorbeeld Node.js, Java, Python en andere talen of technologieën
zijn talen of technologieën zijn vaak niet eenvoudig te updaten, meestal helpt alleen wachten. Zelfs moderne en
standaard technologieën zoals MongoDB, MySQL, Kafka, NATS, RabbitMQ, Redis, Prometheus, InfluxDB, Grafana, Kibana,
Elastic Search enz. zijn niet beschikbaar of te duur. Zonder dergelijke standaarddiensten bevindt men zich vaak in het
virtuele stenen tijdperk en gebruikt men verouderde oplossingen, bijv. webhooks voor externe communicatie. Bovendien is
de manoeuvreerruimte op het gebied van regelgeving, compliance, gegevensbescherming en fail-safety ernstig beperkt. De
cloud moet daarom agnostisch worden uitgevoerd om snel te kunnen schakelen tussen AWS, Azure, Google, on-premise, enz.
en de kosten te vergelijken. Beperkingen komen ook vaak voor in de cloud, wat leidt tot creatieve workarounds, die op
hun beurt de complexiteit vergroten. toename. Integratietesten kunnen ook duur worden, omdat elke ontwikkelaar zijn
eigen ontwikkelomgeving in de cloud nodig heeft. omdat veel clouddiensten lokaal niet of nauwelijks te testen zijn. Maar
zelfs zonder testen is de cloud duur. Terwijl het bij on-premise systemen vooral gaat om hardwarekosten, moet je in de
cloud ook betalen voor verkeer, sommige standaarddiensten en vaak zelfs voor meerdere en vaak zelfs voor meerdere
belastingen. Bovendien is het in de cloud gemakkelijk om het overzicht te verliezen, want het gaat niet om het gaat niet
om gebruiksvriendelijkheid, maar om geld. De kosten zijn zo verborgen dat je ze pas merkt als het te laat is. te laat
is. De basisprincipes van architectuur en infrastructuur moeten opnieuw worden uitgevonden in de cloud en vooral in
serverless cloud. moeten opnieuw worden uitgevonden, omdat de implementatie sterk afhangt van de beschikbare functies.
Telkens als ik een architectuur heb ontworpen, denk ik: "Dit had een enkele service kunnen zijn". had kunnen zijn".
Voor mij is serverless een interessant idee en het schaalt goed, maar het verlaagt de kosten niet. Integendeel.
Integendeel, het vereist veel meer kennis en tijd in ontwikkeling. Serverless of de cloud vereisen discipline en
voorkennis. Als de kennis er niet is voor on-premise systemen, zal het niet makkelijker zijn met de cloud. Hoe moeten
ontwikkelaars extra infrastructuurkennis opdoen? Ik zou de voorkeur geven aan een goed beheerd Kubernetes-cluster boven
cloudarchitectuur. De mensen schalen niet. Veel ontwikkelaars hebben geen discipline in het schrijven van code. Helaas
geldt dit voor 80 procent van de ontwikkelaars. Dus hoe gaan deze ontwikkelaars in staat zijn om de cloud te draaien? de
cloud? Het is belangrijk dat organisaties de uitdagingen en implicaties van serverloze architectuur en de cloud
volledig begrijpen. De uitdagingen en implicaties van serverloze architectuur en de cloud volledig begrijpen. Dit
vereist niet alleen technische kennis, maar ook een strategische aanpak. A ondoordachte migratie naar de cloud kan
leiden tot complexiteit, hogere kosten en overbelasting van ontwikkelaars. Samengevat is serverless in de cloud een
veelbelovend concept, maar wel een dat zorgvuldig overwogen moet worden. zorgvuldig overwogen moet worden. Er moet
rekening worden gehouden met kosten, complexiteit, onderhoudbaarheid en de vaardigheden van het ontwikkelteam. rekening
worden gehouden. Elk bedrijf heeft andere eisen en prioriteiten. Er moet een weloverwogen beslissing worden genomen of
Serverless in de cloud de juiste oplossing is of dat alternatieve benaderingen zoals zoals Kubernetes Cluster de betere
keuze zijn. Een succesvolle implementatie van serverless en cloud computing vereist een combinatie van technische
expertise strategische planning en een duidelijk begrip van de bedrijfsvereisten. Alleen dan kan de illusie van
serverless en de juiste beslissing nemen voor uw eigen softwareontwikkeling.

### Fazit

De introductie van serverloze functies in de cloud belooft flexibiliteit, schaalbaarheid en verlichting van
infrastructuurtaken. ontwikkelaars van infrastructuurtaken. We moeten ons echter niet laten verblinden door deze
illusie. De overstap naar de cloud en het gebruik van serverloze functies brengt een aantal uitdagingen met zich mee.
Ontwikkelaars moeten naast de feitelijke ontwikkeling een nieuwe "taal" leren en meer verantwoordelijkheid op zich nemen
zonder de juiste ondersteuning. meer verantwoordelijkheid op zich nemen. De complexiteit van serverless functies is vaak
hoger dan die van microservices, omdat ontwikkelaars veel extra taken op zich moeten nemen, zoals ontwikkelaars veel
extra taken op zich moeten nemen, zoals infrastructuurdefinitie, beveiliging en schaling. Echt integratief testen is
moeilijk en voorkennis en ervaring voor operations zijn nog belangrijker in de cloud. De cloud zelf brengt nog meer
uitdagingen met zich mee. Veel cloudtechnologieën zijn niet up-to-date en het gebruik van moderne off-the-shelf diensten
kan duur of zelfs onmogelijk zijn. Regelgeving, compliance en gegevensbescherming beperken de mogelijkheden. Bovendien
lopen de kosten in de cloud gemakkelijk uit de hand, en is het overzicht over de uitgaven snel verloren. Al met al
moeten de voor- en nadelen van serverless en cloud zorgvuldig worden afgewogen. Bedrijven moeten rekening houden met hun
specifieke vereisten, de bestaande expertise in het team en de langetermijneffecten van een migratie naar de cloud. van
een migratie naar de cloud. Een weloverwogen beslissing op basis van een uitgebreide analyse is cruciaal voor het succes
en de winstgevendheid van het project. van het project. Uiteindelijk is het aan bedrijven om hun ontwikkelaars adequaat
te ondersteunen, de kosten en complexiteit van de cloud realistisch in te schatten en alternatieve oplossingen zoals
goed beheerde Kubernetes-clusters te overwegen. Met een duidelijke strategie en een goed begrip van hun eigen behoeften
kunnen bedrijven de voordelen van de cloud en serverloze mogelijkheden en de illusie doorzien.

### Contact

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
