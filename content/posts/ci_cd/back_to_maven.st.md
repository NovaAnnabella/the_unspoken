---
title: "Zrugg zu Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "Die schwer fassbare Suche nach Einfachheit und eine kurze Reise zur Wiederentdeckung der Macht von Maven."
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# Zurück zu Maven?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

## 10 Johr Gradle. Uf da Suach noch Erleichterung und a kuarze Reise zur Wiederentdeckung der Stärke von Maven.



### Maximierung des Potenzials von Entwicklern - Mir brauchn mehra zeitsparende Tools

Themen, die oft überschaug oder selten diskutiert werden, interessieren mi. Oft sein coole Technologien im Einsatz, doch
kaum jemand spricht über die damit verknaapten Probleme. Entwicklung ist heut zu Tage sehr ufwoadig geworden. Mit den
coolen Buzzwords wie “Serverless”, “Low Code”, “IaC”, “Big Data”, “Cloud”, “DevOps”, “You Build it You run it” usw. hobn
Entwickler bereits mehr als genug Zusatzaufgaben zu bewältigen. Mehr Aufgaben, bedeutet, dass es kaum noch Experten gibt
und immer irgendetwas für den Focus vernachlässigt wird. Daher sind Automationen und Zeitersparnisse mega wichtig.
“Don’t make me think” und “Works out of the Box” sind bereits gute Qualitätsmerkmale, die ich in Gradle noch nicht sehen
kann. Um fair zu sein, Gradle ist nicht das einzige moderne Werkzeug, das uns Arbeit macht, anstatt sie zu erleichtern.

### Die illusorische Suche noach Einfachheit und Automatisierung

Seit SOAP hon i a tiefe Gegenwehr gegen XML-basierte Konfigurationen. Mit Gradle hoff i, dass s Schreim von Bind-Skripten a Kinderspiel sein werd. Leider wurden meine Hoffnungen und meine Motivation von Mol zu Mol weniger. Gradle strebt nach Flexibilität und opfert dafür Automatisierung und Qualität. Entwicklerinnen und Entwickler folgen blind dem Trend ohne Rücksicht auf die Auswirkungen auf die Zuverlässigkeit der Software. Um Gradle Build Skripte einfach und wartungsarm zu halten, bedarf es einer starken Disziplin. So eine Disziplin ist scho im Quellcode selten zu finden und daher ist sie in den Build-Skripten noch viel seltener.

### Übersetzungen und Workarounds - Wenn Build-Skripte zu a Herausforderung werdn

Gradle obratet im Hintergrund nit völ onsersch als Maven. Es sein einige Übersetzungen netwendig. Features wia der Dependency Catalog, des Maven Release Plugin, der Dependabot und viele mehr sein werkli Abhilfen für grundlegende Funktionen, die Maven bereits mitbringt. Mit der Biegsamkeit von Gradle entstehen oft komplexe Build Konfigurationen, die schwirig zu warten sein.
Gradle Plugins sein häufig mit Kompatibilitätsprobleme, Limits oder begrenzte Weiterentwicklungen konfrontiert. Diese Probleme entstehen aufgrund der sich entwickelnden Natur des Gradle-Ökosystems, der Vielfalt der Umgebungen, in denen Gradle eingesetzt wird, und des spezifischen Implementierungs- und Wartungsaufwands für jedes Plugin. Alles ist mitanander verbunden.


### Der Dominoeffekt von Gradle - A Albtraumszenario in der echten Welt

I hob viele Microservices gsegn, de nur a poar Johr olt worn und schu aufgrund von Gradle nimma aufrecht z'hoitn 
woan. Wichtig zum neamnen, des isch nit des erste Mol dass I sowas gsechn hob, und na, es worn koane
Junior Devs.

Meine **Aufgob wor, a Spring Boot 2.x auf 2.7-Upgrade durchzufiahn**. Spoiler: I hob noch an Johr
aufgebn! De Probleme im Kurzen:

* Des Gradle-Build-File verlongt -> Downgrade meiner lokaln Java-Version auf 11 (WTF) (Normalerweise isch Java
  obwärtskompatibel - es gibt a do wieder Workaround-Tools wia SdkMan...)
