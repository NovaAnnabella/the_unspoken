---
title: "Livelli di test: Trovare il giusto equilibrio"
date: 2023-05-31
author: "Nova Annabella"
slug: test_level
tags: [ Testing, Software Testing, Test Levels, Mock Tests, Unit Tests, Integration Tests, Component Tests, Contract Tests, End-to-End Tests ]
categories: [ Technology, Software Development, Quality Assurance ]
description: "Trovare il giusto equilibrio nella selezione dei livelli di test appropriati per il collaudo del software".
draft: false
images:
  - "/images/content/martin_fowler_testing.png"
card: "summary_large_image"
---


# Livelli di test: Trovare il giusto equilibrio

[![testebenen](/images/content/martin_fowler_testing.png)](https://martinfowler.com/articles/microservice-testing/)

### Introduzione

Il tema dei test sembra essere ancora un territorio inesplorato, con un ampio margine di interpretazione. La
tradizionale piramide dei test è stata messa in discussione e sono emerse nuove piramidi di test. A mio avviso, non c'è
bisogno di una piramide di piramide di test, ma una chiara comprensione di ciò che deve essere testato. I test ai
livelli più bassi sono spesso meno significativi. L'attenzione dovrebbe essere focalizzata principalmente sul
comportamento del test, per garantire che l' API o l'interfaccia utente funzionino come desiderato. Una panoramica
completa dei possibili tipi di test si trova qui: [Martinfowler Testing](https://martinfowler.com/articles/microservice-
testing/).

### Livello 1 - Mock Test e Unit Test

Obiettivo: Esercitare le più piccole parti di software testabili dell'applicazione per vedere se funzionano come
previsto. lavoro. I test di simulazione e i test unitari possono essere controproducenti e spesso ostacolano il
processo di sviluppo. Questi test sono spesso spesso sono staccati dal contesto e hanno poca relazione con la realtà.
Spesso servono solo a mantenere le funzioni non necessarie tramite i test test unitari esistenti. Una volta aggiunti i
mock, diventa un esercizio autodistruttivo. I risultati attesi risultati attesi dai test mock sono limitati a ciò che è
stato definito nel mock originale. Gli utenti finali non sono interessati alle funzioni interne. Per esempio, in uno
scenario di scenario di login `loginUser(nome, password, securityAlgorithm)`. Se il test unitario esegue un controllo
nullo su il parametro `securityAlgorithm`, vengono eseguiti troppi test perché gli utenti non possono impostare il
parametro `securityAlgorithm`. impostare il parametro `securityAlgorithm'.

### Livello 2 - Test di integrazione

Scopo: verifica dei percorsi di comunicazione e delle interazioni tra i componenti per rilevare i difetti di
interfaccia. difetti di interfaccia. I test di integrazione forniscono indicazioni preziose sulle prestazioni e
sull'indipendenza delle diverse parti dell'applicazione. applicazione. Con meno mock, i test diventano più
comprensibili. Tuttavia, mancano ancora di contesto e c'è il rischio che i test di integrazione siano semplicemente test
unitari sotto mentite spoglie. rischio che i test di integrazione siano semplicemente test unitari sotto mentite spoglie
con un numero inferiore di mock.

### Livello 3 - Test dei componenti

Scopo: limitare l'ambito del software in fase di test a una parte del sistema in esame, manipolare il sistema attraverso
interfacce interne al codice e l'uso di doppi per isolare il codice in fase di test da altri componenti. sistema tramite
interfacce interne al codice e l'uso di doppi di prova per isolare il codice in prova da altri componenti. componenti.
Il test dei componenti fornisce una grande quantità di informazioni sulla qualità e sulle prestazioni dell'applicazione.
Invece di mock si testa finalmente l'applicazione. Il confine tra il test dei componenti e il test end-to-end non è
significativo. Con un buon ambiente di test, i confini tra i due diventano spesso sfumati, in modo da testare il
comportamento reale anziché funzioni isolate e prive di contesto. comportamento reale invece di funzioni isolate e prive
di contesto. Tuttavia, la creazione di classi di test aggiuntive Tuttavia, la creazione di classi di test aggiuntive,
come gli stub dei componenti, i fake e i mock, nel codice di produzione può aggiungere costi di manutenzione.

### Livello 4 - Test del contratto

Lo scopo di questo blocco di codice è verificare le interazioni al confine di un servizio esterno e assicurarsi che sia
conforme ai requisiti contrattuali di un servizio utilizzatore. che sia conforme ai requisiti contrattuali di un
servizio utilizzatore. I test contrattuali spesso assomigliano ai test unitari e la differenza tra loro è minima.
Alcuni sviluppatori associano questi test ai test Pact, che agiscono essenzialmente come test unitari con un server in
mezzo. L'impegno di mantenere questi sforzo di mantenere questi test potrebbe non valere la pena. Per esempio, un test
Pact potrebbe utilizzare il metodo REST API `loginUser?name=aa&password=bb)` e aspettarsi una risposta JSON schema che è
stata precedentemente caricata sul server Pact. server. Questo schema è statico e soggetto a errori come formati di data
o fusi orari errati nella risposta dell'API. risposta dell'API. Gli effetti negativi possono essere enormi.

### Livello 5 - Test end-to-end (chiamati anche test black box)

Scopo: verificare che un sistema soddisfi i requisiti esterni e raggiunga i suoi obiettivi testando l'intero sistema
dall'inizio alla fine. dall'inizio alla fine. Il test end-to-end è affidabile e robusto. Una volta superati gli
ostacoli legati all'allestimento dell'ambiente di test, l'impegno è ripagato. sforzo viene ripagato. Questi test
simulano il comportamento reale ed eliminano la necessità dei mock. Gli errori si verificano meno frequentemente e sono
più facili da riprodurre localmente. Il debug e il logging in produzione, che richiedono molto tempo, sono in gran parte
evitati, così come lo sono i casi rari. sono in gran parte evitati, così come gli incidenti rari. Gli sviluppatori
lavorano meno spesso, se non mai, con i dati di produzione. dati di produzione, il che riduce le responsabilità e
aumenta la concentrazione. Inoltre, le automazioni come gli aggiornamenti automatici del software facilitano
l'implementazione, poiché il comportamento è già stato testato. Ci sono altri vantaggi! Una volta una volta che i test
sono stati scritti in forma riutilizzabile, possono essere integrati nei test di carico per ottenere un quadro completo
della funzionalità. un quadro completo della funzionalità. Questi test possono anche essere eseguiti continuamente
nell'ambiente di produzione e fornire informazioni in tempo reale sullo stato dei vari flussi di lavoro. Quando un
sottosistema, ad esempio un servizio REST, ad esempio, va offline, è possibile identificare immediatamente quali flussi
di lavoro degli utenti sono interessati. sono interessati.

### Fazit

In sintesi, il testing è un aspetto essenziale dello sviluppo del software e la scelta dei livelli di testing dipende
dai requisiti e dagli obiettivi specifici dell'applicazione. dai requisiti e dagli obiettivi specifici
dell'applicazione. Mentre i mock test e i test unitari possono avere un'efficacia limitata, i test di integrazione e i
test unitari forniscono informazioni preziose sul comportamento e sulle prestazioni dell'applicazione. efficacia, i test
di integrazione e i test unitari forniscono preziose informazioni sul comportamento e sulle prestazioni
dell'applicazione. prestazioni dell'applicazione. I test di contratto aiutano a verificare le interazioni con i servizi
esterni, ma la loro differenziazione dai test unitari può essere minima. In definitiva, i test end-to-end forniscono il
massimo livello di fiducia nella funzionalità del sistema e consentono di eseguire test completi. La verifica end-to-end
fornisce il massimo livello di fiducia nella funzionalità del sistema e consente di eseguire test completi dell'intera
applicazione. Selezionando i livelli di test appropriati e combinandoli livelli di test appropriati e combinandoli in
modo efficace, gli sviluppatori possono garantire la qualità, l'affidabilità e la robustezza del software. software.

### Contatto

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
