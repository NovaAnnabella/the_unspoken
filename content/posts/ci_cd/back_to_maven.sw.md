---
title: "Rudi kwa Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "Utafutaji mgumu wa urahisi na safari fupi ya kugundua tena nguvu ya Maven."
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# Kurudi kwa Maven?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

## Miaka 10 ya Gradle. Katika kutafuta urahisi na safari fupi ya kugundua tena nguvu ya Maven.



### Kuongeza Uwezo wa Watengenezaji - Tunahitaji Zana Zaidi za Kuokoa Muda

Mada ambazo mara nyingi zinapuuzwa au mara chache zinajadiliwa zinanivutia. Mara nyingi teknolojia cool zinatumika,
lakini karibu hakuna mtu anayezungumzia matatizo yanayohusiana nayo. Maendeleo yamekuwa ya gharama kubwa siku hizi. Kwa
maneno makubwa kama "Serverless", "Low Code", "IaC", "Big Data", "Cloud", "DevOps", "You Build it You run it" nk.
Wakitengenezaji tayari wana zaidi ya kazi za ziada za kushughulikia. Kazi zaidi, inamaanisha hakuna tena Wataalamu wapo
na kila wakati kitu fulani kinapuuzwa kwa sababu ya umakini. Ndiyo sababu automation na kuokoa wakati ni muhimu sana
muhimu. "Usinifanye nifikirie" na "Inafanya kazi nje ya Box" tayari ni sifa nzuri za ubora ambazo sijaziona katika
Gradle bado siweza kuona. Kuwa fair, Gradle sio zana pekee ya kisasa inayotufanyia kazi, badala ya kuturahisishia.

### Utafutaji wa illusory wa Urahisi na Utautomatishaji

Tangu SOAP, nina chuki iliyojikita sana dhidi ya usanidi unaotegemea XML. Na Gradle, nilikuwa natumaini, kwamba kuandika
skripti za Bind itakuwa mchezo wa watoto. Kwa bahati mbaya, matumaini yangu na motisha yangu yalipungua kila wakati.
Gradle inalenga kwenye utofauti na inatoa kafara kwa ajili ya automatiseringi na ubora. Waendelezaji na waendelezaji
hufuata kwa kipofu mtindo huo bila kuzingatia athari kwa kuaminika kwa programu. Kuweka skripti za kuunda za Gradle kuwa
rahisi na zenye matunzo ya chini, inahitaji nidhamu kali. Nidhamu kama hiyo ni nadra sana kupatikana katika msimbo wa
chanzo na ndiyo maana ni nadra zaidi katika skripti za ujenzi.

### Tafsiri na Mbinu za Muda - Wakati Skripti za Ujenzi Zinapokuwa Changamoto

Gradle hufanya kazi nyuma ya pazia sio tofauti sana na Maven. Kwa hivyo, baadhi ya tafsiri zinahitajika. Vipengele kama
Catalog ya Dependency, Plugin ya Release ya Maven, Dependabot na zingine nyingi ni mbinu za kufanya kazi kwa matatizo ya
msingi ambayo Maven tayari inaleta. Kwa kutumia uwezo wa Gradle mara nyingi hutokea usanidi wa kujenga utata, ambayo ni
ngumu kudumisha. Plugins za Gradle mara nyingi zina matatizo ya utangamano, mipaka au maendeleo ya kikomo. Matatizo haya
hutokea kutokana na asili inayoendelea ya mfumo wa eco wa Gradle, aina anuwai ya mazingira ambayo Gradle imewekwa
kutumiwa, na gharama maalum ya kutekeleza na kudumisha kila Plugin. Kila kitu kinaunganishwa pamoja.

### Athari ya Mnyororo wa Gradle - Hali ya Kusikitisha katika Ulimwengu Halisi

Nimeona huduma nyingi ndogo ambazo ni za miaka michache tu na tayari hazikuwezeshwa tena kwa sababu ya Gradle.
Ni muhimu kusema kuwa hii sio mara ya kwanza nimeona hivi, na hapana, hawakuwa Devs wa Junior.

**Kazi yangu ilikuwa kuboresha Spring Boot 2.x hadi 2.7**. Spoiler: Nilikata tamaa baada ya mwaka mmoja!
Matatizo kwa ufupi:

* Faili ya Gradle-Build inahitaji -> Kushusha hadhi toleo langu la Java hadi 11 (WTF) (Kawaida Java
  inaendana nyuma - kuna pia zana nyingine za muda wa ziada za SdkMan...)
