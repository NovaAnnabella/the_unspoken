---
title: "العودة إلى مافن؟"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "البحث الصعب عن البساطة ورحلة قصيرة لإعادة اكتشاف قوة Maven."
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# العودة إلى مافين؟

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)


## 10 سنوات من Gradle. بحثًا عن الراحة ورحلة قصيرة لإعادة اكتشاف قوة Maven.



### تعظيم إمكانات المطورين - نحتاج إلى المزيد من الأدوات التي توفر الوقت

المواضيع التي غالبًا ما يتم تجاهلها أو ناقشت نادرًا تهمني. غالبًا ما يتم استخدام التكنولوجيا الرائعة، ولكن قلة قليلة فقط
تتحدث عن المشكلات المرتبطة بها. تطوير البرمجيات أصبح في الوقت الحالي عملية مكلفة جدا. مع الكلمات الجذابة مثل "الخادم
الغير مرئي"، "البرمجة القليلة "، "IaC"، "كبير البيانات"، "السحاب"، "DevOps"، "أنت تصنعه أنت تشغله" إلخ. أصبح للمطورين
بالفعل المزيد من المهام الإضافية للتعامل معها. المزيد من المهام، التي تعني أنه لا يوجد الكثير من الخبراء وأن شيئًا ما
دائمًا يتم تجاهله من أجل التركيز. لذلك، الأتمتة وتوفير الوقت من الأهمية بمكان مهمة. "لا تجعلني أفكر" و"يعمل خارج
الصندوق" هي بالفعل علامات جودة جيدة، التي لا يمكنني رؤيتها في Gradle حتى الآن لأكون عادلا، Gradle ليست الأداة الحديثة
الوحيدة التي تجعلنا نعمل، بدلاً من تسهيل العمل.

### البحث الوهمي عن البساطة والأتمتة

منذ SOAP ، كان لدي عداوة غائرة للتكوينات القائمة على XML. كنت أأمل مع Gradle أن كتابة نصوص التثبيت ستكون لعبة أطفال.
للأسف، تقلصت آمالي وحماسي من مرة لأخرى. Gradle يسعى للمرونة ويقدم التكنولوجيا والجودة مقابلها. المطورين يتبعون الاتجاهات
بكل ضعف دون النظر إلى الآثار على موثوقية البرمجيات. الحفاظ على نصوص التثبيت الخاصة بـ Gradle بسيطة وسهلة الصيانة يتطلب
تعزيز الانضباط. إن هذا الانضباط نادر الوجود حتى في الكود المصدر، ولذلك فهو أقل وجودا في سيناريوهات التثبيت.

### الترجمات والحلول المؤقتة - عندما تصبح سكريبتات البناء تحديا

Gradle لا يعمل في الخلفية بشكل مختلف كثيرًا عن Maven. لذا، بعض الترجمات ضرورية. الميزات مثل كتالوج التبعية، إضافة Maven
Release، Dependabot والعديد غيرها هي في الواقع حلول بديلة للوظائف الأساسية التي يوفرها Maven بالفعل. مع مرونة Gradle،
غالبًا ما تنشأ تكوينات بناء معقدة، التي يصعب صيانتها. إضافات Gradle غالبًا ما تواجه مشكلات في التوافق، الحدود أو
التطويرات المحدودة. هذه المشكلات تنشأ بسبب الطبيعة المتطورة لنظام Gradle، تنوع البيئات التي يتم فيها استخدام Gradle ،
وجهد التنفيذ والصيانة الخاص بكل إضافة. كل شيء متصل ببعضه البعض.

### تأثير الدومينو من Gradle - سيناريو الكابوس في العالم الحقيقي

لقد رأيت العديد من الخدمات الصغرى التي لم تكن سوى بضعة سنوات وكانت أصبحت بالفعل غير قابلة للتحديث بسبب Gradle.
هنا أود أن أذكر أن هذه ليست المرة الأولى التي أرى فيها مثل هذا الخلل, ولا, لم يكونوا المطورين المبتدئين.

مهمتي **كانت ترقية Spring Boot 2.x إلى 2.7**. حذر: قد تتوقف بعد سنة! ذكرت المشاكل بإجمال:

