---
title: "Tornare a Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "La ricerca sfuggente della semplicità e un breve viaggio alla riscoperta del potere di Maven"
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# Tornare a Maven?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)


```

## 10 anni di Gradle. Alla ricerca di un sollievo e un breve viaggio alla riscoperta della forza di Maven.

Mi dispiace, ma non c'è testo markdown da tradurre. Puoi fornirmi un testo markdown specifico da tradurre in italiano?

### Massimizzazione del potenziale degli sviluppatori - abbiamo bisogno di strumenti che risparmiano tempo

Argomenti spesso trascurati o raramente discussi mi interessano. Spesso vengono utilizzate tecnologie interessanti, ma
pochi parlano dei relativi problemi. Lo sviluppo oggi è diventato molto impegnativo. Con parole alla moda come
"Serverless", "Low Code", "IaC", "Big Data", "Cloud", "DevOps", "You Build it You run it", gli sviluppatori hanno già
abbastanza compiti accessori da gestire. Più compiti significano che ci sono sempre meno esperti e che verrà trascurato
qualcosa per concentrarsi su altro. Pertanto, l'automazione e il risparmio di tempo sono importantissimi. "Don't make me
think" e "Works out of the Box" sono già buoni indicatori di qualità che non riesco ancora a vedere in Gradle. Ad essere
onesti, Gradle non è l'unico strumento moderno che ci crea lavoro invece di facilitarcelo.

### La ricerca illusoria di semplicità e automazione

Da SOAP ho una forte antipatia per le configurazioni basate su XML. Con Gradle avevo sperato che la scrittura di script
di associazione sarebbe stata una passeggiata. Purtroppo, le mie speranze e la mia motivazione sono diminuite di volta
in volta. Gradle mira alla flessibilità sacrificando l'automatizzazione e la qualità. Gli sviluppatori seguono
ciecamente la tendenza, senza considerare gli effetti sulla affidabilità del software. Per mantenere i script di
compilazione di Gradle semplici e facilmente manutenibili, è necessaria una forte disciplina. Una disciplina del genere
è già rara nel codice sorgente e quindi ancora più rara negli script di compilazione.

### Traduzioni e soluzioni alternative - Quando gli script di build rappresentano una sfida

Gradle non funziona molto diversamente da Maven in background. Pertanto, alcune traduzioni sono necessarie. Funzionalità come Dependency Catalog, Maven Release Plugin, Dependabot e molte altre sono in realtà work-around per funzioni di base che Maven già fornisce. Con la flessibilità di Gradle, spesso si creano configurazioni di build complesse che sono difficili da mantenere. I plugin di Gradle hanno spesso problemi di compatibilità, limiti o sviluppi limitati. Questi problemi derivano dalla natura in continua evoluzione dell'ecosistema di Gradle, dalla diversità degli ambienti in cui viene utilizzato Gradle e dal costo di implementazione e manutenzione specifico per ogni plugin. Tutto è collegato.

### L'effetto domino di Gradle - Uno scenario da incubo nel mondo reale

Ho visto molti microservizi che avevano appena qualche anno e che erano già diventati impossibili da mantenere a causa di Gradle. Vale la pena menzionare che non è la prima volta che vedo qualcosa del genere e no, non erano sviluppatori junior.

Il mio compito era quello di eseguire un aggiornamento da Spring Boot 2.x a 2.7. Anticipo: dopo un anno ho rinunciato! I problemi in breve:

* Il file di costruzione Gradle richiede -> riduzione della mia versione di Java locale a 11 (WTF) (di solito Java
  è retrocompatibile - ci sono anche qui strumenti di lavoro alternativi come SdkMan...)
* L'aggiornamento di Spring Boot richiede -> aggiornamento di Gradle (WTF)
* L'aggiornamento di Gradle richiede -> Aggiornamento del plugin
* L'aggiornamento del plugin richiede -> Aggiornamento di Groovy (WTF)
* L'aggiornamento di Groovy richiede -> Aggiornamenti del framework di prova e del test (WTF)
* L'aggiornamento del framework di prova richiede -> aggiornamenti delle dipendenze
* \[...]
Inoltre, alcuni plugin non funzionano con le versioni più recenti di Gradle, alcuni non vengono più sviluppati, sono incompatibili con altri plugin, funzionano solo con Gradle KTS, non con Gradle Groovy o hanno semplicemente dei limiti. Anche i plugin di grandi fornitori come Spring hanno funzionalità limitate in confronto ai loro plugin Maven. Alla fine ho una breve e bella file di costruzione Gradle che nessuno può mantenere correttamente, nemmeno gli sviluppatori che l'hanno scritta e che ancora amano Gradle. Conosco solo poche persone che possono realmente capire o scrivere script Gradle.

### La riscoperta della forza di Maven - Sfruttare i poteri magici di Maven

Ecco le mie funzionalità preferite di Maven:
I plugin possono essere avviati e configurati direttamente dalla riga di comando senza doverli definire in precedenza. Inoltre, sono in gran parte indipendenti dalle altre configurazioni dei plugin.

| Comando di esempio                    | Descrizione                                                                                                                                                        | Link                                                                     | 
|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`   | Aggiornamento delle versioni - chi ha bisogno di Dependabot? Sì, i miei progetti vengono aggiornati alla versione più recente senza fastidiosi problemi di merge da anni | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0` | Imposta la versione del progetto ...                                                                                                                                         | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`         | Elenco delle dipendenze e visualizzazione delle relative licenze (può fallire anche con licenze escluse)                                                        | https://www.mojohaus.org/license-maven-plugin/index.html                 | 

