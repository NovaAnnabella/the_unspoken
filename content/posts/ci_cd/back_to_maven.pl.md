---
title: "Powrót do Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "Trudne do uchwycenia poszukiwanie prostoty i krótka podróż odkrywająca ponownie potęgę Maven'a."
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# Powrót do Maven?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

## 10 lat Gradle. W poszukiwaniu ułatwienia i krótkiej podróży w celu ponownego odkrycia siły systemu Maven.

Nie ma treści do przetłumaczenia.

### Maksymalizacja potencjału deweloperów - potrzebujemy więcej narzędzi oszczędzających czas

Tematy, które często są pomijane lub rzadko dyskutowane, interesują mnie. Często używane są fajne technologie, ale
prawie nikt nie mówi o związanych z nimi problemach. Obecnie rozwój stał się bardzo kosztowny. Z fajnymi buzzwordami,
jak "Serverless", "Low Code", "IaC", "Big Data", "Cloud", "DevOps", "You Build it You run it"itd., Deweloperzy już mają
więcej niż wystarczającą ilość dodatkowych zadań do wykonania. Więcej zadań oznacza, że ​​jest coraz mniej ekspertów i
zawsze coś jest zaniedbywane. Dlatego automatyzacja i oszczędność czasu są bardzo ważne. "Niech mnie nie zmuszać do
myślenia" i "Działa od razu" to już dobre wskaźniki jakości, których nie widać w Gradle. Być fair, Gradle nie jest
jedynym nowoczesnym narzędziem, które sprawia, że ​​pracujemy ciężej niż łatwiej.

### Iluzoryczne poszukiwanie prostoty i automatyzacji

Od SOAP mam głęboko zakorzenioną niechęć do konfiguracji opartych na XML. Miałem nadzieję, że pisanie skryptów
powiązanych z Gradle będzie dziecinnie proste. Niestety, moje nadzieje i motywacja stopniowo malały. Gradle dąży do
elastyczności i poświęca przy tym automatyzację i jakość. Programistki i programiści ślepo podążają za trendem, nie
zwracając uwagi na skutki dla niezawodności oprogramowania. Aby zachować proste, łatwe w utrzymaniu skrypty budowania
Gradle, wymagana jest silna dyscyplina. Taka dyscyplina jest już rzadka w kodzie źródłowym, więc jest jeszcze rzadsza w
skryptach budowania.

### Tłumaczenia i rozwiązania problemów - gdy skrypty budowania stają się wyzwaniem.

Gradle działa w tle nieco inaczej niż Maven. Dlatego potrzebne są niektóre tłumaczenia. Funkcje takie jak Katalog
Zależności, Wtyczka Maven Release, Dependabot i wiele innych są tak naprawdę obejściami dla podstawowych
funkcjonalności, które Maven już posiada. Dzięki elastyczności Gradle często powstają złożone konfiguracje budowania,
które są trudne do utrzymania. Wtyczki Gradle często mają problemy z kompatybilnością, ograniczenia lub ograniczone
rozwijanie. Problemy te wynikają z rozwijającej się natury ekosystemu Gradle, różnorodności środowisk, w których jest
używany oraz konkretnych nakładów na implementację i utrzymanie każdej wtyczki. Wszystko jest ze sobą powiązane.

### Efekt domina Gradle'a - scenariusz koszmaru w rzeczywistym świecie

Oto tekst markdown przetłumaczony na język polski:

Widziałem wiele mikroserwisów, które miały tylko kilka lat i były już nie do utrzymania ze względu na Gradle. Ważne jest to, że nie jest to pierwszy raz, kiedy coś takiego widzę, i nie, to nie byli młodzi programiści.

Moim zadaniem było **przeprowadzenie aktualizacji Spring Boot 2.x na wersję 2.7**. Spoiler: Po roku poddałem się! Oto problemy w skrócie:

* Plik buildu Gradle wymaga wymuszenia wersji lokalnej Java na 11 (Co za tym idzie) (Zazwyczaj Java jest zachowawcza i jest 
  wstecznie zgodna - istnieją narzędzia takie jak SdkMan, które rozwiążą ten problem...)