* Sasisho la Spring Boot linahitaji -> Sasisho la Gradle (WTF)
* Sasisho la Gradle linahitaji -> Sasisho la Plugin
* Sasisho la Plugin linahitaji -> Sasisho la Groovy (WTF)
* Sasisho la Groovy linahitaji -> Sasisho la Test-Framework na sasisho za Test (WTF)
* Sasisho la Test-Framework linahitaji -> Sasisho za Utawala
* \[...]
  Zaidi ya hayo, programu-jalizi kadhaa hazifanyi kazi na matoleo mapya ya Gradle, zingine hazijaendelezwa tena,
  hazikenani na programu-jalizi zingine, zinafanya kazi tu na Gradle KTS, sio na Gradle Groovy, au
  wana mipaka. Hata programu-jalizi kutoka kwa watoa huduma wakubwa kama Spring wana utendaji mdogo ukilinganisha na programu-jalizi zao za Maven.
  Mwishowe, nilikuwa na faili fupi, nzuri ya kujenga Gradle ambayo hakuna mtu anayeweza kuitunza vizuri,
  hata watengenezaji ambao waliandika, na bado wanapenda Gradle. Ninajua tu wachache ambao
  kuchukua maandiko ya Gradle kwa uzito au kuandika.

### Ugunduzi wa nguvu za Maven tena - Kutumia uchawi wa Maven

Hapa kuna vipengele vyangu vipendwa vya Maven:
Vijalizo vinaweza kuzinduliwa na kusanidiwa moja kwa moja kutoka kwa mstari wa amri, bila haja ya kufafanuliwa mapema.
Zaidi, viko huru kabisa kutoka kwa mipangilio mingine ya vijalizo.

| Amri za Mfano                         | Mwongozo                                                                                                                                                                          | Kiungo                                                                      |
|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`   | Sasaisha toleo - nani anahitaji Dependabot? Ndio, miradi yangu imekuwa ikisasaishwa kwenye toleo jipya bila maswala yoyote yanayosumbua ya muungano wa maombi kwa miaka            | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html    |
| `mvn versions:set -DnewVersion=1.0.0` | Weka toleo la mradi...                                                                                                                                                            | https://www.mojohaus.org/versions/versions-maven-plugin/index.html          |
| `mvn license:add-third-party`         | Orodhesha tegemezi na uonyeshe leseni zake (zinaweza hata kushindwa kwa leseni zilizotengwa)                                                                                        | https://www.mojohaus.org/license-maven-plugin/index.html                    |

Orodha hii inaweza kuendelea milele. Inanikumbusha hatua za mtiririko wa kazi wa GitHub.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)


### Hupendi XML?

Hakuna Tatizo! Andika tu faili yako ya Build katika `ruby`, `groovy`, `scala`, `yaml`, `atom` au `Java`. Ugani wa Polygot (https://github.com/takari/polyglot-maven) unafanya iwezekane. Kwa kujaribu tu,
tekeleza`mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` na kwa milisekunde chache faili yako ya Build imekamilishwa. Ni jambo la kusikitisha hakuna tafsiri nzuri ya Maven <> Gradle inayoaminika:(
Ndiyo, Faili za Build za Maven ni kubwa, lakini pia ni rahisi kuelewa. Marekebisho au utatuzi wa matatizo unaweza kufanywa kwa muda mfupi.

### Umri ni namba tu - Utulivu na Mageuzi ya Mavens

Kwa hakika, Maven amekuwepo kwa muda mrefu na aesthetics yake huenda hailingani na viwango vya leo. Lakini, umri wa
Maven umemwezesha kubadilika na kuendelea kukua. Maven anafanya kazi kwa uhuru kutoka kwa mradi wako. Faili za ujenzi
zinaweza kutumika tena kwa urahisi. Viambatisho vinafanya kazi katika sandbox na ni huru kutoka kwa kila mmoja na kwa
toleo la Java au Maven. Muundo huu unaendeleza utulivu na utabiri na hufanya iwe rahisi kusimamia michakato ya ujenzi
ngumu bila migogoro isiyotarajiwa.

### Hitimisho

Siku hizi, mazingira ya maendeleo yamejaa kazi nyingi na teknolojia kwa waendelezaji. Katika kutafuta urahisi na
automatisering, Gradle imejitokeza kama chombo cha kisasa cha kujenga, lakini imeleta changamoto zake mbinu. Hakuna
shaka, wazo la Gradle ni zuri! Lakini kwa kuzingatia utata na wakati unaotumika katika scripts za kujenga Gradle, swali
linajitokeza ikiwa ingekuwa rahisi zaidi kupanua Maven jaribu. Kwa vidonge na upanuzi, Maven inaweza kusasishwa na
kuhuishwa wakati wowote. Je, si ingekuwa maendeleo zaidi ya kufurahisha na endelevu, badala ya kuruka kutoka teknolojia
moja kwenda nyingine?

### Viungo

* [Kurudi Nyuma kutoka Gradle hadi maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### Mawasiliano

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
