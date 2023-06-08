---
title: "Terug naar Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "```De moeilijk te grijpen zoektocht naar eenvoud en een korte reis om de kracht van Maven opnieuw te ontdekken```"
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


```
# Terug naar Maven?
```

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)



## 10 jaar Gradle. Op zoek naar verlichting en een korte reis naar het herontdekken van de kracht van Maven.

Sorry, there is no text to translate in the given markdown code. Please provide a valid markdown text.

### Het maximaliseren van het potentieel van ontwikkelaars - We hebben meer tijdbesparende tools nodig

Onderwerpen die vaak over het hoofd worden gezien of zelden worden besproken, interesseren mij. Vaak worden coole
technologieën gebruikt, maar bijna niemand praat over de ermee verbonden problemen. Ontwikkeling is tegenwoordig erg
tijdrovend geworden. Met coole buzzwoorden zoals "serverloos", "low code", "IaC", "big data", "cloud", "DevOps", "you
build it you run it" etc. hebben ontwikkelaars al genoeg extra taken te doen. Meer taken betekent dat er bijna geen
experts meer zijn en er altijd iets wordt verwaarloosd. Daarom zijn automatiseringen en tijdsbesparingen mega
belangrijk. "Don't make me think" en "Works out of the Box" zijn al goede kwaliteitskenmerken die ik nog niet kan zien
in Gradle. Om eerlijk te zijn is Gradle niet het enige moderne hulpmiddel dat ons werk geeft in plaats van het te
vergemakkelijken.

### De illusoire zoektocht naar eenvoud en automatisering

Sinds SOAP heb ik een diepgewortelde afkeer van op XML gebaseerde configuraties. Met Gradle had ik gehoopt dat het schrijven van bindingscripts kinderspel zou zijn. Helaas werden mijn hoop en motivatie steeds kleiner. Gradle streeft naar flexibiliteit en offert daarvoor automatisering en kwaliteit op. Ontwikkelaars volgen blindelings de trend zonder rekening te houden met de impact op de betrouwbaarheid van de software. Om Gradle-buildscripts eenvoudig en onderhoudsarm te houden, is sterke discipline vereist. Zo'n discipline is al zeldzaam in de broncode en is daarom nog veel zeldzamer in de buildscripts.

### Vertalingen en workarounds - Als buildscripts uitdagend worden

Gradle werkt in de achtergrond niet veel anders dan Maven. Daarom zijn er enkele vertalingen nodig. Features zoals de Dependency Catalog, het Maven Release Plugin, de Dependabot en vele anderen zijn eigenlijk workarounds voor fundamentele functies die Maven al heeft. Met de flexibiliteit van Gradle ontstaan vaak complexe buildconfiguraties die moeilijk te onderhouden zijn.
Gradle-plugins hebben vaak compatibiliteitsproblemen, beperkingen of beperkte verdere ontwikkeling. Deze problemen ontstaan door de ontwikkelende aard van het Gradle-ecosysteem, de diversiteit van de omgevingen waarin Gradle wordt toegepast, en de specifieke implementatie- en onderhoudsinspanning voor elke plugin. Alles is met elkaar verbonden.

### Het Domino-effect van Gradle - Een nachtmerriescenario in de echte wereld

Ik heb veel Microservices gezien die slechts een paar jaar oud waren en al onhoudbaar waren vanwege Gradle. Belangrijk om te vermelden is dat dit niet de eerste keer is dat ik zoiets heb gezien, en nee, het waren geen Junior Devs.

Mijn taak was het upgraden van Spring Boot 2.x naar 2.7. Spoiler: ik heb het na een jaar opgegeven! De problemen in het kort:

* De Gradle-buildfile vereist -> Verlaging van mijn lokale Java-versie naar 11 (WTF) (Java is normaal gesproken downwards compatible - er zijn ook hier weer Workaround-tools zoals SdkMan...)
* De Spring Boot-update vereist -> Gradle-update (WTF)
* De Gradle-update vereist -> Plugin-update
* De Plugin-update vereist -> Groovy-update (WTF)
* De Groovy-update vereist -> Test-Framework- en Test-Updates (WTF)
* Het Test-Framework-update vereist -> Afhankelijkheidsupdates
* [...]