* يتطلب ملف Gradle Build -> تخفيض إصدار جافا المحلي إلى 11 (WTF) (عادة ، Java تتوافق مع الإصدارات القديمة - هناك أيضًا أدوات تعمل كحلول بديلة مثل SdkMan ...)
* يتطلب تحديث Spring Boot -> تحديث Gradle (WTF)
* يتطلب تحديث Gradle -> تحديث الإضافة
* يتطلب تحديث الإضافة -> تحديث Groovy (WTF)
* يتطلب تحديث Groovy -> تحديثات تست الإطار والاختبار (WTF)
* يتطلب تحديث تست الإطار -> تحديث التبعيات
* \[...\]
بالإضافة إلى ذلك، بعض الإضافات لا تعمل مع الإصدارات الأحدث من Gradle، بعضها لا يتطور بعد الآن، غير متوافق مع الإضافات الأخرى، يعمل فقط مع Gradle KTS، وليس مع Gradle Groovy، أو لديه ببساطة حدود. حتى الإضافات من موردين كبار مثل Spring لديها وظائف محدودة مقارنة بإضافات Maven الخاصة بهم. في النهاية، أنا أملك ملف بناء Gradle رائع وقصير، لا أحد يستطيع صيانته بشكل صحيح، ولا حتى المطورين الذين كتبوه، ومع ذلك، ما زالوا يحبون Gradle. أنا أعرف فقط القليل الذين يمكن أن يفهموا بالفعل أو يكتبون سكريبتات Gradle.

### إعادة اكتشاف قوة مافين - استغلال قدرات مافين السحرية

هنا بعض الميزات المفضلة لدي من Maven:
يمكن بدء التشغيل وتكوين الإضافات مباشرة من سطر الأوامر دون الحاجة لتعريفها مسبقًا. بالإضافة إلى ذلك، فإنها مستقلة إلى حد كبير عن تكوينات الوظائف الإضافية الأخرى.

| الأمر كمثال                      | الوصف                                                                                                                                    | الرابط                                                                   | 
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| `mvn versions:use -latest-versions` | تحديث الإصدارات - من يحتاج إلى Dependabot؟ نعم، تم تحديث مشاريعي لسنوات بدون مشاكل إلى الإصدار الأحدث بدون طلبات دمج مزعجة | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0` | تعيين إصدار المشروع...                                                                                                                    | https://www.mojohaus.org/versions/versions-maven-plugin/index.html      |
| `mvn license:add-third-party`       | سرد التبعيات وعرض تراخيصها (قد يكون هناك فشل حتى في حالة الرخص المستبعدة)                                                              | https://www.mojohaus.org/license-maven-plugin/index.html                | 

هذه القائمة قد تستمر إلى الأبد بهذه الطريقة. يذكرني بخطوات عمل GitHub بطريقة ما.

![args_command_line_plugin_maven](/images/content/maven_plugin_command_line_args.png)


### لا تحب XML؟

لا مشكلة! فقط اكتب ملف بناء البرنامج الخاص بك في `ruby`, `groovy`, `scala`, `yaml`, `atom` أو `Java`. يجعل الامتداد Polygot
(https://github.com/takari/polyglot-maven) ذلك ممكنا. للتجربة ،
قم بتشغيل `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` وفي غضون مللي ثانية واحدة يتم ترجمة ملف بناء البرنامج الخاص بك. من الأسف أنه لا يوجد مترجم موثوق Maven <> Gradle
:( 

نعم ، ملفات بناء Maven كبيرة ، لكنها أيضًا سهلة الفهم للغاية. يمكن انجاز التعديلات أو تصحيح الأخطاء في غمضة عين.

### العمر مجرد رقم - الاستقرار والتطور في Mavens

نعم، لقد مرت فترة طويلة منذ ظهور Maven وربما لا تتوافق جماليته مع المعايير الحالية. ومع ذلك، أتاحت البقاء الطويل لـ
Maven له التكيف والتطور. يعمل Maven بشكل مستقل عن مشروعك. يمكن استخدام ملفات البناء ببساطة مرة أخرى. الإضافات تعمل في
صندوق رمل وهي مستقلة عن بعضها ومستقلة عن نسخة Java أو Maven. هذا التصميم يعزز الاستقرار والقدرة على التنبؤ ويسهل إدارة
عمليات البناء المعقدة بدون تعارضات غير متوقعة.

### الخلاصة

في الوقت الحاضر، ازدحمت بيئة التطوير بالعديد من المهام والتقنيات للمطورين. في البحث عن البساطة والأتمتة، ظهر Gradle
كأداة بناء حديثة، لكنه جلب معه تحدياته الخاصة. بلا شك، مفهوم Gradle جيد! ولكن في ضوء التعقيد والوقت الذي يتم استثماره في
برامج بناء Gradle، يطرح السؤال عما إذا كان من الأسهل توسيع Maven. من خلال الإضافات والتوسعات، يمكن تحديث Maven وتبسيطه
في أي وقت. ألن يكون التطور أكثر إثارة واستدامة، بدلاً من القفز من تقنية إلى أخرى؟

### الروابط

* [الانتقال مرة أخرى من Gradle إلى maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### الاتصال

[قضايا GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).