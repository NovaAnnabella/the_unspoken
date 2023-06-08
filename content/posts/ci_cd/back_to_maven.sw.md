---
title: "```Rudi kwa Maven?```"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "Tafsiri maandishi ya markdown kuwa kwa Kiswahili:```Kutafuta kitu cha kueleweka kwa ugumu na safari fupi ya kugundua upya nguvu za Maven```"
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# Kurudi kwa Maven?

Hakuna kitu cha kutafsiri kwa hapa, kwa sababu hii ni kipande cha nambari cha Markdown ambacho hakina maneno ya lugha
yetu. Asante!

## Miaka 10 ya Gradle. Kutafuta unafuu na safari fupi ya kugundua nguvu ya Maven tena.

Sijaelewa ombi lako. Tafadhali nipe maandishi ya ujumbe ambao ungependa nipate nisaidie kutafsiri.

### Kukuza Uwezo wa Waendelezaji - Tunahitaji Zana Zinazookoa Wakati Zaidi

Themen ambazo mara nyingi hupuuzwa au hutajwa kidogo hunivutia. Mara nyingi teknolojia nzuri zinatumika, lakini hakuna
mtu anayezungumza juu ya matatizo yanayohusiana nayo. Maendeleo yamekuwa magumu siku hizi. Kwa maneno mazuri kama
"Serverless", "Low Code", "IaC", "Big Data", "Cloud", "DevOps", "You Build it You run it" nk, wasanidi programu wana
majukumu ya ziada ya kushughulikia. Majukumu zaidi yanamaanisha kwamba wataalam hawapatikani sana na kuna vitu ambavyo
hutengenezwa bila kuchunguzwa vizuri. Kwa hivyo, automation na kuokoa muda ni muhimu sana. "Usinifanye nifikirie" na
"Inafanya kazi kwa urahisi" ni viashiria vizuri vya ubora ambavyo bado sijaweza kuona katika Gradle. Kuwa haki, Gradle
sio chombo pekee cha kisasa kinachotufanya kazi ngumu badala ya kutusaidia.

### Kutafuta udanganyifu wa utimilifu na uporeshaji wa kiotomatiki

Seit bei SOAP nina chuki iliyokita sana dhidi ya mipangilio ya msingi ya XML. Nilikuwa nikitarajia kuwa kuandika skrip
za Bind kwa kutumia Gradle ingekuwa rahisi sana. Kwa bahati mbaya, matumaini yangu na motisha yangu yameshindwa baada ya
muda. Gradle inatafuta urembo na kwa hivyo inaacha automatiki na ubora. Watengenezaji hufuata mtindo kwa upofu bila
kuzingatia athari kwa uaminifu wa programu. Ili kuweka skri za ujenzi za Gradle rahisi na zinazohitaji matengenezo
kidogo, inahitaji nidhamu kali. Aina hii ya nidhamu ni nadra kupatikana katika msimbo wa chanzo, kwa hivyo ni nadra sana
katika skri za ujenzi.

### Tafsiri na Majaribio ya Kufanya Kazi - Wakati Scripts ya Ujenzi inakuwa changamoto.

Gradle hufanya kazi nyuma ya pazia sio tofauti sana na Maven. Kwa hivyo, tafsiri kadhaa ni lazima. Huduma kama Katalogi
ya Utegemezi, Plugin ya Kutolewa kwa Maven, Dependabot, na wengine wengi ni suluhisho la muda ambalo inatekeleza kazi za
msingi ambazo Maven tayari ina nazo. Kwa utendaji wa juu wa Gradle, kuna mipangilio ya ujenzi iliyo tata ambayo ni ngumu
sana kudumisha. Upatikanaji wa Vibwagizo vya Gradle una matatizo ya utangamano mara nyingi, na mipaka au ushiriki mdogo
wa maendeleo. Matatizo haya yanatokana na nyakati za kuendelea kwa mfumo wa Gradle, aina tofauti za mazingira ambayo
Gradle inatumika, na gharama maalum za utekelezaji na matengenezo kwa kila Vibwagizo. Kila kitu kina uhusiano.

### Athari ya Domino ya Gradle - Skenario la Ndoto Mbaya katika Dunia Halisi

Nimeona Microservices nyingi ambazo zina umri mdogo na tayari hazifai kutengenezwa tena kwa sababu ya Gradle. Ni muhimu kutaja kwamba hii sio mara ya kwanza ninaona kitu kama hicho, na hapana, sio waendelezaji wadogo wanaohusika.

Kazi yangu ilikuwa **kupandisha ngazi Spring Boot 2.x hadi 2.7**. Sambamba na hayo:

