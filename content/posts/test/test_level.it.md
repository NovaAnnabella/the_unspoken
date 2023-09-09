---
title: "Livelli di test: Trovare il giusto equilibrio"
date: 2023-05-31
author: "Nova Annabella"
slug: test_level
tags: [ Testing, Software Testing, Test Levels, Mock Tests, Unit Tests, Integration Tests, Component Tests, Contract Tests, End-to-End Tests ]
categories: [ Technology, Software Development, Quality Assurance ]
description: "Trovare il giusto equilibrio nella scelta dei livelli di test appropriati per i test del software"
draft: false
images:
  - "/images/content/martin_fowler_testing.png"
card: "summary_large_image"
---


# Livelli di test: Trovare il giusto equilibrio

[![testebenen](/images/content/martin_fowler_testing.png)](https://martinfowler.com/articles/microservice-testing/)

### Introduzione

Il tema Testing sembra essere ancora un territorio inesplorato con molto spazio per l'interpretazione. La tradizionale
piramide di test è stata messa in discussione e sono nate nuove piramidi di test. A mio parere, non c'è bisogno di una
piramide di test, ma piuttosto una chiara comprensione di ciò che deve essere testato. I test a livelli inferiori sono spesso
meno significativi. L'enfasi dovrebbe essere soprattutto sul test del comportamento, per assicurarsi che 
API
o UI funzioni come desiderato. Una panoramica completa delle possibili tipologie di test può essere trovata qui:
[MartinFowler Testing](https://martinfowler.com/articles/microservice-testing/).


### Livello 1 - Test simulati e Test unitari

Obiettivo: Esercitare le parti di software più piccole e testabili nell'applicazione per determinare se funzionano come
previsto. I test mock e i test unitari possono essere controproducenti e spesso ostacolano il processo di sviluppo.
Questi test sono spesso scorporati dal contesto e hanno poco attinenza con la realtà. Servono spesso solo a mantenere
funzioni superflue su esistenti test unitari. Non appena vengono aggiunti dei mock, diventa un autocommiserazione. I
risultati attesi dei test mock sono limitati a quanto definito nel mock originale. Gli utenti finali non si interessano
delle funzioni interne. Ad esempio, in uno scenario di login `loginUser(name, password, securityAlgorithmus)`. Se il
test di unità esegue un controllo nullo su il parametro `securityAlgorithm`, si sta testando troppo, poiché gli utenti
non possono impostare il parametro `securityAlgorithm`.

### Livello 2 - Test di Integrazione

Scopo: Verifica dei percorsi di comunicazione e delle interazioni tra componenti per il rilevamento di difetti di
interfaccia. I test di integrazione forniscono informazioni preziose sulla capacità e l'indipendenza di diverse parti
della applicazione. Con meno mock, i test diventano più comprensibili. Tuttavia, manca ancora loro il contesto, e c'è il
rischio che i test di integrazione siano semplicemente unit test camuffati con meno mock.

### Livello 3 - Test del componente

Scopo: Limitazione dell'ambito del software testato a una parte del sistema da verificare, manipolazione del sistema
attraverso interfacce di codice interne e utilizzo di Test doubles per isolare il codice da testare da altri
componenti.

I test di componente forniscono una miriade di informazioni sulla qualità e sulla capacità di prestazione dell'applicazione. Invece di
Mocks stai finalmente testando la tua applicazione. Il confine tra i test di componente e i test end-to-end non è
significativo. Con un buon ambiente di test, i confini tra di loro spesso si sfumano, rendendo possibile il test del reale
comportamento invece di funzioni isolate e senza contesto. Tuttavia, la creazione di ulteriori
classi di test come stub di componenti, finti e mock nel codice di produzione può comportare un ulteriore lavoro di manutenzione.



### Livello 4 - Test del Contratto

Lo scopo di questo blocco di codice è verificare le interazioni al confine di un servizio esterno e
assicurarsi che esso rispetti le richieste contrattuali di un servizio consumatore.

I test contrattuali spesso assomigliano ai test di componente, e la differenza tra di loro è minima. Alcuni sviluppatori
associare questi test con i test Pact, che fungono essenzialmente come test di unità con un server in mezzo. Lo
sforzo per mantenere questi test potrebbe tuttavia non essere conveniente. Per esempio, un test Pact potrebbe verificare
l'API REST `loginUser?name=aa&password=bb)` e aspettarsi una risposta in formato JSON-Schema che prima è stata caricata sul server Pact.
Questo schema è statico e suscettibile ad errori come formati di data errati o fusi orari nella
risposta dell'API. L'impatto negativo può essere enorme.

### Livello 5 - Test End-to-End (chiamati anche Test della Black-Box)

Scopo: Verificare se un sistema soddisfa i requisiti esterni e raggiunge i suoi obiettivi testando l'intero sistema dall'inizio alla fine.

I test end-to-end sono affidabili e robusti. Una volta superati gli ostacoli della creazione dell'ambiente di test, lo sforzo ripaga. Questi test simulano il comportamento reale ed eliminano la necessità di mock. Gli errori si verificano raramente e possono essere riprodotti localmente in modo più semplice. Il debugging complesso e la registrazione in produzione sono per lo più evitati, così come i casi rari. Gli sviluppatori interagiscono raramente, se mai, con i dati di produzione, riducendo la responsabilità e aumentando la concentrazione. Inoltre, le automazioni come gli aggiornamenti software automatici facilitano l'implementazione, poiché il comportamento è già stato testato. Ci sono altri vantaggi! Una volta che i test sono scritti in una forma riutilizzabile, possono essere integrati nei test di carico per ottenere un quadro completo della funzionalità. Questi test possono anche essere eseguiti continuamente nell'ambiente di produzione e fornire informazioni in tempo reale sullo stato di diversi flussi di lavoro. Se un sotto-sistema, come un servizio REST esterno, va offline, si può immediatamente identificare quali flussi di lavoro degli utenti sono interessati.

### Conclusione

In sintesi, il test è un aspetto essenziale dello sviluppo del software, e la scelta dei livelli di test dipende
dalle specifiche esigenze e obiettivi dell'applicazione. Sebbene i test simulati e i test unitari possano essere limitati in termini di efficacia,
i test di integrazione e i test di componente offrono preziose intuizioni sul comportamento e le prestazioni dell'applicazione. I test del contratto aiutano a verificare le interazioni con servizi esterni, ma la loro distinzione dai test sui componenti può essere minima. Infine, i test end-to-end offrono il massimo livello di fiducia nelle funzionalità del sistema e consentono test completi dell'intera applicazione. Mediante la scelta dei livelli di test appropriati e il loro efficace abbinamento, gli sviluppatori possono garantire la qualità, l'affidabilità e la robustezza del software.

### Contatto

[Problemi GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
