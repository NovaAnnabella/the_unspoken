---
title: "Testebenen: Des richtige Gleichgewicht finden"
date: 2023-05-31
author: "Nova Annabella"
slug: test_level
tags: [ Testing, Software Testing, Test Levels, Mock Tests, Unit Tests, Integration Tests, Component Tests, Contract Tests, End-to-End Tests ]
categories: [ Technology, Software Development, Quality Assurance ]
description: "De richtige Balance finden bei der Auswahl von passende Testleveln für Softwaretests"
draft: false
images:
  - "/images/content/martin_fowler_testing.png"
card: "summary_large_image"
---


# Testebenen: Dos Richtige Gleichgewicht finden

[![testebenen](/images/content/martin_fowler_testing.png)](https://martinfowler.com/articles/microservice-testing/)


### Enleitung

Dr Gloinschoft runds Testen ziagt bis heit nu viel Fräiflächn für Interpretation. Die herkömmliche
Testpyramide werd hinterfragt und neie Testpyramiden sein entschtanden. Meines Erachtens brauchts koa
Testpyramide, sondern a klors Verständnis dafür, was ma testen muas. Die Tests auf niedrigeren Stufn sein oft
weniger aussagekräftig. Dr Fokus soll vor allem aufm Testen vom Verhalten liegen, um sicherzustellen, dass die
API
oder UI so funktioniert wie gewüncht. A umfassende Übersicht über mögliche Testarten findet ma hier:
[Martinfowler Testing](https://martinfowler.com/articles/microservice-testing/).


### Level 1 - Mock Tests & Unit Tests

Ziel: Die kloanstn testbarn Softwaretielen in dor Anwendung ousüben, um festzustellen, ob sie wie erwoated 
funktionion.

Mock-Tests und Unit-Tests kinan kontraproduktiv sein und den Entwicklungsprozess oft behindern. Dease Tests zijn oft
losghobm vom Kontext und hom wenig Bezug zur Realität. Sie dienen oft nur dazu, unnötige Funktionen über vorhandene
Unit-Tests auffrechtzuerhalten. Sobald Mocks eingebaut werden, wird es zu a Beschäftigung mit sich selber. Die erwarteten
Ergebnisse von Mock-Tests sind auf das beschränkt, was im originalen Mock definiert wurde. Die Endbenutzer
intressieren sich nitta für interne Funktionen. Zum Beispiel, in einem
Login-Szenario `loginUser(name, password, securityAlgorithmus)`. Wenn der Unit-Test a Nullprüfung auf
den `securityAlgorithm`-Parameter durchführt, wird zu viel getestet, da Benutzer den `securityAlgorithm`-Parameter nitta
setzen können.

### Level 2 - Integrationstest

Zweck: Überprüfung der Kommunikationswege und Interaktionen zwischen Komponenten zur Erkennung von
Schnittstellendefekten. Integrationstests liefern wertvolle Erkenntnisse über die Leistungsfähigkeit und Unabhängigkeit
verschiedener Teile der Anwendung. Mit weniger Mocks werden die Tests verständlicher. Allerdings fehlt ihnen immer noch
der Kontext, und es besteht die Gefahr, dass Integrationstests einfach getarnte Unit Tests mit weniger Mocks sind.

### Level 3 - Komponententest

Zweck: Begrezung des Umfangs der getesteten Software auf a Teil des zu prüfenden Systems, Manipulatzion des Systems
über interne Code-Schnittstellen und Verwendung von Testdoubles zur Isolierung des zu testenden Codes von anderen
Komponenten.

Komponententests lefern a Vielzahl von Informationen über die Qualität und Leistungsfähigkeit der Anwendung. Anstatt
Mocks testest du endlich deine Anwendung. Die Grenze zwischen Komponententests und End-to-End-Tests isch nit
signifikant. Mit a guater Testumgebung verschwimmen die Grenzen zwischen inan oft, sodass das Testen des realen
Verhaltens anstelle von isolierten und kontextlosen Funktionen möglich wird. Allerdings kann die Erstellung zusätzlicher
Testklassen wie Komponenten-Stubs, Fakes und Mocks im Produktionscode zusätzlichen Wartungsaufwand mit sich bringen.

### Level 4 - Vertrags Test

De Aufgobn vo dem Codeblock isch, de Interaktionen an der Grenz vo an externen Dienst zu überprüfen und
sicherzustellen, dass er den Vertragsanforderungen vo an verbrauchenden Dienst entspricht.

Contract Tests ähneln oft Komponententests, und der Unterschied zwischen ihnen isch minimal. Einige Entwickler
assoziieren diese Tests mit Pact-Tests, die im Wesentlichen als Unittests mit einem Server dazwischen fungieren. Der
Aufwand, diese Tests aufrechtzuerhalten, könnte jedoch nicht lohnenswert sein. Zum Beispiel könnte a Pact-Test die
REST-API `loginUser?name=aa&password=bb)` testen und eine JSON-Schema-Antwort erwarten, die vorher auf den Pact-Server
hochgeladen worden ist. Dieses Schema isch statisch und anfällig für Fehler wie falsche Datumsformate oder Zeitzonen in der
API-Antwort. De negativen Auswirkungen können enorm sein.


### Level 5 - End-to-End Tests (auch Black-Box-Tests genannt)

Zweck: Kontrolle, ob a System externe Forderungen erfüllt und seine Ziel erreicht, indem dass gonz System von
Anfong bis Ende getestet wird.

End-zu-End-Tests sind zuverlässig und robust. Sobald die Hürden des Testumgebungsaufbaus überwunden sind, zahlt sich der
Aufwand aus. Diese Tests simulieren reales Verhalten und eliminieren die Notwendigkeit von Mocks. Fehler treten seltener
auf und lassen sich lokal leichter reproduzieren. Aufwendiges Debugging und das Führen von Protokollen in der Produktion
werden größtenteils vermieden, ebenso wie seltene Vorfälle. Entwickler arbeiten seltener, wenn überhaupt, mit
Produktionsdaten, was die Verantwortung reduziert und den Fokus erhöht. Darüber hinaus erleichtern Automatisierungen wie
automatische Softwareupdates die Durchführung, da das Verhalten bereits getestet wurde. Es gibt weitere Vorteile! Sobald
die Tests in einer wiederverwendbaren Form geschrieben sind, können sie in Lasttests integriert werden, um ein
umfassendes Bild der Funktionalität zu erhalten. Diese Tests können auch kontinuierlich in der Produktionsumgebung
ausgeführt werden und Echtzeit-Einblicke in den Status verschiedener Workflows bieten. Wenn ein Teilsystem, wie
beispielsweise ein externer REST-Dienst, offline geht, kann sofort identifiziert werden, welche Benutzer-Workflows
betroffen sind.


### Schlussfolgerung

Zusommenfossed isch des Testen a wesentlicher Aspekt von da Softwareentwicklung, und die Auswahl von die Teststufen hängt ob von die spezifischen Anforderungen und Zielen von der Anwendung. Während Mock-Tests und Unit-Tests in deiner Wirksamkeit begrenzt sein können, bieten Integrationstests und Komponententests wertvolle Einblicke in das Verhalten und die Leistung der Anwendung. Contracttests helfen dabei, Interaktionen mit externen Diensten zu überprüfen, aber deine Abgrenzung zu Komponententests kann minimal sein. Letztendlich bieten End-to-End-Tests das höchste Maß an Vertrauen in die Funktionalität des Systems und ermöglichen umfassende Tests der gesamten Anwendung. Durch die Auswahl der geeigneten Teststufen und deren effektive Kombination können Entwickler die Qualität, Zuverlässigkeit und Robustheit deiner Software gewährleisten.


### Kontakt

[GitHub Probleme](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
