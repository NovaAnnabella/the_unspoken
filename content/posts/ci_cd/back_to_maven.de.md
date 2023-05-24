---
title: "Zurück zu Maven?"
date: 2023-05-01T01:01:01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "Die schwer fassbare Suche nach Einfachheit und eine kurze Reise zur Wiederentdeckung der Macht von Maven"
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---

# Zurück zu Maven?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)


## 10 Jahre Gradle. Auf der Sucher nach Erleichterung und eine kurze Reise zur Wiederentdeckung der Stärke von Maven.

### Maximierung des Potenzials von Entwicklern

#### Wir benötigen mehr zeitsparende Tools

Themen, die oft übersehen oder selten diskutiert werden, interessieren mich. Oft sind coole Technologien im Einsatz,
doch kaum jemand spricht über die damit verbundenen Probleme.
Entwicklung ist heut zu Tage sehr aufwendig geworden.
Mit den coolen Buzzwords wie “Serverless”, “Low Code”, “IaC”, “Big Data”, “Cloud”, “DevOps”, “You Build it You run it”
usw. haben Entwickler bereits mehr als genug Zusatzaufgaben zu bewältigen. Mehr Aufgaben, bedeutet, dass es kaum noch
Experten gibt und immer irgendetwas für den Focus vernachlässigt wird. Daher sind Automationen und Zeitersparnisse mega
wichtig. “Don’t make me think” und “Works out of the Box” sind bereits gute Qualitätsmerkmale, die ich in Gradle noch
nicht sehen kann. Um fair zu sein, Gradle ist nicht das einzige moderne Werkzeug, das uns Arbeit macht, anstatt sie zu
erleichtern.

### Die illusorische Suche nach Einfachheit und Automatisierung

Seit SOAP habe ich eine tief verwurzelte Abneigung gegen XML-basierte Konfigurationen. Mit Gradle hatte ich gehofft,
dass das Schreiben von Bind-Skripten ein Kinderspiel sein würde. Leider wurden meine Hoffnungen und meine Motivation von
Mal zu Mal geringer. Gradle strebt nach Flexibilität und opfert dafür Automatisierung und Qualität. Entwicklerinnen und
Entwickler folgen blind dem Trend ohne Rücksicht auf die Auswirkungen auf die Zuverlässigkeit der Software. Um Gradle
Build Skripte einfach und wartungsarm zu halten, bedarf es einer starken Disziplin. Eine solche Disziplin ist schon im
Quellcode selten zu finden und daher ist sie in den Build-Skripten noch viel seltener.

### Übersetzungen und Workarounds

#### Wenn Build-Skripte zu einer Herausforderung werden

Gradle arbeitet im Hintergrund nicht viel anders als Maven. Daher sind einige Übersetzungen notwendig. Features wie der
Dependency Catalog, das Maven Release Plugin, der Dependabot und viele mehr sind eigentlich Workarounds für grundlegende
Funktionen, die Maven bereits mitbringt. Mit der Flexibilität von Gradle entstehen oft komplexe Build Konfigurationen,
die schwer zu warten sind.
Gradle Plugins haben häufig Kompatibilitätsprobleme, Limits oder begrenzte Weiterentwicklungen. Diese Probleme entstehen
aufgrund der sich entwickelnden Natur des Gradle-Ökosystems, der Vielfalt der Umgebungen, in denen Gradle eingesetzt
wird, und des spezifischen Implementierungs- und Wartungsaufwands für jedes Plugin. Alles ist miteinander verbunden.

### Der Dominoeffekt von Gradle

#### Ein Albtraumszenario in der realen Welt

Ich habe viele Microservices gesehen, die nur wenige Jahre alt waren und bereits aufgrund von Gradle nicht mehr wartbar
waren. Wichtig zu erwähnen, dass dies nicht das erste Mal ist, dass ich so etwas gesehen habe, und nein, es waren keine
Junior Devs.

Meine **Aufgabe war, ein Spring Boot 2.5 auf 2.7-Upgrade durchzuführen**. Spoiler: Ich habe nach einem Jahr
aufgegeben! Die Probleme im Kurzen:

* Das Gradle-Build-File erfordert -> Downgrade meiner lokalen Java-Version auf 11 (WTF) (Normalerweise ist Java
  abwärtskompatibel - es gibt auch hier wieder Workaround-Tools wie SdkMan...)
