---
title: "Illusion Bezserwerowy & Chmura"
date: 2023-05-24
author: "Nova Annabella"
slug: illusion_serverless_cloud
tags: [ Development, Serverless, Cloud, Microservices, Scalability, Architecture, Infrastructure ]
categories: [ Technology, Software, Cloud ]
description: "Wyzwania i rzeczywistość funkcji serwerowych w chmurze. Cenne spostrzeżenia dla firm, które rozważają migrację do chmury."
draft: false
images:
  - "/images/content/onprem_vs_cloud.png"
card: "summary_large_image"
---


# Iluzja funkcji bezserwerowych w chmurze

![aws_costs_twitter_1](/images/content/onprem_vs_cloud.png)

### Wprowadzenie

Jestem rozczarowany, jak często marketing wygrywa ze zdrowym rozsądkiem. Wielu menedżerów ignoruje 
swoich własnych ekspertów - programistów. Dotyczy to również migracji do chmury. Spoiler: Ktoś, kto musi oszczędzać 
powinien unikać chmury. Ponieważ nowe modne słowo "Bezserwerowe" w chmurze znaczy: Ty troszczysz się o 
oprogramowanie, my troszczymy się o sprzęt. Kto jednak ma zdolnego, zmotywowanego i ciekawego świata administratora, ten 
może prowadzić środowisko bezserwerowe samodzielnie (np. [KNative](https://knative.dev)).

![aws_costs_twitter_1](/images/content/aws_costs_twitter_1.png)


### Funkcje serwerowe vs mikrousługi:



#### Mikroserwisy

Typowy bezstanowy mikrousługa zajmuje się określoną funkcją / domeną i jest wdrażany w środowisku orkiestracji
kontenerów. To środowisko zajmuje się infrastrukturą, bezpieczeństwem, firewallem, logowaniem, metrykami, sekretami,
siecią, kopiami zapasowymi i wieloma innymi. Dużą zaletą jest to, że mikrousługę można przetestować lokalnie z użyciem
niewielu zasobów i jest ona agnostyczna wobec chmury / serwerów (można jej używać wszędzie).

#### Bezserwerowe Funkcje

Mały żart na początek: Paradoks, ale prawda - funkcje bezserwerowe są mocno zależne od środowiska serwera. :)
Typowa funkcja bezserwerowa również troszczy się tylko o jedną określoną funkcję/dziedzinę i jest napisana bez frameworków
w
czystym kodzie, aby być szybszą niż mikroserwis (to również dobre ćwiczenie dla mikrouslug). Dużą
zaletą jest to, że funkcje bezserwerowe są automatycznie skalowane. Jednak każda funkcja bezserwerowa wymaga
znacznej ilości tzw. kodu klejącego (GlueCode), aby zdefiniować infrastrukturę - bezpieczeństwo, zaporę ogniową, sieć, rejestrację, metryki,
sekrety, buforowanie, kopie zapasowe i wiele innych.
Dlatego prosta funkcja, jak kopiowanie pliku, włącznie z API, może szybko osiągnąć 1500 linii kodu (wraz z IaC).
Koszty administracyjne przesuwają się od administracji do rozwoju w stosunku 1:N (1 do funkcji bezserwerowych). Wiedza i implementacja nie są już
zbundowane i mogą szybko stać się niestabilne. Dodatkowo zwiększają się koszty utrzymania.
Rzeczywiste testy integracyjne są rzadkie w przypadku rozwiązań bezserwerowych lub wymagają dużego wysiłku.
Ostatecznie, kompleksowość funkcji bezserwerowych jest znacznie większa niż pojedynczego mikrouslugi.
Wyższy poziom skomplikowania oznacza również niższą utrzywalność. Nowi członkowie zespołu mają trudniej i wymagają znacznie
więcej wiedzy z góry.

### Serverless i chmura w ogólnym ujęciu

Większość technologii chmurowych nie jest na najnowszym poziomie. Na przykład Node.js, Java, Python i inne języki czy technologie często nie są łatwe do zaktualizowania, najczęściej pozostaje tylko czekać.
Również nowoczesne i standardowe technologie, takie jak MongoDB, MySQL, Kafka, NATS, RabbitMQ, Redis, Prometheus, InfluxDB, Grafana,
Kibana, Elastic Search, itp. są albo niedostępne, albo zbyt drogie.
Bez takich standardowych usług często znajdujemy się w wirtualnej epoce kamienia łupanego i korzystamy ze starych rozwiązań, np.
Webhooks do komunikacji zewnętrznej. Dodatkowo, margines manewru w kwestiach, takich jak regulacje,
zgodność, ochrona danych i niezawodność jest bardzo ograniczony.

Chmura powinna być zatem obsługiwana w sposób agnostyczny, aby szybko przełączać między AWS, Azure, Google, On-Premise itd. i
porównywać koszty.
Ograniczenia często dotyczą również chmury, co prowadzi do kreatywnych obejść, które z kolei zwiększają złożoność.
Również testy integracyjne mogą okazać się kosztowne, ponieważ każdy programista potrzebuje własnego środowiska deweloperskiego w chmurze,
ponieważ wiele usług chmurowych jest trudno lub wcale nie można przetestować lokalnie.
Jednak nawet bez testów chmura jest droga. Podczas gdy w przypadku systemów On-Premise głównie
naliczane są koszty sprzętu, w chmurze płaci się dodatkowo za ruch, niektóre usługi standardowe i często nawet za
podwójne opodatkowanie. Co więcej, w chmurze łatwo jest stracić orientację, bo chodzi tu nie o
użyteczność, ale pieniądze. Koszty są tak ukryte, że dostrzegasz je dopiero, gdy jest już za późno.

Podstawy architektury i infrastruktury muszą być w chmurze, a zwłaszcza w obszarze Serverless,
ponownie wynalezione, ponieważ implementacja zależy w dużej mierze od dostępnych funkcji.
Zawsze po zaprojektowaniu architektury przychodzi mi do głowy myśl: "To mogła być jedna usługa".

Dla mnie Serverless to interesujący pomysł i jest dobrze skalowalny, ale nie obniża kosztów. Przeciwnie,
wymaga dużo więcej wiedzy i czasu na rozwijanie. Serverless lub chmura wymaga dyscypliny i
wiedzy wstępnej.
Jeśli wiedza o systemach On-Premise nie jest dostępna, chmura nie ułatwia sprawy.
Jak programiści mają zdobywać dodatkową wiedzę o infrastrukturze?

Wolałbym dobrze zarządzanego klastra Kubernetes nad architekturą chmury.
Pracownicy nie skalują. Wielu programistów nie ma dyscypliny w pisaniu kodu.
Niestety, dotyczy to 80 procent programistów. Jak więc ci programiści mają obsługiwać chmurę?

Ważne jest, aby firmy w pełni zrozumiały wyzwania i skutki architektury serverless i chmury.
Wymaga to nie tylko wiedzy technicznej, ale także strategicznego podejścia. Nierozważna migracja do chmury może prowadzić do złożoności, wyższych kosztów i przeciążenia programistów.

Podsumowując, Serverless w chmurze to obiecujący koncept, który jednak powinien być starannie przemyślany.
Należy uwzględnić koszty, złożoność, możliwość obsługi i umiejętności zespołu programistów.
Każde przedsiębiorstwo ma inne wymagania i priorytety. Należy podjąć przemyślaną decyzję, czy
Serverless w chmurze jest właściwym rozwiązaniem, czy też alternatywne podejścia, takie jak
np. dobre klaster Kubernetes to lepszy wybór.

Skuteczne wykorzystanie Serverless i Cloud Computing wymaga kombinacji ekspertyzy technicznej
strategicznego planowania i jasnego zrozumienia wymagań biznesowych. Tylko w ten sposób można przejrzeć iluzję Serverless
i podjąć właściwą decyzję dla własnego rozwoju oprogramowania.


### Wniosek

Wprowadzenie funkcji bezserwerowych w chmurze obiecuje elastyczność, skalowalność i odciążenie deweloperów od zadań
związanych z infrastrukturą. Nie powinno się jednak dać zwieść tej iluzji. Przejście do chmury i korzystanie z funkcji
bezserwerowych wiąże się z szeregiem wyzwań. Deweloperzy muszą poza właściwym rozwojem nauczyć się nowego "języka" i
przyjąć bez odpowiedniego wsparcia większą odpowiedzialność. Złożoność funkcji bezserwerowych jest często większa niż
mikrousług, ponieważ deweloperzy muszą podjąć wiele dodatkowych zadań, takich jak definicja infrastruktury,
bezpieczeństwo i skalowanie. Prawdziwe testy integracyjne są trudne, a wiedza i doświadczenie potrzebne do operacji w
chmurze są jeszcze ważniejsze. Sama chmura stawia kolejne wyzwania. Wiele technologii chmurowych nie jest na najnowszym
stanowisku a korzystanie z nowoczesnych usług standardowych może być drogie, a nawet niemożliwe. Regulacje, zgodność i
ochrona danych ograniczają swobodę działania. Co więcej, koszty w chmurze łatwo wymykają się spod kontroli, a
przejrzystość wydatków szybko znika. Ogólnie rzecz biorąc, należy starannie rozważyć zalety i wady bezserwerowości i
chmury. Firmy powinny uwzględniać swoje konkretne wymagania, istniejącą wiedzę w zespole oraz długoterminowe skutki
migracji do chmury. Przemyślana decyzja na podstawie wszechstronnej analizy jest kluczowa dla powodzenia i rentowności
projektu. Ostatecznie to firmy mają na swojej barku odpowiedzialność za odpowiednie wsparcie deweloperów, realistyczną
ocenę kosztów i złożoności chmury oraz za rozważanie alternatywnych rozwiązań, takich jak dobrze zarządzane klastry
Kubernetes. Z klarowną strategią i gruntownym zrozumieniem własnych potrzeb firmy mogą optymalnie wykorzystać korzyści
płynące z chmury i funkcji bezserwerowych oraz przejrzeć iluzję.

### Kontakt

[Problemy GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).

