---
title: "Terug naar Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "De ongrijpbare zoektocht naar eenvoud en een korte reis naar de herontdekking van de kracht van Maven."
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# Terug naar Maven?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

## 10 Jaar Gradle. Op zoek naar verlichting en een korte reis naar de herontdekking van de kracht van Maven.



### Maximalisatie van het potentieel van ontwikkelaars - We hebben meer tijdbesparende tools nodig

Onderwerpen die vaak over het hoofd worden gezien of zelden worden besproken, interesseren mij. Vaak worden er coole
technologieën gebruikt, maar bijna niemand praat over de bijbehorende problemen. Ontwikkeling is tegenwoordig erg
complex geworden. Met de coole buzzwoorden zoals "Serverless", "Low Code", "IaC", "Big Data", "Cloud", "DevOps", "You
Build it You run it" enz. hebben ontwikkelaars al meer dan genoeg extra taken te volbrengen. Meer taken betekent dat er
nauwelijks nog experts zijn en dat er altijd iets wordt verwaarloosd voor de focus. Daarom zijn automatiseringen en
tijdbesparing mega belangrijk. "Don't make me think" en "Works out of the Box" zijn al goede kwaliteitskenmerken, die ik
in Gradle nog niet kan zien. Om eerlijk te zijn, Gradle is niet het enige moderne hulpmiddel dat ons werk geeft in
plaats van het te vergemakkelijken.

### De illusoire zoektocht naar eenvoud en automatisering

Sinds SOAP heb ik een diepgewortelde afkeer van XML-gebaseerde configuraties. Met Gradle had ik gehoopt,
dat het schrijven van Bind-scripts een fluitje van een cent zou zijn. Helaas werden mijn verwachtingen en mijn motivatie van
keer tot keer minder. Gradle streeft naar flexibiliteit en offert daarvoor automatisering en kwaliteit op. Ontwikkelaars
volgen blindelings de trend zonder rekening te houden met de impact op de betrouwbaarheid van de software. Om Gradle
Bouwscripts eenvoudig en onderhoudsarm te houden, is een sterke discipline vereist. Zo'n discipline is zeldzaam in
de broncode te vinden en is daarom in de bouwscripts nog veel zeldzamer.

### Vertalingen en Workarounds - Wanneer Build-Scripts een uitdaging worden

Gradle werkt op de achtergrond niet veel anders dan Maven. Daarom zijn enkele vertalingen nodig. Functies zoals de
Dependency Catalog, de Maven Release Plugin, de Dependabot en vele anderen zijn in feite oplossingen voor basisfuncties
die Maven al biedt. Met de flexibiliteit van Gradle ontstaan er vaak complexe buildconfiguraties die moeilijk te 
onderhouden zijn.
Gradle plugins hebben vaak compatibiliteitsproblemen, limieten of beperkte verdere ontwikkelingen. Deze problemen ontstaan
door de evoluerende aard van het Gradle-ecosysteem, de diversiteit van omgevingen waarin Gradle wordt gebruikt en de specifieke
implementatie- en onderhoudsinspanningen voor elke plugin. Alles is met elkaar verbonden.

### Het Domino-effect van Gradle - Een nachtmerriescenario in de echte wereld

Ik heb veel microservices gezien die slechts enkele jaren oud waren en al ononderhoudbaar waren vanwege Gradle. Belangrijk om te vermelden dat dit niet de eerste keer is dat ik zoiets heb gezien, en nee, het waren geen junior devs.

Mijn **taak was om een Spring Boot 2.x naar 2.7 upgrade uit te voeren**. Spoiler: ik gaf op na een jaar! De problemen in het kort:

* Het Gradle-Build-bestand vereist -> een downgrade van mijn lokale Java-versie naar 11 (WTF) (Normaal gesproken is Java
  achterwaarts compatibel - er zijn hier ook weer tools beschikbaar als workaround, zoals SdkMan...)
