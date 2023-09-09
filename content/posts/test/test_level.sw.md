---
title: "Ngazi za Mtihani: Kupata usawa sahihi"
date: 2023-05-31
author: "Nova Annabella"
slug: test_level
tags: [ Testing, Software Testing, Test Levels, Mock Tests, Unit Tests, Integration Tests, Component Tests, Contract Tests, End-to-End Tests ]
categories: [ Technology, Software Development, Quality Assurance ]
description: "Pata usawa sahihi unapochagua ngazi sahihi za majaribio kwa mitihani ya programu"
draft: false
images:
  - "/images/content/martin_fowler_testing.png"
card: "summary_large_image"
---


# Majaribio Ya Ngazi: Kupata Usawa Sahihi

[![testebenen](/images/content/martin_fowler_testing.png)](https://martinfowler.com/articles/microservice-testing/)

### Utangulizi

Mada ya Upimaji inaonekana kuwa eneo jipya hadi leo lenye nafasi nyingi za tafsiri. Piramidi ya upimaji ya jadi 
ilihojiwa na piramidi mpya za upimaji zimeibuka. Kwa maoni yangu, hakuna haja ya 
piramidi ya upimaji, ila tu uelewa wazi kuhusu kile kinachotakiwa kupimwa. Mitihani kwenye viwango vya chini mara nyingi 
ni chini ya utambuzi. Mkazo unapaswa kuwa hasa kwenye upimaji wa tabia, kuhakikisha kuwa 
API
au UI inafanya kazi kama inavyotakiwa. Muhtasari kamili wa aina za upimaji zinazowezekana unaweza kupatikana hapa: 
[Martinfowler Upimaji](https://martinfowler.com/articles/microservice-testing/).


### Ngazi 1 - Mitihani ya Mazoezi & Mitihani ya Kitengo

Lengo: Kutumia sehemu ndogo zaidi zinazoweza kujaribiwa za programu katika maombi, ili kubainisha kama zinafanya kazi
kama ilivyotarajiwa. Mitihani ya Mock na Unit inaweza kuwa na athari kinyume na kusababisha usumbufu mara kwa mara
katika mchakato wa maendeleo. Mitihani hii mara nyingi iko kando na muktadha na ina uhusiano mdogo na uhalisia. Mara
nyingi hutumika tu kuendeleza kazi zisizo na maana kupitia mitihani ya Unit iliyopo. Mara Mocks zinapoongezwa, inakuwa
kama kujishughulisha. Matokeo yanayotarajiwa kutoka kwa mitihani ya Mock yamepunguzwa kwa kile kilichofafanuliwa kwenye
Mock ya asili. Wateja wa mwisho hawajali kazi za ndani. Kwa mfano, katika hali ya kuingia `loginUser(name, password,
securityAlgorithmus)`. Ikiwa mtihani wa Unit unafanya ukaguzi wa Null kwenye parameter ya `securityAlgorithm`,
kinajaribiwa kikubwa mno, kwani watumiaji hawawezi kuweka parameter ya `securityAlgorithm`.

### Ngazi 2 - Mtihani wa Ujumuishaji

Lengo: Kupitia njia za mawasiliano na mwingiliano kati ya sehemu kwa kutambua Hitilafu za kiolesura. Majaribio ya
ushirikiano hutoa ufahamu wa thamani kuhusu uwezo na uhuru wa sehemu tofauti za Programu. Na vifaa vya uigaji vichache,
mitihani inakuwa rahisi kuelewa. Baa, wanaendelea kukosa muktadha, na kuna hatari kwamba majaribio ya ushirikiano ni tu
mitihani ya kitengo iliyofichwa na vifaa vya uigaji vichache.

### Ngazi ya 3 - Mtihani wa Kiungo

Kusudi: Kupunguza kiasi cha programu iliyotestwa kwenye sehemu ya mfumo wa kuchunguzwa, kuendesha mfumo kupitia
viunganishi vya ndani vya kificho na kutumia vipimo vya mara mbili ili kuziweka nje sehemu za kificho zinazotestwa
kutoka kwa viungo vingine.  Majaribio ya viungo hutoa habari nyingi kuhusu ubora na uwezo wa programu. Badala ya Kuiga,
unajaribu programu yako kwa mwisho. Ufafanuzi kati ya majaribio ya sehemu na majaribio ya mwisho hadi mwisho sio una
maana kubwa. Pamoja na mazingira mazuri ya majaribio, mipaka kati yao mara nyingi hufifia, kwa hivyo kupima tabia halisi
inakuwa inawezekana badala ya kazi zilizotengwa na zisizo na muktadha. Hata hivyo, kuunda darasa za ziada za majaribio
kama vile mabanzi ya mfumo, fakes na kuiga kwenye kificho cha uzalishaji kunaweza kuongeza kazi ya ziada ya kudumisha.

### Ngazi ya 4 - Mtihani wa Mkataba

Kusudi la kizuizi hiki cha kificho ni kuangalia mwingiliano kwenye mipaka ya huduma ya nje na kuthibitisha kwamba
inaendana na mahitaji ya mkataba wa huduma inayotumika. Majaribio ya Mkataba mara nyingi yanafanana na majaribio ya
sehemu, na tofauti kati yao ni ndogo. Baadhi ya waendelezaji huunganisha majaribio haya na Majaribio ya Pact, ambayo
kimsingi hufanya kazi kama majaribio ya kitengo na seva kati. Hata hivyo, gharama ya kudumisha majaribio haya inaweza
isiwe ya thamani. Kwa mfano, Jaribio la Pact linaweza jaribu API ya REST `loginUser?name=aa&password=bb)` na kutarajia
jibu la mfumo wa JSON, ambalo awali lilipakiwa kwenye seva ya Pact. Mfumo huu ni wa kudumu na unaweza kuathiriwa na
makosa kama vile muundo mbaya wa tarehe au maeneo ya wakati katika jibu la API. Athari hasi zinaweza kuwa kubwa sana.

### Ngazi 5 - Mwisho hadi Mwisho Mtihani (pia unaitwa Maboxi Meusi-Mtihani)

Kusudi: Kagua ikiwa mfumo unatimiza mahitaji ya nje na kufikia malengo yake kwa kujaribu mfumo mzima kutoka mwanzo hadi
mwisho. Majaribio ya mwisho hadi mwisho ni ya kuaminika na imara. Mara baada ya vizuizi vya kujenga mazingira ya
uchunguzi kuvukwa, juhudi hulipa. Majaribio haya huiga tabia halisi na kuondoa haja ya vitsauzi vya kimakebelieve.
Hitilafu hutokea nadra na ni rahisi kunakili kwa urahisi kimahali. Ufuatiliaji wa hitilafu na uendeshaji wa leja za
kwenye uzalishaji kwa kiasi kikubwa zinazuiliwa, pamoja na matukio nadra. Waendelezaji kwa nadra hufanya kazi na, ikiwa
kabisa, data za uzalishaji, ambazo hupunguza uwajibikaji na kuongeza umakini. Zaidi ya hayo, uautomatishaji kama vile
sasisho za programu moja kwa moja huwezesha utekelezaji kwani tabia tayari imejaribiwa. Kuna faida zingine zaidi! Mara
tu majaribio yameandikwa kwa njia inayoweza kutumika tena, yanaweza kuunganishwa katika majaribio ya mzigo ili kupata
picha kamili ya utendaji. Majaribio haya pia yanaweza kuendeshwa kila wakati kwenye mazingira ya uzalishaji na kutoa
maoni ya muda halisi juu ya hali ya taratibu anuwai. Ikiwa sehemu ya mfumo, kama huduma ya REST ya nje, itaenda nje ya
mtandao, inaweza kutambuliwa mara moja ni utaratibu upi wa mtumiaji ulioathiriwa.

### Hitimisho

Kwa ufupi, upimaji ni sehemu muhimu ya maendeleo ya programu, na uchaguzi wa viwango vya upimaji unategemea mahitaji na malengo maalum ya programu. Wakati Mock-Tests na Unit-Tests zinaweza kuwa na ufanisi mdogo, mitihani ya integration na mitihani ya sehemu inatoa mwanga muhimu juu ya tabia na utendaji wa programu. Contracttests husaidia kuthibitisha mwingiliano na huduma za nje, lakini mipaka yako kwa mitihani ya sehemu wanaweza kuwa ndogo. Mwishowe, mitihani ya mwisho kwa mwisho inatoa kiwango cha juu zaidi cha uaminifu katika utendaji wa mfumo na kuwezesha upimaji kamili wa programu yote. Kwa kuchagua viwango sahihi vya upimaji na kuunganisha kwa ufanisi, watengenezaji wanaweza kuhakikisha ubora, uaminifu na uthabiti wa programu yako.

### Mawasiliano

[Matatizo ya GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
