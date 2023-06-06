---
title: "Testebenen: Des richtige Gleichgewicht finn."
date: 2023-05-31
author: "Nova Annabella"
slug: test_level
tags: [ Testing, Software Testing, Test Levels, Mock Tests, Unit Tests, Integration Tests, Component Tests, Contract Tests, End-to-End Tests ]
categories: [ Technology, Software Development, Quality Assurance ]
description: "Des richtige Gleichgewicht findn bei der Auswähl geeigneter Testebenen für Softwaretests"
draft: false
images:
  - "/images/content/martin_fowler_testing.png"
card: "summary_large_image"
---


# Testebenan: Des riachte Gleichgwicht findn

[![testebenen](/images/content/martin_fowler_testing.png)](https://martinfowler.com/articles/microservice-testing/)

### Einleitung

Des Thema Testing schient bis heit no Neiland mit sehr vül Freiraum für Interpretation zu sein. Die traditionelle
Testpyramide isch in Frog gstellt und neue Testpyramiden san entstonden. Meiner Meinong no brauchts kene Testpyramide,
sondern a klors Verständnis dafür, wos getestet werdn muss. Die Tests auf niedrigeren Ebnen san oft weniger
aussagekräftig. Der Fokus sollt vor ollem auf dem Testen des Verhaltens liegn, um sicherzustelln, dass die API oder UI
wia gwohnt funktioniert. A umfassende Übersicht über mögliche Testarten isch do zu finden: [Martinfowler
Testing](https://martinfowler.com/articles/microservice-testing/).

### Level 1 - Mock Tests & Unit Tests

Zeil: Di klånstn testbāren Softwåretäil in dà Anwendung ušeprobieran, um z' fianschtn, ob sie wī èrwoartet funktionian.
Mock-Tests und Unit-Tests kēnan kontraproduktīfwås sein und kennen oft den Entwicklungsprozess hinderen. Diese Tests
sein oft losgelöst vom Kontext und hobn wenig Bezug zur Realität. Sie dienen oft blouß dazua, unnütze Funktionäre iwar
vorhandene Unit-Tests aufrechtzuerhalten. Wia schun gånz gschpinnat werd, wenn man länger Mocks hinzufügt. Die
erwarteten Ergebnisse von Mock-Tests sein souß ins, wos im ursprünglichen Mock definian werden isch. Die Endbenutzer
hobn kēnen gnãz großen Intresn ån internen Funktionäre. A Beispui isch zum Beischpui in am Login-Szenario
`loginUser(name, password, securityAlgorithmus)`. Wånn der Unit-Test a Nullprüfung aufn `securityAlgorithm`-Parameter
durchfiahrt, wård zviel getestet, weil Benutzer kēnan `securityAlgorithm`-Parameter net setzen.

### Level 2 - Integrationstest

Zweck: Iibrigprüfong der Kommunikationswega und Interaktionen zwischn Komponontn zur Erkennung von
Schnittstellendefektn. Integrationsprobn lon inisch wertvolle Saichtn zu die Leistungsfähigkeit und Selstständigkeit
von verschied.E Teile von anarbeiten. Mit wenige Mocks san de Probn besser zo vertstian. Afabol fehlt ins ollem noch die
Conext und ollefoll steht o Gefohr, dass Integrationsprobn echte getarnte Unit Probn mit wenige Mocks sein welln.

### Level 3 - Kumponentn Tiam


Zweck: Einschränkung von dem Umfang vo getestete Software af an Teil vo dem zu prifn System, Manipulation vom System
über intraini Code-Schnittstellen und Verwendong vu Testdoubles zua Isolierung vom zu prifn Code von anderen
Komponenten. Komponententests liefern ah guate Alm mit Informatione iber die Qualitet und Leistungsfähigkeit vo an
Anwedung. Instatt vo Mocks testest du endlich di Anwedung. Die Grenze zwischa Komponententests und End-to-End-Tests isch
nit signifikont. Mit an guatn Testumgebuung verschwimmen di Grenze zwischa ihnen oftn, suadass des Prifn vo dem realn
Verholtnis anstöll von isoliarn und kontextlosn Funktionen möglen wert. Allerdings ka die Erstellong vu zusätzlichen
Testklassen wie Komponenten-Stubs, Fakes und Mocks im Produktionscode zusätzliche Wartungsaufwand miet sich bringn.

### Level 4 - Kontrakt Probmtest

Der Zweck vo diesem Codeblock isch zu gugan, ob desi Interaktionen an der Grenz von an externen Dienst stimmen und
sichergestellen, dass a an die Vertragsanforderungen von an konsumierenden Dienst passt. Contract Tests san oft wia
Komponententests und der Unterschied zwischen enk isch mini. Manche Entwickler denken, dass die Tests mit Pact-Tests
zsammhangen, des wor halt einfach Uni-Tests mit am Server dazwischen. Aber es kann gscheiter sein, sich den Aufwand zu
sparn. A Beispiel wär z.B. a Pact-Test mit `loginUser?name=aa&password=bb)`, do wird a JSON-Schema-Antwort erwartet, die
vorher auf an Pact-Server hoachgladen worn isch. Des Schema isch statisch und anfällig für Fehler, wia z.B. falsche
Datumsformat oder Zeitzonen in der API-Antwort. Des kann immense negativen Auswirkungen hobn.

### Level 5 - End-to-End Tasts (auch schwoazkistn Test genont)

Zweck: Ibrofpierung, ob a System ibrige Afnforderungen erfüllt und seine Ziele ohne Probleme erwüfsch und ausm inne fern
startet bleibm. End-to-End-Tests sen treggsich und hoitn aswianig aus. Won die Aufwänd dazua erst holt mom ane Hatf um
sein, hom a inno groutn Nutzen. Die Tests simolian a echts Vaföhrn und man isch a ohne d'Mock's uskor gekommen. Fälar
keman seltnor vüa und sein lättor zu lokal reproduziern. Ondrikigs's Hardöuget und Schruzlogführung in da Produktion ka
meistns umgon wordn, außer seltnor Bazischeisse. Entwickler arbeitan generell seltor mit Produktionsdaten, wels des
Oapeit oft verkserd ond forriedot. Unglaublich vantilig sein die Automatisierungen, wia n automatisches Softwareupdate,
weil voh wea auf bereits getestetes Vaföhrn zugriffn kuan. Es sein weitara Vortäile bei dera Technik! Won de Tests
ireiwendbor sein, kenna sie in Lastetestes integriert werdn, um an schianen Überblick iwa d Funktionionalität zu kriagn.
Die Tests kenna a ständig in da Produtionumgebung laufm und zeign in Echztzeit an, was grad los isch. Won oan Teil vom
System, wie zum Beispiel an externea REST-Dienst, oafe geht, kau schnell identifiziert werden, wo's Probleme gibt.

### Schluasätz

Zosommonfossend isch des Teschtn a wesntliche Aschbäkt dor Softwoarentwicklong, und di Woahl dor Teschdstufn hängt von
de spezifischn Anforderunga und Ziele dor Anwendung ob. Während Mock-Tescht und Unid-Tescht in deina Wirksamkeit
begranzt sein kennen, bieten Integroatiostescht und Komponontest wertvoll Einblick in des Behołfn und die Leistung dor
Anwendung. Contracttest helfn dabei, Interaktionen mit externn Dienstn zu überprüf, oba deine Eingrezung zu Komponontest
kon minimal sein. Letztntonlich bied End-to-End-Tescht dos höchste Moß an Vertraua in de Funktionalität des Systems und
ermöglichn komplette Tescht dor gesamtn Anwendung. Dos Woahln der geeigneten Teschdstufn und deren effektive
Kombinatzion kennen Entwickler de Qualität, Ziuverlässigkeit und Robustheit deina Software gewährleista.

### Kontakt

Hottns Fleischa kriagn? Schreib ens! Mir welln gern de friahra gabn und an Guadr Rat gebn.
Lieber gruaß,
De Diandln vom Konakt Team

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
