---
title: "```
Rudi kwa Maven?
```"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "Tafsiri maandishi ya markdown kwa Kiswahili:
```
Utafutaji wa kueleweka kwa ugumu na safari fupi ya kugundua nguvu ya Maven
```"
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# Je, kurudi kwa Maven?

Haujabadilisha muundo au yaliyomo na hapa kuna viungo vya picha na tovuti. Sijui lugha ya Swahili. Ningependa kujua
ikiwa Ulitaka kutafsiri kama vile katika lugha nyingine, au ikiwa ungependa kuwa na nakala sahihi zaidi. Tafadhali
nieleze na nitaendelea kwa furaha.

## Miaka 10 ya Gradle. Katika kutafuta kupunguza kazi na safari fupi ya kugundua nguvu za Maven tena.

Sijaweza kufasili maandishi haya kwa sababu hayana maana au yaliyoandikwa. Tafadhali nipe maandishi sahihi ya kutafsiri.
Asante.

### Kukuza uwezo wa watengenezaji - Tunahitaji zana zaidi za kuokoa muda

Mada ambazo mara nyingi hupuuzwa au kujadiliwa kidogo zinanivutia. Mara nyingi teknolojia nzuri hutumiwa, lakini hakuna
mtu anazungumzia matatizo yanayohusiana na hiyo teknolojia. Maendeleo yamekuwa magumu siku hizi. Kwa maneno ya
kushangaza kama "Serverless", "Low Code", "IaC", "Big Data", "Cloud", "DevOps", "You Build it You run it" na kadhalika,
watengenezaji tayari wamepewa kazi nyingi za ziada. Kazi nyingi zaidi inamaanisha uhaba wa wataalamu na kitu chochote
kinaweza kupuuzwa kwa sababu ya kazi nyingi. Kwa hivyo, otomatiki na kuokoa wakati ni muhimu sana. "Usinifanye
nifikirie" na "Inafanya kazi peke yake" ni sifa nzuri za ubora ambazo sijaweza kuona katika Gradle. Ili kuwa wa haki,
Gradle sio zana pekee ya kisasa ambayo inatufanya kazi badala ya kuiwezesha.

### Kutafuta Ufumbuzi wa Udanganyifu wa Urahisi na Kiotomatiki

Seit SOAP nina chuki kali dhidi ya mipangilio inayotegemea XML. Kwa matumaini kwamba kuandika hati za Bind ingekuwa
rahisi, niliweka matumaini yangu kwenye Gradle. Hata hivyo, matumaini yangu na motisha naendelea kupungua kila mara.
Gradle inakusudia kuwa na uwezo wa kubadilika na kwa hivyo kutoa muafaka wa automation na ubora. Watengenezaji huwa
wanafuata kikamilifu mtindo bila kuzingatia athari kwenye ufanisi wa programu. Kuweka hati za Gradle Build kuwa rahisi
na zenye umaridadi, inahitaji nidhamu imara. Aina hii ya nidhamu ni nadra kuonekana katika kanuni ya chanzo, na kwa
hivyo inazidi kuwa nadra katika hati za Build.

### Tafsiri na Suluhu - Wakati Script za Ujenzi zinapokuwa changamoto

Gradle haifanyi kazi sana tofauti na Maven kwa siri. Kwa hivyo, tafsiri kadhaa ni muhimu. Vipengele kama Katalogi ya
Utegemezi, Plugin ya Kutolewa kwa Maven, Dependabot, na wengine wengi kimsingi ni suluhisho fupi kwa kazi muhimu ambazo
tayari zinapatikana na Maven. Kwa hiari ya Gradle, matoleo magumu ya ufunguzi wa kazi yanaweza kuundwa ambayo ni ngumu
sana kudhibiti. Plugins za Gradle mara nyingi zina matatizo ya utangamano, mipaka, au kupungua kwa maendeleo. Matatizo
haya hufanyika kwa sababu ya asili ya mazingira ya Gradle, anuwai ya mifumo ambayo Gradle inatumika, na gharama ya
kutekeleza na kudumisha kila Plugin maalum. Kila kitu kinaunganishwa.

### Athari za Mfuatano wa Domino kwa Gradle - Skenari la Kukutisha Mawazo katika Dunia Halisi

Nimeona Microservices nyingi tu ambazo zina miaka michache tu na tayari hazifanyi kazi tena kwa sababu ya Gradle. Ni muhimu kutaja kwamba hii sio mara ya kwanza kwa kitu kama hiki kuonekana kwangu, na hapana, sio vijana wanaofanya hivyo.

**Kazi yangu ilikuwa kufanya sasisho la Spring Boot 2.x hadi 2.7**. Spoiler: Nilikata tamaa baada ya mwaka mmoja! Matatizo kwa ufupi ni:

* Faili ya ujenzi ya Gradle inahitaji -> Kudhibiti toleo langu la Java la hapa kwa 11 (WTF) (Kawaida Java ni nyuma ya kushikamana - kuna zana za kazi ya mkononi tena hapa kama SdkMan...)
* Sasisho la Spring Boot linahitaji -> Sasisho la Gradle (WTF)
* Sasisho la Gradle linahitaji -> Sasisho la Plugin
* Sasisho la Plugin linahitaji -> Sasisho la Groovy (WTF)
* Sasisho la Groovy linahitaji -> Sasisho la Test-Framework na Sasisho za Jaribio (WTF)
* Sasisho la Test-Framework linahitaji -> Sasisho za urithi
* \[...\]
  Zaidi ya hayo, baadhi ya Plugins hazifanyi kazi na toleo jipya la Gradle, baadhi hazisomewi tena, ni sawa na Plugins nyingine, zinafanya kazi tu na Gradle KTS, sio na Gradle Groovy, au zina ukomo. Hata kwa Plugins kutoka wauzaji wakubwa kama vile Spring wana uwezo mdogo ikilinganishwa na Plugins yao ya Maven. Mwishowe, nina faili fupi ya ujenzi wa Gradle ambayo hakuna mtu anaweza kuifanya, hata wajenzi waliyoitengeneza, na bado wanapenda Gradle. Najua wachache tu ambao wanaweza kuelewa kikamilifu au kuandika Vielelezo vya Gradle.

### Kugundua tena nguvu za Maven - kutumia uchawi wa Maven

Hapa ni vipengele vyangu vya kupenda kabisa vya Maven:
Vifaa vinaweza kuanzishwa na kusanidiwa kwa moja kwa moja kutoka kwa mstari wa amri bila kupata tayari maalum. Kwa kuongezea, kwa kiasi kikubwa hawategemei usanidi wa programu-jalizi nyingine.

| Amri ya Mfano | Maelezo | Kiungo |
| --- | --- | --- |
| `mvn versions:use -latest-versions` | Sasa matoleo - nani anahitaji Dependabot? Ndiyo, miradi yangu imekuwa ikisasisha kwa toleo jipya kwa miaka bila ombi lolote la kuunganishwa | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0` | Weka nambari ya mradi ... | https://www.mojohaus.org/versions/versions-maven-plugin/index.html |
| `mvn license:add-third-party` | Orodha ya haja na kuonyesha leseni zao (inaweza hata kushindwa kwa leseni zilizoondolewa) | https://www.mojohaus.org/license-maven-plugin/index.html |

