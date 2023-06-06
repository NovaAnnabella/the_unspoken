---
title: "Poziomy testowe: Znalezienie właściwej równowagi"
date: 2023-05-31
author: "Nova Annabella"
slug: test_level
tags: [ Testing, Software Testing, Test Levels, Mock Tests, Unit Tests, Integration Tests, Component Tests, Contract Tests, End-to-End Tests ]
categories: [ Technology, Software Development, Quality Assurance ]
description: "Znalezienie właściwej równowagi w wyborze odpowiednich poziomów testów do testowania oprogramowania"
draft: false
images:
  - "/images/content/martin_fowler_testing.png"
card: "summary_large_image"
---


# Poziomy testów: Znalezienie właściwej równowagi

[![testebenen](/images/content/martin_fowler_testing.png)](https://martinfowler.com/articles/microservice-testing/)

### Wprowadzenie

Temat testowania nadal wydaje się być niezbadanym terytorium z dużym polem do interpretacji. Tradycyjna piramida
piramida testów została zakwestionowana i pojawiły się nowe piramidy testów. Moim zdaniem piramida testów nie jest
potrzebna. piramida testów, ale jasne zrozumienie tego, co należy przetestować. Testy na niższych poziomach są często
mniej znaczące. Należy skupić się przede wszystkim na testowaniu zachowania, aby upewnić się, że API lub UI działa
zgodnie z oczekiwaniami. Kompleksowy przegląd możliwych typów testów można znaleźć tutaj: [Martinfowler
Testing](https://martinfowler.com/articles/microservice-testing/).

### Poziom 1 - Testy próbne i testy jednostkowe

Cel: Ćwiczenie najmniejszych testowalnych części oprogramowania w aplikacji, aby sprawdzić, czy działają zgodnie z
oczekiwaniami. praca. Testy próbne i jednostkowe mogą przynieść efekt przeciwny do zamierzonego i często utrudniają
proces rozwoju. Testy te są często oderwane od kontekstu i mają niewielki związek z rzeczywistością. Często służą
jedynie do utrzymywania niepotrzebnych funkcji poprzez istniejące testy jednostkowe. testów jednostkowych. Po dodaniu
makiet staje się to ćwiczeniem samobójczym. Oczekiwane wyniki testów są ograniczone do tego, co zostało zdefiniowane w
oryginalnej makiecie. Użytkownicy końcowi nie są zainteresowani funkcjami wewnętrznymi. Na przykład w scenariuszu
logowania `loginUser(name, password, securityAlgorithm)`. Jeśli test jednostkowy sprawdza wartość null dla parametru
`securityAlgorithm`, wykonywanych jest zbyt wiele testów, ponieważ użytkownicy nie mogą ustawić parametru
`securityAlgorithm`. ustawić parametr `securityAlgorithm`.

### Poziom 2 - Test integracji

Cel: Sprawdzanie ścieżek komunikacji i interakcji między komponentami w celu wykrycia wad interfejsu. defektów
interfejsu. Testy integracyjne zapewniają cenny wgląd w wydajność i niezależność różnych części aplikacji.
Zastosowanie. Przy mniejszej liczbie makiet testy stają się bardziej zrozumiałe. Jednak nadal brakuje im kontekstu i
istnieje ryzyko, że testy integracyjne są po prostu testami jednostkowymi w przebraniu. Niebezpieczeństwo, że testy
integracyjne są po prostu testami jednostkowymi w przebraniu z mniejszą liczbą makiet.

### Poziom 3 - Test zawartości

Cel: ograniczenie zakresu testowanego oprogramowania do części testowanego systemu, manipulowanie systemem poprzez
wewnętrzne interfejsy kodu i użycie podwójnych testów w celu odizolowania testowanego kodu od innych komponentów. System
poprzez wewnętrzne interfejsy kodu i użycie podwójnych testów w celu odizolowania testowanego kodu od innych
komponentów. komponenty. Testowanie komponentów dostarcza wielu informacji na temat jakości i wydajności aplikacji.
Zamiast makiety ostatecznie testujesz swoją aplikację. Granica między testowaniem komponentów a testowaniem end-to-end
nie jest znacząca. istotna. Przy dobrym środowisku testowym granice między nimi często się zacierają, dzięki czemu
testowanie rzeczywistego zachowania zamiast odizolowanych i pozbawionych kontekstu funkcji. Jednak tworzenie dodatkowych
klas testowych, takich jak Jednak tworzenie dodatkowych klas testowych, takich jak stuby komponentów, podróbki i makiety
w kodzie produkcyjnym może zwiększyć koszty utrzymania.

### Poziom 4 - Test umowy

Celem tego bloku kodu jest sprawdzenie interakcji na granicy usługi zewnętrznej oraz zapewnienie, że jest ona zgodna z
wymaganiami umownymi usługi konsumującej. Testy kontraktowe często przypominają testy jednostkowe, a różnica między
nimi jest minimalna. Niektórzy deweloperzy kojarzą te testy z testami Pact, które zasadniczo działają jak testy
jednostkowe z serwerem pomiędzy nimi. Wysiłek wysiłek związany z utrzymaniem tych testów może jednak nie być opłacalny.
Na przykład, test Pact może wykorzystywać REST API `loginUser?name=aa&password=bb)` i oczekiwać odpowiedzi w postaci
schematu JSON, który został wcześniej przesłany na serwer Pact. serwer. Ten schemat jest statyczny i podatny na błędy,
takie jak nieprawidłowe formaty daty lub strefy czasowe w odpowiedzi API. API. Negatywne skutki mogą być ogromne.

### Poziom 5 - Testy kompleksowe (zwane również testami czarnoskrzynkowymi)

Cel: Weryfikacja, czy system spełnia wymagania zewnętrzne i osiąga swoje cele poprzez testowanie całego systemu od
początku do końca. od początku do końca. Testowanie od początku do końca jest niezawodne i solidne. Po pokonaniu
przeszkód związanych z konfiguracją środowiska testowego, wysiłek się opłaca. wysiłek się opłaca. Testy te symulują
rzeczywiste zachowanie i eliminują potrzebę stosowania makiet. Błędy występują rzadziej i są łatwiejsze do odtworzenia
lokalnie. W dużej mierze unika się czasochłonnego debugowania i rejestrowania w środowisku produkcyjnym, podobnie jak
rzadkich błędów. są w dużej mierze unikane, podobnie jak rzadkie incydenty. Deweloperzy pracują rzadziej, jeśli w ogóle,
z danymi z danymi produkcyjnymi, co zmniejsza odpowiedzialność i zwiększa koncentrację. Ponadto automatyzacja, taka jak
automatyczne aktualizacje oprogramowania ułatwiają wdrożenie, ponieważ zachowanie zostało już przetestowane. Są też inne
korzyści! Raz testy są napisane w formie wielokrotnego użytku, można je zintegrować z testami obciążeniowymi, aby
uzyskać kompleksowy obraz funkcjonalności. kompleksowy obraz funkcjonalności. Testy te mogą być również uruchamiane w
sposób ciągły w środowisku produkcyjnym i zapewniać wgląd w czasie rzeczywistym w stan różnych przepływów pracy. Gdy
podsystem, taki jak np. na przykład usługa REST, przechodzi w tryb offline, możliwe jest natychmiastowe
zidentyfikowanie, na które przepływy pracy użytkowników ma to wpływ. są dotknięte.

### Fazit

Podsumowując, testowanie jest istotnym aspektem tworzenia oprogramowania, a wybór poziomów testowania zależy od
konkretnych wymagań i celów aplikacji. Podczas gdy mock testy i testy jednostkowe mogą mieć ograniczoną skuteczność,
testy integracyjne i jednostkowe zapewniają cenny wgląd w zachowanie i wydajność aplikacji. Testy integracyjne i
jednostkowe zapewniają cenny wgląd w zachowanie i wydajność aplikacji. wydajność aplikacji. Testy kontraktowe pomagają
zweryfikować interakcje z usługami zewnętrznymi, ale ich od testów jednostkowych mogą być minimalne. Ostatecznie, testy
end-to-end zapewniają najwyższy poziom zaufania do funkcjonalności systemu i umożliwiają kompleksowe testowanie. Testy
jednostkowe zapewniają najwyższy poziom pewności co do funkcjonalności systemu i umożliwiają kompleksowe testowanie
całej aplikacji. Wybierając odpowiednie i efektywnie je łącząc, programiści mogą zapewnić jakość, niezawodność i
solidność oprogramowania. oprogramowania.

### Kontakt

[Problemy GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
