---
title: Testebenen: Kupata usawa wa haki
date: 2023-05-31
author: "Nova Annabella"
slug: test_level
tags: [ Testing, Software Testing, Test Levels, Mock Tests, Unit Tests, Integration Tests, Component Tests, Contract Tests, End-to-End Tests ]
categories: [ Technology, Software Development, Quality Assurance ]
description: Kupata usawa sahihi katika kuchagua viwango sahihi vya majaribio ya programu.
draft: false
images:
  - "/images/content/martin_fowler_testing.png"
card: "summary_large_image"
---


# Testebenen: Kupata usawa sahihi

[![testebenen] (/picha/maudhui/martin_fowler_testing.png)] (https://martinfowler.com/articles/microservice-testing/)

### Utangulizi

Das Thema Testing scheint bis heute noch Neuland mit sehr viel Freiraum für Interpretation zu sein. Die traditionelle
Testpyramide wurde in Frage gestellt und neue Testpyramiden sind entstanden. Meiner Meinung nach benötigt es keine
Testpyramide, sondern ein klares Verständnis dafür, was getestet werden muss. Die Tests auf niedrigeren Ebenen sind oft
weniger aussagekräftig. Der Fokus sollte vor allem auf dem Testen des Verhaltens liegen, um sicherzustellen, dass die
API oder UI wie gewünscht funktioniert. Eine umfassende Übersicht über mögliche Testarten ist hier zu finden:
[Martinfowler Testing](https://martinfowler.com/articles/microservice-testing/).

### Level 1 - Majaribio ya Uongo & Majaribio ya Vitengo

Lengo: Kutekeleza sehemu ndogo zaidi za programu katika maombi ili kubaini ikiwa zinafanya kazi kama ilivyotarajiwa.
Mock-Tests na Unit-Tests wanaweza kuwa kinyume cha uzalishaji na mara nyingi wanazuia mchakato wa maendeleo. Vipimo hivi
mara nyingi vimejitenga na muktadha na havina uhusiano na ukweli. Mara nyingi hutumika tu kuendeleza vipengele
visivyohitajika juu ya Unit-Tests vilivyopo. Mara tu ukweli unaongezwa, unakuwa shughuli ya ndani. Matokeo
yanayotarajiwa kutoka kwa Mock-Tests yanahusiana na kile kilichoelekezwa kwenye ujanja wa awali. Wateja hawajali kuhusu
shughuli za ndani. Kwa mfano, katika kisa cha Login "loginUser (jina, nywila, algorithmus ya usalama)". Ikiwa Unit-Test
inafanya uhakiki wa sifuri kwenye kipengee cha "algorithm ya usalama", ni mtihani sana kwani watumiaji hawawezi kuweka
kipengee cha "algorithm ya usalama".

### Kiwango cha 2 - Jaribio la Ushirikiano

Zweck: Kuthibitisha njia za mawasiliano na uingiliano kati ya vipengele kwa kutambua kasoro za interface. Mitihani ya
Integretion hutoa ufahamu muhimu juu ya utendaji na uhuru wa sehemu mbalimbali za programu. Kwa kutumia zana chache za
uonevu (mocks), mitihani huwa rahisi. Hata hivyo bado hawana mazingira yanayohusiana na nafasi ya uwezekano wa kuwa
mitihani ya uchambuzi wa sehemu na zana chache za uonevu (mocks).

### Ngazi ya 3 - Jaribio la Kiungo

Lengo: Kupunguza kiasi cha programu inayopimwa kwa sehemu ya mfumo wa kupima, kufanya upotoshaji wa mfumo kupitia
vipengee vya ndani vya nambari na kutumia Testdoubles kwa kufunga nambari inayopimwa kutoka kwa sehemu nyingine. Vipimo
vya sehemu hutoa habari nyingi kuhusu ubora na ufanisi wa maombi. Badala ya uigaji wa vipengele vyako, unajaribu maombi
yako kwa kweli. Mstari kati ya vipimo vya sehemu na vipimo vya mwisho-hadi-hadi sio mkubwa. Kwa mazingira mazuri ya
upimaji, mipaka kati yao mara nyingi huwa haieleweki, hivyo kupima tabia halisi badala ya kazi iliyosimamishwa na pasipo
muktadha huwa na uwezekano. Walakini, uundaji wa darasa la majaribio kama vile Komponenten-Stubs, Fakes na Mocks katika
nambari ya uzalishaji unaweza kuleta mzigo wa ziada wa matengenezo.

### Level 4 - Jaribio la Mkataba

Madhumuni ya kifungu hiki cha nambari ni kuangalia mwingiliano kwenye mpaka wa huduma ya nje na kuhakikisha inakidhi
mahitaji ya mkataba wa huduma inayotumia. Vipimo vya Mkataba mara nyingi vinakaribiana na vipimo vya sehemu, na tofauti
kati yao ni ndogo. Baadhi ya waendelezaji huunganisha vipimo hivi na vipimo vya Pact, ambavyo kimsingi hufanya kazi kama
vipimo vya Unittests na seva kati yake. Hata hivyo, gharama ya kuendeleza vipimo hivi inaweza kuwa haiendani na thamani
yake. Kwa mfano, vipimo vya Pact vinaweza kujaribu `loginUser?name=aa&password=bb)` ya API ya REST na kujibu kwa
kutarajia mfumo wa JSON uliohifadhiwa awali kwenye seva ya Pact. Mfumo huu ni statiki na unavunjika kwa urahisi, kama
vile muundo sahihi wa tarehe au muda kwenye jibu la API. Madhara hasi yanaweza kuwa makubwa.

### Kiwango cha 5 - Vipimo vya Mwisho hadi Mwisho (pia huitwa Vipimo vya Sanduku Jeusi)

Malengo: Kuhakiki ikiwa mfumo unaingiliana na mahitaji ya nje na kufikia malengo yake kwa kufanyiwa jaribio kutoka
mwanzo hadi mwisho wa mfumo.  Vipimo vya mwisho-hadi-mwisho ni imara na vinapatikana kwa urahisi. Mara baada ya kuvuka
vizuizi vya usanidi wa mazingira ya majaribio, juhudi zinakua na manufaa. Majaribio haya husimulisha tabia za kweli na
kufuta haja ya Mocks. Makosa hutokea ya nadra sana na ni rahisi kujirudia eneo la tukio. Kazi kubwa ya kutatua makosa na
kuongoza michakato kwenye uzalishaji huwekwa kwa kiwango cha chini kabisa pamoja na visa vidogo sana. Timu ya
Watengenezaji huenda ikafanya kazi mara chache sana, kama kabisa, na data ya uzalishaji, ikipunguza jukumu lao na
kuongeza umakini wao. Aidha, uwezekano wa kufanya kazi kwa urahisi unaongezeka kwa kuwezesha kiotomatiki kwa
uppdateringen programvaran kwani tabia tayari imeshajaribiwa. Kuna faida zingine! Mara tu vipimo vinapoitwa kwa namna
inayoweza kutumika tena, vinaweza kujumuishwa katika vipimo vya mizigo kwa ufahamu mpana wa kazi. Majaribio haya
yanaweza pia kutumiwa kwa uwazi kwenye mazingira ya uzalishaji na kutoa ufahamu wa muda halisi wa hali ya hatua
mbalimbali. Ikiwa sehemu ya mfumo kama huduma ya nje ya REST, itashuka, ni rahisi kutambua mara moja mifumo gani ya
watumiaji inayoathiriwa.

### Hitimisho

Kwa ufupi, kupima ni sehemu muhimu ya maendeleo ya programu, na chaguo la viwango vya upimaji linategemea mahitaji na
malengo maalum ya programu. Ingawa vipimo vya bandia na vipimo vya kitengo vinaweza kuwa na ufanisi mdogo, vipimo vya
ushirikiano na vipimo vya vipengele hutoa ufahamu muhimu juu ya tabia na utendaji wa programu. Vipimo vya mkataba
husaidia kuangalia mwingiliano na huduma za nje, lakini kiwango chake cha utofautishaji na vipimo vya vipengele kinaweza
kuwa kidogo. Hatimaye, vipimo vya mwisho hadi mwisho hutoa kiwango cha juu zaidi cha uaminifu katika kazi ya mfumo na
kuruhusu vipimo kamili vya programu nzima. Kwa kuchagua viwango sahihi vya upimaji na kuunganisha kwa ufanisi,
watengenezaji wanaweza kuhakikisha ubora, uaminifu, na utulivu wa programu yao.

### Wasiliana

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