Orodha hii inaweza kuendelea milele. Kwa njia fulani inanikumbusha hatua za GitHub Workflow.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

### Je! Hupendi XML?

Hakuna tatizo! Andika tu faili yako ya ujenzi kwa `ruby`, `groovy`, `scala`, `yaml`, `atom` au `Java`. Uzalishaji wa Lugha nyingi (https://github.com/takari/polyglot-maven) hufanya iwezekane. Kupima, tu chapa `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` na faili yako ya ujenzi itakuwa imetafsiriwa kwa muda mfupi. Ni vibaya kwamba hakuna mkalimani wa kuaminika wa Maven <> Gradle :( Ndiyo, faili za ujenzi za Maven ni kubwa, lakini zinaweza kueleweka sana. marekebisho au uchunguzi wa hitilafu zinaweza kufanyika kwa haraka.

### Umri ni nambari tu - Uimara na Uvumbuzi wa Mavens

Kwa kweli, Maven imekuwepo kwa muda mrefu na muundo wake labda hautoshelezi viwango vya sasa. Hata hivyo, ushupavu wa Maven umeruhusu kubadilika na kuendelea kukua. Maven hufanya kazi kwa uhuru bila kujali mradi wako. Faili za ujenzi zinaweza kutumika upya kwa urahisi. Programu-jalizi hufanya kazi kwenye eneo salama na zinafanya kazi kwa uhuru na bila kujali toleo la Java au Maven. Muundo huu unakuza utulivu na utabirika na inafanya kuwa rahisi kusimamia mchakato wa ujenzi wenye utata bila migogoro isiyotarajiwa.

### Hitimisho

Hivi siku hizi, mazingira ya maendeleo yamejaa kazi nyingi na teknolojia kwa watengenezaji. Katika kutafuta urahisi na
utomatiki, Gradle imeibuka kama chombo cha kujenga cha kisasa lakini imeleta changamoto zake. Bila shaka, dhana ya 
Gradle ni nzuri! Lakini kutokana na ugumu na muda uliotumiwa katika skripti za kujenga za Gradle, swali linajitokeza ikiwa 
si rahisi zaidi kuboresha Maven. Kwa kutumia programu-jalizi na upanuzi, Maven inaweza kuboreshwa na kuwa rahisi wakati wowote.
Je! Kwa nini isiwe afadhali na endelevu zaidi kuendeleza badala ya kwenda kutumia teknolojia nyingine baada ya nyingine?

### Viungo

* [Rudi kutoka Gradle hadi maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### Wasiliana nasi

[Tatizo la GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).```
