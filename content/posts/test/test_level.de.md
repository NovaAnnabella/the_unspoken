---
title: "Testebenen: Das richtige Gleichgewicht finden"
date: 2023-05-31
author: "Nova Annabella"
slug: test_level
tags: [ Testing, Software Testing, Test Levels, Mock Tests, Unit Tests, Integration Tests, Component Tests, Contract Tests, End-to-End Tests ]
categories: [ Technology, Software Development, Quality Assurance ]
description: "Das richtige Gleichgewicht finden bei der Auswahl der geeigneten Testebenen für Softwaretests."
draft: false
images:
  - "/images/content/martin_fowler_testing.png"
card: "summary_large_image"
---

# Testebenen: Das richtige Gleichgewicht finden

[![testebenen](/images/content/martin_fowler_testing.png)](https://martinfowler.com/articles/microservice-testing/)

### Introduction

### Einleitung

Das Thema Testing scheint bis heute noch Neuland mit sehr viel Freiraum für Interpretation zu sein. Die traditionelle
Testpyramide wurde in Frage gestellt und neue Testpyramiden sind entstanden. Meiner Meinung nach benötigt es keine
Testpyramide, sondern ein klares Verständnis dafür, was getestet werden muss. Die Tests auf niedrigeren Ebenen sind oft
weniger aussagekräftig. Der Fokus sollte vor allem auf dem Testen des Verhaltens liegen, um sicherzustellen, dass die
API
oder UI wie gewünscht funktioniert. Eine umfassende Übersicht über mögliche Testarten ist hier zu finden:
[Martinfowler Testing](https://martinfowler.com/articles/microservice-testing/).

### Level 1 - Mock Tests & Unit Tests

Ziel: Die kleinsten testbaren Softwareteile in der Anwendung ausüben, um festzustellen, ob sie wie erwartet
funktionieren.

Mock-Tests und Unit-Tests können kontraproduktiv sein und den Entwicklungsprozess häufig behindern. Diese Tests sind oft
losgelöst vom Kontext und haben wenig Bezug zur Realität. Sie dienen oft nur dazu, unnötige Funktionen über vorhandene
Unit-Tests aufrechtzuerhalten. Sobald Mocks hinzugefügt werden, wird es zu einer Selbstbeschäftigung. Die erwarteten
Ergebnisse von Mock-Tests sind auf das beschränkt, was im ursprünglichen Mock definiert wurde. Die Endbenutzer
interessieren sich nicht für interne Funktionen. Zum Beispiel, in einem
Login-Szenario `loginUser(name, password, securityAlgorithmus)`. Wenn der Unit-Test eine Nullprüfung auf
den `securityAlgorithm`-Parameter durchführt, wird zu viel getestet, da Benutzer den `securityAlgorithm`-Parameter nicht
setzen können.

### Level 2 - Integrationstest

Zweck: Überprüfung der Kommunikationswege und Interaktionen zwischen Komponenten zur Erkennung von
Schnittstellendefekten.

Integrationstests liefern wertvolle Erkenntnisse über die Leistungsfähigkeit und Unabhängigkeit verschiedener Teile der
Anwendung. Mit weniger Mocks werden die Tests verständlicher. Allerdings fehlt ihnen immer noch der Kontext, und es
besteht die Gefahr, dass Integrationstests einfach getarnte Unit Tests mit weniger Mocks sind.

### Level 3 - Komponententest

Zweck: Begrenzung des Umfangs der getesteten Software auf einen Teil des zu prüfenden Systems, Manipulation des Systems
über interne Code-Schnittstellen und Verwendung von Testdoubles zur Isolierung des zu testenden Codes von anderen
Komponenten.

Komponententests liefern eine Vielzahl von Informationen über die Qualität und Leistungsfähigkeit der Anwendung. Anstatt
Mocks testest du endlich deine Anwendung. Die Grenze zwischen Komponententests und End-to-End-Tests ist nicht
signifikant. Mit einer guten Testumgebung verschwimmen die Grenzen zwischen ihnen oft, sodass das Testen des realen
Verhaltens anstelle von isolierten und kontextlosen Funktionen möglich wird. Allerdings kann die Erstellung zusätzlicher
Testklassen wie Komponenten-Stubs, Fakes und Mocks im Produktionscode zusätzlichen Wartungsaufwand mit sich bringen.

### Level 4 - Contract Test

Purpose: Verify interactions at the boundary of an external service, asserting that it meets the contract expected by a
consuming service.

Contract tests are often similar to component tests, and the distinction between them is minimal. Some developers
associate these tests with Pact tests, which essentially function as unit tests with a server in between. The effort
involved in maintaining these tests might not be worthwhile. For instance, a Pact test may test the REST
API `loginUser?name=aa&password=bb)` and expect a JSON schema response that was uploaded to the Pact server beforehand.
This schema is static, making it prone to errors such as incorrect date formats or time zones in the API response. The
negative impact can be enormous.

Vertragsprüfungen ähneln oft Komponententests und die Unterscheidung zwischen ihnen ist minimal. Einige Entwickler
verbinden diese Tests mit Pact-Tests, die im Wesentlichen als Unittests mit einem Server dazwischen funktionieren. Der
Aufwand, diese Tests zu pflegen, mag nicht lohnenswert sein. Zum Beispiel kann ein Pact-Test die
REST-API `loginUser?name=aa&password=bb)` testen und eine JSON-Schema-Antwort erwarten, die zuvor auf den Pact-Server
hochgeladen wurde. Dieses Schema ist statisch und anfällig für Fehler wie falsche Datumsformate oder Zeitzonen in der
API-Antwort. Die negativen Auswirkungen können enorm sein.

### Level 5 - End-to-End Tests (auch Black-Box-Tests genannt)

Zweck: Überprüfung, ob ein System externe Anforderungen erfüllt und seine Ziele erreicht, indem das gesamte System von
Anfang bis Ende getestet wird.

End-to-End-Tests sind zuverlässig und robust. Sobald die Hürden des Testumgebungsaufbaus überwunden sind, zahlt sich der
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

### Fazit

Zusammenfassend ist das Testen ein wesentlicher Aspekt der Softwareentwicklung, und die Wahl der Teststufen hängt von
den spezifischen Anforderungen und Zielen der Anwendung ab. Während Mock-Tests und Unit-Tests in deiner Wirksamkeit
begrenzt sein können, bieten Integrationstests und Komponententests wertvolle Einblicke in das Verhalten und die
Leistung der Anwendung. Contracttests helfen dabei, Interaktionen mit externen Diensten zu überprüfen, aber deine
Abgrenzung zu Komponententests kann minimal sein. Letztendlich bieten End-to-End-Tests das höchste Maß an Vertrauen in
die Funktionalität des Systems und ermöglichen umfassende Tests der gesamten Anwendung. Durch die Auswahl der geeigneten
Teststufen und deren effektive Kombination können Entwickler die Qualität, Zuverlässigkeit und Robustheit deiner
Software
gewährleisten.

### Kontakt

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
