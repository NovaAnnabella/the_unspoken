---
title: "Illusion Serverless & Cloud"
date: 2023-05-24
author: "Nova Annabella"
slug: illusion_serverless_cloud
tags: [ Development, Serverless, Cloud, Microservices, Scalability, Architecture, Infrastructure ]
categories: [ Technology, Software, Cloud ]
description: "Wyzwania i realia możliwości bezserwerowych w chmurze. Cenne spostrzeżenia dla firm rozważających migrację do chmury"
draft: false
images:
  - "/images/content/onprem_vs_cloud.png"
card: "summary_large_image"
---



# Iluzja funkcji bezserwerowych w chmurze

![aws_costs_twitter_1](/images/content/onprem_vs_cloud.png)

### Wprowadzenie

Jestem rozczarowany tym, jak często marketing triumfuje nad zdrowym rozsądkiem. Wielu menedżerów stawia się nad własnymi
ekspertami - programistami. Dotyczy to również migracji do chmury. Spoiler: Jeśli chcesz zaoszczędzić pieniądze Jeśli
chcesz zaoszczędzić pieniądze, powinieneś unikać chmury. Ponieważ nowe hasło "serverless" w chmurze oznacza: Ty
zajmujesz się oprogramowaniem, my zajmujemy się sprzętem. Ty zajmiesz się oprogramowaniem, my zajmiemy się sprzętem.
Jeśli jednak masz zdolnego, zmotywowanego i dociekliwego administratora, możesz może również samodzielnie obsługiwać
serverless (np. [KNative](https://knative.dev)). ![aws_costs_twitter_1](/images/content/aws_costs_twitter_1.png)

### Funkcje bezserwerowe a mikrousługi:



#### Microservices

Typowa bezstanowa mikrousługa zajmuje się określoną funkcją/domeną i jest wdrażana w środowisku orkiestracji kontenerów.
środowisku orkiestracji kontenerów. Środowisko to dba o infrastrukturę, bezpieczeństwo, zaporę sieciową, logowaniem,
metrykami, sekretami, siecią, kopiami zapasowymi i nie tylko. Dużą zaletą jest to, że mikrousługę można wdrożyć lokalnie
za pomocą niewielką ilością zasobów zasobów i jest niezależna od chmury/serwera (może być wdrożona w dowolnym miejscu).

#### Funkcje bezserwerowe

Na wstępie mały żart: paradoksalne, ale prawdziwe - funkcje serverless w dużej mierze zależą od środowiska serwerowego.
:) Typowa funkcja bezserwerowa zajmuje się również tylko jedną konkretną funkcją / domeną i jest napisana w czystym
kodzie bez frameworków, aby być szybszym niż mikrousługa. kod, aby być szybszym niż mikrousługa (również dobre ćwiczenie
dla mikrousług). Dużą zaletą jest to, że funkcje bezserwerowe skalują się automatycznie. Jednak każda funkcja
bezserwerowa wymaga znacznej ilości GlueCode, aby zdefiniować infrastrukturę - bezpieczeństwo, firewall, sieć,
logowanie, metryki, sekrety, buforowanie, kopie zapasowe i wiele więcej. Dlatego prosta funkcja, taka jak kopiowanie
pliku zawierającego API, może szybko obejmować 1500 linii kodu (w tym IaC). mogą być zaangażowane. Koszty
administracyjne przenoszą się z administracji na rozwój w stosunku 1:N (1 do funkcji Serverless). funkcji). Wiedza i
implementacja nie są już zatem w pakiecie i mogą szybko stać się niestabilne. Ponadto występują zwiększone koszty
utrzymania. Prawdziwe testy integracyjne są również rzadkością w przypadku serverless lub są możliwe tylko przy dużym
wysiłku. Ostatecznie złożoność funkcji bezserwerowych jest znacznie wyższa niż w przypadku pojedynczej mikrousługi.
Wyższa złożoność oznacza również niższą łatwość konserwacji. Nowi członkowie zespołu mają trudniej i potrzebują znacznie
więcej wcześniejszej wiedzy. więcej wcześniejszej wiedzy.

### Serverless i ogólnie chmura