Daarnaast werken sommige plugins niet met nieuwere Gradle-versies, sommige worden niet meer onderhouden, zijn incompatibel met andere plugins, werken alleen met Gradle KTS, niet met Gradle Groovy, of hebben simpelweg beperkingen. Zelfs plugins van grote leveranciers zoals Spring hebben beperkte functionaliteit in vergelijking met hun Maven-plugins. Uiteindelijk heb ik een coole, korte Gradle-buildfile die niemand goed kan onderhouden, zelfs niet de ontwikkelaars die het hebben geschreven, en ze houden nog steeds van Gradle. Ik ken maar weinig mensen die Gradle-scripts serieus kunnen begrijpen of schrijven.

### De herontdekking van de kracht van Maven - Het benutten van de magische krachten van Maven

Hier zijn mijn favoriete functies van Maven: Plugins kunnen direct vanaf de opdrachtregel worden gestart en geconfigureerd zonder dat ze eerder gedefinieerd moeten worden. Bovendien zijn ze grotendeels onafhankelijk van andere plug-inconfiguraties.

| Voorbeeldopdracht                       | Beschrijving                                                                                        | Link                                                                       | 
|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`   | Updates van versies doorvoeren - wie heeft Dependabot nodig? Ja, mijn projecten worden al jaren probleemloos bijgewerkt naar de nieuwste versie, zonder vervelende Merge-verzoeken | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0` | Projectversie instellen...                                                                                                                                         | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`         | Afhankelijkheden weergeven en hun licenties tonen (kan zelfs mislukken bij uitgesloten licenties)                                                        | https://www.mojohaus.org/license-maven-plugin/index.html                 |

Deze lijst kan eindeloos doorgaan. Het doet me een beetje denken aan GitHub Workflow-stappen.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

### Vind je geen XML leuk?

Geen probleem! Schrijf gewoon je Build-bestand in `ruby`, `groovy`, `scala`, `yaml`, `atom` of `Java`. De Polygot Extension (https://github.com/takari/polyglot-maven) maakt het mogelijk. Om het uit te proberen, voer je gewoon `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` uit en binnen enkele milliseconden is je Build-bestand vertaald. Helaas is er geen betrouwbare Maven <> Gradle vertaler :( Ja, Maven Build-bestanden zijn groot, maar ook heel gemakkelijk te begrijpen. Correcties of debugging zijn in een handomdraai gedaan.

### Leeftijd is slechts een getal - Maven's stabiliteit en evolutie

Euhrlijk gezegd, Maven bestaat al een tijdje en de esthetiek ervan komt misschien niet overeen met de huidige standaarden. Maar de levensduur van Maven heeft ervoor gezorgd dat het zich heeft kunnen aanpassen en verder ontwikkelen. Maven werkt onafhankelijk van jouw project. Build-bestanden kunnen gemakkelijk opnieuw worden gebruikt. De plugins draaien in een sandbox en zijn onafhankelijk van elkaar en onafhankelijk van de Java- of Maven-versie. Dit ontwerp bevordert de stabiliteit en voorspelbaarheid en maakt het gemakkelijk om complexe build-processen te beheren zonder onverwachte conflicten.

### Conclusie

Tegenwoordig is de ontwikkelomgeving overbelast met veel taken en technologieën voor ontwikkelaars. Op zoek naar eenvoud en automatisering is Gradle als modern build-tool opgekomen, maar dit heeft zijn eigen uitdagingen met zich meegebracht. Zonder twijfel is het concept van Gradle goed! Maar gezien de complexiteit en tijd die geïnvesteerd wordt in Gradle build-scripts, rijst de vraag of het niet eenvoudiger zou zijn om Maven uit te breiden. Met plugins en extensies kan Maven op elk moment verfrist en vereenvoudigd worden. Zou een verdere ontwikkeling niet veel spannender en duurzamer zijn dan van de ene technologie naar de andere te springen?

### Koppelingen

* [Terugkeren van Gradle naar Maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### Contact

[GitHub-problemen](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
