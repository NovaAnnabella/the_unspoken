---
title: "Serverless Illusion & Cloud"
date: 2023-05-24
author: "Nova Annabella"
slug: illusion_serverless_cloud
tags: [ Development, Serverless, Cloud, Microservices, Scalability, Architecture, Infrastructure ]
categories: [ Technology, Software, Cloud ]
description: "Sfide e realtà delle funzioni serverless nel cloud. Preziosi spunti per le aziende che stanno considerando la migrazione al cloud"
draft: false
images:
  - "/images/content/onprem_vs_cloud.png"
card: "summary_large_image"
---


# L'illusione delle funzioni Serverless nel Cloud

![aws_costs_twitter_1](/images/content/onprem_vs_cloud.png)

### Introduzione

Sono deluso di quanto spesso il marketing prevalga sul buon senso. Molti manager ignorano
i loro stessi esperti - gli sviluppatori. Questo vale anche per la migrazione al cloud. Spoiler: chi deve risparmiare
dovrebbe evitare il cloud. Perché la nuova parola d'ordine "Serverless" nel cloud significa: Tu ti prendi cura del
software, noi della hardware. Tuttavia, chi ha un amministratore capace, motivato e curioso, può 
gestire Serverless da solo (ad es. [KNative](https://knative.dev)).

![aws_costs_twitter_1](/images/content/aws_costs_twitter_1.png)


### Funzioni Serverless vs Microservizi:



#### Microservizi

Un tipico microservizio senza stato si prende cura di una funzione/dominio specifico ed è distribuito in un ambiente di
orchestrazione dei contenitori. Questo ambiente si prende cura dell'infrastruttura, sicurezza, firewall, logging,
metriche, segreti, rete, backup e molto altro. Un grande vantaggio è che un microservizio può essere testato localmente
con poche risorse e è agnostico rispetto alla nuvola/server (utilizzabile ovunque).

#### Funzioni Serverless

Un piccolo scherzo iniziale: Paradossale, ma vero - Le funzioni serverless dipendono fortemente dall'ambiente del server. :)
Una tipica funzione serverless si occupa anche solo di una specifica funzione/dominio e viene scritta senza framework
in
codice puro per essere più veloce di un microservizio (Anche un buon esercizio per i MicroServices). Un grande
vantaggio è che le funzioni serverless vengono scalate automaticamente. Tuttavia, ogni funzione serverless richiede una
quantità considerevole di GlueCode per definire l'infrastruttura - Sicurezza, firewall, rete, logging, metriche,
segreti, cache, backup e molto altro.
Pertanto, una funzione semplice come la copia di un file compresa l'API può facilmente raggiungere le 1500 righe di codice (incl. IaC).
I costi amministrativi si spostano dall'amministrazione allo sviluppo nel rapporto 1:N (1 a funzioni serverless). La conoscenza e l'implementazione non sono quindi più concentrate e possono diventare instabili rapidamente. Inoltre, i costi di manutenzione aumentano.
Anche i veri test integrativi sono rari con serverless o richiedono un grande sforzo.
Infine, la complessità delle funzioni serverless è significativamente più alta di quella di un singolo microservizio. 
Maggiore complessità significa anche minore manutenibilità. I nuovi membri del team hanno più difficoltà e richiedono decisamente più conoscenze preliminari.

### Serverless e il Cloud in generale

La maggior parte delle tecnologie cloud non sono aggiornate. Ad esempio, Node.js, Java, Python e altri
lingue o tecnologie spesso non sono facili da aggiornare, solitamente l'unica soluzione è aspettare.
Anche le moderne e le tecnologie standard come MongoDB, MySQL, Kafka, NATS, RabbitMQ, Redis, Prometheus, InfluxDB, Grafana,
Kibana, Elastic Search ecc. sono spesso non disponibili o costano troppo.
Senza tali servizi standard, spesso ci si ritrova nell'epoca della pietra virtuale e si utilizzano soluzioni obsolete, ad es. 
Webhooks per la comunicazione esterna. A questo si aggiunge che la libertà d'azione su temi come regolamentazione,
compliance, protezione dei dati e affidabilità è fortemente limitata.

La cloud dovrebbe quindi essere gestita in modo agnostico, per poter passare rapidamente da AWS, Azure, Google, On-Premise ecc. e
confrontare i costi.
I limiti sono anche frequenti nel cloud, portando a soluzioni creative che a loro volta aumentano la complessità
Aumenta. Anche i test integrativi possono diventare costosi, poiché ogni sviluppatore ha bisogno di un proprio ambiente di sviluppo nel cloud
, poiché molti servizi cloud sono difficilmente o per niente testabili localmente.
Ma anche senza test il cloud è costoso. Mentre con i sistemi On-Premise si hanno soprattutto
costi dell'hardware, nel cloud si deve pagare anche per il traffico, alcuni servizi standard e spesso anche per la
doppia imposizione. Inoltre, nel cloud è facile perdere di vista l'insieme, perché non si tratta di
facilità d'uso, ma di soldi. I costi sono così nascosti che si notano solo quando è troppo tardi
è.

Le basi dell'architettura e dell'infrastruttura devono essere reinventate nel cloud e in particolare nel campo del senza server
, perché l'implementazione dipende fortemente dalle funzioni disponibili.
Ogni volta che ho progettato l'architettura, ho pensato: "Questo avrebbe potuto essere un singolo servizio
".

Per me, il serverless è un'idea interessante ed è facilmente scalabile, ma non riduce i costi. Al
contrario, richiede molta più conoscenza e tempo nello sviluppo. Serverless o il cloud richiedono disciplina e
conoscenze pregresse.
Se la conoscenza per i sistemi On-Premise non è disponibile, non sarà più facile con il cloud.
Come dovrebbero gli sviluppatori acquisire ulteriori conoscenze sull'infrastruttura?

Preferirei un cluster Kubernetes ben gestito all'architettura cloud.
Il personale non scala. Molti sviluppatori non hanno disciplina nella scrittura del codice.
Purtroppo, questo vale per l'80 percento degli sviluppatori. Quindi, come dovrebbero questi sviluppatori essere in grado di gestire il cloud
possono?

È importante che le aziende comprendano pienamente le sfide e le implicazioni dell'architettura senza server e del cloud.
Ciò richiede non solo conoscenze tecniche, ma anche un approccio strategico. Un'immigrazione sconsiderata nel cloud può portare a complessità, costi più elevati e sovraccarico degli sviluppatori.

In sintesi, il serverless nel cloud è un concetto promettente che tuttavia dovrebbe essere attentamente
considerato. I costi, la complessità, la manutenibilità e le capacità del team di sviluppo devono essere
presi in considerazione.
Ogni azienda ha diverse esigenze e priorità. Si dovrebbe prendere una decisione informata se
il serverless nel cloud è la soluzione giusta o se ci sono approcci alternativi come
ad es. un buon cluster Kubernetes sono una scelta migliore.

Il successo di Serverless e Cloud Computing richiede una combinazione di competenze tecniche
pianificazione strategica e una chiara comprensione dei requisiti di business. Solo così è possibile vedere attraverso l'illusione del serverless
e prendere la decisione giusta per il proprio sviluppo software.

### Conclusione

L'introduzione di funzioni serverless nel cloud promette flessibilità, scalabilità e sollievo per i
sviluppatori dai compiti infrastrutturali. Tuttavia, non si dovrebbe lasciare abbagliare da quest'illusione. Il
passaggio al cloud e l'uso di funzioni serverless comportano una serie di sfide.

Gli sviluppatori devono usare insieme alla sviluppo effettivo, una nuova "lingua" e assumersi più responsabilità senza il supporto appropriato.
La complessità delle funzioni serverless è spesso superiore a quella dei microservizi, poiché gli sviluppatori devono assumersi molti compiti aggiuntivi
come la definizione dell'infrastruttura, la sicurezza e la scalabilità. I veri test integrativi sono
difficili e il know-how e l'esperienza per il funzionamento nel cloud sono ancora più importanti.

Il cloud stesso comporta ulteriori sfide. Molte tecnologie cloud non sono aggiornate
e l'uso di servizi standard moderni può essere costoso o addirittura impossibile. Regolamenti, conformità e
la protezione dei dati limitano la flessibilità. Inoltre, i costi nel cloud possono facilmente sfuggire al controllo,
e la panoramica delle spese si perde rapidamente.

Nel complesso, è necessario valutare accuratamente i pro e i contro di Serverless e del Cloud.
Le aziende dovrebbero considerare le loro specifiche esigenze, le competenze esistenti nel team e le conseguenze a lungo termine
di una migrazione al cloud.
Una decisione ben ponderata basata su un'analisi completa è fondamentale per il successo e la redditività
del progetto.

Infine, spetta alle aziende sostenere adeguatamente i loro sviluppatori, stimare realisticamente i costi e la complessità del
cloud e considerare soluzioni alternative come i cluster Kubernetes ben gestiti.
Con una strategia chiara e una solida comprensione delle proprie esigenze, le aziende possono sfruttare al meglio i vantaggi del
cloud e delle funzioni serverless e vedere oltre l'illusione.

### Contatto

[Problemi GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