* De Spring Boot-update vereist -> Gradle-update (WTF)
* De Gradle-update vereist -> Plugin-update
* De Plugin-update vereist -> Groovy-update (WTF)
* De Groovy-update vereist -> Testraamwerk- en testupdates (WTF)
* De update van het testraamwerk vereist -> afhankelijkheidsupdates
* \[...]
  Bovendien werken enkele plugins niet met nieuwere Gradle-versies, worden sommige niet langer ontwikkeld, zijn ze incompatibel met andere plugins, werken ze alleen met Gradle KTS, niet met Gradle Groovy, of hebben ze gewoon limieten. Zelfs plugins van grote aanbieders zoals Spring hebben beperkte functionaliteit in vergelijking met hun Maven-plugins. Uiteindelijk heb ik een coole, korte Gradle-build-bestand, dat niemand echt kan onderhouden, zelfs niet de ontwikkelaars die het hebben geschreven, en zij houden nog steeds van Gradle. Ik ken maar weinigen die echt Gradle-scripts kunnen begrijpen of schrijven.

### De herontdekking van de kracht van Maven - De magische krachten van Maven gebruiken

Hier zijn mijn favoriete functies van Maven:
Plugins kunnen direct vanaf de opdrachtregel worden gestart en geconfigureerd zonder dat ze vooraf gedefinieerd hoeven te worden. Bovendien zijn ze grotendeels onafhankelijk van andere plugin-configuraties.

| Voorbeeldcommando                     | Beschrijving                                                                                                                                              | Link                                                                      | 
|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`   | Versies updaten - wie heeft Dependabot nodig? Ja, mijn projecten worden al jaren probleemloos bijgewerkt naar de nieuwste versie, zonder vervelende mergeverzoeken | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0` | Projectversie instellen...                                                                                                                                | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`         | Afhankelijkheden vermelden en hun licenties weergeven (kan zelfs mislukken bij uitgesloten licenties)                                                     | https://www.mojohaus.org/license-maven-plugin/index.html                 | 

Deze lijst kan eindeloos doorgaan. Het doet me op een of andere manier denken aan GitHub Workflow Steps.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)


### Houd je niet van XML?

Geen probleem! Schrijf gewoon je buildbestand in `ruby`, `groovy`, `scala`, `yaml`, `atom` of `Java`. De Polyglot
extensie (https://github.com/takari/polyglot-maven) maakt het mogelijk. Om het te proberen
voer je gewoon `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` uit en binnen
enkele milliseconden is je buildbestand vertaald. Jammer dat er geen betrouwbare Maven <> Gradle vertaler
beschikbaar is :(
Ja, Maven-buildbestanden zijn groot, maar ook heel gemakkelijk te begrijpen. Aanpassingen of debugging zijn in een handomdraai
gedaan.

### Leeftijd is slechts een getal - Mavens Stabiliteit en Evolutie

Toegegeven, Maven bestaat al een hele tijd en zijn esthetiek voldoet misschien niet aan de huidige normen.
De levensduur van Maven heeft het echter mogelijk gemaakt om zich aan te passen en verder te ontwikkelen. Maven werkt onafhankelijk
van je project. Build-bestanden kunnen eenvoudig hergebruikt worden.
De plug-ins draaien in een sandbox en zijn onafhankelijk van elkaar en onafhankelijk van de Java- of Maven-versie.
Dit ontwerp bevordert de stabiliteit en voorspelbaarheid en maakt het eenvoudig om complexe build-processen zonder onverwachte
conflicten te beheren.

### Conclusie

Tegenwoordig is de ontwikkelomgeving overbelast met veel taken en technologieën voor ontwikkelaars. Op zoek naar
eenvoud en automatisering is Gradle naar voren gekomen als modern bouwgereedschap, maar heeft zijn eigen
uitdagingen met zich meegebracht. Zonder twijfel, het concept van Gradle is goed! Maar gezien de complexiteit en de
tijd die wordt geïnvesteerd in Gradle Build-scripts, rijst de vraag of het niet eenvoudiger zou zijn om Maven te
uitbreiden. Met plugins en extensies kan Maven op elk moment worden opgefrist en vereenvoudigd. Zou een
verdere ontwikkeling niet veel spannender en ook duurzamer zijn, in plaats van van de ene technologie naar de volgende te springen?

### Links

* [Terugkeren van Gradle naar Maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### Contact

[GitHub-problemen](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