* Das Spring Boot-Update erfordert -> Gradle-Update (WTF)
* Das Gradle-Update erfordert -> Plugin-Update
* Das Plugin-Update erfordert -> Groovy-Update (WTF)
* Das Groovy-Update erfordert -> Test-Framework- und Test-Updates (WTF)
* Das Test-Framework-Update erfordert -> Abhängigkeitsupdates
* \[...]
  Darüber hinaus funktionieren einige Plugins nicht mit neueren Gradle-Versionen, einige werden nicht mehr weiter
  entwickelt, sind inkompatibel mit anderen Plugins, funktionieren nur mit Gradle KTS, nicht mit Gradle Groovy, oder
  haben einfach Limits. Selbst Plugins von großen Anbietern wie Spring haben im Vergleich zu ihren Maven-Plugins
  eingeschränkte Funktionalität. Am Ende habe ich eine coole, kurze Gradle-Build-Datei, die niemand richtig warten kann,
  nicht einmal die Entwickler, die sie geschrieben haben, und sie lieben Gradle immer noch. Ich kenne nur wenige, die
  Gradle Scripte ernsthaft verstehen doer schreiben können.

### Die Wiederentdeckung der Stärke von Maven

#### Die Zauberkräfte von Maven nutzen

Hier sind meine Lieblingsfunktionen von Maven:
Plugins können direkt von der Befehlszeile aus gestartet und konfiguriert werden, ohne dass sie vorher definiert werden
müssen. Plus, sie sind weitgehend unabhängig von anderen Plugin-Konfigurationen.

| Beispielbefehl                        | Beschreibung                                                                                                                                                        | Link                                                                     | 
|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`   | Versions aktualisieren - wer braucht Dependabot? Ja, meine Projekte werden seit Jahren problemlos auf die neueste Version aktualisiert, ohne lästige Merge-Anfragen | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0` | Projektversion festlegen...                                                                                                                                         | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`         | Abhängigkeiten auflisten und deren Lizenzen anzeigen (kann sogar bei ausgeschlossenen Lizenzen fehlschlagen)                                                        | https://www.mojohaus.org/license-maven-plugin/index.html                 | 

Diese Liste könnte ewig so weitergehen. Es erinnert mich irgendwie an GitHub Workflow Steps.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

### Du Magst du kein XML?

Kein Problem! Schreibe einfach dein Build File in `ruby`, `groovy`, `scala`, `yaml`, `atom` oder `Java`. Die Polygot
Extension (https://github.com/takari/polyglot-maven) macht es möglich. Zum Ausprobieren
einfach `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` ausführen und in
wenigen Millisekunden ist dein Build File übersetzt. Schade, dass es keinen zuverlässigen Maven <> Gradle Übersetzer
gibt :(
Ja, Maven Build Files sind groß, aber auch sehr leicht verständlich. Nachbesserungen oder Debugging sind im Handumdrehen
erledigt.

### Alter ist nur eine Zahl

#### Mavens Stabilität und Evolution

Zugegeben, Maven gibt es schon eine ganze Weile und seine Ästhetik entspricht vielleicht nicht den heutigen Standards.
Die Langlebigkeit von Maven hat es jedoch ermöglicht, sich anzupassen und weiterzuentwickeln. Maven arbeitet unabhängig
von Ihrem Projekt. Build-Dateien können einfach wiederverwendet werden.
Die Plugins laufen in einer Sandbox und sind unabhängig voneinander und unabhängig von der Java- oder Maven-Version.
Dieses Design fördert die Stabilität und Vorhersagbarkeit und macht es einfach, komplexe Build-Prozesse ohne unerwartete
Konflikte zu verwalten.

### Fazit

Heutzutage ist die Entwicklungsumgebung mit vielen Aufgaben und Technologien für Entwickler überladen. Auf der Suche
nach Einfachheit und Automatisierung ist Gradle als modernes Build-Tool aufgetaucht, hat aber seine eigenen
Herausforderungen mit sich gebracht. Ohne Frage, das Konzept von Gradle ist gut! Doch angesichts der Komplexität und der
Zeit, die in Gradle Build-Skripte investiert wird, stellt sich die Frage, ob es nicht einfacher wäre, Maven zu
erweitern. Mit Plugins und Extensions könnte man Maven jederzeit aufgefrischt und vereinfacht werden. Wäre eine
Weiterentwicklung nicht viel spannender und auch nachhaltiger, als von einer Technologie zur nächsten zu springen?

### Links

* (Moving Back from Gradle to maven)[https://phauer.com/2018/moving-back-from-gradle-to-maven/]

### Kontakt

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
