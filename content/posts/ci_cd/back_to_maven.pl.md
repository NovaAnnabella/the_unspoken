---
title: "Powrót do Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "Nieuchwytne poszukiwanie prostoty i krótka podróż do ponownego odkrycia mocy Mavena"
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---



# Powrót do Maven?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

## 10 lat Gradle. W poszukiwaniu ulgi i krótka podróż, by na nowo odkryć moc Mavena.



### Maksymalne wykorzystanie potencjału deweloperów - potrzebujemy więcej narzędzi oszczędzających czas

Tematy, które są często pomijane lub rzadko omawiane, interesują mnie. Często w użyciu są fajne technologie, ale mało
kto mówi o problemach z nimi związanych. Rozwój stał się obecnie bardzo kosztowny. Dzięki fajnym hasłom, takim jak
"serverless", "low code", "IaC", "big data", "cloud", "DevOps", "you build it you run it" itp. deweloperzy mają już
dość. itp., programiści mają już więcej niż wystarczająco dodatkowych zadań do wykonania. Więcej zadań oznacza, że
prawie nie ma ekspertów i zawsze coś jest zaniedbywane, aby się na tym skupić. Dlatego automatyzacja i oszczędność czasu
są mega ważne. "Nie każ mi myśleć" i "Działa po wyjęciu z pudełka" to już dobrej jakości funkcje, których jeszcze nie
widzę w Gradle. jeszcze nie widzę. Aby być uczciwym, Gradle nie jest jedynym nowoczesnym narzędziem, które ułatwia nam
pracę zamiast ją ułatwiać. ją ułatwia.

### Iluzoryczne dążenie do prostoty i automatyzacji

Od czasu SOAP miałem głęboko zakorzenioną niechęć do konfiguracji opartych na XML. Miałem nadzieję, że dzięki Gradle że
pisanie skryptów bind będzie dziecinnie proste. Niestety, moje nadzieje i motywacja malały za każdym razem. malały za
każdym razem. Gradle dąży do elastyczności i poświęca dla niej automatyzację i jakość. Deweloperzy ślepo podążają za
Deweloperzy ślepo podążają za trendem, nie zważając na wpływ na niezawodność oprogramowania. Aby Gradle Build było
proste i łatwe w utrzymaniu, wymaga silnej dyscypliny. Taka dyscyplina jest już rzadkością w kodzie źródłowym i dlatego
jest jeszcze rzadsza w skryptach kompilacji.

### Tłumaczenia i obejścia - gdy skrypty kompilacji stają się wyzwaniem

Gradle nie działa dużo inaczej w tle niż Maven. Dlatego konieczne są pewne tłumaczenia. Funkcje takie jak Dependency
Catalog, Maven Release Plugin, Dependabot i wiele innych są w rzeczywistości obejściami dla podstawowych funkcji, które
Maven już oferuje. Elastyczność Gradle często wiąże się ze złożonymi konfiguracjami kompilacji, które są trudne w
utrzymaniu. Wtyczki Gradle często mają problemy z kompatybilnością, ograniczenia lub ograniczone możliwości. Problemy te
pojawiają się ze względu na ewoluujący charakter ekosystemu Gradle, różnorodność środowisk, w których Gradle jest
Gradle, a także specyficznej implementacji i wysiłku związanego z utrzymaniem wymaganego dla każdej wtyczki. Wszystko
jest ze sobą powiązane.

### Efekt domina Gradle - koszmarny scenariusz w prawdziwym świecie

Widziałem wiele mikrousług, które miały zaledwie kilka lat, a już nie były możliwe do utrzymania z powodu Gradle. z
powodu Gradle. Ważne jest, aby wspomnieć, że nie jest to pierwszy raz, kiedy widzę coś takiego i nie, nie byli to Junior
Devs. Moim **zadaniem było wykonanie aktualizacji Spring Boot 2.x do 2.7**. Spoiler: Poddałem się po roku Poddałem się!
Problemy w skrócie: * Plik kompilacji Gradle wymaga -> Downgrade mojej lokalnej wersji Java do 11 (WTF) (Normalnie Java
jest  kompatybilna w dół - ponownie, istnieją narzędzia obejścia, takie jak SdkMan...) * Aktualizacja Spring Boot
wymaga -> Aktualizacja Gradle (WTF) * Aktualizacja Gradle wymaga -> Aktualizacja wtyczki * Aktualizacja wtyczki wymaga
-> aktualizacji Groovy (WTF) * Aktualizacja Groovy wymaga -> Aktualizacja frameworka testowego i testów (WTF) *
Aktualizacja frameworka testowego wymaga -> Aktualizacji zależności. * \[...]  Ponadto niektóre wtyczki nie działają z
nowszymi wersjami Gradle, niektóre nie są już rozwijane, niektóre są niekompatybilne z innymi wersjami Gradle, niektóre
nie są już rozwijane, niektóre są niekompatybilne z innymi wersjami Gradle.  są niekompatybilne z innymi wtyczkami,
działają tylko z Gradle KTS, a nie z Gradle Groovy, lub po prostu mają ograniczenia.  po prostu mają ograniczenia.
Nawet wtyczki od dużych dostawców, takich jak Spring, mają ograniczoną funkcjonalność w porównaniu do ich wtyczek Maven.
ograniczona funkcjonalność. Kończę z fajnym, krótkim plikiem kompilacji Gradle, którego nikt tak naprawdę nie może
utrzymać,  Nawet programiści, którzy go napisali, a wciąż kochają Gradle. Znam bardzo niewiele osób, które  rozumieją
skrypty Gradle i piszą je na poważnie.

