---
title: "العودة إلى مافن؟"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: Die schwer fassbare Suche nach Einfachheit und eine kurze Reise zur Wiederentdeckung der Macht von Maven.
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---



# العودة إلى Maven؟

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

## 10 سنوات من Gradle. بحثًا عن السهولة ورحلة قصيرة لاكتشاف قوة Maven مرة أخرى.

# Zusammenfassung In diesem Kapitel haben wir gelernt, wie man Markdown-Dokumente schreibt und formatiert. Wir haben
verschiedene Formatierungsoptionen wie Überschriften, Fett-, Kursiv- und durchgestrichenen Text kennengelernt. Auch die
Erstellung von Listen und Links wurde behandelt. Wir hoffen, dass Sie jetzt in der Lage sind, effektive Markdown-
Dokumente zu schreiben und zu formatieren! # Beispiel ## Einführung Willkommen zur Einführung in meine Markdown-Datei!
In dieser Datei werde ich verschiedene Markdown-Syntax verwenden, um Ihnen zu zeigen, wie man Markdown-Dokumente
schreibt und formatiert. ## Abschnitt 1: Überschriften Die erste Sache, die ich in diesem Abschnitt besprechen werde,
sind Überschriften. Überschriften werden verwendet, um Abschnitte zu kennzeichnen und ihnen eine Hierarchie zu geben.
## Abschnitt 2: Listen Ein weiteres wichtiges Feature von Markdown sind Listen. Es gibt zwei Arten von Listen:
ungeordnete Listen und geordnete Listen. ## Abschnitt 3: Links Der letzte Abschnitt, den ich in diesem Beispiel
behandeln werde, sind Links. Links ermöglichen es Ihnen, auf andere Webseiten oder Dateien zu verlinken.

### تعظيم إمكانيات المطورين - نحن بحاجة إلى المزيد من الأدوات التي توفر الوقت

Themen, die oft übersehen oder selten diskutiert werden, interessieren mich. Oft sind coole Technologien im Einsatz,
doch kaum jemand spricht über die damit verbundenen Probleme. Entwicklung ist heut zu Tage sehr aufwendig geworden. Mit
den coolen Buzzwords wie “Serverless”, “Low Code”, “IaC”, “Big Data”, “Cloud”, “DevOps”, “You Build it You run it” usw.
haben Entwickler bereits mehr als genug Zusatzaufgaben zu bewältigen. Mehr Aufgaben, bedeutet, dass es kaum noch
Experten gibt und immer irgendetwas für den Focus vernachlässigt wird. Daher sind Automationen und Zeitersparnisse mega
wichtig. “Don’t make me think” und “Works out of the Box” sind bereits gute Qualitätsmerkmale, die ich in Gradle noch
nicht sehen kann. Um fair zu sein, Gradle ist nicht das einzige moderne Werkzeug, das uns Arbeit macht, anstatt sie zu
erleichtern.

### البحث الواهم عن البساطة والتأتأة

منذ SOAP لدي انزعاج عميق من التكوينات المبنية على XML. مع Gradle، كنت قد أملت أن كتابة نصوص الربط ستكون سهلة. للأسف،
تضاءلت آمالي ودافعي في كل مرة. يسعى Gradle إلى المرونة ولكن يضحي الأتمتة والجودة لذلك. يتبع المطورون الاتجاه عميانًا
بدون أخذ في الاعتبار تأثيره على موثوقية البرامج. لجعل نصوص بناء Gradle سهلة وقليلة الصيانة، يتطلب الأمر انضباطًا قويًا.
هذا النوع من الانضباط نادرٌ جدًا في رمز المصدر وبالتالي هو أكثر ندرة في نصوص البناء.

### الترجمات وحلول الظروف - عندما تصبح نصوص بناء السكربت تحدًا

لا يختلف Gradle في الخلفية كثيرًا عن Maven. لذلك فإن بعض الترجمات ضرورية. الخصائص مثل Dependency Catalog ، Maven Release
Plugin ، ، و Dependabot وغيرها الكثير هي في الواقع حلول بديلة للوظائف الأساسية التي يتمتع بها Maven. تؤدي مرونة Gradle
في بعض الأحيان إلى تكوينات بناء معقدة يصعب صيانتها. غالبًا ما يواجه تطبيقات Gradle مشكلات التوافق والقيود أو التطورات
المحدودة. تنشأ هذه المشكلات بسبب طبيعة نظام Gradle المتطور ، وتنوع البيئات التي يتم استخدام Gradle فيها ، وتكاليف
التنفيذ والصيانة الخاصة بكل تطبيق. كل شيء يترابط مع بعضه البعض.

### الآثار التدريجية لـGradle - سيناريو كابوسي في العالم الحقيقي

