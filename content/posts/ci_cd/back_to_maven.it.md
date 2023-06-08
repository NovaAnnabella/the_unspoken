---
title: "Tornare a Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "La ricerca sfuggente della semplicità e un breve viaggio alla riscoperta del potere di Maven."
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# Tornando a Maven?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/tornando-a-maven-da-gradle/)

## 10 anni di Gradle. Alla ricerca del sollievo e un breve viaggio alla riscoperta della forza di Maven.

Mi dispiace, ma non è possibile tradurre un testo vuoto o costituito solamente da codice di formattazione come il
markdown. Si prega di fornire un testo effettivo da tradurre.

### Massimizzazione del potenziale degli sviluppatori - Abbiamo bisogno di più strumenti che risparmiano tempo

Gli argomenti spesso trascurati o raramente discussi mi interessano. Spesso sono in uso tecnologie cool, ma pochissimi
parlano dei problemi ad esse associati. Lo sviluppo è diventato molto complesso ai giorni nostri. Con buzzword come
"Serverless", "Low Code", "IaC", "Big Data", "Cloud", "DevOps", "You Build it You run it" e così via, i programmatori
hanno già abbastanza compiti aggiuntivi da gestire. Più compiti significano meno esperti e sempre qualcosa viene
trascurato. Quindi, le automazioni e il risparmio di tempo sono estremamente importanti. "Don't make me think" e "Works
out of the Box" sono già dei buoni indicatori di qualità che non riesco ancora a vedere in Gradle. Ad essere onesti,
Gradle non è l'unico strumento moderno che ci dà lavoro invece di rendercelo più facile.

### La ricerca illusoria di semplicità e automazione

Da SOAP ho un profondo avversione per le configurazioni basate su XML. Con Gradle, avevo sperato che scrivere gli script
di bind sarebbe stato un gioco da ragazzi. Purtroppo, le mie speranze e la mia motivazione sono diminuite di volta in
volta. Gradle mira alla flessibilità e sacrifica l'automazione e la qualità in tal senso. Gli sviluppatori seguono
ciecamente la tendenza senza preoccuparsi delle conseguenze sulla affidabilità del software. Per mantenere semplici e
facili da mantenere gli script di build di Gradle, è necessaria una forte disciplina. Una tale disciplina è già rara nel
codice sorgente e quindi molto più rara negli script di build.

### Traduzioni e soluzioni alternative - quando gli script di compilazione diventano una sfida

Gradle non lavora molto diversamente da Maven sullo sfondo. Pertanto, alcune traduzioni sono necessarie. Caratteristiche
come il Catalogo di Dipendenza, il Plugin Rilascio Maven, Dependabot e molti altri sono effettivamente soluzioni
alternative per le funzionalità di base che Maven ha già. Con la flessibilità di Gradle, spesso si creano configurazioni
di compilazione complesse e difficili da mantenere. I plugin di Gradle spesso presentano problemi di compatibilità,
limiti o sviluppi limitati. Questi problemi derivano dalla natura in evoluzione dell'ecosistema di Gradle, dalla
diversità degli ambienti in cui Gradle viene utilizzato e dalla specifica implementazione e manutenzione richiesta per
ogni plugin. Tutto è collegato.

### L'effetto domino di Gradle - Uno scenario da incubo nel mondo reale

Ho visto molti Microservizi che avevano solo pochi anni e che non erano più gestibili a causa di Gradle. È importante
notare che non è la prima volta che vedo una cosa del genere e no, non erano sviluppatori Junior.

Il mio **compito era di effettuare un upgrade di Spring Boot 2.x a 2.7**. Spoiler: mi sono arreso dopo un anno!
I problemi in breve:

* Il file di costruzione di Gradle richiede -> il downgrade della mia versione locale di Java a 11 (WTF) (di solito Java è
  retrocompatibile - ci sono anche strumenti di lavoro alternativi come SdkMan...)
