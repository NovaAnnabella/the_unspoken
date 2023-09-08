---
title: "Torna a Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "La ricerca sfuggente della semplicità e un breve viaggio per riscoprire il potere di Maven"
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# Ritorno a Maven?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

## 10 anni di Gradle. Alla ricerca di sollievo e un breve viaggio per riscoprire la forza di Maven.

You haven't provided any text to translate. Please provide the text you want translated into Italian.

### Massimizzazione del potenziale degli sviluppatori - Abbiamo bisogno di più strumenti che risparmiano tempo

Temi che vengono spesso trascurati o raramente discussi mi interessano. Spesso vengono utilizzate tecnologie
interessanti, ma pochi ne parlano dei problemi ad esse associati. Lo sviluppo è diventato molto impegnativo al giorno
d'oggi. Con i moderni buzzword come “Serverless”, “Low Code”, “IaC”, “Big Data”, “Cloud”, “DevOps”, “You Build it You
run it” ecc. gli sviluppatori hanno già abbastanza compiti aggiuntivi da gestire. Più compiti, significa che ci sono
pochi esperti e qualcosa viene sempre trascurato per il focus. Pertanto, le automazioni e il risparmio di tempo sono
molto importanti. “Non farmi pensare” e “Funziona direttamente fuori dalla scatola” sono già buoni indicatori di qualità
che non posso vedere ancora in Gradle. Per essere giusti, Gradle non è l'unico strumento moderno che ci dà lavoro invece
di semplificarlo.

### La ricerca illusoria di semplicità e automazione

Da SOAP, ho sviluppato un'avversione radicata per le configurazioni basate su XML. Con Gradle, speravo che la scrittura
degli script di binding fosse un gioco da ragazzi. Purtroppo, le mie speranze e la mia motivazione si sono ridotte di
volta in volta. Gradle mira alla flessibilità e sacrifica per questo l'automazione e la qualità. Gli sviluppatori
seguono ciecamente la tendenza senza considerare l'impatto sulla affidabilità del software. Per mantenere gli script di
build Gradle semplici e a bassa manutenzione, è necessaria una forte disciplina. Tale disciplina è rara nel codice
sorgente ed è quindi ancora più rara negli script di build.

### Traduzioni e soluzioni temporanee - Quando gli script di Build diventano una sfida

Gradle non lavora molto diversamente da Maven in background. Pertanto, sono necessarie alcune traduzioni.
Caratteristiche come il Catalogo delle dipendenze, il Plugin di rilascio Maven, Dependabot e molti altri sono in realtà
soluzioni alternative per le funzionalità di base che Maven già fornisce. Con la flessibilità di Gradle spesso emergono
configurazioni di compilazione complesse, che sono difficili da mantenere. I plugin Gradle hanno spesso problemi di
compatibilità, limiti o sviluppi limitati. Questi problemi sorgono a causa della natura in continua evoluzione
dell'ecosistema Gradle, la varietà di ambienti in cui Gradle viene utilizzato e lo specifico sforzo di implementazione e
manutenzione per ogni plugin. Tutto è interconnesso.
