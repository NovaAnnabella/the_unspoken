---
title: "عودة إلى Maven؟"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "### الترجمة:Die schwer fassbare Suche nach Einfachheit und eine kurze Reise zur Wiederentdeckung der Macht von Maven#### البحث الشاق عن البساطة ورحلة قصيرة لإعادة اكتشاف قوة مافن"
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# العودة إلى مفِن؟

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

لا يوجد ترجمة لتخطيط الماركدون لأنه لا يحتوي على نص من اللغة الإنجليزية أو أي لغة أخرى.

## ١٠ سنوات من Gradle. البحث عن الراحة ورحلة قصيرة لإعادة اكتشاف قوة Maven.

هذا النص لا يحتوي على أي معلومات للترجمة.

### تعظيم إمكانيات المطورين - نحتاج إلى المزيد من الأدوات الموفرة للوقت

المواضيع التي غالباً ما تُغفل أو نادراً ما يُناقشها، تُهمُّني. في كثير من الأحيان يتم استخدام تقنيات رائعة، ولكن لا أحد
يتحدث عن المشاكل المرتبطة بها. أصبح التطوير في الوقت الحالي مكلفًا جداً. مع الكلمات الرنانة الرائعة مثل "سيرفرليس"،
"لوكو"، "IaC"، "بيج داتا"، "سحابة"، "ديفوبس"، "أنت تبنيه وأنت تشغله"، هناك الكثير من المهام الإضافية التي يجب على
المطورين التعامل معها. المزيد من المهام يعني أنه يكاد لا يوجد خبراء بعد، ودائمًا ما يتم تجاهل شيء ما لتركيزه على شيء
آخر. لذلك، الإجراءات التلقائية وتوفير الوقت أمران مهمان جداً. "لا تجعلني أفكر" و"يعمل مباشرةً" هما مؤشرات جيدة جداً
للجودة، والتي لا يمكن العثور عليها في Gradle. يجب أن نكون عادلين، فGradle ليس الأداة الحديثة الوحيدة التي تسبب لنا
المشاكل بدلاً من تسهيل العمل.

### البحث المغلوط عن البساطة والتَّأتأة

منذ SOAP ، لدي مقت وجذور عميقة ضد تكوينات XML المستندة. كنت آمل أن يكون كتابة نصوص الربط سهلاً مع Gradle. للأسف ، تضاءلت
آمالي ودوافعي من مرة إلى أخرى. يسعى Gradle إلى المرونة ويضحي بالتلقائية والجودة من أجل ذلك. المطورون يتبعون التيار بلا
تفكير في الآثار على موثوقية البرامج. للحفاظ على بناء Skripte Gradle بسيطة وقابلة للصيانة ، يتطلب الأمر انضباطًا قويًا.
مثل هذا الانضباط نادر في الأصلي في الشفرة المصدرية ولذلك فهو أكثر ندرةً في نصوص البناء.

### الترجمات والحلول المؤقتة - عندما تصبح نصوص بناء الأكواد تحدٍّا

لا يختلف تعامل Gradle في الخلفية كثيرًا عن Maven. لذلك ، هناك بعض الترجمات اللازمة. الميزات مثل كتالوج الاعتمادات وملحق
إصدار Maven و Dependabot والعديد من الأدوات الأخرى هي في الواقع حيل للوظائف الأساسية التي يتضمنها Maven بالفعل. مع مرونة
Gradle ، تنشأ غالبًا تكوينات بناء معقدة ، والتي يصعب صيانتها. عادةً ما يواجه مكونات إضافية في Gradle مشكلات التوافق
وحدودًا أو تطويرًا محدودًا. تنشأ هذه المشكلات بسبب الطبيعة التي يتطور بها نظام Gradle ، وتنوع البيئات التي يتم استخدام
Gradle فيها ، وتكلفة التنفيذ والصيانة الخاصة بكل مكون إضافي. كل شيء مترابط.

### التأثير المتسلسل لـ Gradle - سيناريو كابوسي في الحياة الحقيقية

لقد رأيت العديد من خدمات مايكرو العمر يتراوح من عدة سنوات وبالفعل لم يعد يمكن الصيانة بسبب Gradle. من المهم أن نشير إلى أن هذا ليس المرة الأولى التي أرى فيها شيئًا من هذا القبيل ، وليس كان المطورين المبتدئين.

مهمتي هي ** ترقية Spring Boot 2.x إلى 2.7 **. المفاجأة: استسلمت بعد عام! المشاكل بشكل مختصر:

