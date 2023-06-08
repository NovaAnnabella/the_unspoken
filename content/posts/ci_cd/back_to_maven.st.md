---
title: "Zrugg zu Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "Die toggra Suiche noch Einfachheit und a kürze Reise zur Wiedahentdeckung der Macht von Maven."
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# Zruck zua Maven?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/gscheiter-umsteig-von-gradle-zu-maven/)

## 10 Johr Gradle. Auf der Suache noch Lechtigkeit und a kurze Reise zur Wiedaholtung der Stärke von Maven.

Sorry, I need a markdown text to translate it for you. Please provide me with the text in the markdown format.

### Ausnutzng ins Mogglichste von Entwicklern - Mir brauchn mehr Zeit sparende Tools.

Themen, die oft übersehen oder selten diskutiert werden, interessieren mi. Oft san kühle Technologien im Einsatz, doch
kane sau redt iba die mitlaufenden Probleme. Entwicklerei is heintzutogs sehr aufwendig worn. Mit de kühlen Buzzwords
wie "Serverless", "Low Code", "IaC", "Big Data", "Cloud", "DevOps", "You Build it You run it" usw. hom Entwickler
bereitß mea ois gnug Zusatzaufgaben zu meistern. Mea Aufgaben, bedeiten, dass kaum mehr Expertn do san und imma wos aufn
Focus vergassn wern muss. Deswegn san Automationen und Zeitersparnisse megageil. "Don’t make me think" und "Works out of
the Box" san bereitß guad Qualitätsmerkmale, die i bei Gradle no nit segn kin. Um fia zu sein, Gradle is nit des einzige
modernde Werkzeug, dass uns de Arbeit mochte, instead sie zu erleichtern.

### Die illesuarische Suache noch Eifochtheit und Automatisierunge

Seit SOAP honn ian tiafa finsta Ekel gegen XML-basiarte Konfigurationen. Mit Gradle honn i ghoft, dass sewos easiesch wia Kinderspui soi. Leida wurdn meine Hoffnungn ond meine Motivation von Mo zu Mo kloaner. Gradle strebt nach Flexibilität ond opfert dafür Automatisierung ond Qualität. Entwicklerinnen ond Entwickler föla blind dem Trend ohne Rücksicht auf die Auswirkungen auf die Zuverlässigkeit der Software. Um Gradle Build Skripte einfach ond wartungsarm zu halten, bedarf es einer stãrkan Disziplin. A solche Disziplin is schun im Quellcode seltn zu findn ond daher is sie in den Build-Skripten no viel seltener.

### Iwwasetzungen und Workarounds - Wånn Build-Skripte zu ara Herausforderung werdn

Gradle arbeidn im Hintagrund nit vül anders wia Maven. Do hommens eppes everzieln zi miaßen. Featurs wia der 
Dependency Catalog, dos Maven Release Plugin, der Dependabot und vül mear sein eigentlich Workarounds zi grondlegn 
Funkzionen, die Maven schun butt mitbrocht. Mittn Flexibilotät von Gradle entstean oft komplexe Build Konfigurationen, 
die schwer zu wartn sein sein.

Gradle Plugins hom häufig Kompatibilitätsprobleme, Limits odo begrenztn Weitarentwicklungen. Diese Probleme entstean 
aufgrund der sich entwickelndn Natur des Gradle-Ökosystams, der Vielfalt der Umgebm, in denen Gradle eingesetzt 
wird, und des spezifischn Implementierungs- und Wartungsaufwands für jedes Plugin. Alles isch miteinondn verbundn.

### Der Domineffekt von Gradle - A Almträumszenario in dor reoln Wölt

I hob vül Microservices gseng, de nur a poar Joar oltn und schun wegen Gradle nit mea wartbor worn. 
Wichtig isch zu erwähnen, dass des nit des erschte Moi isch, wo i so wos gseng hob. Und nein, es san koan Junior Devs gwesn.

Meine **Heaschaft isch gschen, a Spring Boot 2.x auf 2.7-Upgrade durchzuführen**. Spoiler: I hon no am Joar ahns ufgebm! Die Probleme kurz zommnfassn:

* Das Gradle-Build-File erfordert -> Downgrade meiner lokalen Java-Version auf 11 (WTF) (Normalerweise isch Java 
  abwärtskompatibel - es gibt a Werkzeig namens SdkMan... dos hilft)
