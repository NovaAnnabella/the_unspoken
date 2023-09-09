---
title: "Powrót do Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "Trudne do uchwycenia poszukiwanie prostoty i krótka podróż do odkrycia na nowo mocy Mavena."
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# Powrót do Mavena?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

## 10 lat Gradle. W poszukiwaniu ulgi i krótkiej podróży do ponownego odkrycia siły Maven.



### Maksymalizacja potencjału programistów - Potrzebujemy więcej narzędzi oszczędzających czas

Tematy, które często są pomijane lub rzadko dyskutowane, interesują mnie. Często są stosowane fajne technologie, ale
niewielu ludzi rozmawia o związanych z nimi problemach. Deweloperia stała się dzisiaj bardzo pracochłonna. Z fajnymi
słowami kluczowymi, takimi jak „Bezserwerowe”, „Niski kod”, „IaC”, „Big Data”, „Chmura”, „DevOps”, „Budujesz to,
prowadzisz to” itd. deweloperzy mają już do pokonania więcej niż wystarczająco dużo dodatkowych zadań. Więcej zadań
oznacza, że eksperci są już rzadkością, a zawsze coś jest zaniedbywane dla skupienia. Dlatego automatyzacje i
oszczędność czasu są mega ważne. „Nie zmuszaj mnie do myślenia” i „Działa od razu” to już dobre cechy jakości, których
nie mogę zobaczyć w Gradle. Aby być sprawiedliwym, Gradle nie jest jedynym nowoczesnym narzędziem, które zamiast
ułatwiać, sprawia nam więcej pracy.

### Iluzoryczne poszukiwanie prostoty i automatyzacji

Od czasu SOAP mam głęboko zakorzenioną niechęć do konfiguracji opartych na XML. Miałem nadzieję, że z Gradle pisanie
skryptów Bind będzie bułką z masłem. Niestety, moje nadzieje i motywacja stawały się coraz mniejsze z każdym razem.
Gradle dąży do elastyczności, ofiarowując za to automatyzację i jakość. Programistki i programiści ślepo podążają za
trendem, nie zważając na skutki dla niezawodności oprogramowania. Aby utrzymać skrypty budowania Gradle proste i łatwe
do utrzymania, potrzebna jest silna dyscyplina. Znalezienie takiej dyscypliny w kodzie źródłowym jest rzadkością,
dlatego w skryptach budujących jest ona jeszcze rzadsza.

### Tłumaczenia i obejścia - Kiedy skrypty budujące stają się wyzwaniem

Gradle pracuje w tle nie różniąc się wiele od Mavena. Dlatego wymagane są pewne tłumaczenia. Funkcje takie jak Katalog
zależności, wtyczka Maven Release, Dependabot i wiele innych to tak naprawdę obejścia dla podstawowych funkcji, które
Maven już posiada. Z elastycznością Gradle często pojawiają się skomplikowane konfiguracje budowy, które są trudne do
utrzymania. Wtyczki Gradle często mają problemy z kompatybilnością, ograniczeniami lub ograniczonym rozwojem. Te
problemy powstają na skutek ewolucji ekosystemu Gradle, różnorodności środowisk, w których jest używany Gradle i
specyficznego wysiłku implementacyjnego i konserwacyjnego dla każdej wtyczki. Wszystko jest ze sobą powiązane.

### Efekt domina w Gradle - Koszmarne scenariusze w prawdziwym świecie

Widziałem wiele mikrousług, które miały zaledwie kilka lat i już były nienaprawialne z powodu Gradle.
Warto wspomnieć, że nie jest to pierwszy raz, kiedy widzę coś takiego, i nie, nie byli to
Junior Devs.

Moim **zadaniem było przeprowadzenie aktualizacji Spring Boot 2.x na 2.7**. Spoiler: Poddałem się po roku.
Problemy w skrócie:

* Plik budowy Gradle wymaga -> zdowngradowanie mojej lokalnej wersji Java na wersję 11 (WTF) (Zazwyczaj Java
  jest wstecznie kompatybilna - istnieją również narzędzia omijające, takie jak SdkMan...)
