---
title: "Tornare a Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "L'inafferrabile ricerca della semplicità e un breve viaggio alla riscoperta della potenza di Maven".
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---



# Tornare a Maven?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

## 10 anni di Gradle. Alla ricerca di sollievo e di un breve viaggio per riscoprire la potenza di Maven.



### Massimizzare il potenziale degli sviluppatori: servono più strumenti per risparmiare tempo

Gli argomenti spesso trascurati o raramente discussi mi interessano. Spesso vengono utilizzate tecnologie interessanti,
ma quasi nessuno parla dei problemi ad esse associati. Lo sviluppo è diventato molto costoso al giorno d'oggi. Con
parole d'ordine come "serverless", "low code", "IaC", "big data", "cloud", "DevOps", "you build it you run it", ecc.
eccetera, gli sviluppatori hanno già più che sufficienti compiti aggiuntivi da affrontare. Un maggior numero di compiti
significa che non ci sono quasi esperti e qualcosa viene sempre trascurato per concentrarsi. Ecco perché l'automazione e
il risparmio di tempo sono mega importante. "Non farmi pensare" e "Works out of the Box" sono già caratteristiche di
buona qualità che non vedo ancora in Gradle. non si vedono ancora. Per essere onesti, Gradle non è l'unico strumento
moderno che rende il nostro lavoro più semplice. semplificarlo.

### L'illusoria ricerca della semplicità e dell'automazione

Fin dai tempi di SOAP, ho avuto una radicata avversione per le configurazioni basate su XML. Con Gradle, speravo che che
scrivere script di bind sarebbe stato un gioco da ragazzi. Purtroppo, le mie speranze e la mia motivazione sono
diminuite diminuiscono ogni volta. Gradle punta alla flessibilità e per questo sacrifica l'automazione e la qualità. Gli
sviluppatori seguono ciecamente la Gli sviluppatori seguono ciecamente la tendenza senza considerare l'impatto
sull'affidabilità del software. Per rendere Gradle script di build semplici e a bassa manutenzione richiede una forte
disciplina. Tale disciplina è già rara nel codice sorgente e quindi è ancora più rara negli script di compilazione.

### Traduzioni e soluzioni - Quando gli script di compilazione diventano una sfida

Gradle non funziona in modo molto diverso in background rispetto a Maven. Pertanto, sono necessarie alcune traduzioni.
Funzionalità come il catalogo delle dipendenze, il Maven Release Plugin, il Dependabot e molte altre sono in realtà dei
workaround per le funzioni di base che Maven già offre. funzioni di base che Maven già offre. La flessibilità di Gradle
è spesso accompagnata da complesse configurazioni di build, che sono difficili da mantenere. I plugin di Gradle hanno
spesso problemi di compatibilità, limiti o progressi limitati. Questi problemi sorgono a causa della natura evolutiva
dell'ecosistema Gradle, della diversità degli ambienti in cui Gradle viene e lo sforzo specifico di implementazione e
manutenzione richiesto per ogni plugin. Tutto è interconnesso.

### L'effetto domino di Gradle - Uno scenario da incubo nel mondo reale

Ho visto molti microservizi che avevano solo pochi anni e già non erano più mantenibili a causa di Gradle. a causa di
Gradle. È importante sottolineare che non è la prima volta che vedo qualcosa di simile, e no, non erano Giovani
sviluppatori. Il mio **compito era quello di eseguire un aggiornamento di Spring Boot da 2.x a 2.7**. Spoiler: Ho
rinunciato dopo un anno Ho rinunciato! I problemi in breve: * Il file di compilazione di Gradle richiede -> il
downgrade della mia versione locale di Java alla 11 (WTF) (Normalmente Java è  compatibile con la versione precedente -
ancora una volta, ci sono strumenti di workaround come SdkMan...) * L'aggiornamento di Spring Boot richiede ->
Aggiornamento di Gradle (WTF) * L'aggiornamento di Gradle richiede l'aggiornamento dei plugin. * L'aggiornamento del
plugin richiede l'aggiornamento di Groovy (WTF) * L'aggiornamento di Groovy richiede -> Aggiornamenti del framework di
test e dei test (WTF) * L'aggiornamento del framework di test richiede -> Aggiornamenti delle dipendenze. * \[...]
Inoltre, alcuni plugin non funzionano con le versioni di Gradle più recenti, alcuni non sono più sviluppati, alcuni sono
incompatibili con altre versioni di Gradle, alcuni non sono più sviluppati, alcuni sono incompatibili con altre versioni
di Gradle.  sono incompatibili con altri plugin, funzionano solo con Gradle KTS, non con Gradle Groovy, o semplicemente
hanno dei limiti.  hanno semplicemente dei limiti. Anche i plugin di grandi produttori come Spring hanno funzionalità
limitate rispetto ai loro plugin Maven.  funzionalità limitate. Mi ritrovo con un file di build Gradle bello e corto,
che nessuno è in grado di mantenere,  nemmeno gli sviluppatori che l'hanno scritto, che comunque amano Gradle. Conosco
pochissime persone che  che capiscono seriamente gli script di Gradle e che li scrivono.