* Faili la kujenga Gradle linahitajika -> Punguza toleo la Java kwenye mashine hadi 11 (WTF) (Kawaida Java ina sifa ya kuwa na uwezo wa kurudishwa nyuma - Kuna zana za kufanya kazi hapa kama vile SdkMan...)
* Sasisho la Spring Boot linahitaji -> Sasisho la Gradle (WTF)
* Sasisho la Gradle linahitaji -> Sasisho la Plugin
* Sasisho la Plugin linahitaji -> Sasisho la Groovy (WTF)
* Sasisho la Groovy linahitaji -> Sasisho la mfumo wa majaribio na sasisho la majaribio (WTF)
* Sasisho la mfumo wa majaribio linahitaji -> Sasisho la tegemeo
* \[...]
Mbali na hayo, baadhi ya vipulizi havifanyi kazi na toleo jipya la Gradle, baadhi ya vipulizi havina tena maendeleo, sio sambamba na vipulizi vingine, wanafanya kazi tu na Gradle KTS, sio na Gradle Groovy au wana vikwazo. Hata vipulizi kutoka kwa watoa huduma wakubwa kama Spring wana kazi chache ikilinganishwa na vipulizi vyao vya Maven. Mwishowe, ninafaili fupi na nzuri ya kujenga Gradle ambayo hakuna mtu anaweza kuitunza vizuri, hata waendelezaji wa awali, na bado wanapenda Gradle. Najua wachache tu ambao wanaweza kuelewa na kuandika skripti za Gradle ipasavyo.

### Kugundua Upya Nguvu za Maven - Kutumia Uchawi wa Maven

Hapa ndio vipengele vyangu vya kupenda kutoka kwa Maven:
Zana za programu zinaweza kuanzishwa na kusanidiwa moja kwa moja kutoka kwa mstari wa amri bila kuhitaji ufafanuzi wa awali. Aidha, zinafaa kwa kiasi kikubwa bila kuingiliana sana na mipangilio mingine ya zana za programu.

| Amri ya mfano                         | Maelezo                                                                                                                                                       | Kiunga                                                                  | 
|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`   | Sasisha toleo - nani anahitaji Dependabot? Ndio, miradi yangu imekuwa ikisasishwa kwa miaka bila shida yoyote kwa toleo jipya zaidi, bila ombi la suluhisho la mzozo | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0` | Weka toleo la mradi...                                                                                                                                         | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`         | Onyesha orodha ya uitegemezi pamoja na leseni zao (hata ina uwezo wa kushindwa wakati leseni zimechaguliwa kuondolewa)                                         | https://www.mojohaus.org/license-maven-plugin/index.html                 | 

Orodha hii inaweza kuwa ndefu zaidi. Kwa njia fulani inanikumbusha hatua za kazi za Ghithub.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

### Je! Hupendi XML?

Hakuna shida! Andika tu faili yako ya ujenzi katika `ruby`, `groovy`,` scala`, `yaml`, `atom` au` Java`. Ugani wa Polygot
(https://github.com/takari/polyglot-maven) inawezekana. Kwa kujaribu
tu endesha `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` na
kipindi cha millisekunde chache faili yako ya ujenzi itakuwa imebadilishwa. Ni aibu kwamba hakuna mtu mwenye uwezo wa kutafsiri kwa ufanisi kati ya Maven <> Gradle :(
Ndio, faili za Ujenzi wa Maven ni kubwa, lakini ni rahisi kueleweka. Marekebisho au ufuatiliaji mdogo wa masuala hufanywa kwa haraka.

### Umri ni nambari tu - Uimara na Maendeleo ya Mavuno.

Zinazohusiana, Maven imekuwepo kwa muda mrefu na estetiki yake labda haiendani na viwango vya sasa. Uimara wa Maven hata hivyo umewezesha kubadilika na kuendelea kukua. Maven hufanya kazi kwa uhuru bila kujali mradi wako. Faili za kujenga (Build- Dateien) zinaweza kutumika tena kwa urahisi. Vidaku hufanya kazi katika sandbox na ni huru kati yao na huru kutoka kwa toleo la Java au Maven. Ubunifu huu hufanya kudumisha utulivu, uwezekano wa kutabirika, na inafanya kuwa rahisi kudhibiti michakato ya ujenzi wa ngumu bila migogoro yoyote isiyotarajiwa.

### Hitimisho

Hivi sasa, mazingira ya maendeleo yana majukumu mengi na teknolojia nyingi kwa waendelezaji. Kwa kutafuta urahisi na
uhakiki, Gradle imetokea kama chombo cha ujenzi kinachofaa, lakini kina changamoto zake. Hakuna shaka, wazo la Gradle ni
nzuri! Lakini kwa kuzingatia ugumu na wakati unaowekezwa katika hati za kujenga za Gradle, inaibuka swali ikiwa hainge
kuwa rahisi kuongeza suluhisho kwa Maven badala yake. Kwa Plugin na Extensions, Maven inaweza kuboreshwa na kusahilishwa
wakati wowote. Je! Kuboresha hali si ya kusisimua na endelevu zaidi kuliko kuruka kutoka teknolojia hadi nyingine?

### Viungo

* [Kurudi Nyuma Kutoka Kwenye Gradle hadi maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### Mawasiliano

[Tatizo za GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
