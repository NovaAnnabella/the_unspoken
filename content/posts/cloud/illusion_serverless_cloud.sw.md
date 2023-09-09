---
title: "Ilani ya Serverless & Cloud"
date: 2023-05-24
author: "Nova Annabella"
slug: illusion_serverless_cloud
tags: [ Development, Serverless, Cloud, Microservices, Scalability, Architecture, Infrastructure ]
categories: [ Technology, Software, Cloud ]
description: "Changamoto na Ukweli wa Kazi za Serverless kwenye Wingu. Mawazo ya thamani kwa makampuni yanayofikiria uhamiaji kwenye wingu."
draft: false
images:
  - "/images/content/onprem_vs_cloud.png"
card: "summary_large_image"
---


# Udhana wa Kazi za Serverless katika Wingu

![aws_costs_twitter_1](/images/content/onprem_vs_cloud.png)

### Utangulizi

Nina kuvunjika moyo, mara ngapi uuzaji hupita juu ya akili timamu. Mameneja wengi wanajipita 
juu ya wataalamu wao wenyewe - waendelezaji. Hii inatumika pia kwa uhamiaji kwenye Cloud. Spoiler: Yeyote anayehitaji kuokoa 
pesa, anapaswa kuepuka Cloud. Kwa sababu neno jipya la msisimko "Serverless" katika Cloud linamaanisha: Unajishughulisha na 
programu, tunajishughulisha na vifaa. Hata hivyo, yeyote anaye na msimamizi mwenye uwezo, anayejituma na mwenye utaalam, anaweza 
kumiliki Serverless mwenyewe (kwa mfano, [KNative](https://knative.dev)).

![aws_costs_twitter_1](/images/content/aws_costs_twitter_1.png)

### Serverless Functions vs Microservices:



#### Huduma Ndogo

Microservice isiyo na hali ya kawaida inashughulikia kazi/eneo fulani la kufanya kazi na inawekwa katika mazingira ya
Orchestration ya Container. Mazingira haya yanashughulikia miundombinu, usalama, firewall, kubandika, metriki, siri,
mtandao, akiba na mengi zaidi. Faida kubwa ni kwamba microservice inaweza kupimwa kwa pamoja na rasilimali chache na
inaweza kutumika kwa urahisi kwenye Cloud / Server (inaweza kutumika popote).

#### Serverless Functions

Utani mdogo kwanza: Ni kinyume na utarajio, lakini ni kweli - Kazi za bila seva zinategemea sana mazingira ya seva. :)
Kazi ya kawaida ya bila seva inashughulikia tu kazi / eneo maalum na huandikwa bila mifumo
ndani
nambari safi, kuwa haraka kuliko huduma ndogo (Pia mazoezi mazuri kwa MicroServices). Faida kubwa
ni kwamba kazi za bila seva zinawezeshwa otomatiki. Hata hivyo, kila kazi ya bila seva inahitaji
kiwango kikubwa cha GlueCode, ili kufafanua miundombinu - Usalama, Firewall, Mtandao, Logging, Metriken,
Siri, Caching, Backups na mengi zaidi.
Kwa hivyo, kazi rahisi kama kunakili faili pamoja na API inaweza kufikia haraka mistari 1500 za nambari (pamoja na IaC)
kujumuisha.
Gharama za utawala zinahamia kutoka kwa utawala hadi maendeleo kwa uwiano wa 1:N (1 kwa
Kazi za bila seva). Maarifa na utekelezaji kwa hivyo sio tena
concentrated na inaweza kuwa dhaifu haraka. Kuna gharama za matengenezo zilizoongezeka.
Pia, majaribio kamili ya kuunganisha na bila seva ni nadra au yanahusisha bidii kubwa.
Mwishowe, ngumu ya kazi za bila seva ni kubwa zaidi kuliko ile ya huduma ndogo moja.
Ugumu zaidi inamaanisha pia uwezo mdogo wa matengenezo. Wanachama wapya wa timu wana wakati mgumu na wanahitaji zaidi
elimu kabla.

### Serverless na Cloud kwa ujumla

Teknolojia nyingi za Cloud hazijasasishwa. Kwa mfano, Node.js, Java, Python na lugha au teknolojia zingine
marahaba sio rahisi kusasisha, mara nyingi unahitaji kusubiri tu.
Pia teknolojia za kisasa na za kawaida kama MongoDB, MySQL, Kafka, NATS, RabbitMQ, Redis, Prometheus, InfluxDB, Grafana,
Kibana, Elastic Search nk huenda zikawa hazipatikani au ziko ghali mno.
Bila huduma kama hizi za kawaida, mara nyingi utajikuta uko katika zama za kale halisi na kutumia suluhisho 
zilizozeeka, kwa mfano,
Webhooks kwa mawasiliano ya nje. Kuna pia suala la kuwa na nafasi ndogo ya kufanya maamuzi kwenye masuala kama vile udhibiti,
utii, usiri wa data na usalama wa upatikanaji.

Cloud inapaswa kusimamiwa kwa njia isiyopendelea, ili uweze haraka kuhamia kati ya AWS, Azure, Google, On-Premise nk na
ulinganishe gharama.
Kuna mipaka mingi katika Cloud, ambayo inasababisha utumiaji wa mbinu za ubunifu, ambazo huzidisha utata 
wa mifumo. Pia upimaji wa kujumuisha unaweza kuwa ghali, kwani kila mtengenezaji anahitaji mazingira yake ya maendeleo katika Cloud
kwani huduma nyingi za Cloud hazipimiki au hazipimiki kabisa kwa kiwango cha chini.
Hata bila majaribio, Cloud ni ghali. Wakati mfumo wa On-Premise unalazimisha gharama kubwa za 
vifaa, kwenye Cloud lazima ulipe pia kwa trafiki, huduma zingine za kawaida na mara nyingi hata kwa 
kutozwa ushuru mara kadhaa. Pia, unaweza kupoteza mtazamo wa jumla katika Cloud, kwa sababu haitoi rahisi ya 
kutumia, bali inazingatia pesa. Gharama zimefichwa kiasi kwamba unazigundua tu wakati ni kuchelewa
sana.

Misingi ya usanifu na miundombinu inahitaji kubuniwa upya katika Cloud na haswa katika eneo la bila seva
kwani utekelezaji hutegemea sana kazi zinazopatikana.
Kila wakati baada ya kubuni usanifu, nakuja na mawazo: "Hii ingeweza kuwa huduma moja tu".

Kwa maoni yangu, bila seva ni wazo la kuvutia na linaweza kusawazishwa vizuri, lakini halipunguza gharama. Badala yake, 
inahitaji ujuzi na wakati zaidi katika maendeleo. Bila seva au Cloud inahitaji nidhamu na 
maarifa ya awali.
Ikiwa maarifa ya mifumo ya On-Premise hayapo, haitakuwa rahisi zaidi na Cloud.
Je, watengenezaji wanapaswa kujifunza pia ujuzi wa miundombinu?

Ningependa kubadilisha kikundi cha Kubernetes kilichosimamiwa vizuri kuliko usanifu wa Cloud.
Wafanyakazi hawapanda kwa kiwango. Watengenezaji wengi hawana nidhamu katika kuandika code.
Kwa bahati mbaya, hii inatumika kwa asilimia 80 ya watengenezaji. Kwa hivyo, je, watengenezaji hawa wanawezaje kutumia Cloud?

Ni muhimu kwa kampuni kuelewa vyema changamoto na athari za usanifu wa bila seva na ya Cloud.
Hii inahitaji sio tu ujuzi wa kiufundi, bali pia mkakati. Uhamisho usiofikiriwa vizuri kwenye Cloud unaweza kusababisha utata, gharama kubwa na watengenezaji kupita kiasi.

Kwa muhtasari, bila seva katika Cloud ni wazo nzuri, hata hivyo, linapaswa kuzingatiwa kwa makini.
Gharama, utata, urahisi wa matengenezo na ujuzi wa timu ya maendeleo lazima kuzingatiwa.
Kila kampuni ina mahitaji na vipaumbele tofauti. Unapaswa kufanya uamuzi ulio na msingi, ikiwa 
bila seva katika Cloud ndiye suluhisho sahihi au ikiwa mbinu mbadala kama vile 
Kikundi cha Kubernetes kinaweza kuwa chaguo bora.

Matumizi mafanikio ya bila seva na Cloud Computing yanahitaji mchanganyiko wa ujuzi wa kiufundi
upangaji wa kimkakati na ufahamu mzuri wa mahitaji ya biashara. Kwa njia hii, unaweza tu kuona kwa uhalisia dhana ya bila seva
na fanya uamuzi sahihi kwa maendeleo ya programu yako mwenyewe.


### Hitimisho

Uzinduzi wa kazi za Serverless katika wingu unasaidia kutoa uwezo wa kubadilika, kutolea nje kwa uzani na kupunguza
mzigo kwa waendelezaji wa miundo msingi. Hata hivyo, usidanganywe na dhana hii. Mabadiliko ya kutumia wingu na kutumia
kazi za Serverless huleta changamoto nyingi. Waendelezaji lazima wajifunze lugha mpya mbali na kazi ya maendeleo na
bila msaada unaofaa kuchukua majukumu mengi zaidi. Uchangamano wa kazi za Serverless mara nyingi ni mkubwa kuliko ule wa
Microservices, kwani waendelezaji wanapaswa kuchukua majukumu mengi ya ziada kama vile ufafanuzi wa miundombinu, usalama
na kuongezeka kwa mzani. Mtihani wa kweli wa integrative ni ngumu na maarifa ya awali na uzoefu wa kuendesha ni muhimu
zaidi katika wingu. Wingu lenyewe husababisha changamoto zaidi. Teknolojia nyingi za wingu sio za kisasa na kutumia
huduma za kisasa za kawaida inaweza kuwa ghali au hata haiwezekani. Mahitaji ya udhibiti, kufuata kanuni na ulinzi wa
data hupunguza nafasi ya mchezo. Gharama katika wingu mara nyingi huvuka mipaka, na muhtasari wa matumizi hupotea
haraka. Kwa jumla, ni muhimu kuzingatia faida na hasara za Serverless na wingu kwa uangalifu. Makampuni yanapaswa
kuzingatia mahitaji yao maalum, ujuzi uliopo katika timu na athari za muda mrefu ya uhamiaji kwenye wingu. Uamuzi wenye
msingi bora kulingana na uchambuzi kamili ni muhimu kwa mafanikio na faida ya mradi. Mwishowe, ni jukumu la makampuni
kuwasaidia waendelezaji wao ipasavyo, kutathmini gharama na uchangamano wa wingu kwa usahihi na kuzingatia suluhisho
mbadala kama vifurushi vya Kubernetes vilivyosimamiwa vizuri. Kwa mkakati wazi na ufahamu kamili wa mahitaji yao
wenyewe, makampuni yanaweza kutumia vizuri faida za wingu na kazi za Serverless na kuchunguza dhana.

### Mawasiliano

[GitHub Mambo](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