### Riscoprire il potere di Maven - Sfruttare la magia di Maven

Ecco le mie caratteristiche preferite di Maven: I plugin possono essere avviati e configurati direttamente dalla riga di
comando, senza doverli definire prima. devono essere definiti. Inoltre, sono largamente indipendenti dalle
configurazioni degli altri plugin. | Esempio Comando | Descrizione | Link | |---------------------------------------|--
------------------------------------------------------------------------------------------------------------------------
-------------------------------------------|--------------------------------------------------------------------------|
| `mvn versions:use -latest-versions` | Aggiornare le versioni - chi ha bisogno di Dependabot? Sì, i miei progetti sono
stati aggiornati all'ultima versione per anni senza problemi e senza fastidiose richieste di unione |
https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html | | `mvn versions:set -DnewVersion=1.0.0` |
Imposta la versione del progetto...
| https://www.mojohaus.org/versions/versions-maven-plugin/index.html | | `mvn license:add-third-party` | Elenca le
dipendenze e mostra le loro licenze (può fallire anche se le licenze sono escluse) | https://www.mojohaus.org/license-
maven-plugin/index.html | Questo elenco potrebbe continuare all'infinito. Mi ricorda un po' i passi del flusso di
lavoro di GitHub. ![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

### Non ti piace XML?

Nessun problema! Basta scrivere il file di compilazione in `ruby`, `groovy`, `scala`, `yaml`, `atom` o `Java`.
L'estensione Polygot Extension (https://github.com/takari/polyglot-maven) lo rende possibile. Per provarla è sufficiente
eseguire `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` e in pochi
millisecondi il file di compilazione sarà millisecondi il file di build viene tradotto. È un peccato che non ci sia un
traduttore Maven <> Gradle affidabile. :( Sì, i file di build di Maven sono grandi, ma anche molto facili da capire. I
perfezionamenti o il debugging si fanno in un attimo. fatto.

### L'età è solo un numero: la stabilità e l'evoluzione di Maven

Certo, Maven esiste da molto tempo e la sua estetica potrebbe non soddisfare gli standard odierni. Tuttavia, la
longevità di Maven gli ha permesso di adattarsi ed evolversi. Maven funziona in modo indipendente dal progetto. I file
di build possono essere facilmente riutilizzati. I plugin vengono eseguiti in una sandbox e sono indipendenti l'uno
dall'altro e dalla versione di Java o Maven. Questo design favorisce la stabilità e la prevedibilità e facilita la
gestione di processi di compilazione complessi senza conflitti inaspettati. conflitti imprevisti.

### Fazit

Al giorno d'oggi, l'ambiente di sviluppo è sovraccarico di numerosi compiti e tecnologie per gli sviluppatori. Nella
ricerca di semplicità e automazione, Gradle è emerso come uno strumento di compilazione moderno, ma ha portato con sé le
sue sfide. Senza dubbio, il concetto di Gradle è buono! Ma data la complessità e il tempo tempo investito negli script
di compilazione di Gradle, ci si chiede se non sarebbe più semplice estendere Maven. esteso. Con plugin ed estensioni,
Maven potrebbe essere sempre aggiornato e semplificato. Non sarebbe un Lo sviluppo ulteriore non sarebbe molto più
eccitante e anche più sostenibile che saltare da una tecnologia all'altra?

### Collegamenti

* [Ritorno da Gradle a maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### Contatto

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
