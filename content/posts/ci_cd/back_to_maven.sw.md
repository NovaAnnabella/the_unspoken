---
title: "Kurudi kwa Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: Die schwer fassbare Suche nach Einfachheit und eine kurze Reise zur Wiederentdeckung der Macht von Maven.
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---



# Kurudi kwa Maven?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

## 10 Jahre Gradle. Auf der Sucher nach Erleichterung und eine kurze Reise zur Wiederentdeckung der Stärke von Maven. 

## Miaka 10 ya Gradle. Katika kutafuta unafuu na safari fupi ya kugundua upya nguvu za Maven.

## Überblick Dies ist ein Beispieltext für eine Markdown-Datei. Mit Markdown können Texte einfach formatiert werden.
## Überschriften Es gibt sechs verschiedene Überschriften, die mit einem `#` beginnen und mit jedem zeichen weniger
deutlicher werden.  ### Einleitung Die Einleitung sollte zusammenfassen, worum es in der Markdown-Datei geht. ##
Absätze Absätze werden durch eine leere Zeile voneinander getrennt. ## Links Links können mit eckigen Klammern und
runden Klammern erstellt werden. Zum Beispiel: [Google](https://www.google.com) ## Bilder Bilder können auf ähnliche
Weise wie Links eingefügt werden. Zum Beispiel: ![Ein Bild](https://via.placeholder.com/150) ## Listen Es gibt zwei
Arten von Listen: ungeordnete und geordnete Listen. - Ungeordnete Listen beginnen mit einem Bindestrich. - Geordnete
Listen beginnen mit einer Zahl gefolgt von einem Punkt. ## Zitate Zitate werden mit einem `>` am Anfang der Zeile
markiert. > Hier ist ein Beispiel-Zitat.  ## Code Code kann mit einem Backtick (`) gekennzeichnet werden. Auch Code-
Blöcke können formatiert werden: ```html <html>  <head>   <title>Meine Webseite</title>  </head>  <body>
<h1>Willkommen auf meiner Webseite!</h1>  </body> </html> ```

### Kuongeza uwezo wa wahandisi - Tunahitaji zaidi ya zana za kuokoa muda

Mada ambazo mara nyingi huwa hazipewi kipaumbele au kutajwa sana, zinanivutia. Mara nyingi teknolojia za wakati huu
zinafanya kazi vizuri, lakini hakuna yeyote anayeongelea matatizo yake. Maendeleo yamekuwa magumu sana leo hii. Kwa
maneno mengine, wataalamu ni wachache na kila mara kuna kitu kinachopuuzwa kwa sababu ya kazi nyingi za ziada kama
"Serverless", "Low Code", "IaC", "Big Data", "Cloud", "DevOps", "You Build it You run it", na kadhalika. Kwa hivyo,
automesheni na kupunguza muda ni muhimu sana. "Usinichoshe" na "Inafanya kazi mara tu sawa" ni alama nzuri ya ubora
ambayo sijaiona katika Gradle. Kuwa na haki, Gradle sio chombo pekee cha kisasa kinachofanya kazi badala ya kuiwezesha.

### Kutafuta Urahisi na Utoaji wa Huduma za Kiotomatiki kwa Udanganyifu

Tangu SOAP, nina chuki kali dhidi ya usanifu wa XML. Kwa kutumia Gradle, nilikuwa natarajia kuandika skripti za bind
kuwa rahisi sana lakini matumaini yangu na motisha ilizidi kupungua kila mara. Gradle inataka uchangamke lakini kwa
gharama ya uhuru na ubora. Watengenezaji wanaongozwa na mwenendo bila kujali athari kwa uaminifu wa programu. Kuweka
skripti za ujenzi wa Gradle rahisi na za kudumisha, inahitaji nidhamu kali. Aina hii ya nidhamu ni nadra sana kupatikana
kwenye msimbo wa chanzo na kwa hiyo ni nadra sana kwenye skripti za ujenzi.

### Tafsiri na Suluhisho - Wakati hati za ujenzi zinapokuwa changamoto

Gradle haifanyi kazi tofauti sana na Maven kwa nyuma. Kwa hivyo, tafsiri kadhaa zinahitajika. Vipengele kama Katalog ya
Utegemezi, Plugin ya Utoaji ya Maven, Dependabot, na mengi zaidi ni ufumbuzi wa kazi kwa kazi za msingi ambazo Maven
tayari ina. Kwa uwezo wa Gradle, mara nyingi ujenzi wa maandalizi ya maendeleo huchanganyikiwa sana na ni ngumu
kusimamia. Programu-jalizi za Gradle mara nyingi zina shida za utangamano, mipaka, au maendeleo ya kikomo. Shida hizi
hutokana na mabadiliko ya mazingira ya Gradle, aina anuwai ya mazingira ambayo Gradle hutumiwa, na juhudi maalum za
utekelezaji na matengenezo kwa kila programu-jalizi. Kila kitu kimeunganishwa.

### Domino athari za Gradle - Skenariyo la ndoto mbaya katika ulimwengu wa kweli.

Sijapata huduma nyingi za Microservices ambazo hazikuwa na umri wa miaka mingi na tayari hawakuweza kuendelea kudumisha
kutokana na Gradle. Tunapaswa kuzingatia kwamba hii sio mara ya kwanza kwangu kuona kitu kama hiki, na hapana, hawakuwa
wanaendeleza. **Kazi yangu ilikuwa kufanya toleo la Spring Boot 2.x kwa 2.7**. SPOILER: Niliketi baada ya mwaka mmoja!
Matatizo kwa ufupi: * Kwa ajili ya faili ya ujenzi wa Gradle -> Punguza hadi kwenye toleo la Java la ndani la 11 (WTF)
(Kwa kawaida, Java ni sambamba kulingana na toleo - kuna zana za kukabiliana tena hapa kama SdkMan...) * Kwa ajili ya
Sas

### Kugundua upya nguvu ya Maven - Kutumia uchawi wa Maven

Hapa kuna vipengele vyangu vipendwa vya Maven: Vifaa vinaweza kuzinduliwa na kusanidiwa moja kwa moja kutoka kwa mstari
wa amri bila kuwa tayari vimeshatengenezwa. Zaidi ya hayo, kwa kiasi kikubwa vina uhuru kutoka kwa mipangilio mingine ya
vifaa. | Amri ya mfano             | Maelezo
| Kiungo                                 | |---------------------------------------|---
------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------|--------------------------------------------------------------
----------| | `mvn versions:use -latest-versions`  | Kubadilisha toleo - nani anahitaji Dependabot? Ndiyo, miradi yangu
imesasishwa kwa miaka bila shida kwa toleo jipya zaidi, bila ombi la kuunganisha kuchukiza. |
https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html | | `mvn versions:set -DnewVersion=1.0.0` |
Kuweka toleo la mradi ...
| https://www.mojohaus.org/versions/versions-maven-plugin/index.html    | | `mvn license:add-third-party`     |
Orodha ya tegemezi na kuonyesha leseni zao (inaweza kushindwa hata kwa leseni zilizozuiliwa)
| https://www.mojohaus.org/license-maven-plugin/index.html         | Orodha hii inaweza kuendelea na kuendelea.
Kwa njia fulani inanikumbusha hatua za GitHub Workflow.
![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

### Je, hupendi XML?

Hakuna tatizo! Andika tu faili yako ya kujenga katika `ruby`,`groovy`,`scala`,`yaml`,` atom` au `Java`. Uuzaji wa
Polygot (https://github.com/takari/polyglot-maven) unawezesha hii. Kujaribu, tuendeshe tu `mvn io.takari.polyglot:
polyglot-translate-plugin: tafsiri -Dinput=pom.xml -Doutput=pom.yaml` na ndani ya millisecond chache faili ya kujenga
yako itakuwa imebadilishwa. Ni jambo la kusikitisha kwamba hakuna mtumiaji wa kuaminika wa Maven <> Gradle :( Ndani ya
Maven Build Files ni kubwa lakini ni rahisi sana kueleweka. Ubadilishaji wa marekebisho au uboreshaji unaweza kufanywa
haraka.

### Umri ni tu nambari - Mavens Uimara na Kuendelea

Kwa kweli, Maven imekuwepo kwa muda mrefu na muundo wake labda haufai viwango vya sasa. Hata hivyo, uimara wa Maven
umewezesha kuendelea kubadilika na kukua. Maven inafanya kazi kwa uhuru bila kujali mradi wako. Faili za ujenzi zinaweza
kutumika tena kwa urahisi. Vifaa vya ndani hufanya kazi ndani ya Sanduku na ni huru kutoka kwa kila mmoja na kutoka kwa
toleo la Java au Maven. Ubunifu huu unachochea ustahimilivu na unatabirika na unafanya iwe rahisi kudhibiti mchakato
ngumu wa ujenzi bila migongano isiyotegemewa.

### Hitimisho

Leo hii, mazingira ya maendeleo yamejaa kazi nyingi na teknolojia kwa watengenezaji. Kujaribu kupata urahisi na
otomesheni, Gradle kama chombo cha ujenzi cha kisasa kimejitokeza, lakini kimeleta changamoto zake za kipekee. Bila
shaka, dhana ya Gradle ni nzuri! Lakini kwa ujumla wa ugumu na muda uliotumika katika hati za ujenzi wa Gradle,
kunajitokeza swali kama ingekuwa rahisi zaidi kuongeza uwezo wa Maven. Kwa programu-jalizi na nyongeza, Maven inaweza
daima kufanywa mpya na rahisi. Je! Kuendeleza sio zaidi ya kuvutia na endelevu kuliko kwenda kutoka teknolojia moja hadi
nyingine?

### Viungo

* [Kurudi Nyuma Kutoka kwa Gradle hadi maven](https://phauer.com/2018/kurudi-nyuma-kutoka-kwa-gradle-hadi-maven/)

### Mawasiliano

[GitHub Masuala](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