* Das Spring Boot-Update erfordert -> Gradle-Update (WTF)
* Das Gradle-Update erfordert -> Plugin-Update
* Das Plugin-Update erfordert -> Groovy-Update (WTF)
* Das Groovy-Update erfordert -> Test-Framework- und Test-Updates (WTF)
* Das Test-Framework-Update erfordert -> Abhängigkeitsupdates
* \[...]
  Außerdem funktionieren a poar Plugins nit mit neieren Gradle-Versionen. A poar san nimma in der Weiterentwicklung, 
  san inkompatibel mit ondern Plugins, funktionieren lei mit Gradle KTS, nit mit Gradle Groovy, ond hond einfach 
  Grenzen. Sogar Plugins von großn Anbiatern wia Spring hond im Vergleich zu ihre Maven-Plugins kane so große 
  Funktionalität. Am Ende hon i a kools, kurzes Gradle-Build-File, des koaner richtig wartn kinnt, nit amoi die 
  Entwickler, die es gschrieben hon, ond sie liabn Gradle immr no. I kenn lei a poar, die Gradle-Scripte ernst wörtlich 
  verstian oder schreim kennen.

### Die Wiedafaundung der Stiakke fria Maven - Die Zauba-kräft von Maven wiaßn benutzn

Do sein meine Liablingsfunktionen von Maven:
Plugins kinnan direkt von da Befehlszeile aus gstartet und kintrolliert wern, ohne dass sie vorher definiert werdn brauchen. Plus, sie san weitgehend unabhängig von andern Plugin-Konfigurationen.

| Beispielbefehl                        | Beschreibung                                                                                                                                                                     | Link                                                                     |
|---------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`   | Versionen aktualisieren - wer braucht Dependabot? Jo meie Projechte wern seit Johren problemlos auf die neie Version aktualisiert, ohne lästige Merge-Anfraan                           | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0` | Projecktfersion festlegen...                                                                                                                                                     | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`         | Abhängigkeiten auflisten und deren Lizenzen anzeigen (kint sogar bei ausschlossenen Lizenzen fehlgeschlagen)                                                                   | https://www.mojohaus.org/license-maven-plugin/index.html                 |

Die liste konnt ewig so weider gehn. Es erinnert mich irgendwie an GitHub Workflow Steps.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

```

### Mogsch koa XML lei net?

Koan Problem! Schreibn insch einfoch dein Build File in `ruby`, `groovy`, `scala`, `yaml`, `atom` oder `Java`. Die Polygot Extension (https://github.com/takari/polyglot-maven) makt sches möglich. Zum Uasprubm insch einfoch `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` usführen und in weingn Millisekunden isch dein Build File übersetzt. Schad, dass es keinen zevrlässign Maven <> Gradle Übersetzt gibt :( Jo, Maven Build Files san groß, oba a vrschtehbar. Nochbarscheischn oder Debugging san im Handumdrehn erledigt.```

### Ôlta isch lei a Zahl - Mavens Staibiltät und Evolution

Zuigem es scho a Haufn Zeit und sei Optik entspricht vielleicht net de heitigen Standards. Doch d Lebnsdauer vo Maven hot et ermöglich en ze sich onzopassen und weiderzientwickln. Maven uabate duafontselbm vo dein Projekt. Build-Datei kinnn leicht wiederwondt wern. Die Plugins lafn in oana Sandbox und san unsongig vonanda und von da Java- oder Maven-Version. Es Design favdert de Ongehaut und Vohersogbarket und moch es easi komplexe Build-Prozesse ohne unerwartete Konflikte z valten.```

### Oarschlechtigung

Haitzutog isch die Entwicklungsumgebung mit vielen Aufgobm und Technologien fir Entwickler iberloatn. Auf dor Suach noch Eifochheit und Automatisierung isch Gredl ols moderns Build-Tool ufgiatu, hot obor seine eigene Herausforderungen mit sich brocht. Ohne Frog, dos Konzept von Gredl isch guat! Doch ogsichts dor Komplexität und dor Zeit, die in Gredl Build-Skript investiert wird, stellt sich de Frog, of nit eifocha wöre Maven zu ibrarbeitn. Mit Plugins und Extensions kinn man Maven jederzeit aufigfrischt und vereifocht werdn. Wöre a Weiterentwicklung nit völle spannender und essa noochholto, dos ibr von a Technologie zur nächstn ibrzischne?

### Verlinkungen

* [Zruckkemmen von Gradle zu Maven](https://phauer.com/2018/zruckkemmen-von-gradle-zu-maven/)

### Kontakt

[GitHub Inßn](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).```
