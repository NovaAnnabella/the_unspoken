---
title: "Torna a Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "La sfuggente ricerca della semplicità e un breve viaggio per riscoprire il potere di Maven."
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# Tornare a Maven?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

## 10 anni di Gradle. Alla ricerca di sollievo e un breve viaggio per riscoprire la forza di Maven.



### Massimizzazione del potenziale degli sviluppatori - Abbiamo bisogno di più strumenti che risparmiano tempo

Argomenti che vengono spesso trascurati o raramente discussi mi interessano. Spesso ci sono tecnologie fantastiche in
uso, ma quasi nessuno parla dei problemi ad esse collegati. Lo sviluppo è diventato molto complesso oggigiorno. Con le
fresche parole d'ordine come "Serverless", "Low Code", "IaC", "Big Data", "Cloud", "DevOps", "You Build it You run it"
ecc. gli sviluppatori hanno già più che abbastanza compiti aggiuntivi da svolgere. Più compiti, significa che ci sono a
malapena gli esperti rimasti e sempre qualcosa viene trascurato per il focus. Quindi automazioni e risparmi di tempo
sono mega importanti. "Don't make me think" e "Works out of the Box" sono già buoni indicatori di qualità che non vedo
ancora in Gradle. Per essere giusti, Gradle non è l'unico strumento moderno che ci dà lavoro, invece di semplificarlo.

### La illusoria ricerca di semplicità e automazione

Dall'epoca di SOAP, ho sviluppato un'antipatia radicata per le configurazioni basate su XML. Con Gradle, speravo che
scrivere script di binding sarebbe stato un gioco da ragazzi. Sfortunatamente, le mie speranze e la mia motivazione sono
dimate a poco a poco. Gradle cerca la flessibilità a scapito dell'automazione e della qualità. Gli sviluppatori e
sviluppatrici seguono ciecamente la tendenza senza considerare le implicazioni sulla affidabilità del software. Per
mantenere gli script di build di Gradle semplici e a bassa manutenzione, è necessaria una forte disciplina. Tale
disciplina è già rara nel codice sorgente, quindi è ancora più rara negli script di build.

### Traduzioni e soluzioni alternative - Quando gli script di build diventano una sfida

Gradle non funziona molto diversamente in background rispetto a Maven. Pertanto, sono necessarie alcune traduzioni. Le
funzionalità come il Catalogo di dipendenze, il Plugin di rilascio Maven, il Dependabot e molti altri sono in realtà
soluzioni alternative per le funzioni di base che Maven offre già. Con la flessibilità di Gradle spesso si creano
configurazioni di build complesse, che sono difficili da mantenere. I plugin Gradle hanno spesso problemi di
compatibilità, limiti o sviluppi limitati. Questi problemi si verificano a causa della natura in continua evoluzione
dell'ecosistema Gradle, della varietà di ambienti in cui Gradle è utilizzato e dello specifico impegno di
implementazione e manutenzione per ogni plugin. Tutto è collegato.

### L'effetto domino di Gradle - Uno scenario da incubo nel mondo reale

Ho visto molti microservizi che avevano solo pochi anni e già non erano più gestibili a causa di Gradle. È importante menzionare che questa non è la prima volta che vedo una cosa del genere, e no, non erano
Junior Devs.

Il mio **compito era eseguire un aggiornamento da Spring Boot 2.x a 2.7**. Spoiler: ho rinunciato dopo un anno
! I problemi in breve:

* Il file di build Gradle richiede -> downgrade della mia versione locale di Java a 11 (WTF) (Di solito Java
  è retrocompatibile - ci sono anche strumenti di risoluzione alternativi come SdkMan...)
