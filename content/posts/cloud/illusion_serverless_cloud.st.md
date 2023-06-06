---
title: "Illusion Serverless & Cloud"
date: 2023-05-24
author: "Nova Annabella"
slug: illusion_serverless_cloud
tags: [ Development, Serverless, Cloud, Microservices, Scalability, Architecture, Infrastructure ]
categories: [ Technology, Software, Cloud ]
description: "Herausforderungen und Realitäten von Serverless-Funktionen in der Cloud. Wertvolle Einblicke für Unternehmen, die eine Migration zur Cloud in Erwägung ziehen"
draft: false
images:
  - "/images/content/onprem_vs_cloud.png"
card: "summary_large_image"
---



# Die Illusion von Serverless Funktionen in der Cloud

Die Voöstöllung von Serverless Fonktioun in der Cloud

![aws_costs_twitter_1](/images/content/onprem_vs_cloud.png)

### Einfiorung

I bin enttäusch, wie oft dos Marketing übern gsunden Menschenverstond siegt. Viele Manager sangsch di eigene Expertn -
de Entwickler. Dos gilt a fir die Migration in die Cloud. Spoiler: Wem des Gald sporn muass, solltn die Cloud meiden.
Weil des neue Buzzword "Serverless" in da Cloud bedeut: Du kümmerst di um de Software, mir kümmern ins um de Hardware.
Wem owa an fleißign, aagognen und neigirign Administrator hot, der kinnt Serverless a selbst betreibn (z.B.
[KNative](https://knative.dev)). ![aws_kosten_twitter_1](/images/content/aws_kosten_twitter_1.png)

### Serverlose Funkzionen vs. Mircroservischn:

# Heileitn ## Schiess ki Gwenzn! Grias eich Leitln,  heint gruass i enk olle und winsch enk a scheanen Tog.  In dera
schiessn Zeit isch's wichtig, dass mr auf insa Gsundheit aufpassn. Drum ben i a großer Fan von Heileitn. I wünsch enk
olle a scheans Heileitn und a scheas Überstian dera Zeit.  Drum in dem Sinn: Schiess ki Gwenzn!  Eire Nächstn

#### Microservices

A typischer zustandsloser Microservice kümmert sich um a bestemmt Funktion/Domäne und wird in an Container
Orchestrierungsumgebung bereitgestellt. Des Umgebung kümmert sich um Infrastruktur, Sicherheit, Firewall, Logging,
Metriken, Secrets, Netzwerk, Backups und vieles mehr. A großer Vorteil isch, dass a Microservice lokal mit wenigen
Ressourcen integriert getestet werdn und Cloud-/Server-agnostisch (überoll einsetzbar) isch.

#### Serverlose Funktionen

A klaner Witz vorweg: Paradox, owa woah - Serverless-Funktionen hängen stark von der Serverumgebung ob. :) A typische
Serverless Funktion kimert sich a und o um nur oane bestimmte Funktion/Domäne und wird ohne Frameworks in reinem Code
geschrieben, um schneicha als a Microservice zu sein (Auch a gute Übung für MicroServices). A großer Vorteil isch, dass
Serverless Funktionen automatisch skaliert werden. Jedoch braucht jede Serverless Funktion a beträchtliche Menge an
GlueCode, um die Infrastruktur zu definieren - Security, Firewall, Netzwerk, Logging, Metriken, Secrets, Caching,
Backups und viel mehr. Dohrta könna einfache Funktion wie zum Beispui des Kopieren oaner Datei inklusive API schnell mol
1500 Zeilen Code (inkl. IaC) umfassen. Die Administrationskosten verschieben sich von der Administration zur Entwicklung
im Verhältnis 1:N (1 zu Serverless-Funktionen). Das Wissen und die Implementierung sein somit nimmer gebündelt und
können schnell instabil werdn. Noch dazu kemmen erhöhte Wartungskosten. Auch echte integrative Tests sein mit Serverless
selten oder nur mit großem Aufwand verbunden. Letztlich isch die Komplexität von Serverless-Funktionen deutlich höher
als die eines einzlns Microservices. Höhere Komplexität bedeutet a geringere Wartbarkeit. Noie Teammitglieder hobn es
schwoiriger und brauchen deutlich mehr Vorwissen.

### Serverless und die Cloud im Allgemeinen

Isch friaherzit ollas auf Server gschpeichert worden und de meischtn Programmierer hom glan om Serverinfrastrukturen aufzubauen. Mit der Zait hob sich de Technologie wieda weitraentwickelt und heute hom ma Infastrukturen in da Cloud. In de Zukunft sogn Viele, dass sich Serverless als Standard durchsetzen wird. Dabei werdn Programmierer nit mehr auf de Serverinfrastruktur fokussiert sein, sondern se werdn sich voll und gaenzlich auf die Anwendungsentwicklung konzentrieren können.

Die meischt'n Cloud-Technologien san net auf'm neischt'n Stand. Zum Beispui san Node.js, Java, Python und ondre
Schwammerl oft net einfåch uppdatebor. Meist hilft nur åbwoarten. Aich moderne und Standardtechnologien wie MongoDB,
MySQL, Kafka, NATS, RabbitMQ, Redis, Prometheus, InfluxDB, Grafana, Kibana, Elastic Search etz. san entweder net
verfügbor oder åberteuert. Ohne solche Standarddienste bist oft in da virtuellen Steinzeit und nutzt vārweltete Lösn,
z.B. Webhooks für die Kommunikation naus. Außerdem is der Handlungsspielraum bei Themen wie Regulierung, Compliance,
Datenschutz und Ausfallsicherheit stark eingeschränkt. De Cloud soi daher agnostisch betrieben werdn, um schnöi zwischn
AWS, Azure, Google, On-Premise usw. wechseln und Kostn vergleichen zu können. Grenzen san a in da Cloud oft vorhanden,
wos zu kreativen Workarounds führt, die wiedrum die Komplexität erhöhn. A integratives Testen ko teiar werdn, weil jeder
Entwickler oane eigene Entwicklungsumgebung in da Cloud braucht, weil viele Cloud-Dienste kaum oder gar net lokal
testbar san. Oba a ohne Tests is de Cloud teier. Während bei On-Premise Systemen vor allem Hardwarekostn anfallen, muss
in da Cloud zusätzlich für Traffic, a paar Standard Services und oft sogoa für de Mehrfachbesteiarung bezohlt werdn.
Außerdem verliert man in da Cloud leichn den Überblick, weil's net um Benutzerfreindlichkeit geht, sondern ums Geld. Die
Kostn san so versteckt, dass man sie erst bemerkt, wenn's schon z'spät is. Die Grundlagn der Architektur und
Infrastruktur müssen in da Cloud und insbesondere im Bereich der Serverless neu erfundn werdn, weil de Implementierung
stark von de verfügbarn Funktionen abhängt. Immer nochn Konzeptdesign denk i ma: "Olles, wos ich do mach, hätt a oana
alleiniger Service sei könn." Für mi is Serverless a interissant's Idee und es is guat skalierbar, oba's senkt net de
Kostn. Im Gegenteil, es foat vui mehra Wissn und Zeit in da Entwicklung. Serverless oder de Cloud foarnd Disziplin und
Vorwissen. Wenn a oan Wissn fia On-Premise-Systeme net vorhandn ist, werd's mit da Cloud net einfacher. Wia solln sich
Entwickler zusätzlich Infrastrukturwissn aneignen? I dad an guat gemanagtn Kubernetes Cluster da Cloud Architektur
vorzeihen. De Mitarbeiter skalieren net. Vüle Entwickler hobn ka Disziplin im Code schreibn. Leida trifft's auf 80
Prozent der Entwickler zu. Wia solln diese Entwickler dann no de Cloud bedien'n könna? Es is wichtig, dass Unternehmen
die Herausforderungen und Auswirkungen der Serverlosn Architektur und da Cloud umfassend verstehn. Des erfordert net nur
technisches Wissn, sondern a a strategischen Ansatz. A unüberlegte Migration in de Cloud ko zu Komplexität, höheren
Kostn und Überforderung der Entwickler führen. Zusammnfasst gsoch, dass Serverless in the Cloud a vielversprechend's
Konzept is, das jodoch sorgfältig betrachtet werd'n sollt. Kostn, Komplexität, Wartbarkeit und de Fähigkeiten des
Entwicklungsteams müssen berücksichtigt werd'n. Jedes Unternehmen hot ondre Anforderungen und Prioritäten. Man sollt a
fundierte Entscheidung treffen, ob Serverless in da Cloud die rechte Lösn is oder ob alternative Ansätze wia z.B. guate
Kubernetes Cluster de bessere Wahl sein. Da erfolgreiche Einsatz von Serverless und Cloud Computing erfordert a
Kombination aus technischer Expertise strategischer Planung und a klaren Verständnis der Geschäftsanforderungen. Nur so
ko ma de Illusion von Serverless durchschauen und de richtige Entscheidung für die eigene Softwareentwicklung treffen.

### Resumee

Die Einfirührung von Serverless-Funktione in da Cloud wersetzt Flexibilität, Scholierborkeit und Entlastung von
Entwicklern in Infrastrukturaufgoben. Doch von dera Illusione sollte man si gleiße net blosn lossn. Die Umstellig in da
Cloud und de Nutzung von Serverless-Funktione bringt a Riehe von Herausforderungen mit sich. Entwickler missn neb'm
eigentlichen Entwicklung a neie "Sprache" lossn und ohne entsprechnde Unterstiznng meahr Verantwortung übernehm. Die
Komplixität von Serverless-Funktione ist oft heihar os die von Microservices, weil Entwickler vüle zusätzlige Aufgobn
wie Infrastrukturdifinizione, Sicherheit und Scholierung overnehm missn. Echte integrative Teschte sein schwierig und
das Vorwissen sowie die Erfahrung fürn Betrieb sein in da Cloud noch wichtige. Die Cloud selbst bringt weidere
Herausforderungen mit sich. Vüle Cloud-Technologie sein net aufm neischtm Stand und de Nutzung moderner Standarddienste
kann tia oder sogar unmglich sein. Regulatorische Vorgaben, Compliance und Datenschutz schränkenn da Spielrum ein. Zudem
laffen overall di Koschn in da Cloud leicht ausm Ruder und der Überblick über de Ausgaben geht schnell verlor'n.
Insgeosamt gilts abzuwägen, was fürs Unternehmen Vor- und Nachteile von Serverless und Cloud sein. Unternehmen sollten
ihre spezifischen Anforderungen, das vorhondene Know-how im Team und die langfristigen Auswirkungen von a Migration in
die Cloud bedenken. Eine fundierte Entscheidung auf Basis von a umfassenden Analyse is entscheidend für den Erfolg und
die Rentabilität vom Projekt. Letztendlich ligt es an den Unternehmen, ihre Entwickler angemessen zu unterstützen, de
Koschn und Komplixität von da Cloud realistisch einzuschätz und alternative Lösungen wie gut verwalte Kubernetes-
Klauster in Betracht zu zieng. Mit a klaren Strategie und a fundiertn Verständnis von de eigenen Bedürfnisse können
Unternehmen de Vorteile von da Cloud und Serverless-Funktione optimal nutzen und die Illusione durchschauen.

### Kontakt

Kontakt aufnehman kinnst du dahier:
- Telefoun: 123456789
- E-Mail: office@example.com
- Adrass: Mustergass 123, 12345 Beispueltid

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