* Aktualizacja Spring Boot wymaga -> aktualizacji Gradle (WTF)
* Aktualizacja Gradle wymaga -> aktualizacji wtyczki
* Aktualizacja wtyczki wymaga -> aktualizacji Groovy (WTF)
* Aktualizacja Groovy wymaga -> aktualizacji Frameworku testowego i testów (WTF)
* Aktualizacja testowego frameworku wymaga -> aktualizacji zależności
* \[...]
  Poza tym niektóre wtyczki nie działają z nowszymi wersjami Gradle, niektóre nie są już rozwijane, są niekompatybilne z innymi wtyczkami, działają tylko z Gradle KTS, nie z Gradle Groovy, lub
  mają po prostu limity. Nawet wtyczki od dużych dostawców jak Spring mają ograniczoną funkcjonalność w porównaniu do ich wtyczek Maven.
  Na końcu mam fajny, krótki plik budowy Gradle, którego nikt nie potrafi naprawdę utrzymać,
  nawet deweloperzy, którzy go napisali, nadal kochają Gradle. Znam tylko niewielu, którzy
  mogliby napisać skrypty Gradle na poważnie.

### Odkrycie na nowo mocy Maven - Wykorzystanie magicznych mocy Maven

Oto moje ulubione funkcje Mavena:
Wtyczki można uruchamiać i konfigurować bezpośrednio z linii poleceń, bez konieczności wcześniejszego definiowania
muszą. Co więcej, są one w dużej mierze niezależne od innych konfiguracji wtyczek.

| Przykładowe polecenie                  | Opis                                                                                                                                                               | Link                                                                     | 
|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`   | Aktualizacja wersji - kto potrzebuje Dependabota? Tak, moje projekty są aktualizowane do najnowszej wersji od lat, bez irytujących żądań scalenia                | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -D.newVersion=1.0.0`| Ustawienie wersji projektu...                                                                                                                                     | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`         | Wyświetlanie listy zależności i ich licencji (może nawet zawieść w przypadku wykluczonych licencji)                                                               | https://www.mojohaus.org/license-maven-plugin/index.html                 | 

Ta lista mogłaby trwać w nieskończoność. Jakoś przypomina mi to kroki GitHub Workflow.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

### Nie lubisz XML?

Nie ma problemu! Napisz po prostu swój plik Build w `ruby`, `groovy`, `scala`, `yaml`, `atom` lub `Java`. Wtyczka Polygot
(https://github.com/takari/polyglot-maven) to umożliwia. Aby wypróbować,
po prostu uruchom `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` i w
kilka milisekund Twój plik Build zostanie przetłumaczony. Szkoda, że nie ma niezawodnego tłumacza Maven <> Gradle
:(

Tak, pliki Build Maven są duże, ale również bardzo łatwe do zrozumienia. Poprawki i debugowanie są wykonane w mgnieniu
oka.

### Wiek to tylko liczba - Stabilność i ewolucja Mavens

Trzeba przyznać, że Maven jest już od jakiegoś czasu i jego estetyka może nie odpowiadać dzisiejszym standardom. Długa
żywotność Mavena pozwoliła mu jednak na dostosowanie się i rozwijanie. Maven działa niezależnie od Twojego projektu.
Pliki budowy można łatwo ponownie wykorzystać. Wtyczki działają w piaskownicy i są niezależne od siebie oraz od wersji
Javy lub Mavena. Takie projektowanie promuje stabilność i przewidywalność i ułatwia zarządzanie złożonym procesem budowy
bez nieoczekiwanych konfliktów.

### Podsumowanie

Obecnie środowisko programistyczne jest przeładowane wieloma zadaniami i technologiami dla programistów. W poszukiwaniu
prostoty i automatyzacji, pojawiło się narzędzie do budowy Gradle, ale przyniosło swoje własne wyzwania. Bez wątpienia,
koncepcja Gradle jest dobra! Ale wobec złożoności i czasu inwestowanego w skrypty budowy Gradle, nasuwa się pytanie, czy
nie byłoby prościej rozbudować Mavena. Za pomocą wtyczek i rozszerzeń, Maven mógłby być w każdej chwili odświeżany i
upraszczany. Czy dalszy rozwój nie byłby dużo bardziej ekscytujący i zrównoważony, niż skakanie od jednej technologii do
drugiej?

### Łącza

* [Powrót z Gradle do maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### Kontakt

[Problemy GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