* L'aggiornamento di Spring Boot richiede -> Aggiornamento di Gradle (WTF)
* L'aggiornamento di Gradle richiede -> Aggiornamento del plugin
* L'aggiornamento del plugin richiede -> Aggiornamento di Groovy (WTF)
* L'aggiornamento di Groovy richiede -> Aggiornamenti del framework di test e dei test (WTF)
* L'aggiornamento del framework di test richiede -> aggiornamenti delle dipendenze
* \[...]
  Inoltre, alcuni plugin non funzionano con versioni più recenti di Gradle, alcuni non sono più sviluppati,
  sono incompatibili con altri plugin, funzionano solo con Gradle KTS, non con Gradle Groovy, o
  hanno semplici limiti. Perfino i plugin di grandi fornitori come Spring hanno una funzionalità limitata rispetto ai loro plugin Maven.
  Alla fine, ho un bel file di build Gradle corto che nessuno può davvero manutenere,
  nemmeno gli sviluppatori che lo hanno scritto, e amano ancora Gradle. Conosco solo poche persone che
  possono davvero capire o scrivere script Gradle.

### La riscoperta della forza di Maven - Utilizzare i poteri magici di Maven

Ecco le mie funzioni preferite di Maven:
I plugin possono essere avviati e configurati direttamente dalla riga di comando, senza doverli definire in anticipo. 
Inoltre, sono in gran parte indipendenti da altre configurazioni del plugin.

| Comando di esempio                    | Descrizione                                                                                                                                                        | Link                                                                     | 
|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`   | Aggiorna le versioni - chi ha bisogno di Dependabot? Sì, i miei progetti vengono aggiornati senza problemi all'ultima versione da anni, senza fastidiose richieste di unione | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0` | Impostare la versione del progetto...                                                                                                                              | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`         | Elencare le dipendenze e mostrare le loro licenze (può persino fallire nelle licenze escluse)                                                                      | https://www.mojohaus.org/license-maven-plugin/index.html                 | 

Questa lista potrebbe continuare all'infinito. Mi ricorda in qualche modo i passaggi del flusso di lavoro di GitHub.

![maven_plugin_command_line_args](/immagini/contenuto/maven_plugin_command_line_args.png)

### Non ti piace XML?

Nessun problema! Scrivi semplicemente il tuo file di Build in `ruby`, `groovy`, `scala`, `yaml`, `atom` o `Java`. L'estensione Polygot (https://github.com/takari/polyglot-maven) lo rende possibile. Per provarlo, esegui semplicemente `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` e in pochi millisecondi il tuo file di Build è tradotto. Peccato che non ci sia un traduttore affidabile Maven <> Gradle :(

Sì, i file di Build Maven sono grandi, ma anche molto facili da capire. Miglioramenti o debugging sono fatti in un baleno.

### L'età è solo un numero - Stabilità ed evoluzione di Maven

Certo, Maven esiste da un bel po' di tempo e la sua estetica potrebbe non rispettare gli standard di oggi. Tuttavia, la
longevità di Maven ha permesso di adattarsi e svilupparsi. Maven funziona indipendentemente dal tuo progetto. I file di
build possono essere facilmente riutilizzati. I plugin funzionano in un sandbox e sono indipendenti l'uno dall'altro e
indipendenti dalla versione di Java o Maven. Questo design promuove la stabilità e la prevedibilità e rende facile
gestire processi di build complessi senza inaspettati conflitti.

### Conclusione

Oggi l'ambiente di sviluppo è sovraccarico di molte attività e tecnologie per gli sviluppatori. Nella ricerca di
semplicità e automazione, Gradle è emerso come un moderno strumento di compilazione, ma ha portato con sé i suoi sfide.
Senza dubbio, il concetto di Gradle è buono! Tuttavia, data la complessità e il tempo investito negli script di
compilazione Gradle, sorge la domanda se non sarebbe più semplice estendere Maven a invece. Con plugin ed estensioni,
Maven potrebbe essere rinfrescato e semplificato in qualsiasi momento. Non sarebbe più interessante ed anche più
sostenibile, evolvere piuttosto che saltare da una tecnologia all'altra?

### Link

* [Tornando indietro da Gradle a maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### Contatto

[Problemi GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
