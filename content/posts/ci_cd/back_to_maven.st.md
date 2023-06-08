---
title: "Zrugg zu Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "De schwoar fassbare Such nooch Einfachheit und a kuaze Reis zur Wiedaentdeckong vu de Macht vo Maven."
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# Zruck zu Maven?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/zuruck-zu-maven-von-gradle/)

## 10 Johr Gradle. Auf da Suach nooch Erleichtrung und a kurze Reis zur Wiederaufdeckung der Stärke von Maven.

I hob a problem mit meim Computer und brauch Hilfe. Kinnst tu mir helfn?

### Maximierung des Potenzials von Entwicklern - Mir brauchn mei Zeit sparisch Instrumente

Themn, die oft übersehm oder seltn diskutiart werden, interesserien mich. Oft sein schian kühle Technologien is Einsatz,
jedoch kemma kaum Leit daher, die über die dazua größten Probleme schbreschn. Entwicklung is heitzuag sehr aufwendig
gwordn. Mit de kühln Buzzwords wie “Serverless”, “Low Code”, “IaC”, “Big Data”, “Cloud”, “DevOps”, “You Build it You run
it” usw. hobm Entwickler schun mehr ois gnua Zubm zu kämpfen. Mehr Arbatn, bedeitn, dass es kaum mehr Experten gibt und
imma wos für den Fokus vernachlässigt wird. Deshalb sein Automationen und Zeitersparnisse meggawicht. “Don’t make me
think” und “Works out of the Box” san bereit klanne Qualitätsmerkmal, die i bei Gradle noch nit sehn konn. Um fair zu
sein, Gradle is nit das einzige moderne Wäigezoug, das uns Arbat macht, statt se uns leihtern zu solln.

### Die illusorischa Suach noch Einfachheit und Automatisierung

Seit SOAP hon i a tief verwurzlte Obneigung gegen XML-basierte Konfigurationen. Mit Gradle hon i ghofft, dass des Schriebm von Bind-Skripten a Kindaspiel werd. Leider zijn meine Hoffnungn und meine Motivation von Mal zu Mal kloaner gwordn. Gradle strebt noch Flexibilität und opfert dafür Automatisierung und Qualität. Entwicklerinnen und Entwickler folln blind dem Trend ohne Rücksicht auf die Auswirkungen auf die Zuverlässigkeit der Software. Um Gradle Build Skriptn einfåch und wartungsarm zu hom, bedarf es oana starkn Disziplin. A solche Disziplin isch scho im Quellcode sölt´n zu finden und dahor isch sie in de Build-Skripten no vü söltner.```

### Ibersetzungen und Workarounds - Wenn Build-Schribe zu ana Herausforderung werdn.

Gradle arbeidt im Hintergrund nit viel andrs ols Maven. Do sein olm sou eppas iatz, die ma iatz üschibruschian muass. Features wia der Dependency Catalog, des Maven Release Plugin, der Dependabot und vül mehr san eigntlich Workarounds für grundlegende Funktionen, die Maven schun mitbringn tut. Mit dor Flexibilität vu Gradle entstian oft komplexe Build Konfigurationen, die schwa zu woarten sein. Gradle Plugins hom haufig Kompatibilitätsschwierigkeiten, Limits oder begrenzte Weiterentwicklungen. Diese Probleme entstian wegen der sich entwickelnden Natua vu dem Gradle-Ökosystem, der Vielfalt der Umgebungn, in dea Gradle eingesetzt wert, und des spezifischn Implementierungs- und Woartungsaufwands fia jedes Plugin. Olles is miteinondan verbundn.

### Der Dominooeffekt vu Gradle - A Albtraum-Szenario in da realn Welt

I hob vül Microservices gsegn, wonschte paar Johr oltn worn sen und schun aufgrund von Gradle net mer wortbor woren sen. Wochtzichtig isch dobei zu sogn, dass des net des erschte Moi isch, dass i a so wos gseng hon und koane Junger Devs worn sen. 

Mei **Ofgr wills sein, a Spring Boot 2.x auf 2.7-Upgrade durchzufiarn**. Spoiler: I hon noch oam Joa afgebm! Die Probleme im Kriztn: 

* Des Gradle-Build-File erfordert -> Downgrade meina lokaln Java-Version auf 11 (WTF) (Normalerweis isch Java abwärtskompatibel - es gibt a wieder Workaround-Tools wia SdkMan...)
* Des Spring Boot-Update erfordert -> Gradle-Update (WTF)
* Des Gradle-Update erfordert -> Plugin-Update
* Des Plugin-Update erfordert -> Groovy-Update (WTF)
* Des Groovy-Update erfordert -> Test-Framework- und Test-Updates (WTF)
* Des Test-Framework-Update erfordert -> Abhängigkeitsupdates
* \[...\]
  Obovoi funktionieren oine Plugins net mit neinere Gradle-Versionen, oine werdn net mer weihtaweiterentwickelt, sein inkomptabel mit anderen Plugins, funktionier'n nur mit Gradle KTS, net mit Gradle Groovy, oder hon einfach Limits. Söbst Plugins von groaßen Anbieiata wia Spring hon im Vergleich zu ihre Maven-Plugins aig'schränkte Funktionalität. Zum End hon i a kools, kurzes Gradle-Build-File, dass kanoricht wortbor ko, net amol die Entwickler, die es gschrieben hon, und sie liewen Gradle imm'r no. I kenn lei wenige, die Gradle-Scripte andlich verstian oder schreim kenna.

### Die Wiederentdeckung der Stärke von Maven - Die Zauberkräfte von Maven nutzen

Do isch meine liabelsten Funkzionen von Maven:
Plugins kennen direkt von der Befehlszeile aus gestartet und konfiguriert wern, onse dass sie vorher definiert sein missn. Plus, sie sein weitgehend unabhängig von anderen Plugin-Konfigurationen.

| Beispielbefehl                        | Beschreibung                                                                                                                                                        | Link                                                                     | 
|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`   | Versionen aktualisiern - wer braucht Dependabot? Jo, meine Projekte sein seit Johrn problemlos auf die neie Version aktualisiert, onse lästige Merge-Anfragen | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0` | Projektversion festlegen...                                                                                                                                         | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`         | Abhängigkeiten aufschian und deren Lizenzen anzeigen (kann sogor bei ausgeschlossenen Lizenzen fehlschlagen)                                                        | https://www.mojohaus.org/license-maven-plugin/index.html                 | 