* يتطلب ملف Gradle Build -> تخفيض إصدار Java المحلي الخاص بي إلى 11 (WTF) (عادةً ما يكون Java متوافقًا للأسفل - هناك أيضًا أدوات Workaround مثل SdkMan ...)
* تتطلب تحديث Spring Boot -> تحديث Gradle (WTF)
* يتطلب تحديث Gradle -> تحديث Plugin
* يتطلب تحديث Plugin -> تحديث Groovy (WTF)
* يتطلب تحديث Groovy -> تحديث اختبار الإطار والتحديثات الخاصة بالاختبارات (WTF)
* تحديث إطار الاختبار يتطلب -> تحديث المعتمدات
* [....]
   بالإضافة إلى ذلك ، لا يتوافق بعض البرامج الإضافية مع إصدارات Gradle الأحدث ، ولا تزال بعضها غير قيد التطوير ، وغير متوافقة مع بعض البرامج الإضافية ، وتعمل فقط مع Gradle KTS ، وليس مع Gradle Groovy، أو لديها حدود بسيطة. بنهاية المطاف ، حصلت على ملف Gradle Build قصير وجميل ، لا يمكن لأي شخص الصيانة بشكل صحيح ، لا حتى المطورين الذين كتبوها ، ولا يزالوا يحبون Gradle. أعرف قلة فقط من يفهمون برامج Gradle بشكل جاد أو يمكنهم كتابة النصوص.

### إعادة اكتشاف قوة مافن - استخدام قوى مافن السحرية

هنا خمسة من ميزاتي المفضلة لـ Maven:
يمكن تشغيل الوظائف المساعدة مباشرة من سطر الأوامر وتكوينها دون الحاجة إلى تحديدها مسبقًا. بالإضافة إلى ذلك ، فإنها تعتمد إلى حد كبير على تكوينات المكوّنات الإضافية الأخرى.

| أمر المثال                                    | الوصف                                                                                            | الرابط                                                                 | 
|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`   | تحديث الإصدارات - من يحتاج إلى Dependabot؟ نعم ، تم تحديث مشاريعي بدون مشاكل لسنوات إلى الإصدار الأحدث، بدون طلبات دمج مزعجة| https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0` | تحديد إصدار المشروع ...                                                                                                                                         | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`         | عرض ال plugins والتبعيات وعرض تراخيصها (قد يفشل حتى في حالة حظر الترخيص)                                                        | https://www.mojohaus.org/license-maven-plugin/index.html                 | 

ويمكن أن تستمر هذه القائمة إلى الأبد. يذكرني ذلك بخطوات سير العمل في GitHub.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

### هل لا تحب الـ XML؟

لا مشكلة! ما عليك سوى كتابة ملف البناء الخاص بك باستخدام `ruby`، `groovy`، `scala`، `yaml`، `atom` أو` Java`. تجعل إضافة اللغات المختلفة (https://github.com/takari/polyglot-maven) ذلك ممكنًا. لتجربته ، ما عليك سوى تشغيل `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` وخلال بضع مللي ثانية يتم ترجمة ملف البناء الخاص بك. للأسف ، لا يوجد مترجم موثوق به بين Maven و Gradle :( . نعم ، ملفات Maven Build كبيرة ، ولكنها سهلة الفهم للغاية. يتم التحكم بها وإصلاحها بسرعة.

### العمر مجرد رقم - استقرار Maven وتطوره

بإعترافنا، فإن Maven موجود لفترة طويلة وشكله الجمالي لا يتوافق ربما مع المعايير الحالية. ومع ذلك، فإن الثبات الذي يتمتع
به Maven قد سمح له بالتكيف والتطور. يعمل Maven بشكل مستقل عن مشروعك. يمكن إعادة استخدام ملفات البناء بسهولة. تعمل
المكوّنات الإضافية في مجال رملي وهي مستقلة عن بعضها البعض ومستقلة عن إصدارات Java أو Maven. يشجع هذا التصميم على
الاستقرار والتنبؤية ويجعل من السهل إدارة عمليات البناء المعقدة دون توقع صدامات غير متوقعة.

### نتيجة

حاليًا، تم تحميل بيئة التطوير بالعديد من المهام والتقنيات على المطورين. في البحث عن البساطة والتلقائية، ظهر Gradle كأحدث
أداة بناء، ولكنه أحضر تحديات خاصة به. من الواضح أن مفهوم Gradle جيد، ولكن في ظل التعقيد والوقت الذي يستثمر في بناء نصوص
Gradle، فإن السؤال الذي يطرح هو: هل ليس من الأسهل تعديل Maven بدلاً من ذلك؟ يمكن تحديث Maven في أي وقت باستخدام الإضافات
والملحقات لمزجها وتبسيطها. هل من الأفضل تطويرها بدلاً من القفز من تقنية إلى أخرى؟

### الروابط

* [العودة من Gradle إلى Maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### الاتصال

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
