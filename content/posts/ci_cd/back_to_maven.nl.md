---
title: "Terug naar Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "De ongrijpbare zoektocht naar eenvoud en een korte reis naar herontdekking van de kracht van Maven."
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# Terug naar Maven?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

## 10 jaar Gradle. Op zoek naar verlichting en een korte reis om de kracht van Maven weer te ontdekken.

Sorry, as a language model, I am not able to generate a response without input. Please provide me with the text you want
me to translate.

### Maximaliseren van het potentieel van ontwikkelaars - We hebben meer tijdbesparende tools nodig

Onderwerpen die vaak over het hoofd worden gezien of zelden besproken worden, interesseren mij. Vaak worden coole
technologieën gebruikt, maar bijna niemand spreekt over de bijbehorende problemen. Ontwikkeling is tegenwoordig erg
tijdrovend geworden. Met de coole buzzwords zoals "Serverless", "Low Code", "IaC", "Big Data", "Cloud", "DevOps", "You
Build it You run it", enz. hebben ontwikkelaars al meer dan genoeg extra taken te vervullen. Meer taken betekent dat er
nauwelijks nog experts zijn en er altijd iets voor de focus wordt verwaarloosd. Daarom zijn automatisering en
tijdsbesparingen heel belangrijk. "Don't make me think" en "Works out of the Box" zijn al goede kwaliteitskenmerken die
ik niet kan zien in Gradle. Om eerlijk te zijn, Gradle is niet het enige moderne hulpmiddel dat ons werk geeft in plaats
van ons te ontlasten.

### De illusoire zoektocht naar eenvoud en automatisering

Sinds SOAP heb ik een diepgewortelde afkeer van op XML gebaseerde configuraties. Met Gradle had ik gehoopt dat het schrijven van bindingscripts kinderspel zou zijn. Helaas werden mijn hoop en motivatie steeds minder. Gradle streeft naar flexibiliteit en offert daarvoor automatisering en kwaliteit op. Ontwikkelaars volgen blindelings de trend zonder rekening te houden met de effecten op de betrouwbaarheid van de software. Om Gradle-buildscripts eenvoudig en onderhoudsvriendelijk te houden, is sterke discipline vereist. Een dergelijke discipline is al zeldzaam in de broncode en dus nog veel zeldzamer in de buildscripts.

### Vertalingen en workarounds - Wanneer build-scripts een uitdaging worden

Gradle werkt in de achtergrond niet veel anders dan Maven. Daarom zijn er een aantal vertalingen nodig. Functies zoals de Dependency Catalog, de Maven Release Plugin, de Dependabot en nog veel meer zijn eigenlijk workarounds voor basisfuncties die Maven al heeft. Met de flexibiliteit van Gradle ontstaan vaak complexe build configuraties, die moeilijk te onderhouden zijn.
Gradle-plugins hebben vaak compatibiliteitsproblemen, limieten of beperkte ontwikkelingen. Deze problemen ontstaan door de zich ontwikkelende aard van het Gradle-ecosysteem, de diversiteit van de omgevingen waarin Gradle wordt gebruikt, en de specifieke implementatie- en onderhoudskosten voor elk plugin. Alles is met elkaar verbonden.

### Het Domino-effect van Gradle - Een Nachtmerrie-scenario in de echte wereld

Ik heb veel Microservices gezien die slechts enkele jaren oud waren en al onhoudbaar waren vanwege Gradle. Belangrijk om te vermelden is dat dit niet de eerste keer is dat ik zoiets heb gezien en nee, dit waren geen junior ontwikkelaars.

Mijn opdracht was om een ​​Spring Boot 2.x naar 2.7 te upgraden. Spoiler: Na een jaar heb ik het opgegeven! De problemen in het kort:

* Het Gradle-Build-File vereist -> Downgrade van mijn lokale Java-versie naar 11 (WTF) (Normaal is Java achterwaarts compatibel - er zijn hier ook weer Workaround-Tools zoals SdkMan ...)
* De Spring Boot-update vereist -> Gradle-update (WTF)
* De Gradle-update vereist -> Plugin-update
* De Plugin-update vereist -> Groovy-update (WTF)
* Het Groovy-update vereist -> Test Framework- en Test-updates (WTF)
* Het Test Framework-update vereist -> Afhankelijkheidsupdates
* [...]

