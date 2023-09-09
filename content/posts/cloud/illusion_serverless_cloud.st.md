---
title: "Illusion Serverless & Wolke"
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

![aws_costs_twitter_1](/images/content/onprem_vs_cloud.png)

### Enleitung

I bin enttäuscht, wie oft des Marketing über den gsunden Menschenverstand siegt. Viele Manager setzen sich
über ihre eigenen Experten - die Entwickler. Des gilt a für die Migration in die Cloud. Spoiler: Wer Geld sparen
muss, sollt die Cloud meiden. Denn des neue Buzzword "Serverless" in der Cloud bedeutet: Du kümmerst dich um die
Software, mir kümmern uns um die Hardware. Wer jedoch einen fähigen, motivierten und neugierigen Administrator hat, der
kann Serverless a selbst betreiben (z.B. [KNative](https://knative.dev)).

![aws_costs_twitter_1](/images/content/aws_costs_twitter_1.png)

### Serverless Funktionen vs Microservices:



#### Mikroservices

A typischer zustandloser Microservice kimmert sich um a bestimmte Funktion/Domäne und wird in aner
Container Orchestrierungsumgebung bereitgstellt. Diese Umgebung kimmert sich um Infrastruktur, Sicherheit, Firewall,
Logging, Metriken, Secrets, Netzwerk, Backups und vieles mehr. A großer Vorteil ist, dass a Microservice lokal mit
wenigen
Ressourcen integriert gtestet werden kann und Cloud-/Server-agnostisch (überall einsetzbar) ist.


#### Serverless Funktionen

A klaner Witz voran: Paradox, ober wahr - Serverless-Funktionen hängen stark von der Serverumgebung ob. :)
A typische Serverless Funktion kimmert sich a glei um lei a bestimmte Funktion/Domäne und werd ohne Frameworks
in
reinem Code gschrieben, um schneller als ein Microservice zu sein (A a guate Übung für MicroServices). A großer
Vorteil isch, dass Serverless Funktionen automatisch skaliert werden. Allerdings benötigt jede Serverless Funktion a
beträchtliche Menge an GlueCode, um die Infrastruktur zu definieren - Security, Firewall, Netzwerk, Logging, Metriken,
Secrets, Caching, Backups und vieles mehr.
Daher kann a einfache Funktion wie das Kopieren einer Datei inklusive API schnell mal 1500 Zeilen Code (inkl. IaC)
umfassen.
Die Administrationskosten verschieben sich von der Administration zur Entwicklung im Verhältnis 1:N (1 zu Serverless
Funktionen). Das Wissen und die Implementierung sind somit nicht mehr
gebündelt und können schnell instabil werden. Hinzu kommen erhöhte Wartungskosten.
Auch echte integrative Tests sind mit Serverless selten oder nur mit großem Aufwand verbunden.
Letztlich isch die Komplexität von Serverless-Funktionen deutlich höher als die eines einzelnen Microservices.
Höhere Komplexität bedeutet auch geringere Wartbarkeit. Neue Teammitglieder haben es schwerer und benötigen deutlich
mehr Vorwissen.

### Serverless und die Cloud im Allgemeinen

De meistn Cloud-Technologien san net auf dem neuesten Stand. Zum Beispiel san Node.js, Java, Python und andere
Sprochen oder Technologien oft net einfach zu aktualisieren, meist hilft nur obwarten.
Auch moderne und Standardtechnologien wie MongoDB, MySQL, Kafka, NATS, RabbitMQ, Redis, Prometheus, InfluxDB, Grafana,
Kibana, Elastic Search etc. san entweder net verfügbar oder überteuert.
Ohne solche Standarddienste befindet man sich oft in der virtuellen Steinzeit und nutzt veraltete Lösungen, z.B.
Webhooks für die Kommunikation nach außen. Hinzu kommt, dass der Handlungsspielraum bei Themen wie Regulierung,
Compliance, Datenschutz und Ausfallsicherheit stark eingeschränkt ist.

Die Cloud sollte daher agnostisch betrieben werden, um schnell zwischen AWS, Azure, Google, On-Premise usw. wechseln und
Kosten vergleichen zu können.
Grenzen san auch in der Cloud häufig vorhanden, was zu kreativen Workarounds führt, die wiederum die Komplexität
erhöhen. Auch integratives Testen kann teuer werden, da jeder Entwickler eine eigene Entwicklungsumgebung in der Cloud
benötigt, da viele Cloud Dienste kaum oder gar net lokal testbar san.
Doch auch ohne Tests ist die Cloud teuer. Während bei On-Premise Systemen vor allem
Hardwarekosten anfallen, muss in der Cloud zusätzlich für Traffic, einige Standard Services und oft sogar für die
Mehrfachbesteuerung bezahlt werden. Zudem verliert man in der Cloud leicht den Überblick, denn es geht net um
Benutzerfreundlichkeit, sondern ums Geld geht. Die Kosten san so versteckt, dass man sie erst bemerkt, wenn es zu spät
ist.

Die Grundlagen der Architektur und Infrastruktur müssen in der Cloud und insbesondere im Bereich der Serverless
neu erfunden werden, da die Implementierung stark von den verfügbaren Funktionen abhängt.
Immer nachdem ich die Architektur designed habe, kommt mir der Gedanke: "Das hätte auch ein einzelner Service sein
können".

Für mich ist Serverless eine interessante Idee und es ist gut skalierbar, aber es senkt net die Kosten. Im
Gegenteil, es erfordert viel mehr Wissen und Zeit in der Entwicklung. Serverless oder die Cloud erfordern Disziplin und
Vorwissen.
Wenn das Wissen für On-Premise-Systeme net vorhanden ist, wird es mit der Cloud net einfacher.
Wie sollen sich Entwickler zusätzlich Infrastrukturwissen aneignen?

Ich würde einen gut gemanagten Kubernetes Cluster der Cloud Architektur vorziehen.
Die Mitarbeiter skalieren net. Viele Entwickler haben keine disziplin im code schreiben.
Leider trifft das auf 80 Prozent der Entwickler zu. Wie also sollen diese Entwickler dann noch die Cloud bedienen
können?

Es ist wichtig, dass Unternehmen die Herausforderungen und Auswirkungen der serverlosen Architektur und der Cloud
umfassend verstehen. Dies erfordert net nur technisches Wissen, sondern auch einen strategischen Ansatz. Eine
unüberlegte Migration in die Cloud kann zu Komplexität, höheren Kosten und Überforderung der Entwickler führen.

Zusammenfassend lässt sich sagen, dass Serverless in the Cloud ein vielversprechendes Konzept ist, das jedoch sorgfältig
betrachtet werden sollte. Kosten, Komplexität, Wartbarkeit und die Fähigkeiten des Entwicklungsteams müssen
berücksichtigt werden.
Jedes Unternehmen hat andere Anforderungen und Prioritäten. Man sollte eine fundierte Entscheidung treffen, ob
Serverless in der Cloud die richtige Lösung ist oder ob alternative Ansätze wie
z.B. gut Kubernetes Cluster die bessere Wahl san.

Der erfolgreiche Einsatz von Serverless und Cloud Computing erfordert eine Kombination aus technischer Expertise
strategischer Planung und einem klaren Verständnis der Geschäftsanforderungen. Nur so kann die Illusion von Serverless
durchschauen und die richtige Entscheidung für die eigene Softwareentwicklung treffen.


### Konklusion

De Eafiarung vo Serverless-Funktionen in der Cloud vaspricht Flexibilität, Skalierbarkeit und Entlastung vo
Entwickler vo Infrastrukturaufgaben. Vo dieser Illusion sollte man sich jedoch neet blenden lossen. De
Wechsel in de Cloud und de Nutzung vo Serverless-Funktionen bringt a Reihe vo Herausforderungen mit sich.

Entwickler musn neba der eigentlichen Entwicklung a neue "Sprache" lernen und ohne entsprechende Unterstützung
meha Verantwortung übernehmen.
Die Komplexität vo Serverless-Funktionen is oft höher als die vo Microservices, do Entwickler veele zusätzliche
Aufgaben wie Infrastrukturdefinition, Sicherheit und Skalierung übernehmen miasn. Echte integrative Tests sind
schwierig und das Vorwissen sowie die Erfahrung für den Betrieb sind in der Cloud no wichtiger.

De Cloud selbst bringt weite Herausforderungen mit sich. Veele Cloud-Technologien sind nit auf dem neuesten Stand
und de Nutzung moderner Standarddienste kann teuer oda sogar unmöglich sein. Regulatorische Vorgaben, Compliance und
Datenschutz schränken den Spielraum ein. Zudem laufen de Kosten in der Cloud leicht aus dem Ruder,
und der Überblick üba de Ausgaben geht schnell verloren.

Insgesamt gilt es, die Vor- und Nachteile vo Serverless und Cloud sorgfältig abzuwägen.
Unternehmen sollten ihre spezifischen Anforderungen, das vorhandene Know-how im Team und die langfristigen Auswirkungen
einer Migration in die Cloud berücksichtigen.
A fundierte Entscheidung auf Basis einer umfassenden Analyse is entscheidend für den Erfolg und die Rentabilität
des Projekts.

Letztendlich liegt es an den Unternehmen, ihre Entwickler angemessen zu unterstützen, die Kosten und Komplexität der
Cloud realistisch einzuschätzen und alternative Lösungen wie gut verwaltete Kubernetes-Cluster in Betracht zu ziehen.
Mit einer klaren Strategie und einem fundierten Verständnis der eigenen Bedürfnisse können Unternehmen die Vorteile der
Cloud und Serverless-Funktionen optimal nutzen und die Illusion durchschauen.

### Kontakt

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