Większość technologii chmurowych nie jest aktualna. Na przykład, Node.js, Java, Python i inne języki lub technologie są
nieaktualne. Języki lub technologie często nie są łatwe do aktualizacji, zwykle pomaga tylko czekanie. Nawet nowoczesne
i standardowe technologie, takie jak MongoDB, MySQL, Kafka, NATS, RabbitMQ, Redis, Prometheus, InfluxDB, Grafana,
Kibana, Elastic Search itp. są albo niedostępne, albo zbyt drogie. Bez takich standardowych usług często znajdujemy się
w wirtualnej epoce kamienia łupanego i korzystamy z przestarzałych rozwiązań, np. webhooków do komunikacji zewnętrznej.
Ponadto pole manewru w kwestiach takich jak regulacje, zgodność z przepisami, ochrona danych i bezpieczeństwo w
przypadku awarii są poważnie ograniczone. Chmura powinna być zatem uruchamiana agnostycznie, aby móc szybko przełączać
się między AWS, Azure, Google, on-premise itp. i porównywać koszty. porównywać koszty. Ograniczenia są również
powszechne w chmurze, co prowadzi do kreatywnych obejść, które z kolei zwiększają złożoność. wzrost. Testowanie
integracyjne może również stać się kosztowne, ponieważ każdy programista potrzebuje własnego środowiska
programistycznego w chmurze. ponieważ wiele usług w chmurze jest trudno lub wcale nie testowalnych lokalnie. Ale nawet
bez testowania chmura jest droga. Podczas gdy w przypadku systemów lokalnych są to głównie koszty sprzętu, w chmurze
trzeba również płacić za ruch, niektóre standardowe usługi, a często nawet za wielokrotne opodatkowanie. a często nawet
za wielokrotne opodatkowanie. Co więcej, w chmurze łatwo jest stracić kontrolę nad rzeczami, ponieważ nie chodzi tu o
nie chodzi o łatwość obsługi, ale o pieniądze. Koszty są tak ukryte, że zauważa się je dopiero wtedy, gdy jest już za
późno. jest za późno. Podstawy architektury i infrastruktury muszą zostać wymyślone na nowo w chmurze, a zwłaszcza w
rozwiązaniach bezserwerowych. muszą zostać wymyślone na nowo, ponieważ implementacja zależy w dużej mierze od dostępnych
funkcji. Ilekroć projektowałem architekturę, myślałem: "To mogła być pojedyncza usługa". mogłoby być". Dla mnie
serverless jest ciekawym pomysłem i dobrze się skaluje, ale nie obniża kosztów. Wręcz przeciwnie Wręcz przeciwnie,
wymaga znacznie więcej wiedzy i czasu na rozwój. Serverless lub chmura wymagają dyscypliny i wcześniejszej wiedzy.
wcześniejszej wiedzy. Jeśli nie ma tej wiedzy w przypadku systemów lokalnych, nie będzie to łatwiejsze w przypadku
chmury. W jaki sposób programiści mają zdobyć dodatkową wiedzę na temat infrastruktury? Wolałbym dobrze zarządzany
klaster Kubernetes niż architekturę chmury. Ludzie się nie skalują. Wielu programistów nie ma dyscypliny w pisaniu kodu.
Niestety, dotyczy to 80 procent deweloperów. Jak więc ci deweloperzy będą w stanie uruchomić chmurę? chmurę? Ważne
jest, aby organizacje w pełni rozumiały wyzwania i implikacje architektury bezserwerowej i chmury. W pełni zrozumieć
wyzwania i implikacje architektury bezserwerowej i chmury. Wymaga to nie tylko wiedzy technicznej, ale także
strategicznego podejścia. A Nieprzemyślana migracja do chmury może prowadzić do złożoności, wyższych kosztów i
przeciążenia programistów. Podsumowując, serverless w chmurze to obiecująca koncepcja, ale należy ją dokładnie
rozważyć. należy rozważyć ostrożnie. Należy wziąć pod uwagę koszty, złożoność, łatwość konserwacji i umiejętności
zespołu programistów. należy wziąć pod uwagę. Każda firma ma inne wymagania i priorytety. Należy podjąć świadomą
decyzję, czy Serverless w chmurze jest właściwym rozwiązaniem lub czy alternatywne podejścia, takie jak np. klaster
Kubernetes są lepszym wyborem. Pomyślne wdrożenie technologii serverless i przetwarzania w chmurze wymaga połączenia
wiedzy technicznej planowania strategicznego i jasnego zrozumienia wymagań biznesowych. Tylko wtedy iluzja
bezserwerowości będzie możliwa i podjąć właściwą decyzję dotyczącą rozwoju własnego oprogramowania.

### Fazit

Wprowadzenie funkcji bezserwerowych w chmurze obiecuje elastyczność, skalowalność i odciążenie od zadań związanych z
infrastrukturą. deweloperów od zadań związanych z infrastrukturą. Nie należy jednak dać się zaślepić tej iluzji.
Przejście do chmury i korzystanie z funkcji bezserwerowych niesie ze sobą szereg wyzwań. Programiści muszą nauczyć się
nowego "języka" oprócz faktycznego rozwoju i wziąć na siebie większą odpowiedzialność bez odpowiedniego wsparcia. wziąć
na siebie większą odpowiedzialność. Złożoność funkcji bezserwerowych jest często wyższa niż w przypadku mikrousług,
ponieważ programiści muszą podjąć się wielu dodatkowych zadań, takich jak Deweloperzy muszą wziąć na siebie wiele
dodatkowych zadań, takich jak definiowanie infrastruktury, bezpieczeństwo i skalowanie. Prawdziwe testowanie
integracyjne jest trudne, a wcześniejsza wiedza i doświadczenie w zakresie operacji są jeszcze ważniejsze w chmurze.
Sama chmura niesie ze sobą kolejne wyzwania. Wiele technologii chmurowych nie jest aktualnych a korzystanie z
nowoczesnych, gotowych usług może być kosztowne lub nawet niemożliwe. Wymogi regulacyjne, zgodność z przepisami i i
ochrona danych ograniczają ich zakres. Ponadto koszty w chmurze łatwo wymykają się spod kontroli, a przegląd wydatków
jest szybko tracony. Podsumowując, należy dokładnie rozważyć zalety i wady rozwiązań bezserwerowych i chmurowych. Firmy
powinny wziąć pod uwagę swoje specyficzne wymagania, istniejącą wiedzę specjalistyczną w zespole i długoterminowe skutki
migracji do chmury. migracji do chmury. Świadoma decyzja oparta na kompleksowej analizie ma kluczowe znaczenie dla
powodzenia i rentowności projektu. projektu. Ostatecznie to firmy muszą odpowiednio wspierać swoich programistów,
realistycznie oceniać koszty i złożoność migracji do chmury. chmury i rozważenie alternatywnych rozwiązań, takich jak
dobrze zarządzane klastry Kubernetes. Dzięki jasnej strategii i dobremu zrozumieniu własnych potrzeb, firmy mogą w pełni
wykorzystać zalety chmury i możliwości serverless. z chmury i możliwości bezserwerowych oraz przejrzeć iluzję.

### Kontakt

[Problemy GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