لقد رأيت الكثير من خدمات المايكرو التي لم تعد صيانة بعد عدة سنوات فقط بسبب Gradle. يجدر بالذكر أن هذه ليست المرة الأولى
التي أرى مثل هذا الأمر، ولا، لم تكن المطورين المبتدئين. كانت مهمتي تحديث Spring Boot 2.x إلى 2.7. المشاكل كانت كالتالي:
* يتطلب ملف Gradle Build تخفيض إصدار Java المحلي إلى 11 (WTF) (عادةً ما يكون Java متوافقًا مع الإصدارات السابقة - هناك
أدوات تحويلية مثل SdkMan...) * تحديث Spring Boot يتطلب تحديث Gradle (WTF) * تحديث Gradle يتطلب تحديث المكون الإضافي *
تحديث المكون الإضافي يتطلب تحديث Groovy (WTF) * تحديث Groovy يتطلب تحديث إطار الاختبار والتحديث (WTF) * تحديث إطار
الاختبار يتطلب تحديثات في المعتمدات * [...] بالإضافة إلى ذلك، بعض المكونات الإضافية لا تعمل مع إصدارات Gradle الأحدث،
وبعضها لم يعد يتم تطويره، وبعضها غير متوافق مع المكونات الإضافية الأخرى، ويعمل فقط مع Gradle KTS وليس مع Gradle Groovy،
أو لها حدود بسيطة. حتى المكونات الإضافية من مزودي الخدمة الكبيرة مثل Spring لديها وظائف محدودة بالمقارنة مع مكونات Maven
الخاصة بهم. في النهاية، لدي ملف Gradle-Build قصير وجميل ولكن لا يمكن لأحد إصلاحه بشكل صحيح، حتى لمطوريه الذين كتبوه، ولا
يزالون يحبون Gradle. أنا أعرف قلة قليلة فقط الذين يفهمون بجدية كتابة نصوص Gradle.

### إعادة اكتشاف قوة `Maven` - الاستفادة من قوى `Maven` السحرية

هنا بعض وظائفي المفضلة لـ Maven: يمكن تشغيل الوظائف المساعدة في سطر الأوامر وتكوينها مباشرةً دون الحاجة إلى تعريفها
مسبقًا. بالإضافة إلى ذلك ، فهي مستقلة بشكل كبير عن تكوين الوظائف المساعدة الأخرى. | أمر المثال
| الوصف
| الرابط                                       | |-------------------------------
----------|-------------------------------------------------------------------------------------------------------------
----------------------------------------------------|-------------------------------------------------------------------
---------------| | `mvn versions:use -latest-versions`  | تحديث الإصدارات - من يحتاج إلى Dependabot؟ نعم ، تم تحديث
مشاريعي لسنوات دون مشكلة إلى الإصدار الأحدث دون الحاجة إلى طلب دمج مزعج            |
https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html | | `mvn versions:set -DnewVersion=1.0.0` |
تحديد إصدار المشروع...
| https://www.mojohaus.org/versions/versions-maven-plugin/index.html    | | `mvn license:add-third-party`     |
إدراج قائمة الاعتماديات وعرض تراخيصها (يمكن أن يفشل حتى مع تراخيص مستبعدة)
| https://www.mojohaus.org/license-maven-plugin/index.html         |  يمكن لهذه القائمة أن تستمر إلى الأبد.
يذكرني ذلك بخطوات سير العمل في GitHub. ! [] (/images/content/maven_plugin_command_line_args.png)

### هل تكره XML؟

لا مشكلة! ما عليك سوى كتابة ملف البناء الخاص بك بـ `ruby`، `groovy`، `scala`، `yaml`، `atom` أو `Java`. تجعل إضافة
Polygot (https://github.com/takari/polyglot-maven) ذلك ممكناً. لتجربة ذلك، ما عليك سوى تشغيل `mvn
io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` وفي غضون بضع ميلي ثانية يتم
ترجمة ملف بناءك. يتمنى أن يكون هناك مترجم Maven <> Gradle يمكن الاعتماد عليه :( نعم ، ملفات بناء Maven كبيرة ، لكنها
سهلة الفهم جداً. يتم تحسينها أو تصحيحها أو تشخيصها في لحظة.

### العمر مجرد رقم - ثبات وتطور مفنز

منحى الحقيقة، Maven موجودة منذ وقت طويل وأسلوبها الجمالي لا يتوافق ربما مع المعايير الحالية. الطول الذي دام لحظة Maven
سمح لها بالتكيف والتطور. يعمل Maven بشكل مستقل من مشروعك. يمكن إعادة استخدام ملفات البناء بسهولة. تعمل المكونات الإضافية
في صندوق رملي وتعمل بشكل مستقل ولا تعتمد على إصدار Java أو Maven. يعزز هذا التصميم الاستقرار والتنبؤية ويجعل من السهل
إدارة عمليات البناء المعقدة دون صدامات غير متوقعة.

### استنتاج

اليوم ، بيئة التطوير محملة بالمهام والتقنيات المختلفة للمطورين. في سعينا للبساطة والتحسينات التلقائية ، ظهر Gradle كأداة
بناء حديثة ومع ذلك أحدبت التحديات الخاصة به. من الواضح أن مفهوم Gradle جيد! ولكن مع تعقيدات بناء السكربتات والوقت
المستهلك في برنامج Gradle ، يطرح السؤال ما إذا كان من الأسهل توسيع Maven. باستخدام الإضافات والمكونات الإضافية ، يمكن
تحديث وتبسيط Maven في أي وقت. هل ليس من المثير والمستدام العمل على تطوير التقنية بدلاً من القفز من تقنية إلى أخرى؟

### الروابط

* [العودة من Gradle إلى Maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### الاتصال

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose)