Bovendien werken sommige plugins niet met nieuwere Gradle-versies, sommige worden niet meer verder ontwikkeld, zijn incompatibel met andere plugins, werken alleen met Gradle KTS, niet met Gradle Groovy, of hebben gewoon beperkingen. Zelfs plugins van grote aanbieders zoals Spring hebben in vergelijking met hun Maven-plugins beperkte functionaliteit. Uiteindelijk heb ik een coole, korte Gradle-Build-File die niemand goed kan onderhouden, zelfs de ontwikkelaars die het hebben geschreven niet, en ze houden nog steeds van Gradle. Ik ken maar weinig mensen die Gradle-scripts serieus begrijpen of kunnen schrijven.

### De herontdekking van de kracht van Maven - Het gebruik maken van de toverkrachten van Maven

Hier zijn mijn favoriete functies van Maven: 

Plugins kunnen direct vanaf de command line worden gestart en geconfigureerd zonder dat ze vooraf gedefinieerd hoeven te worden. Bovendien zijn ze grotendeels onafhankelijk van andere plugin-configuraties.

| Voorbeeldcommando                     | Beschrijving                                                                                                                                                  | Link                                                                     |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`   | Versies bijwerken - wie heeft Dependabot nodig? Ja, mijn projecten worden al jaren probleemloos bijgewerkt naar de nieuwste versie, zonder vervelende samenvoegingsverzoeken. | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0` | Projectversie instellen...                                                                                                                                     | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`         | Afhankelijkheden weergeven en hun licenties weergeven (kan zelfs mislukken bij uitgesloten licenties)                                                            | https://www.mojohaus.org/license-maven-plugin/index.html                 |

Deze lijst kan eindeloos doorgaan. Het doet me op de een of andere manier denken aan GitHub Workflow Steps.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

### Houd je niet van XML?

Geen probleem! Schrijf gewoon je Build File in `ruby`, `groovy`, `scala`, `yaml`, `atom` of`Java`. De Polygot Extension (https://github.com/takari/polyglot-maven) maakt het mogelijk. Om het uit te proberen, voer eenvoudigweg `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` uit en binnen enkele milliseconden is je Build File vertaald. Jammer dat er geen betrouwbare Maven <> Gradle vertaler is :( Ja, Maven Build Files zijn groot, maar ook zeer gemakkelijk te begrijpen. Aanpassingen of debuggen zijn binnen enkele seconden gedaan.

### Leeftijd is slechts een nummer - Maven's stabiliteit en evolutie

Toegegeven, Maven bestaat al een tijdje en zijn esthetiek komt misschien niet overeen met de huidige normen. De duurzaamheid van Maven heeft het echter mogelijk gemaakt om zich aan te passen en verder te ontwikkelen. Maven werkt onafhankelijk van uw project. Bouwbestanden kunnen eenvoudig opnieuw worden gebruikt. De plug-ins worden uitgevoerd in een sandbox en zijn onafhankelijk van elkaar en onafhankelijk van de Java- of Maven-versie. Dit ontwerp bevordert de stabiliteit en voorspelbaarheid en maakt het gemakkelijk om complexe build-processen te beheren zonder onverwachte conflicten.

### Conclusie

Tegenwoordig is de ontwikkelingsomgeving overladen met veel taken en technologieën voor ontwikkelaars. Op zoek naar
eenvoud en automatisering is Gradle als modern build-hulpmiddel opgekomen, maar bracht zijn eigen uitdagingen met zich mee. Het concept van Gradle is zonder twijfel goed! Maar gezien de complexiteit en de tijd die wordt geïnvesteerd in Gradle Build-scripts, rijst de vraag of het niet gemakkelijker zou zijn om Maven uit te breiden. Met plugins en extensies kan Maven op elk moment worden vernieuwd en vereenvoudigd. Zou de ontwikkeling niet veel spannender en duurzamer zijn dan van de ene technologie naar de andere te springen?

### Links

* [Terugkeren van Gradle naar Maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### Contact

[GitHub-problemen](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).```
