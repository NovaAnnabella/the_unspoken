---
title: "Illusion Serverless & Cloud"
date: 2023-05-24
author: "Nova Annabella"
slug: illusion_serverless_cloud
tags: [ Development, Serverless, Cloud, Microservices, Scalability, Architecture, Infrastructure ]
categories: [ Technology, Software, Cloud ]
description: "Sfide e realtà delle funzionalità serverless nel cloud. Spunti preziosi per le aziende che stanno valutando una migrazione al cloud"
draft: false
images:
  - "/images/content/onprem_vs_cloud.png"
card: "summary_large_image"
---



# L'illusione delle funzioni serverless nel cloud

![aws_costs_twitter_1](/images/content/onprem_vs_cloud.png)

### Introduzione

Sono deluso da quanto spesso il marketing trionfi sul buon senso. Molti manager si antepongono ai loro stessi esperti,
gli sviluppatori. Questo vale anche per la migrazione al cloud. Spoiler: Se avete bisogno di risparmiare Se avete
bisogno di risparmiare, dovreste evitare il cloud. Perché la nuova parola d'ordine "serverless" nel cloud significa: voi
vi occupate del software, noi dell'hardware. Voi vi occupate del software, noi ci occupiamo dell'hardware. Tuttavia, se
si dispone di un amministratore capace, motivato e curioso, si può possono anche gestire autonomamente i serverless (ad
esempio [KNative](https://knative.dev)). ![aws_costs_twitter_1](/images/content/aws_costs_twitter_1.png)

### Funzioni serverless vs microservizi:



#### Microservizi

Un tipico microservizio stateless si occupa di una funzione/un dominio specifico ed è distribuito in un ambiente di
ambiente di orchestrazione di container. Questo ambiente si occupa di infrastruttura, sicurezza, firewall,
registrazione, metriche, segreti, rete, backup e altro ancora. Un grande vantaggio è che un microservizio può essere
implementato localmente con poche risorse ed è agnostico rispetto al cloud/server (può essere distribuito ovunque).

#### Funzioni serverless

Una piccola battuta in anticipo: paradossale, ma vero: le funzioni serverless dipendono fortemente dall'ambiente server.
:) Una tipica funzione serverless si occupa inoltre di una sola funzione/dominio specifico ed è scritta in puro codice
senza framework per essere più veloce di un microservizio. codice per essere più veloce di un microservizio (un buon
esercizio anche per i microservizi). Un grande vantaggio è che le funzioni Serverless scalano automaticamente. Tuttavia,
ogni funzione serverless richiede una una quantità considerevole di GlueCode per definire l'infrastruttura - sicurezza,
firewall, rete, logging, metriche, segreti, cache, backup e molto altro. Pertanto, una semplice funzione come la copia
di un file con API può comportare rapidamente 1500 righe di codice (IaC inclusa). possono essere coinvolti. I costi di
amministrazione passano dall'amministrazione allo sviluppo in un rapporto di 1:N (1 per le funzioni Serverless).
funzioni Serverless). La conoscenza e l'implementazione non sono più non sono più raggruppate e possono diventare
rapidamente instabili. Inoltre, i costi di manutenzione aumentano. Anche il vero testing integrativo è raro con i
serverless, o è possibile solo con grande sforzo. In definitiva, la complessità delle funzioni serverless è notevolmente
superiore a quella di un singolo microservizio. Una maggiore complessità significa anche una minore manutenibilità. I
nuovi membri del team hanno più difficoltà e necessitano di una conoscenza più conoscenze pregresse.

### Serverless e il cloud in generale

