---
title: "Poziomy testów: Znalezienie właściwej równowagi"
date: 2023-05-31
author: "Nova Annabella"
slug: test_level
tags: [ Testing, Software Testing, Test Levels, Mock Tests, Unit Tests, Integration Tests, Component Tests, Contract Tests, End-to-End Tests ]
categories: [ Technology, Software Development, Quality Assurance ]
description: "Znalezienie właściwej równowagi podczas wyboru odpowiednich poziomów testów dla testów oprogramowania"
draft: false
images:
  - "/images/content/martin_fowler_testing.png"
card: "summary_large_image"
---


# Poziomy testów: Znalezienie odpowiedniej równowagi

[![testebenen](/images/content/martin_fowler_testing.png)](https://martinfowler.com/articles/microservice-testing/)

### Wstęp

Temat testowania wydaje się do dziś być terra incognita z dużą przestrzenią do interpretacji. Tradycyjna piramida testowa została podważona, a powstały nowe piramidy testowe. Moim zdaniem nie potrzebujemy piramidy testów, ale klarownego zrozumienia tego, co musi być testowane. Testy na niższych poziomach często są mniej wymowne. Szczególny nacisk powinien być położony na testowanie zachowania, aby upewnić się, że API lub UI działa tak, jak to jest oczekiwane. Obszerny przegląd możliwych typów testów można znaleźć tutaj: [Martinfowler Testing](https://martinfowler.com/articles/microservice-testing/).


### Poziom 1 - Testy próbne i testy jednostkowe

Cel: Wykonać najmniejsze testowalne elementy oprogramowania w aplikacji, aby ustalić, czy działają zgodnie z
oczekiwaniami. Testy mockujące i jednostkowe mogą być przeciwwskazane i często utrudniają proces rozwijania
oprogramowania. Te testy są często odłączone od kontekstu i mają mało wspólnego z rzeczywistością. Często służą tylko do
utrzymania niepotrzebnych funkcji za pośrednictwem istniejących testów jednostkowych. Gdy dodawane są mocki, staje się
to zajęciem w samym sobie. Oczekiwane wyniki testów mockujących ograniczają się do tego, co zostało zdefiniowane w
oryginalnym mocku. Końcowi użytkownicy nie interesują się funkcjami wewnętrznymi. Na przykład, w scenariuszu logowania
`loginUser(name, password, securityAlgorithmus)`. Jeżeli test jednostkowy wykonuje sprawdzenie zerowe na parametrze
`securityAlgorithm`, jest przetestowane za dużo, ponieważ użytkownicy nie mogą ustawić parametru `securityAlgorithm`.

### Poziom 2 - Test Integracyjny

Cel: Sprawdzenie dróg komunikacji i interakcji między komponentami w celu wykrycia błędów interfejsu. Testy
integracyjne dostarczają cennych informacji o wydajności i niezależności różnych części aplikacji. Dzięki ograniczeniu
mocków testy stają się bardziej zrozumiałe. Jednak nadal brakuje im kontekstu, a istnieje ryzyko, że testy integracyjne
są po prostu przemaskowanymi testami jednostkowymi z mniejszą ilością mocków.

### Poziom 3 - Test Komponentu

Cel: Ograniczenie zakresu testowanego oprogramowania do części systemu do sprawdzenia, manipulacja systemem za pomocą
wewnętrznych interfejsów kodu i użycie dublerów testowych do izolacji testowanego kodu od innych komponentów. Testy
komponentów dostarczają wiele informacji na temat jakości i wydajności aplikacji. Zamiast mocków w końcu testujesz swoją
aplikację. Granica między testami komponentów a testami od początku do końca nie jest znacząca. Dzięki dobrej środowisku
testowemu granice między nimi często zacierają się, umożliwiając testowanie prawdziwego zachowania zamiast izolowanych i
bezkontekstowych funkcji. Jednak tworzenie dodatkowych klas testowych, takich jak dublerzy komponentów, fałszywki i
mocki, w kodzie produkcyjnym może wiązać się z dodatkowym wysiłkiem konserwacyjnym.

### Poziom 4 - Test Kontraktu

Celem tego bloku kodu jest sprawdzenie interakcji na granicy zewnętrznej usługi i
zapewnienie, że spełnia ona wymagania kontraktowe usługi konsumpcyjnej.

Testy kontraktów często przypominają testy komponentów, a różnica między nimi jest minimalna. Niektórzy deweloperzy
kojarzą te testy z testami Pact, które zasadniczo działają jako testy jednostkowe z serwerem pomiędzy. Jednak
wysiłek potrzebny do utrzymania tych testów, może nie być opłacalny. Na przykład, test Pact może
przetestować REST-API `loginUser?name=aa&password=bb` i oczekiwać odpowiedzi w formacie JSON, która została wcześniej wgrana na serwer Pact.
To schemat jest statyczny i podatny na błędy, takie jak nieprawidłowe formaty daty lub strefa czasowa w
odpowiedzi API. Negatywne skutki mogą być ogromne.


### Poziom 5 - Testy od końca do końca (zwane także testami Black-Box)

Cel: Sprawdzenie, czy system spełnia zewnętrzne wymagania i osiąga swoje cele, poprzez przetestowanie całego systemu od
początku do końca.

Testy End-to-End są niezawodne i solidne. Gdy tylko pokonane są przeszkody związane z tworzeniem środowiska testowego, wysiłek
opłaca się. Te testy symulują realne zachowanie i eliminują potrzebę stosowania mocków. Błędy pojawiają się rzadziej
i są łatwiejsze do odtworzenia lokalnie. Złożone debugowanie i prowadzenie logów w produkcji
są w dużej mierze unikane, jak również rzadkie incydenty. Programiści rzadziej, jeśli w ogóle, pracują z
danymi produkcyjnymi, co redukuje odpowiedzialność i zwiększa skupienie. Co więcej, automatyzacje takie jak
automatyczne aktualizacje oprogramowania ułatwiają przeprowadzenie, ponieważ zachowanie już było testowane. Są jeszcze inne zalety! Kiedy
testy są napisane w postaci możliwej do ponownego użycia, mogą być zintegrowane z testami obciążeniowymi, aby uzyskać
kompletny obraz funkcjonalności. Te testy mogą również być ciągle wykonywane w środowisku produkcyjnym
i dostarczać w czasie rzeczywistym informacje o statusie różnych przepływów pracy. Jeśli pewien podsystem, tak jak
na przykład zewnętrzna usługa REST, przestanie działać, natychmiast można zidentyfikować, które przepływy pracy użytkownika
są dotknięte.

### Wnioski

Podsumowując, testowanie jest kluczowym aspektem rozwoju oprogramowania, a wybór poziomów testów zależy od konkretnych
wymagań i celów aplikacji. Podczas gdy testy Mock i testy jednostkowe mogą być ograniczone w swojej skuteczności, testy
integracyjne i testy komponentów dostarczają cennych informacji o zachowaniu i wydajności aplikacji. Testy umowy
pomagają sprawdzić interakcje z zewnętrznymi usługami, ale twoja granica z testami komponentów może być minimalna.
Ostatecznie testy od końca do końca dają największy poziom zaufania do funkcjonalności systemu i umożliwiają kompleksowe
testowanie całej aplikacji. Poprzez wybór odpowiednich poziomów testów i ich skuteczną kombinację, deweloperzy mogą
zapewnić jakość, niezawodność i robustność twojego oprogramowania.

### Kontakt

[GitHub Problemy](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