### Ponowne odkrywanie mocy Mavena - wykorzystanie magii Mavena

Oto moje ulubione funkcje Mavena: Wtyczki można uruchamiać i konfigurować bezpośrednio z wiersza poleceń bez
konieczności ich wcześniejszego definiowania. nie muszą być definiowane. Ponadto są one w dużej mierze niezależne od
innych konfiguracji wtyczek. | Przykład Polecenie | Opis | Link | |---------------------------------------|------------
------------------------------------------------------------------------------------------------------------------------
---------------------------------|--------------------------------------------------------------------------| | `mvn
versions:use -latest-versions` | Aktualizacja wersji - kto potrzebuje Dependabota? Tak, moje projekty są aktualizowane
do najnowszej wersji od lat bez żadnych problemów i bez irytujących żądań scalania |
https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html | | `mvn versions:set -DnewVersion=1.0.0` |
Ustaw wersję projektu...
| https://www.mojohaus.org/versions/versions-maven-plugin/index.html | | `mvn license:add-third-party` | Wylistuj
zależności i pokaż ich licencje (może się nie udać nawet jeśli licencje są wykluczone) |
https://www.mojohaus.org/license-maven-plugin/index.html | Ta lista mogłaby ciągnąć się w nieskończoność. Przypomina mi
to trochę GitHub Workflow Steps. ![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

### Nie lubisz XML?

Nie ma problemu! Wystarczy napisać plik kompilacji w `ruby`, `groovy`, `scala`, `yaml`, `atom` lub `Java`. Rozszerzenie
Polygot Extension (https://github.com/takari/polyglot-maven) sprawia, że jest to możliwe. Aby je wypróbować wystarczy
uruchomić `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` i po kilku
milisekundach plik kompilacji jest milisekund plik kompilacji zostanie przetłumaczony. Szkoda, że nie ma niezawodnego
tłumacza Maven <> Gradle. :( Tak, pliki kompilacji Maven są duże, ale również bardzo łatwe do zrozumienia. Udoskonalenia
lub debugowanie są wykonywane w mgnieniu oka. zrobione.

### Wiek to tylko liczba - stabilność i ewolucja Mavena

Trzeba przyznać, że Maven istnieje już od dłuższego czasu, a jego estetyka może nie spełniać dzisiejszych standardów.
Jednak długowieczność Maven pozwoliła mu się dostosować i ewoluować. Maven działa niezależnie od od projektu. Pliki
kompilacji można łatwo ponownie wykorzystać. Wtyczki działają w piaskownicy i są niezależne od siebie nawzajem oraz od
wersji Java lub Maven. Taka konstrukcja promuje stabilność i przewidywalność oraz ułatwia zarządzanie złożonymi
procesami kompilacji bez nieoczekiwanych konfliktów. konfliktów.

### Fazit

W dzisiejszych czasach środowisko programistyczne jest przeładowane wieloma zadaniami i technologiami dla programistów.
W poszukiwaniu w poszukiwaniu prostoty i automatyzacji, Gradle stał się nowoczesnym narzędziem do kompilacji, ale
przyniósł ze sobą własne wyzwania. wyzwania. Bez wątpienia koncepcja Gradle jest dobra! Ale biorąc pod uwagę złożoność i
czas zainwestowany w skrypty kompilacji Gradle, pojawia się pytanie, czy nie byłoby prościej rozszerzyć Maven.
rozszerzony. Dzięki wtyczkom i rozszerzeniom Maven może być zawsze odświeżany i upraszczany. Czy Czy dalszy rozwój nie
byłby o wiele bardziej ekscytujący, a także bardziej zrównoważony niż przeskakiwanie z jednej technologii do drugiej?

### Linki

* Powrót z Gradle do maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### Kontakt

[Problemy GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
