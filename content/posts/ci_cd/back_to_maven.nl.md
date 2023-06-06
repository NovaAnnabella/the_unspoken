---
title: "Terug naar Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "De ongrijpbare zoektocht naar eenvoud en een korte reis om de kracht van Maven te herontdekken".
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---



# Terug naar Maven?

[maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

## 10 jaar Gradle. Op zoek naar verlichting en een korte reis om de kracht van Maven te herontdekken.



### Het potentieel van ontwikkelaars maximaliseren - we hebben meer tijdbesparende tools nodig

Onderwerpen die vaak over het hoofd worden gezien of zelden worden besproken, interesseren me. Er worden vaak coole
technologieën gebruikt, maar bijna niemand praat over de problemen die ermee gepaard gaan. Ontwikkeling is tegenwoordig
erg duur geworden. Met coole modewoorden als "serverless", "low code", "IaC", "big data", "cloud", "DevOps", "you build
it you run it", enz. hebben ontwikkelaars er al genoeg van. enz. hebben ontwikkelaars al meer dan genoeg extra taken om
zich mee bezig te houden. Meer taken betekent dat er nauwelijks experts en er wordt altijd iets verwaarloosd voor de
focus. Daarom zijn automatisering en tijdsbesparing mega belangrijk. "Don't make me think" en "Works out of the Box"
zijn al functies van goede kwaliteit die ik nog niet in Gradle zie. nog niet zie. Om eerlijk te zijn, Gradle is niet de
enige moderne tool die ons werk maakt in plaats van het makkelijker maakt.

### De illusoire zoektocht naar eenvoud en automatisering

Sinds SOAP heb ik een diepgewortelde afkeer van op XML gebaseerde configuraties. Met Gradle had ik gehoopt dat het
schrijven van bind scripts een fluitje van een cent zou zijn. Helaas, mijn hoop en motivatie elke keer minder. Gradle
streeft naar flexibiliteit en offert daarvoor automatisering en kwaliteit op. Ontwikkelaars volgen blindelings de
ontwikkelaars volgen blindelings de trend zonder rekening te houden met de impact op de betrouwbaarheid van de software.
Om Gradle Build scripts eenvoudig en onderhoudsarm te maken is een sterke discipline nodig. Zulke discipline is al
zeldzaam in broncode en daarom is het nog zeldzamer in de build scripts.

### Vertalingen en workarounds - Wanneer buildscripts een uitdaging worden

Gradle werkt op de achtergrond niet veel anders dan Maven. Daarom zijn sommige vertalingen noodzakelijk. Functies zoals
de Dependency Catalog, de Maven Release Plugin, de Dependabot, en nog veel meer zijn eigenlijk workarounds voor basis
functies die Maven al biedt. Met Gradle's flexibiliteit komen vaak complexe bouwconfiguraties, die moeilijk te
onderhouden zijn. Gradle plugins hebben vaak compatibiliteitsproblemen, beperkingen of beperkte vooruitgang. Deze
problemen ontstaan door de evoluerende aard van het Gradle ecosysteem, de diversiteit van de omgevingen waarin Gradle
wordt wordt gebruikt en de specifieke implementatie- en onderhoudsinspanningen die voor elke plugin nodig zijn. Alles is
met elkaar verbonden.

### Het Gradle domino-effect - Een nachtmerriescenario in de echte wereld

Ik heb veel microservices gezien die nog maar een paar jaar oud waren en nu al niet meer te onderhouden waren door
Gradle. door Gradle. Belangrijk om te vermelden is dat dit niet de eerste keer is dat ik zoiets zie, en nee, het waren
geen Junior ontwikkelaars. Mijn **taak was het uitvoeren van een Spring Boot 2.x naar 2.7 upgrade**. Spoiler: Ik gaf
het op na een jaar Ik heb het opgegeven! De problemen in het kort: * Het Gradle build-bestand vereist -> Downgrade mijn
lokale Java-versie naar 11 (WTF) (Normaal gesproken is Java  naar beneden compatibel - nogmaals, er zijn workaround
tools zoals SdkMan...) * De Spring Boot update vereist -> Gradle update (WTF) * De Gradle update vereist -> Plugin
update * De plugin update vereist -> Groovy update (WTF) * De Groovy update vereist -> Test framework en test updates
(WTF) * De test framework update vereist -> Dependency updates. * \[...]  Daarnaast werken sommige plugins niet met
nieuwere Gradle-versies, sommige zijn niet meer ontwikkeld, sommige zijn incompatibel met andere Gradle-versies, sommige
zijn niet meer ontwikkeld, sommige zijn incompatibel met andere Gradle-versies.  zijn incompatibel met andere plugins,
werken alleen met Gradle KTS, niet met Gradle Groovy, of hebben simpelweg  hebben gewoonweg beperkingen. Zelfs plugins
van grote leveranciers zoals Spring hebben beperkte functionaliteit in vergelijking met hun Maven plugins.  beperkte
functionaliteit. Ik eindig met een cool, kort Gradle build bestand dat niemand echt kan onderhouden,  zelfs de
ontwikkelaars die het geschreven hebben niet, en ze houden nog steeds van Gradle. Ik ken maar weinig mensen die  Gradle
scripts serieus begrijpen en ze schrijven.

### De kracht van Maven herontdekken - De magie van Maven benutten

Dit zijn mijn favoriete functies van Maven: Plugins kunnen direct vanaf de opdrachtregel worden gestart en
geconfigureerd zonder dat je ze vooraf hoeft te definiëren. moeten worden gedefinieerd. Bovendien zijn ze grotendeels
onafhankelijk van andere plugin configuraties. | Voorbeeld Commando Beschrijving Link |--------------------------------
-------|----------------------------------------------------------------------------------------------------------------
-----------------------------------------------------|------------------------------------------------------------------
--------| | `mvn versions:use -latest-versions` | Versies bijwerken - wie heeft Dependabot nodig? Ja, mijn projecten
worden al jaren zonder problemen en zonder vervelende samenvoegverzoeken bijgewerkt naar de nieuwste versie |
https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html | | `mvn versions:set -DnewVersion=1.0.0` |
Stel projectversie in...
| https://www.mojohaus.org/versions/versions-maven-plugin/index.html | `mvn license:add-third-party` | Maak een lijst
van afhankelijkheden en toon hun licenties (kan mislukken, zelfs als licenties zijn uitgesloten) |
https://www.mojohaus.org/license-maven-plugin/index.html | Deze lijst kan eindeloos doorgaan. Het doet me een beetje
denken aan GitHub Workflow Stappen. maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

### Hou je niet van XML?

Geen probleem! Schrijf je build bestand gewoon in `ruby`, `groovy`, `scala`, `yaml`, `atom` of `Java`. De Polygot
Extension (https://github.com/takari/polyglot-maven) maakt het mogelijk. Om het uit te proberen voer je simpelweg `mvn
io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` uit en in een paar
milliseconden is je build milliseconden je buildbestand vertaald. Het is jammer dat er geen betrouwbare Maven <> Gradle
vertaler is. :( Ja, Maven build bestanden zijn groot, maar ook erg makkelijk te begrijpen. Verfijningen of debuggen zijn
in een mum van tijd gedaan. klaar.

### Leeftijd is maar een getal - Mavens stabiliteit en evolutie

Toegegeven, Maven bestaat al een tijdje en de esthetiek voldoet misschien niet aan de hedendaagse normen. De lange
levensduur van Maven heeft het echter mogelijk gemaakt om zich aan te passen en te evolueren. Maven werkt onafhankelijk
van je project. Build bestanden kunnen gemakkelijk hergebruikt worden. Plugins draaien in een sandbox en zijn
onafhankelijk van elkaar en onafhankelijk van de Java of Maven versie. Dit ontwerp bevordert stabiliteit en
voorspelbaarheid en maakt het makkelijk om complexe bouwprocessen te beheren zonder onverwachte conflicten.

### Fazit

Tegenwoordig is de ontwikkelomgeving overladen met vele taken en technologieën voor ontwikkelaars. In de zoektocht naar
eenvoud en automatisering, is Gradle naar voren gekomen als een moderne buildtool, maar het heeft zijn eigen uitdagingen
met zich mee. Zonder twijfel is het concept van Gradle goed! Maar gezien de complexiteit en de tijd geïnvesteerd in
Gradle build scripts, rijst de vraag of het niet eenvoudiger zou zijn om Maven uit te breiden. uitgebreid. Met plugins
en extensies zou Maven altijd ververst en vereenvoudigd kunnen worden. Zou een Zou verdere ontwikkeling niet veel
spannender en ook duurzamer zijn dan van de ene technologie naar de andere te springen?

### Links

* [Teruggaan van Gradle naar maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### Contact

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