Questa lista potrebbe continuare all'infinito. In qualche modo mi ricorda i GitHub Workflow Steps.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

### Non ti piace XML?

Nessun problema! Scrivi semplicemente il tuo file di creazione in `ruby`, `groovy`, `scala`, `yaml`, `atom` o `Java`. L'estensione Polygot (https://github.com/takari/polyglot-maven) lo rende possibile. Per provarlo, esegui semplicemente `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` e il tuo file di creazione sarà tradotto in pochi millisecondi. Peccato che non ci sia un traduttore affidabile da Maven a Gradle :(
Sì, i file di creazione di Maven sono grandi, ma anche molto comprensibili. Gli aggiustamenti o il debug sono fatti in un attimo.

### L'età è solo un numero - La stabilità e l'evoluzione dei Maven

Ammettiamolo, Maven esiste già da un po' di tempo e la sua estetica potrebbe non corrispondere agli standard attuali.
Tuttavia, la durata di Maven ha permesso di adattarsi ed evolversi. Maven lavora indipendentemente dal tuo progetto.
I file di compilazione possono essere facilmente riutilizzati. Le plug-in funzionano in una sandbox e sono indipendenti
l'una dall'altra e indipendenti dalla versione Java o Maven. Questo design promuove la stabilità e la prevedibilità e rende facile gestire
processi di compilazione complessi senza conflitti imprevisti.

### Conclusione

Oggi ambiente di sviluppo è sovrabbondante di compiti e tecnologie per gli sviluppatori. Alla ricerca di semplicità e
automazione, Gradle è emerso come moderno strumento di compilazione, ma ha portato con sé le sue sfide. Senza dubbio, il
concetto di Gradle è buono! Tuttavia, considerando la complessità e il tempo investito negli script di compilazione di
Gradle, sorge la domanda se non sarebbe più semplice estendere Maven. Con plugin ed estensioni, Maven potrebbe essere
rinfrescato e semplificato in qualsiasi momento. Non sarebbe più stimolante e sostenibile sviluppare ulteriormente Maven
piuttosto che saltare da una tecnologia all'altra?

### Collegamenti

* [Tornando indietro da Gradle a Maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### Contatto

[Problemi GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).```
