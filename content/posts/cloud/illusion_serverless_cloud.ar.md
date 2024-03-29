---
title: "خادم الوهم بلا خادم و السحاب"
date: 2023-05-24
author: "Nova Annabella"
slug: illusion_serverless_cloud
tags: [ Development, Serverless, Cloud, Microservices, Scalability, Architecture, Infrastructure ]
categories: [ Technology, Software, Cloud ]
description: "تحديات وواقع الوظائف بدون خادم في السحابة. رؤى قيمة للشركات التي تنظر في الهجرة إلى السحابة"
draft: false
images:
  - "/images/content/onprem_vs_cloud.png"
card: "summary_large_image"
---


# الوهم من الوظائف الخالية من الخوادم في السحابة

![aws_costs_twitter_1](/images/content/onprem_vs_cloud.png)

### مقدمة

أنا خائب الأمل في كم المرات التي يتغلب فيها التسويق على العقل السليم. العديد من المديرين يتجاوزون خبرائهم الخاصين - المطورين. هذا ينطبق أيضًا على الترحيل إلى السحابة. تنبيه: من يحتاج إلى توفير المال ، يجب أن يتجنب السحابة. لأن الكلمة الجديدة المتداولة "خالي من الخادم" في السحابة تعني: أنت تهتم بالبرنامج ، ونحن نهتم بالأجهزة. ولكن من لديه مسؤول تكنولوجيا المعلومات ماهر، ومتحمس، وفضولي، يمكنه أيضًا تشغيل خدمة بدون خادم بنفسه (على سبيل المثال [KNative](https://knative.dev)).

![aws_costs_twitter_1](/images/content/aws_costs_twitter_1.png)


### الدوال بلا خادم مقابل المايكروسيرفس:



#### الميكروسيرفس


يهتم المايكروسيرفيس النمطي الخالي من الحالة بوظيفة / مجال معين ويتم نشره في بيئة تنسيق الحاويات. تهتم هذه البيئة بالبنية
التحتية ، والأمان ، وجدار الحماية ، التسجيل ، المقاييس ، الأسرار ، الشبكة ، النسخ الاحتياطي وأكثر من ذلك بكثير. ميزة
كبيرة هي أنه يمكن اختبار مايكروسيرفيس محليًا مع قليل من الموارد وأنه محايد للسحابة / الخادم (قابل للتطبيق في كل مكان).

#### وظائف بدون خادم

نكتة صغيرة أولاً: معادلة مثيرة للتعقيد ولكنها صحيحة - الدوال بلا خادم تعتمد بشدة على بيئة الخادم. :)
الدالة بلا خادم النموذجية تعتني بدورة/نطاق محدد أيضًا ويتم كتابتها بدون إطارات عمل
في 
كود نقي لكي تكون أسرع من الخدمة المصغرة (أيضًا تمرين جيد للخدمات المصغرة). ميزة كبيرة 
هي أن الدوال بلا خادم تتم مقياسها تلقائيًا. ومع ذلك، تحتاج كل دالة بلا خادم لكمية كبيرة من الكود اللاصق لتحديد البنية التحتية - الأمان، جدار الحماية، الشبكة، التسجيل، المقاييس،
الأسرار، التخزين المؤقت، النسخ الاحتياطي وأكثر بكثير.
لذلك، قد تشمل وظيفة بسيطة مثل نسخ ملف بما في ذلك API بسرعة حوالي 1500 خط من الكود (بما في ذلك IaC).
تحول تكاليف الإدارة من الإدارة إلى التطوير في نسبة 1: N (واحد إلى وظائف بلا خادم). العلم والتنفيذ ليسا متجمعان أكثر
ويمكن أن يصبحا غير مستقرين بسرعة. بالإضافة إلى ذلك، تزداد تكلفة الصيانة.
كما أن الاختبارات التكاملية الحقيقية نادرة مع خادم بدون خادم أو تتطلب جهد كبير.
في النهاية، تعقيد الدوال بلا خادم أعلى بكثير من تلك لخدمة مصغرة واحدة.
التعقيد الأعلى يعني أيضا صيانة أقل. الأعضاء الجدد في الفريق يجدون صعوبة ويحتاجون إلى
معرفة مسبقة أكثر.


### الخادم بدون خادم والسحابة بشكل عام

معظم تقنيات السحابة ليست حديثة. على سبيل المثال ، Node.js و Java و Python وغيرها من اللغات أو التقنيات غالبًا ما تكون غير سهلة التحديث ، وكثيرًا ما يكون التوقف هو فعلا الوحيد.  
حتى التقنيات الحديثة والقياسية مثل MongoDB و MySQL و Kafka و NATS و RabbitMQ و Redis و Prometheus و InfluxDB و Grafana ،
Kibana ، Elastic Search الخ ما زالت غير متوفرة أو مكلفة للغاية.
بدون هذه الخدمات القياسية ، غالبًا ما نجد أنفسنا في العصور الحجرية الافتراضية ونستخدم حلولًا قديمة ، مثل
الويب للتواصل خارجيًا. بالإضافة إلى ذلك ، يكون نطاق العمل محدودًا بشدة فيما يتعلق بالقضايا مثل التنظيم ،
الامتثال، الخصوصية وسلامة الخروج عن الخدمة.
يجب علينا لذا تشغيل السحابة بصورة محايدة ، للتمكن من التبديل بسرعة بين AWS ، وAzure ، وGoogle ، وOn-Premise ، وما إلى ذلك و
لمقارنة التكاليف.
الحدود موجودة أيضًا في السحابة وغالبا ما تؤدي إلى حلول بديلة إبداعية تزيد من التعقيد في المقابل.
حتى الاختبار التكاملي قد يكون غاليًا ، حيث يحتاج كل مطور لبيئة تطوير خاصة به في السحابة
، لأن العديد من خدمات السحابة ليست قابلة للتجربة محليًا أو لا يمكن اختبارها على الإطلاق.
ولكن السحابة مكلفة حتى بدون اختبارات. بينما تكون معظم التكاليف في الأنظمة المحلية
تتعلق بالأجهزة، يجب في السحابة دفع تكاليف إضافية للحركة ، وبعض الخدمات القياسية وغالبا حتى للضرائب
المتعددة. بالإضافة إلى أنه من السهل فقدان الرؤية العامة في السحابة ، لأن الهدف ليس راحة المستخدمون ، بل جمع الأموال. التكاليف مخفية بشكل تقريبا لا تلاحظ إلا عندما يصبح الأمر متأخرا جدا.

يجب إعادة اختراع أساسيات الهندسة المعمارية والبنية التحتية في السحابة وخصوصا في مجال الخدمات الخالية من الخوادم،
لأن التطبيق التنفيذي يعتمد بشكل كبير على الوظائف المتاحة.
كلما قمت بتصميم الهندسة المعمارية، يأتيني التفكير: "هذا كان يمكن أن يكون خدمة واحدة".
بالنسبة لي ، فإن الخدمات الخالية من الخوادم هي فكرة مثيرة للاهتمام وقابلة للتكيف جيدا ، ولكنها لا تقلل التكاليف. بل على العكس،
تتطلب المزيد من المعرفة والوقت في التطوير. الخدمات الخالية من الخوادم أو السحابة تتطلب الانضباط و
المعرفة المسبقة.
إذا كانت المعرفة بالأنظمة المحلية غير متوفرة ، فلن يصبح الأمر أسهل مع السحابة.
كيف يمكن للمطورين أن يكتسبوا معرفة إضافية بالبنية التحتية؟

أفضل أن يكون لدينا تجمع كوبرنتيس مدار بشكل جيد بدلا من هندسة سحابة.
الموظفين لا يتكيفون. الكثير من المطورين ليس لديهم انضباط في كتابة الرمز.
للأسف ، ينطبق هذا على 80 ٪ من المطورين. كيف يمكن إذا لهؤلاء المطورين تشغيل السحابة
؟

من المهم أن تفهم الشركات التحديات والتأثيرات الشاملة للهندسة المعمارية الخالية من الخوادم والسحابة.
هذا يتطلب ليس فقط المعرفة الفنية ، ولكن أيضا نهج استراتيجي. الهجرة العشوائية إلى السحابة يمكن أن تؤدي إلى تعقيدات ،
وتكاليف أعلى وتجاوز مهارات المطورين.

للخلاصة ، يمكن القول أن الخدمات الخالية من الخوادم في السحابة هي مفهوم واعد ، ولكن يجب أن ينظر إليه بعناية
. التكلفة ، والتعقيد, والقابلية للصيانة, وقدرات فريق التطوير يجب أن يأخذ بعين الاعتبار.
لكل شركة تكون لها احتياجات وأولويات مختلفة. يجب أن نتخذ قرار مستنير ، سواء
كانت الخدمات الخالية من الخوادم في السحابة هي الحل الصحيح أو إذا كانت النهج البديلة مثل
جيدة تجمع Kubernetes هي الخيار الأفضل.

الاستخدام الناجح للخدمات الخالية من الخوادم والحوسبة السحابية يتطلب توليفة من الخبرة الفنية
التخطيط الاستراتيجي وفهم واضح لمتطلبات الأعمال. فقط بهذه الطريقة يمكن رؤية الوهم من الخدمات الخالية من الخوادم
واتخاذ القرار الصحيح للتطوير البرمجي الخاص بك.


### خلاصة

إن إدخال الوظائف الخالية من الخادم في السحابة يعد بالمرونة، والقابلية للتطوير، وتخفيف الأعباء عن المطورين من أعباء
البنية التحتية. ولكن، يجب أن لا نتأثر بالأوهام. تحويل إلى السحابة واستخدام الوظائف الخالية من الخادم ينطوي على العديد من
التحديات. يجب على المطورين أن يتعلموا لغة جديدة بالإضافة إلى التطوير الفعلي وأن يتحملوا المزيد من المسؤولية دون الدعم
المناسب. تعقيد الوظائف الخالية من الخادم غالباً ما يكون أكبر من الخدمات المصغرة، حيث يجب على المطورين أن يتولوا العديد
من المهام الإضافية مثل تعريف البنية التحتية، والأمان، والقابلية للتطوير. الاختبارات التكاملية الحقيقية صعبة والمعرفة
المسبقة والخبرة للتشغيل أكثر أهمية في السحابة. السحابة نفسها تنطوي على المزيد من التحديات. العديد من تقنيات السحابة
ليست حديثة واستخدام الخدمات القياسية الحديثة قد يكون مكلفًا أو مستحيلًا. الأنظمة التنظيمية والامتثال و حماية البيانات
تقيد الحرية. بالإضافة إلى ذلك، التكاليف في السحابة يمكن أن تزداد بسهولة، والرؤية العامة للنفقات يمكن أن تضيع بسرعة.
بصفة عامة، يجب أن يتم تقييم مزايا وعيوب السحابة والوظائف الخالية من الخادم بعناية. يجب على الشركات أن تأخذ بعين الاعتبار
متطلباتها الخاصة، والمعرفة الموجودة في الفريق والأثر طويل الأجل للتحويل إلى السحابة. إتخاذ قرار مستند إلى تحليل شامل أمر
حاسم لنجاح المشروع وربحيته. في النهاية، يعود الأمر إلى الشركات لدعم مطوريها بشكل مناسب، وتقدير تكلفة وتعقيد السحابة
بشكل واقعي والنظر في حلول أخرى مثل مجموعات Kubernetes المدارة بشكل جيد. مع استراتيجية واضحة وفهم مستند للحاجات الخاصة،
يمكن للشركات الاستفادة القصوى من مزايا السحابة والوظائف الخالية من الخادم، ورؤية الأوهام بوضوح.

### الاتصال

[مسائل GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
