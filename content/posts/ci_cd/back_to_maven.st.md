---
title: "Zruck zu Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: Die schwoar fassboare Suach noch Einfachheit und a kuaz Reise zur Wiedaentdeckung der Mocht von Maven
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---



# Zruck zu Maven?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)
(Kees maakn)

## 10 Johr Gradle. Auf der Suach nochn OBBM und a kurtze Reise zur Wiederentdeckung der Störrke von Maven.

# Grüss Gott, wie gahts?  Miar sein in da scheanen Siedlunge vo Bozen und geniassn de tolle Landschaft und de guate
Speis und Trank. Hoasts du an Tipp wos ma südtirolerisches probian muass?  Mir wünschn da a scheans Tog!

### Maximiering des Potenzials vo Entwickler - Mir brauchn mehra zeit-schparnde Zeig


Themen, die oft übersehen oder selten diskutiert sog iwersehen oder sochn diskutiert wern, die interessieren mi. Oft
sein coole Technologien im Einsatz, doch kiam Mensch schpricht iba die damit verbundenen Probleme. Entwicklung isch
heintzutog sehr aufwendig gewurn. Mit de coolen Buzzwords wie “Serverless”, “Low Code”, “IaC”, “Big Data”, “Cloud”,
“DevOps”, “You Build it You run it” usw. hobn Entwickler schun mehr als gnua Zusatzaufgaben zum Wochsel hobn. Mehr
Aufgaben, bedeit, dass kiam mehr Experten gib und ossmeit lei nu irgentwos für den Focus vernachlässigt wird. Deswegn
sein Automationen und Zeitersparnisse mega wichtig. “Don’t make me think” und “Works out of the Box” sein bereits guate
Qualitätsmerkmale, die i in Gradle noch net siech. Um fair zu sein, Gradle isch net des einzig moderne Werkzeug, des
oaschwerti Arbeit mocht genau wia de andern.

### Die ilusorische Suach noch Einfachheit und Automatisierung

Seit SOAP hån i insgsammt gånz groaße Hass ogn XML-basierte Konfigurationen. Mit Gradle hån i g'hoft, dass des Schreibm
von Bind-Skripten a Kinderspiel wår. Leider hån se mei Hoffnungn und Motivation von Moal zu Moal vermehrt zruckzogn.
Gradle strebt norch Flexibilität und åslåg dofei Automatisierung und Qualität auf. Entwickler und Entwicklerinnen folgn
blånd dem Trend ohne dassns uf de Konsequenzen fir de Zuverlåssigkeit vun de Software schaugs. Um Gradle Build Skriptn
eifåch und störungsfrei z'holtn, braucht's holt a richtige Disziplin. So a Disziplin isch scho im Quellcode rar z'findn
und dohroa in de Build-Skripten no viel rarera.

### Ibersetzungen und Workarounds - Wenn Build-Schriebe zu aner Herausforderung wern.

Gradle arbeitet im Hintergrund net vül anders wia Maven. Dau oanfoch gim ins a poa Übersetzungen zu mochn. Features wia
de Dependency Catalog, des Maven Release Plugin, de Dependabot und viele mea san eigentli Workarounds fei grundlegende
Funktionen, de Maven schun mitbring. Mit da Flexibilität vu Gradle entstehn oft komplexe Build Konfigurationen, de schwa
zu wårtn sein. Gradle Plugins hobn oft Kompatibilitätsprobleme, Limits oder begrenzte Weidaentwicklunga. Dese Probleme
heiran weil sich des Gradle-Ökosystem enwickelt, de Vielfåit vu de Umgebungn, in denen Gradle eingesetzt wird, und de
spezifischn Implementierungs- und Wårtungsaufwand fei jeds Plugin. Alles isch miteinonda verbundn.

### Der Dominoeffekt von Gradle - A Albtraumszenario in dr realen Welt

