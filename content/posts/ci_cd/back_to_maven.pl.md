---
title: "Wróć do Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "Trudne do uchwycenia poszukiwania prostoty i krótka podróż w celu ponownego odkrycia potęgi Maven."
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# Powrót do Maven?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

## 10 lat Gradle. W poszukiwaniu ułatwień i krótkiej podróży do odkrycia siły Maven'a.

Nieznany tekst lub brak tekstu.

### Maksymalizacja potencjału programistów - potrzebujemy więcej narzędzi oszczędzających czas

Tematy, które często są pomijane lub rzadko omawiane, mnie interesują. Często używane są fajne technologie, ale prawie
nikt nie rozmawia o problemach z nimi związanymi. Rozwój stał się dzisiaj bardzo uciążliwy. Z fajnymi słowami kluczowymi
takimi jak "bezserwerowe", "niski kod", "IaC", "przetwarzanie dużych danych", "chmura", "DevOps", "ty to budujesz, ty to
uruchamiasz" itp., programiści mają już więcej niż wystarczająco dodatkowych zadań. Więcej zadań oznacza, że ​​jest
coraz mniej ekspertów i zawsze coś zostaje zaniedbane. Dlatego automatyzacja i oszczędność czasu są mega ważne. "Nie
sprawiaj, aby musiał myśleć" i "działa od razu po wypakowaniu" to już dobre cechy jakościowe, których nie widzę w
Gradle. Aby być uczciwym, Gradle nie jest jedynym nowoczesnym narzędziem, które utrudnia nam pracę zamiast ułatwiać ją.

### Iluzoryczne poszukiwanie prostoty i automatyzacji

Od czasów SOAP mam głęboko zakorzenioną niechęć do konfiguracji opartych na XML. Z nadzieją, że pisanie skryptów
wiążących będzie dziecinnie proste w przypadku Gradle, niestety moje nadzieje i motywacja maleją z każdym razem. Gradle
dąży do elastyczności kosztem automatyzacji i jakości. Deweloperzy ślepo podążają za trendami, nie zwracając uwagi na
skutki dla niezawodności oprogramowania. Aby utrzymać skrypty budowania Gradle proste i łatwe w utrzymaniu, wymagana
jest silna dyscyplina. Taka dyscyplina jest już rzadko spotykana w kodzie źródłowym, a tym bardziej w skryptach
budowania.

### Tłumaczenia i obejścia - kiedy skrypty budowania stają się wyzwaniem

Gradle działa w tle nie różniąc się znacznie od Mavena. Dlatego potrzebne są niektóre tłumaczenia. Funkcje takie jak
Katalog Zależności, Wtyczka Wydania Maven, Dependabot i wiele innych to faktycznie obejścia podstawowych funkcji, które
Maven już ma. Dzięki elastyczności Gradle często pojawiają się złożone konfiguracje budowania, które są trudne do
utrzymania. Wtyczki Gradle często mają problemy z kompatybilnością, ograniczeniami lub ograniczonymi funkcjami. Problemy
te wynikają z rozwijającego się charakteru ekosystemu Gradle, różnorodności środowisk, w których jest stosowany i
specyficznej implementacji i utrzymania każdej wtyczki. Wszystko jest ze sobą powiązane.

### Efekt domina Gradle - scenariusz koszmaru w rzeczywistym świecie.

Zobaczyłem wiele mikroserwisów, które miały zaledwie kilka lat i były już nie do utrzymania z powodu Gradle. Ważne jest, aby wspomnieć, że nie był to pierwszy raz, kiedy coś takiego widziałem i nie, to nie byli juniorzy.

Moim **zadaniem było przeprowadzenie aktualizacji Spring Boot 2.x na 2.7**. Spoiler: po roku się poddałem! Problemy w skrócie:

* Plik Gradle Build wymaga -> downgrade do mojej lokalnej wersji Javy na poziomie 11 (WTF) (zwykle Java jest wstecznie kompatybilna - istnieją również narzędzia obsługi problemy takie jak SdkMan...)
* Aktualizacja Spring Boot wymaga -> aktualizacji Gradle (WTF)
* Aktualizacja Gradle wymaga -> aktualizacji pluginu
* Aktualizacja pluginu wymaga -> aktualizacji Groovy (WTF)
* Aktualizacja Groovy wymaga -> aktualizacji platformy testowej i aktualizacji testów (WTF)
* Aktualizacja platformy testowej wymaga -> aktualizacji zależności
* \[...]
Ponadto niektóre pluginy nie działają z nowszymi wersjami Gradle, niektóre nie są już rozwijane, są niekompatybilne z innymi pluginami, działają tylko z Gradle KTS, nie z Gradle Groovy lub po prostu mają ograniczenia. Nawet pluginy od dużych dostawców, takich jak Spring, w porównaniu do ich Mavenowych odpowiedników, mają ograniczoną funkcjonalność. W końcu mam fajny, krótki plik Gradle Build, którego nikt nie może właściwie utrzymać, nawet deweloperzy, którzy to napisali, a nadal kochają Gradle. Znam tylko kilku, którzy naprawdę rozumieją skrypty Gradle i potrafią je pisać.

### Odkrycie na nowo siły narzędzia Maven - Wykorzystanie czarodziejskiej mocy narzędzia Maven

Oto moje ulubione funkcje Mavena:
Wtyczki mogą być uruchamiane i konfigurowane bez wcześniejszej definicji, bezpośrednio z wiersza poleceń. Poza tym, są one w dużej mierze niezależne od innych konfiguracji wtyczek.

| Komenda przykładowa                     | Opis                                                                                                                                                               | Link                                                                     |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`    | Aktualizacja wersji - kto potrzebuje Dependabota? Tak, moje projekty były stale aktualizowane do najnowszej wersji od lat, bez uciążliwych wniosków o scalenie. | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0`  | Ustawienie wersji projektu...                                                                                                                                       | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`          | Wyświetlanie listy zależności i ich licencji (nawet w przypadku wykluczonych licencji może zakończyć się niepowodzeniem)                                          | https://www.mojohaus.org/license-maven-plugin/index.html                 | 

Ta lista mogłaby trwać w nieskończoność. Przypomina mi to w jakiś sposób kroki w GitHub Workflow.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)


```

### Nie lubisz XML?

Nie ma problemu! Po prostu napisz swój plik Build w `ruby`, `groovy`, `scala`, `yaml`, `atom` lub `Java`. Rozszerzenie Polygot
(https://github.com/takari/polyglot-maven) to umożliwia. Aby spróbować,
po prostu wykonaj polecenie `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml`, a w
kilka milisekund Twój plik Build zostanie przetłumaczony. Szkoda, że nie ma niezawodnego translatora Maven <> Gradle
:(
Tak, Maven Build Files są duże, ale też bardzo łatwe do zrozumienia. Poprawki lub debugowanie są realizowane w mig.

### Wiek to tylko liczba - Stabilność i ewolucja Mavens

O ile trzeba przyznać, że Maven istnieje już całkiem sporo czasu i jego estetyka może nie odpowiadać dzisiejszym
standardom. Wytrzymałość Mavena pozwoliła jednak na jego adaptację i rozwój. Maven działa niezależnie od Twojego
projektu. Pliki budowania można łatwo ponownie wykorzystać. Wtyczki działają w piaskownicy i są niezależne od siebie
oraz niezależne od wersji Javy lub Mavena. Ten projekt może pochwalić się stabilnością i przewidywalnością oraz ułatwia
zarządzanie skomplikowanymi procesami budowania bez nieoczekiwanych konfliktów.

### Podsumowanie

Obecnie środowisko programistyczne jest przeciążone wieloma zadaniami i technologiami dla deweloperów. W poszukiwaniu
prostoty i automatyzacji narzędzie do budowania Gradle pojawia się jako nowoczesne rozwiązanie, ale również niesie ze
sobą swoje wyzwania. Bez wątpienia koncepcja Gradle jest dobra! Jednak wobec skomplikowania i czasu poświęconego na
pisanie skryptów budowania Gradle, pojawia się pytanie, czy nie byłoby łatwiej rozwijać Mavena. Z użyciem wtyczek i
rozszerzeń, Maven mógłby być odświeżony i uproszczony w dowolnym momencie. Czy dalszy rozwój nie byłby bardziej
ekscytujący i zrównoważony niż ciągłe przeskakiwanie z jednej technologii na drugą?

### Odnośniki

* [Przechodzenie z powrotem z Gradle do Maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### Kontakt

[Problemy GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).```
