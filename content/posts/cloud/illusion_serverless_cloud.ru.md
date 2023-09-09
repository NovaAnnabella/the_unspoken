---
title: "Серверная Иллюзия & Облако"
date: 2023-05-24
author: "Nova Annabella"
slug: illusion_serverless_cloud
tags: [ Development, Serverless, Cloud, Microservices, Scalability, Architecture, Infrastructure ]
categories: [ Technology, Software, Cloud ]
description: "Вызовы и реальность бессерверных функций в облаке. Ценные взгляды для компаний, рассматривающих возможность миграции в облако."
draft: false
images:
  - "/images/content/onprem_vs_cloud.png"
card: "summary_large_image"
---


# Иллюзия серверлесс функций в облаке

![aws_costs_twitter_1](/images/content/onprem_vs_cloud.png)

### Введение

Меня разочаровывает, как часто маркетинг побеждает здравый смысл. Многие менеджеры пренебрегают
собственными экспертами - разработчиками. Это также относится к миграции в облако. Спойлер: кто хочет
сэкономить, должен избегать облака. Ведь новый жаргон "Бессерверный" в облаке означает: ты заботишься о
программном обеспечении, мы заботимся о оборудовании. Однако, если у вас есть способный, мотивированный и любознательный администратор, тогда
можно самостоятельно управлять Бессерверностью (например, [KNative](https://knative.dev)).

![aws_costs_twitter_1](/images/content/aws_costs_twitter_1.png)

### Бессерверные функции против микросервисов:



#### Микросервисы

Типичный бессостоянийный микросервис заботится о конкретной функции/домене и развертывается в среде оркестровки
контейнеров. Эта среда заботится о инфраструктуре, безопасности, брандмауэре, логировании, метриках, секретах, сети,
резервных копиях и многом другом. Большим преимуществом является то, что микросервис можно локально тестировать с
несколькими ресурсами и он агностичен к облачным/серверным решениям (может быть использован везде).

#### Бессерверные функции

Небольшая шутка на заре: Парадокс, но факт - функции без сервера сильно зависят от серверной среды. :)
Типичная функция без сервера также заботится только о конкретной функции/области и написана без фреймворков
в
чистом коде, чтобы быть быстрее микросервиса (также хорошая практика для микросервисов). Большой
преимуществом является то, что функции без сервера масштабируются автоматически. Однако каждая функция без сервера требует
значительное количество GlueCode, чтобы определить инфраструктуру - безопасность, брандмауэр, сеть, логирование, метрики,
секреты, кэширование, резервное копирование и многое другое.
Поэтому простая функция, такая как копирование файла включая API, может быстро включать 1500 строк кода (вкл. IaC).
Расходы на администрирование смещаются от администрирования к разработке в соотношении 1: N (1 к функциям без сервера)
Знания и реализация больше не
сосредоточены и могут быстро стать нестабильными. К этому добавляются повышенные расходы на обслуживание.
Также реальные интеграционные тесты с сервером редки или связаны с большими усилиями.
В конечном итоге, сложность функций без сервера значительно выше, чем у отдельного микросервиса.
Большая сложность также означает меньшую обслуживаемость. Новым членам команды будет труднее и им потребуется значительно
больше предварительных знаний.

### Бессерверные технологии и облако в целом

Большинство облачных технологий не являются самыми новыми. Например, Node.js, Java, Python и другие языки или технологии часто сложно обновить, в большинстве случаев остается только ждать. Даже современные и стандартные технологии, такие как MongoDB, MySQL, Kafka, NATS, RabbitMQ, Redis, Prometheus, InfluxDB, Grafana, Kibana, Elastic Search и др. либо не доступны, либо завышены по цене. Без таких стандартных сервисов вы часто оказываетесь в виртуальном каменном веке и используете устаревшие решения, например, веб-хуки для внешнего общения. К этому добавляется то, что возможность действовать в вопросах регулирования, соблюдения нормативных требований, защиты данных и надежности сильно ограничена.

Облако, следовательно, должно быть агностическим, чтобы быстро переключаться между AWS, Azure, Google, On-Premise и т.д. и сравнивать стоимость. Ограничения часто есть и в облаке, что приводит к творческим обходным путям, увеличивающим сложность. Интегрированное тестирование также может быть дорогим, поскольку каждому разработчику требуется собственная среда разработки в облаке, поскольку многие облачные услуги сложно или вовсе не тестируются локально. Но даже без тестов облако дорогое. В то время как для систем On-Premise главным образом возникают затраты на оборудование, в облаке дополнительно нужно платить за трафик, некоторые стандартные услуги и даже часто за двойное налогообложение. Кроме того, в облаке легко потерять обзор, поскольку речь идет не о удобстве пользователя, а об деньгах. Стоимость так скрыта, что вы заметите это только тогда, когда уже будет слишком поздно.

Основы архитектуры и инфраструктуры должны быть переизобретены в облаке и, в частности, в области безсерверных технологий, поскольку реализация сильно зависит от доступных функций. Каждый раз, когда я проектирую архитектуру, у меня возникает мысль: "Это мог быть одним сервисом".

Для меня безсерверная технология - интересная идея, и она хорошо масштабируется, но она не снижает стоимости. Напротив, это требует гораздо больше знаний и времени для разработки. Without a server or the cloud requires discipline and prior knowledge. Если знания для систем On-Premise отсутствуют, с облаком это не становится проще. Как разработчикам обучиться еще и знаниям по инфраструктуре?

Я предпочел бы хорошо управляемый кластер Kubernetes архитектуре облака. Работники не масштабируются. У многих разработчиков нет дисциплины в написании кода. К сожалению, это относится к 80 процентам разработчиков. Так как же эти разработчики смогут обрабатывать облако?

Важно, чтобы компании полностью понимали проблемы и последствия бескластерной архитектуры и облака. Это требует не только технических знаний, но и стратегического подхода. Непродуманная миграция в облако может привести к сложности, более высоким затратам и перегрузке разработчиков.

В заключение можно сказать, что безсерверная технология в облаке - это обещающий концепт, который, однако, следует тщательно рассмотреть. Нужно учесть затраты, сложность, удобство обслуживания и навыки команды разработчиков. Каждая компания имеет свои требования и приоритеты. Стоит принять обоснованное решение, правильно ли без сервера в облаке или альтернативные подходы, такие как хороший кластер Kubernetes, являются лучшим выбором.

Успешное применение безсерверных и облачных вычислений требует сочетания технической экспертизы, стратегического планирования и четкого понимания бизнес-требований. Только так можно проникнуть в иллюзию без сервера и принять правильное решение по разработке программного обеспечения.


### Заключение

Внедрение функций без сервера в облаке обещает гибкость, масштабируемость и освобождение
разработчиков от задач по инфраструктуре. Однако этой иллюзией не следует обманываться. Переход
в облако и использование функций без сервера связаны с рядом проблем.

Разработчики должны выучить новый "язык" и без соответствующей поддержки
взять на себя больше ответственности.
Сложность функций без сервера часто превышает сложность микросервисов, так как разработчикам приходится заниматься многими дополнительными
задачами, такими как определение инфраструктуры, безопасность и масштабирование. Реальные интеграционные тесты
сложны, а предварительные знания и опыт работы в облаке становятся еще важнее.

Само облако привносит дополнительные проблемы. Многие технологии облака устарели,
и использование современных стандартных услуг может быть дорогим или даже невозможным. Регулятивные требования, соблюдение нормативов и
защита данных ограничивают диапазон действий. Кроме того, расходы в облаке легко могут выйти из-под контроля,
и обзор расходов быстро теряется.

В целом нужно тщательно взвесить плюсы и минусы функций без сервера и облака.
Компании должны учитывать свои специфические требования, имеющиеся знания в команде и долгосрочные последствия
переноса в облако.
Обоснованное решение на основе всестороннего анализа критично для успеха и рентабельности
проекта.

В конечном итоге зависит от компаний, как они будут поддерживать своих разработчиков, реалистично оценивать стоимость и сложность облака и рассматривать альтернативные решения, такие как хорошо управляемые кластеры Kubernetes.
С четкой стратегией и глубоким пониманием своих потребностей компании могут наиболее эффективно использовать преимущества облака и функций без сервера, прозревая через иллюзии.


### Контакт

[Проблемы на GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).