* Des Spring Boot-Update verlongt -> Gradle-Update (WTF)
* Des Gradle-Update verlongt -> Plugin-Update
* Des Plugin-Update verlongt -> Groovy-Update (WTF)
* Des Groovy-Update verlongt -> Test-Framework- und Test-Updates (WTF)
* Des Test-Framework-Update verlongt -> Abhängigkeitsupdates
* \[...]
  Drüber hinaus funktioniern einige Plugins nit mit neueren Gradle-Versionen, einige wean nimma weida
  entwickelt, sein inkompatibel mit andere Plugins, funktionieren nur mit Gradle KTS, nit mit Gradle Groovy, oda
  hobn einfach Limits. Selbscht Plugins von großen Anbietern wia Spring hobn im Gegnsatz zu ihre Maven-Plugins
  eingschränkte Funktionalität. Oam End hob i a coole, kurze Gradle-Build-Datei, de niemand richtig warten ko,
  nit einmal de Entwickler, de's gschriem hobn, und sie liebn Gradle imma no. I kenn nur wenige, de
  Gradle Scripte ernsthaft verstehn oder schreibn kennan.


### Die Wiederentdeckung der Stärke von Maven - Die Zauberkräfte von Maven nutzen

Do sein meine Lieblingsfunktzionen vo Maven:
Plugins konn ma direkt von der Befehlszeile aus starten und konfigurieren, ohne dass ma sie vorher definieren muss. Plus, se sein ziemlich unabhängig von anderen Plugin-Konfigurations.

| Beispiels-Befehl                    | Beschreibung                                                                                                                                                 | Link                                                                     | 
|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`   | Versions aktualisieren - wer braucht schon Dependabot? Ja, meine Projekte werden schon seit Jahren ohne Probleme auf die neueste Version aktualisiert, ohne störende Merge-Anfragen | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0` | Projektversion festlegen...                                                                                                                                | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`         | Abhängigkeiten auflisten und deren Lizenzen anzeigen (kann sogar bei bestimmten ausgeschlossenen Lizenzen schef gehen)                                     | https://www.mojohaus.org/license-maven-plugin/index.html                 | 

Die Liste könnt ewig so weitergehen. Es erinnert mi irgendwie an GitHub Workflow Steps.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

### Du mogsch koan XML?

Kei Problem! Schreib anfoch dei Build File in `ruby`, `groovy`, `scala`, `yaml`, `atom` oder `Java`. De Polygot
Extension (https://github.com/takari/polyglot-maven) mocht es meglich. Zum Ausprobiern
anfoch `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` ausfiern und in
wianige Millisekunden isch dei Build File ibrsetzt. Schod, dass es koan verlässlichen Maven <> Gradle Ibrsetzer
git :(
Jo, Maven Build Files sein groaß, owa a sehr leicht verständlich. Nochbesserungen oder Debugging sein im Nu
erledigt.

### Oita isch lei a Zahl - Mavens Stabilität und Evolution

Zugem, Maven gibts scho a gonz Weil und seim Ästhetik entspricht vielleicht net de heitige Standards.
De Langlebigkeit von Maven hot owa ermöglicht, sich oanzupassen und weiterzuentwickeln. Maven arbeitet unabhängig
von deim Projekt. Build-Dateien kennan einfach wiederverwendet werden.
Die Plugins rennen in ana Sandbox und sein unabhängig voneinander und unabhängig von da Java- oder Maven-Version.
Deses Design fördert de Stabilität und Vorhersagbarkeit und mocht es einfach, komplex Build-Prozesse ohne unerwartete
Konflikte zu verwalten.

### Fazit

Huatzutog isch de Entwicklungsumgebung mit viele Aufgaben und Technologien für Entwickler überladen. Auf der Suche
noch Einfachheit und Automatisierung isch Gradle als modernes Build-Tool aufgetaucht, hot ober seine eigenen
Herausforderungen mit sich gebracht. Ohne Frage, des Konzept von Gradle isch guat! Ober angesichts der Komplexität und der
Zeit, die in Gradle Build-Skripte investiert wird, stellt sich die Frage, ob es net einfacher wäre, Maven zu
erweitern. Mit Plugins und Extensions würde man Maven jederzeit aufgefrischt und vereinfacht werden. Wäre eine
Weiterentwicklung net viel spannender und a nochhaltiger, als von einer Technologie zur nächsten zu springen?

### Links

* [Zrugggehn von Gradle zu Maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### Kontakt

[GitHub Probleme](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