La maggior parte delle tecnologie cloud non sono aggiornate. Per esempio, Node.js, Java, Python e altri linguaggi o
tecnologie sono linguaggi o tecnologie spesso non sono facili da aggiornare, di solito solo l'attesa aiuta. Anche
tecnologie moderne e standard come MongoDB, MySQL, Kafka, NATS, RabbitMQ, Redis, Prometheus, InfluxDB, Grafana, Kibana,
Elastic Search ecc. non sono disponibili o hanno prezzi eccessivi. Senza questi servizi standard, ci si trova spesso
nell'età della pietra virtuale e si ricorre a soluzioni obsolete, come ad es. webhook per le comunicazioni esterne.
Inoltre, il margine di manovra su questioni come la regolamentazione, conformità, protezione dei dati e sicurezza è
fortemente limitato. Il cloud deve quindi essere gestito in modo agnostico per poter passare rapidamente da AWS, Azure,
Google, on-premise, ecc. e per poter confrontare i costi. confrontare i costi. Anche le limitazioni sono comuni nel
cloud e portano a soluzioni creative, che a loro volta aumentano la complessità. aumentare. Anche i test integrativi
possono diventare costosi, poiché ogni sviluppatore ha bisogno del proprio ambiente di sviluppo nel cloud. poiché molti
servizi cloud sono difficilmente o per nulla testabili a livello locale. Ma anche senza test, il cloud è costoso. Mentre
con i sistemi on-premise i costi sono principalmente hardware, nel cloud bisogna pagare anche il traffico, alcuni
servizi standard e spesso anche più tasse. e spesso anche per la tassazione multipla. Inoltre, nel cloud è facile
perdere di vista le cose, perché non si tratta di non si tratta di facilità d'uso, ma di soldi. I costi sono così
nascosti che ci si accorge di loro solo quando è troppo tardi. è troppo tardi. Le basi dell'architettura e
dell'infrastruttura devono essere reinventate nel cloud e soprattutto nel serverless. devono essere reinventate, poiché
l'implementazione dipende in larga misura dalle funzionalità disponibili. Ogni volta che ho progettato l'architettura,
penso: "Questo avrebbe potuto essere un singolo servizio". avrebbe potuto essere". Per me, serverless è un'idea
interessante e si scala bene, ma non riduce i costi. Al Al contrario, richiede molte più conoscenze e tempo per lo
sviluppo. Serverless o il cloud richiedono disciplina e conoscenze preliminari. Se le conoscenze non ci sono per i
sistemi on-premise, non sarà più facile con il cloud. Come possono gli sviluppatori acquisire conoscenze aggiuntive
sull'infrastruttura? Preferirei un cluster Kubernetes ben gestito all'architettura cloud. Le persone non scalano. Molti
sviluppatori non hanno disciplina nello scrivere codice. Purtroppo questo vale per l'80% degli sviluppatori. Quindi come
faranno questi sviluppatori a gestire il cloud? il cloud? È importante che le organizzazioni comprendano appieno le
sfide e le implicazioni dell'architettura serverless e del cloud. comprendere appieno le sfide e le implicazioni
dell'architettura serverless e del cloud. Ciò richiede non solo conoscenze tecniche, ma anche un approccio strategico. A
migrazione al cloud mal ponderata può portare a complessità, costi maggiori e sovraccarico di lavoro per gli
sviluppatori. In sintesi, l'architettura serverless nel cloud è un concetto promettente, ma che deve essere considerato
con attenzione. dovrebbe essere considerato con attenzione. Occorre considerare i costi, la complessità, la
manutenibilità e le competenze del team di sviluppo. essere presi in considerazione. Ogni azienda ha esigenze e priorità
diverse. È necessario decidere con cognizione di causa se Serverless nel cloud è la soluzione giusta o se approcci
alternativi come ad es. ad esempio, il cluster Kubernetes, sono la scelta migliore. Il successo dell'implementazione di
serverless e del cloud computing richiede una combinazione di competenze tecniche pianificazione strategica e una chiara
comprensione dei requisiti aziendali. Solo allora l'illusione di serverless potrà essere e prendere la decisione giusta
per il proprio sviluppo software.

### Fazit

L'introduzione di funzioni serverless nel cloud promette flessibilità, scalabilità e sgravio dalle incombenze
infrastrutturali. sviluppatori dalle incombenze infrastrutturali. Tuttavia, non bisogna farsi abbagliare da questa
illusione. Il passaggio al passaggio al cloud e all'uso di funzioni serverless comporta una serie di sfide. Gli
sviluppatori devono imparare un nuovo "linguaggio" oltre allo sviluppo vero e proprio e assumersi maggiori
responsabilità senza un supporto adeguato. assumersi maggiori responsabilità. La complessità delle funzioni serverless è
spesso superiore a quella dei microservizi, in quanto gli sviluppatori devono assumersi molti compiti aggiuntivi, ad
esempio Gli sviluppatori devono assumersi molti compiti aggiuntivi, come la definizione dell'infrastruttura, la
sicurezza e la scalabilità. Il vero test integrativo è difficile e la conoscenza e l'esperienza precedenti per le
operazioni sono ancora più importanti nel cloud. Il cloud stesso comporta ulteriori sfide. Molte tecnologie cloud non
sono aggiornate e l'utilizzo di servizi moderni off-the-shelf può essere costoso o addirittura impossibile. I requisiti
normativi, la conformità e la protezione dei dati limitano il campo di applicazione. Inoltre, i costi nel cloud sfuggono
facilmente di mano, e la visione d'insieme delle spese si perde rapidamente. Nel complesso, i vantaggi e gli svantaggi
di serverless e cloud devono essere valutati attentamente. Le aziende devono considerare i loro requisiti specifici, le
competenze esistenti nel team e gli effetti a lungo termine di una migrazione al cloud. di una migrazione al cloud. Una
decisione informata basata su un'analisi completa è fondamentale per il successo e la redditività del progetto. del
progetto. In definitiva, spetta alle aziende supportare adeguatamente i propri sviluppatori, valutare realisticamente i
costi e la complessità del cloud e prendere in considerazione soluzioni alternative come la migrazione al cloud. cloud
in modo realistico e considerare soluzioni alternative come cluster Kubernetes ben gestiti. Con una strategia chiara e
una solida comprensione delle proprie esigenze, le aziende possono sfruttare al meglio i vantaggi del cloud e delle
funzionalità serverless e vedere oltre l'illusione.

### Contatto

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