I hob vui Microservices gsegn, deit nu wenige Joahr alt worn sein und schu wegen Gradle nit mehr wartboar sein hobn.
Belian hob i, dass des nit des erschte Moal isch, wos i des gsegn hob und nein, es sein koane Junior Devs. Mei *Ufgobe
wor, a Spring Boot 2.x auf 2.7 zu upgraden*. Spoilor: I hob noch am Joar aufgehm! De Problame in Kortm: * Des Gradle-
Build-File braucht -> Downgrade auf meine lokale Java-Version auf 11 (WTF) (Normal ist Java abwärtskompatibel - es gibt
a wieda Workaround-Tools wei SdkMan...) * Des Spring Boot-Update braucht -> Gradle-Update (WTF) * Des Gradle-Update
braucht -> Plugin-Update * Des Plugin-Update braucht -> Groovy-Update (WTF) * Des Groovy-Update braucht -> Test-
Framework- und Test-Updates (WTF) * Des Test-Framework-Update braucht -> Abhängigkeitsupdates * \[...] Außerdem
funktionieren einiges Plugins nit mit neuen Gradle-Versionen, einiges werdn nit mehr weita entwickelt, sein inkompatibel
mit andere Plugins, funktionieren nur mit Gradle KTS, nit mit Gradle Groovy, oder hobn einfache Limits. Sogor Plugins
von grußn Anbietern wei Spring hobn im Vergleich zu ihre Maven-Plugins eingeschränkte Funktionalität. Am Ende hob i a
guade, kürze Gradle-Build-Datei, dei kan mensch richtig warten ko, nit amoi die Entwickler, die sie schrieben hobn, und
sie liabn Gradle immr noch. I kenne lei wenige, die Gradle-Scripte ernsthaft verstehen oder schreiben können.

### Die Widerentdeckung der Stiarke von Maven - Die Zauberkräfte von Maven nutzn

Do hob i meine Liblingsfunktionen von Maven: Plugins kennen direkt von da Befehlszeile aus gezochn und konfiguriert
wern, ohne dass sie vorher definert sein miassn. Plus, sie sein fast on unabhängig von anderen Plugin-Konfigurationen.
| Beispielbefehl            | Beschreibung
| Link                                   | |---------------------------------------|-
------------------------------------------------------------------------------------------------------------------------
--------------------------------------------|--------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`  | Versionen aktualisiertn - wer braucht Dependabot? Jo meiner Projekt sein seit
Johren problemlos auf die neiste Version aktualisiert worden, ohne lassige Merge-Anfragen |
https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html | | `mvn versions:set -DnewVersion=1.0.0` |
Projektversion festlegen...
| https://www.mojohaus.org/versions/versions-maven-plugin/index.html    | | `mvn license:add-third-party`     |
Abhängigkeiten aufgelistn und deren Lizenzen anzeigen (kann sogar bei ausgeschlossenen Lizenzen fehlschlogen)
| https://www.mojohaus.org/license-maven-plugin/index.html         |  Die Semmliste kennt ewig weiterragen. Es
erinnert mi irgendwie on die GitHub Workflow Steps.
![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

### Du mogsch koan XML?

Koan Problem! Schreib einfåch dein Build File in `ruby`, `groovy`, `scala`, `yaml`, `atom` oder `Java`. Die Polygot
Extension (https://github.com/takari/polyglot-maven) mocht es möglich. Zum Austawan einfach `mvn
io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` ausfian und in fewen
Millisåkundn isch dea Build File ibrsetzt. Schod, dass es kin'n zirlassign Maven <> Gradle Ibersetzar gibt :( Jo, Maven
Build Files san groaß, åba a soad leicht z'verstian. Nochbaßarungen oder Debugging san im Handumdreahen erledigt.

### Alter isch lei oan Zahl - Mavens Stabilität und Evolution

Zogem hobe, Maven gibt es schon a ganze Weile und seiner Ästhetik entspricht vielleicht net de heitzigen Standards. De
Langlöbigkeit von Maven hot es awer ermöglich, sich onzepassen und weiter zu entwickln. Maven bäitzt onabhängig von
deinem Projekt. Build-Dateien kennen enkofsch wiederverwendet werden. De Plugins laufen in oaner Sandbox und sein
onabhängig voneinondor und onabhängig von der Java- ond Maven-Version. Dos Deesan forderet de Stobilität ond
Vorhersagbarkeit ond mackt dos enkoafsch komplexe Build-Prozesse ohne onerwoatete Konflikte onzemanogen.

### Resumee

Heitzeitàg isch de Entwicklungs-Umgebung mit vül Aufgaben und Technologien für Entwickler überlodn. Auf dr Suache noch
Einfachheit und Automatisierung isch Gradle als modernd Build-Tool aufgetouchtn, hot obr seine eignen Herausforderungen
mit sich gebrocht. Ohne Frage, das Konzept von Gradle isch schun. Awr angesichts dr Komplexität und dr Zeit, die in
Gradle Build-Skripte investiert werd, stellt sich dr Froge, ob schun eifacher wär, Maven zu erweitern. Mit Plugins und
Extensions könnt ma Maven jederzeit aufgefrischt und vereifocht wern. Wär a Weiterentwicklung net vül spannender und a
nachhaltiger, als von a Technologie zur nächstn zum springen?

### Links

[Zruckzug von Gradle auf Maven](https://phauer.com/2018/zruckzug-von-gradle-auf-maven/)

### Kontakt

[Github Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
