---
title: "Назад к Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "Трудно уловимый поиск простоты и короткое путешествие к повторному открытию силы Maven."
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# Вернуться к Maven?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

## 10 лет Gradle. В поисках облегчения и краткое путешествие к повторному открытию силы Maven.



### Максимизация потенциала разработчиков - Нам нужны больше инструментов для экономии времени

Темы, которые часто упускаются из виду или редко обсуждаются, меня интересуют. Часто используются крутые технологии,
однако едва ли кто-то говорит о связанных с ними проблемах.
Разработка сегодня стала очень трудоемкой.
С крутыми ключевыми словами, такими как "Безсерверные", "Низкий код", "IaC", "Большие данные", "Облако", "DevOps", "Вы создаете, вы запускаете"
и т.д. разработчики уже имеют более чем достаточно дополнительных задач. Больше задач означает, что экспертов почти не осталось,
и всегда что-то упускается из виду. Поэтому автоматизация и экономия времени очень важны.
"Don’t make me think" и "Works out of the Box" уже являются хорошими качественными характеристиками, которые я еще
не вижу в Gradle. Чтобы быть справедливым, Gradle - не единственный современный инструмент, который заставляет нас работать, а не
облегчает это.

### Иллюзорный поиск простоты и автоматизации

С тех пор как я познакомился с SOAP, у меня появилось глубокое отвращение к XML-основанным конфигурациям. Я надеялся, что с Gradle написание привязочных скриптов станет проще. К сожалению, мои надежды и мотивация становились все меньше и меньше. Gradle стремится к гибкости, но в ущерб автоматизации и качеству. Разработчики слепо следуют трендам, не принимая во внимание влияние на надежность программного обеспечения. Чтобы держать Gradle Build скрипты простыми и легкими в обслуживании, требуется строгая дисциплина. Такая дисциплина редко найдется в исходном коде, и поэтому она еще реже встречается в сценариях сборки.


### Переводы и обходные решения - Когда сборочные скрипты становятся проблемой

Gradle работает в фоновом режиме не сильно иначе, чем Maven. Поэтому некоторые переводы необходимы. Функции, такие как
Каталог зависимостей, плагин Maven Release, Dependabot и многие другие, на самом деле являются обходными путями для основных
механизмов, которые Maven уже имеет. С гибкостью Gradle часто появляются сложные конфигурации сборки,
которые сложно поддерживать.
Плагины Gradle часто имеют проблемы с совместимостью, ограничения или ограниченную дальнейшую разработку. Эти проблемы возникают
из-за развивающейся природы экосистемы Gradle, разнообразия сред, в которых используется Gradle,
и специфического усилия по реализации и поддержке каждого плагина. Все взаимосвязано.

### Домино-эффект Gradle - Сценарий кошмара в реальном мире

Я видел много микросервисов, которым всего несколько лет, и они уже стали неподдерживаемыми из-за Gradle.
Важно отметить, что это не первый раз, когда я вижу такое, и нет, это не были начинающие разработчики.

Моя **задача была обновить Spring Boot 2.x до 2.7**. Спойлер: Я сдался через год!
Проблемы вкратце:

* Файл сборки Gradle требует -> Понижение моей локальной версии Java до 11 (ЧТО ЗА...) (Обычно Java совместима
  с более старыми версиями - здесь также есть обходные инструменты вроде SdkMan...)
* Обновление Spring Boot требует -> Обновление Gradle (ЧТО ЗА...)
* Обновление Gradle требует -> Обновление плагина
* Обновление плагина требует -> Обновление Groovy (ЧТО ЗА...)
* Обновление Groovy требует -> Обновление плагина тестирования и обновление тестов (ЧТО ЗА...)
* Обновление плагина тестирования требует -> Обновления зависимостей
* \[...]
  Кроме того, некоторые плагины не работают с новыми версиями Gradle, некоторые не развиваются, они несовместимы
  с другими плагинами, работают только с Gradle KTS, а не с Gradle Groovy, или просто имеют ограничения. Даже
  плагины от крупных поставщиков, таких как Spring, имеют ограниченную функциональность по сравнению с их плагинами
  Maven. В итоге у меня есть классная, короткая сборка Gradle, которую никто правильно поддерживать не может,
  даже разработчики, которые ее написали, и они все еще любят Gradle. Я знаю немногих, кто реально понимает
  или может написать скрипты Gradle.


### Переоткрытие силы Maven - Использование волшебных сил Maven

Вот мои любимые функции Maven:
Плагины можно запускать и настраивать прямо с командной строки, не определяя их заранее.
Плюс, они в значительной степени независимы от других конфигураций плагинов.

| Пример команды                        | Описание                                                                                                                                                                | Ссылка                                                                     | 
|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`   | Обновление версий - кому нужен Dependabot? Да, мои проекты уже многие годы без проблем обновляются до последней версии, без раздражающих запросов на слияние         | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0` | Установка версии проекта...                                                                                                                                             | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`         | Вывод списка зависимостей и их лицензий (может даже сбой при исключенных лицензиях)                                                                                     | https://www.mojohaus.org/license-maven-plugin/index.html                 | 

Этот список можно продолжить бесконечно. Это как-то напоминает мне шаги рабочего процесса GitHub.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)


### Тебе не нравится XML?

Нет проблемы! Просто напишите ваш Build File на `ruby`, `groovy`, `scala`, `yaml`, `atom` или `Java`. Расширение Polygot
(https://github.com/takari/polyglot-maven) делает это возможным. Чтобы попробовать,
просто выполните `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` и через
несколько миллисекунд ваш Build File будет переведен. Жаль, что нет надежного переводчика Maven <> Gradle
:( 
Да, файлы сборки Maven большие, но они очень легко понимаются. Доработки или отладка выполняются в мгновение ока.


### Возраст - это просто число - Стабильность и эволюция Mavens

Признаюсь, Maven существует уже довольно долго, и его эстетика, возможно, не соответствует современным стандартам.
Однако долговечность Maven позволила ему приспосабливаться и развиваться. Maven работает независимо от вашего проекта.
Файлы сборки можно легко повторно использовать. Плагины работают в песочнице и независимы друг от друга и от версии Java
или Maven. Этот дизайн способствует стабильности и предсказуемости и облегчает управление сложными процессами сборки без
неожиданных конфликтов.

### Заключение

В наше время среда разработки перегружена множеством задач и технологий для разработчиков. В поисках простоты и
автоматизации вышел Gradle как современный инструмент сборки, но он принес свои собственные проблемы. Без сомнения,
концепция Gradle хороша! Но учитывая сложность и время, вложенное в сценарии сборки Gradle, возникает вопрос, не было бы
проще расширить Maven. С помощью плагинов и расширений можно было бы в любое время обновить и упростить Maven. Не было
бы более интересно и устойчиво развиваться, а не прыгать с одной технологии на другую?

### Ссылки

* [Переход обратно с Gradle на maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### Контакт

[GitHub Проблемы](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).