Do keniast es olles weitarliesen. Es erwinnert mien irgendwie on GitHub Workflow Steps.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)


```

### Kanntsch du XML nit leidn?

Koan Problem! Schreib eifoch dein Build File in `ruby`, `groovy`, `scala`, `yaml`, `atom` oder `Java`. De Polygot Extension (https://github.com/takari/polyglot-maven) mcht´s möglich. Zum Oopsprobn einfach `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` ausführen und in wenige Millisekunden isch dein Build File übersetzt. Schod, dass´s kana ziuverlässigen Maven <> Gradle Übersetzer gibt :(
Joa, Maven Build Files sein groaß, oba a sehr leicht verständlich. Nochbesserungen oder Debugging sein in an Haandenumdrehn erledigt.

### Oitr isch lei a Nummer - Mavens Stabilität und Evolution

Beigeschtaubt, der Maven isch scho a Weil do und sei Eazetik entsprechd wohrscheinlich net de heitign Standards.
De Lebmgschicht vom Maven hot's oba ermöglicht, sich anzupassen und weiterzuentwickeln. Der Maven schafft onofhängig
vom dein Projekt. Build-Dateien kinnsch einfôch wiederweren.
De Plugins loufen in a Sandbox und sein onofhängig voneinônder und onofhängig von de Java- oder Maven-Version.
Dass voie Design fôrdert de Stabilitât und Vorhersehbarkeit und môchts eifoch, komplexe Build-Prozesse ohne onerwartete
Konflikte zu managen.

### Resümee

Haitezutogs isch de Entwicklungs-Umgebung mit oanfoch z'vül Aufgobn und Technologien fö de Entwickler übabladn. Oanfochheit und Automatisierung söchn's isch Gradle als moderens Build-Tool auftogt, hot owa seine eigenen Herausforderungen mit g'brochtn. Ohne Frog, des Konzept von Gradle isch guat! Owa gögn de Komplexität und de Zeit, de öb'n in Gradle Build-Skriptn investiert wird, stöllt sich de Frog, ob's nit oanfocha wäre, Maven zu erweitern. Mit Plugins und Extensions könnt ma Maven jederzeit aufgefrischt und vereinfacht wern. Wär a Weiterentwicklung nit vül spannender und a nachhaltiger, als von oana Technologie zur nächsten zu springen?

### Lenker

* [Zuruck von Gradle zu Maven kemmen](https://phauer.com/2018/zuruck-von-gradle-zu-maven/)

### Kontakt

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