* Aktualizacja Spring Boot wymaga aktualizacji Gradle (Co za tym idzie)
* Aktualizacja Gradle wymaga aktualizacji pluginów
* Aktualizacja pluginów wymaga aktualizacji Groovy (Co za tym idzie)
* Aktualizacja Groovy wymaga aktualizacji frameworka testowego oraz testów (Co za tym idzie)
* Aktualizacja frameworka testowego wymaga aktualizacji zależności
* \[...]
  Ponadto, niektóre wtyczki nie działają z nowszymi wersjami Gradle, niektóre nie są dalej rozwijane, są niekompatybilne z 
  innymi wtyczkami, działają tylko z Gradle KTS, a nie z Gradle Groovy, lub mają po prostu ograniczenia. Nawet wtyczki 
  od dużych dostawców, takich jak Spring, mają ograniczoną funkcjonalność w porównaniu do ich wtyczek Maven. W końcu mam 
  fajny, krótki plik buildu Gradle, którego nikt nie może prawidłowo utrzymać, nawet programiści, którzy go napisali, i 
  wciąż kochają Gradle. Znam tylko kilka osób, które poważnie rozumieją i potrafią pisać skrypty Gradle.

### Odkrycie ponowne siły Mavena - Wykorzystanie magicznej mocy Mavena

Oto moje ulubione funkcje Mavena:
Pluginy można uruchamiać i konfigurować bez wcześniejszego definiowania bezpośrednio z wiersza poleceń. Ponadto są one w dużej mierze niezależne od innych konfiguracji pluginów.

| Przykładowe polecenie                | Opis                                                                                                                                                              | Link                                                                     | 
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `mvn versions:use -latest-versions` | Aktualizacja wersji - kto potrzebuje Dependabot'a? Tak, moje projekty są aktualizowane bez problemu od lat do najnowszej wersji bez irytujących próśb o scalenie       | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0`| Ustawienie wersji projektu...                                                                                                                                      | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`       | Wyświetlanie listy zależności i ich licencji (może nawet zawodzić w przypadku wykluczonych licencji)                                                               | https://www.mojohaus.org/license-maven-plugin/index.html                 | 

Ta lista mogłaby tak trwać w nieskończoność. W jakiś sposób przypomina mi to kroki w przepływie pracy w GitHubie.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

```

### Nie lubisz XML?

Nie ma problemu! Po prostu napisz swój plik budowania w `ruby`, `groovy`, `scala`, `yaml`, `atom` lub `Java`. Rozszerzenie Poliglot (https://github.com/takari/polyglot-maven) to umożliwia. Aby wypróbować, po prostu uruchom `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml`, a w ciągu kilku milisekund Twój plik budowania zostanie przetłumaczony. Szkoda, że nie ma niezawodnego tłumacza Maven <> Gradle. Tak, pliki budowania Mavena są duże, ale również bardzo łatwe do zrozumienia. Poprawki lub debugowanie są wykonywane w mgnieniu oka.

### Wiek to tylko liczba - Stabilność i Ewolucja Mavena

Przyznam, że Maven istnieje już od jakiegoś czasu i jego estetyka może nie odpowiadać obecnym standardom. Jednak
trwałość Mavena umożliwiła mu dostosowanie się i rozwijanie. Maven działa niezależnie od twojego projektu. Pliki budowy
można łatwo ponownie wykorzystać. Wtyczki działają w sandboxie i są niezależne od siebie i niezależne od wersji Java lub
Maven. Ten projekt promuje stabilność i przewidywalność oraz ułatwia zarządzanie skomplikowanymi procesami budowania bez
nieoczekiwanych konfliktów.

### Podsumowanie

Obecnie środowisko programistyczne jest przeciążone wieloma zadaniami i technologiami dla deweloperów. W poszukiwaniu
prostoty i automatyzacji, Gradle pojawił się jako nowoczesne narzędzie do budowania, ale przyniosło ze sobą własne
wyzwania. Bez wątpienia, koncepcja Gradle jest dobra! Jednak w obliczu złożoności i czasu, który jest inwestowany w
skrypty budowania Gradle, pojawia się pytanie, czy nie byłoby łatwiej rozszerzyć Maven. Za pomocą wtyczek i rozszerzeń
Maven mógłby być zawsze ulepszany i uproszczony. Czy rozwój nie byłby o wiele bardziej ekscytujący i trwały niż
przeskakiwanie z jednej technologii do drugiej?

### Linki

* [Powrót do Mavena z Gradle](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### Kontakt

[Problemy GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