* L'aggiornamento di Spring Boot richiede -> l'aggiornamento di Gradle (WTF)
* L'aggiornamento di Gradle richiede -> l'aggiornamento del plugin
* L'aggiornamento del plugin richiede -> l'aggiornamento di Groovy (WTF)
* L'aggiornamento di Groovy richiede -> l'aggiornamento del Framework di Test e gli aggiornamenti per i test (WTF)
* L'aggiornamento del Framework di Test richiede -> Aggiornamenti di Dipendenze
* \[...]
  Inoltre, alcuni plugin non funzionano con versioni più recenti di Gradle, alcuni non sono più sviluppati, sono
  incompatibili con altri plugin, funzionano solo con Gradle KTS, non con Gradle Groovy o hanno semplicemente dei
  limiti. Anche i plugin di grandi fornitori come Spring hanno funzionalità limitate rispetto ai loro plugin Maven. Alla fine,
  ho un file di costruzione breve e figo di Gradle, che nessuno può gestire correttamente, nemmeno gli sviluppatori che lo
  hanno scritto, e ancora adorano Gradle. Conosco solo poche persone che capiscono seriamente i Gradle Scripts o che sono in grado di scriverli.

### La riscoperta della forza di Maven - Sfruttare i poteri magici di Maven

Ecco le mie funzionalità preferite di Maven:
I plugin possono essere avviati e configurati direttamente dalla riga di comando senza essere definiti in precedenza e sono in gran parte indipendenti dalle altre configurazioni dei plugin.

| Comando di esempio | Descrizione | Link |
| ------------------ | ------------------------------------------------- | ------------------------------------------------- |
| `mvn versions:use -latest-versions`   | Aggiorna le versioni - chi ha bisogno di Dependabot? Sì, i miei progetti sono stati aggiornati alla versione più recente senza fastidiose richieste di merge per anni | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion = 1.0.0` | Imposta la versione del progetto ...                                                                                                                              | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`         | Elencare le dipendenze e mostrare le loro licenze (può persino fallire con licenze escluse)  | https://www.mojohaus.org/license-maven-plugin/index.html                 |

Questa lista potrebbe continuare all'infinito. Mi ricorda un po' le operazioni di flusso di lavoro su GitHub.

![maven_plugin_command_line_args] (/images/content/maven_plugin_command_line_args.png)

### Non ti piace XML?

Nessun problema! Basta scrivere il tuo Build File in `ruby`, `groovy`, `scala`, `yaml`, `atom` o `Java`. L'Extension Polyglot (https://github.com/takari/polyglot-maven) lo rende possibile. Per provare basta eseguire `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` e in pochi millisecondi il tuo Build File è tradotto. Peccato che non ci sia un traduttore affidabile Maven <> Gradle :( Sì, i file di build di Maven sono grandi, ma anche molto comprensibili. Le modifiche o il debug sono fatti in un battibaleno.

### L'età è solo un numero - Stabilità ed evoluzione dei Mavens

Ammettiamolo, Maven esiste già da un po' e la sua estetica potrebbe non corrispondere agli standard odierni. Tuttavia, la longevità di Maven ha permesso di adattarsi e di evolversi. Maven lavora in modo indipendente dal tuo progetto. I file di build possono essere facilmente riutilizzati. Le plug-in funzionano all'interno di una sandbox e sono indipendenti l'una dall'altra e indifferenti alla versione di Java o di Maven. Questo design favorisce la stabilità e la prevedibilità e rende facile gestire processi di build complessi senza conflitti imprevisti.

### Conclusion

Oggi, l'ambiente di sviluppo è sovraccarico di molte attività e tecnologie per gli sviluppatori. Alla ricerca di
semplicità e automazione, Gradle è emerso come moderno strumento di compilazione, ma ha portato con sé le sue sfide.
Senza dubbio, il concetto di Gradle è buono! Tuttavia, considerando la complessità e il tempo investito negli script di
compilazione di Gradle, sorge la domanda se non sarebbe più facile estendere Maven. Con plugin ed estensioni, Maven
potrebbe essere costantemente rinnovato e semplificato. Non sarebbe sviluppare Maven ulteriormente più eccitante e
duraturo che passare da una tecnologia all'altra?

### Collegamenti

* [Tornare da Gradle a Maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### Contatti

[Problemi di GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
