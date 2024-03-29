---
title: "بازگشت به Maven؟"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "جستجوی سخت‌گیرانه برای سادگی و سفر کوتاهی برای بازکشف قدرت میون."
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# بازگشت به Maven؟

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

## 10 سال با Gradle. در جستجوی تسهیل و یک سفر کوتاه برای بازکشف قدرت Maven.



### بیشینه سازی پتانسیل توسعه دهندگان - ما به ابزارهایی که زمان را صرفه جویی می کنند بیشتر نیاز داریم

موضوعاتی که اغلب نادیده گرفته می‌شوند یا کمتر مورد بحث قرار می‌گیرند، برای من جذاب هستند. اغلب، فناوری‌های حرفه‌ای در
حال استفاده هستند، اما تعداد کمی در مورد مشکلات مرتبط با آنها صحبت می‌کنند. توسعه در این روزها بسیار زمان بر شده است. با
کلمات حرفه ای مثل "بدون سرور"، "کدپذیری کم"، "IaC"، "داده بزرگ"، "ابر"، "DevOps"، "ساختن آن شما را در دواندن آن" و غیره،
توسعه دهندگان قطعا کار اضافی برای انجام دادن دارند. کارهای بیشتر، یعنی کمتر کسی به عنوان متخصص وجود دارد و همیشه چیزی
برای تمرکز نادیده گرفته می‌شود. بنابراین اتوماسیون‌ها و صرفه‌جویی در زمان بسیار مهم هستند. "فکر نکن" و "کارها از جعبه
خارج می‌شود" نشانه‌های خوبی از کیفیت هستند که من هنوز نمی‌توانم در Gradle ببینم. برای انصاف، Gradle تنها ابزار مدرن نیست
که کار ما را سخت‌تر، بجای آسان‌تر می‌کند.

### جستجوی سرابی برای سادگی و اتوماسیون

از زمان SOAP، من از پیکربندی‌های مبتنی بر XML یک بیزاری عمیق دارم. با Gradle امیدوار بودم که نوشتن اسکریپت‌های Bind خیلی
آسان خواهد بود. متأسفانه، امیدها و انگیزه من بار به بار کمتر شد. Gradle به دنبال انعطاف‌پذیری است و به عنوان قربانی
اتوماسیون و کیفیت را به کنار می‌اندازد. برنامه‌نویسان بدون توجه به تأثیرات بر روی قابلیت اتکاپذیری نرم‌افزار، به طور
کورکورانه این روند را دنبال می‌کنند. برای نگهداری ساده و کم هزینه اسکریپت‌های ساخت Gradle نیاز به انگیزه‌ای قوی است.
چنین انگیزه‌ای کمتر در کد منبع یافت می‌شود و بنابراین در اسکریپت‌های ساخت بسیار نادرتر است.

### ترجمه ها و راه حل ها - وقتی اسکریپت های ساخت به یک چالش تبدیل می شوند

Gradle در پس زمینه به شکل زیادی متفاوت با Maven کار نمی کند. بنابراین ، برخی ترجمه ها ضروری هستند. ویژگی ها مانند
کاتالوگ وابستگی، پلاگین انتشار Maven، Dependabot و بسیاری دیگر در واقع راه حل های موقت برای ویژگی های اساسی هستند که
Maven در حال حاضر با خود می اورد. با انعطاف پذیری Gradle ، اغلب پیکربندی های ساخت پیچیده ای ایجاد می شود، که دشوار است
برای نگهداری کردن قدرت داشته باشید. پلاگین های Gradle اغلب با مشکلات سازگاری، محدودیت ها یا توسعات محدود روبرو هستند.
این مشکلات به دلیل طبیعت در حال توسعه اکوسیستم Gradle، تنوع محیط هایی که Gradle در آنها استفاده می شود و هزینه های خاص
اجرا و نگهداری برای هر پلاگین اتفاق می افتد. همه چیز به هم مرتبط است.

### اثر دمینوی Gradle - سناریوی کابوس در دنیای واقعی

من Microservices های زیادی را دیده ام که فقط چند ساله هستند و قادر به نگهداری بیشتر به دلیل Gradle نیستند. مهم است اشاره کنم که این اولین باری نیست که چنین چیزی را می بینم، و نه، اینها توسعه دهندگان Junior نبودند.

وظیفه من این بود که **یک ارتقاء از Spring Boot 2.x به 2.7 را انجام دهم**. Spoiler: من پس از یک سال
تسلیم شدم! مشکلات به طور خلاصه:

* نیاز به فایل ساخت Gradle -> Downgrade نسخه Java محلی من به 11 (WTF) (معمولا Java
  سازگار با نسخه های قبلی است - اینجا هم دوباره ابزارهای Workaround مانند SdkMan وجود دارد...)
* نیاز به به روزرسانی Spring Boot -> به روزرسانی Gradle (WTF)
* نیاز به به روزرسانی Gradle -> به روزرسانی فرمت افزونه
* نیاز به به روزرسانی افزونه -> به روزرسانی Groovy (WTF)
* نیاز به به روزرسانی Groovy -> به روزرسانی فریمورک تست و تست ها (WTF)
* نیاز به به روزرسانی فریمورک تست -> به روزرسانی وابستگی ها
* \[...]
  علاوه بر این، برخی از افزونه ها با نسخه های جدیدتر Gradle کار نمی کنند، برخی دیگر توسعه یافته اند، با سایر افزونه ها ناسازگار هستند، فقط با Gradle KTS کار می کنند، نه با Gradle Groovy، یا
  سقف های ساده دارند. حتی افزونه هایی از سازندگان بزرگ مانند Spring نسبت به افزونه های Maven خود
  قابلیت های محدودی دارند. در پایان، من یک فایل ساخت Gradle کوتاه و خنده دار داشتم که هیچ کس به درستی نمی تواند آن را نگه دارد،
  حتی توسعه دهندگانی که آن را نوشته اند، و هنوز هم Gradle را دوست دارند. من فقط چند نفر را می شناسم که
  Gradle Script را جدی بردارند و بتوانند بنویسند.


### بازکشف قدرت میون - استفاده از جادوی میون

اینجا قابلیت های مورد علاقه من از ماون هستند:
پلاگین ها می توانند بلافاصله از خط فرمان راه اندازی و پیکربندی شوند ، بدون آنکه نیاز به تعریف اولیه داشته باشند
می بایست. علاوه بر این، آنها بیشتر مستقل از سایر پیکربندی های پلاگین هستند.

| دستور مثال                          | توضیحات                                                                                                                                                    | لینک                                                                  |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| `mvn versions:use -latest-versions` | به روزرسانی نسخه - کی به Dependabot نیاز دارد؟ بله، پروژه های من برای سال ها بدون درخواست ادغام آزاردهنده بر روی آخرین نسخه به روز شده اند | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0` | تعیین نسخه پروژه...                                                                                                                                           | https://www.mojohaus.org/versions/versions-maven-plugin/index.html |
| `mvn license:add-third-party`    | فهرست وابستگی ها و نمایش مجوزهای آنها (حتی می تواند در مورد مجوزهای محروم شکست بخورد)                                                                    | https://www.mojohaus.org/license-maven-plugin/index.html       |

این لیست می تواند به همین ترتیب ادامه یابد. به نوعی یادآور مراحل گردش کار GitHub است.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

### تو XML را دوست نداری؟

هیچ مشکلی نیست! فقط فایل ساخت خود را در `ruby`، `groovy`، `scala`، `yaml`، `atom` یا `Java` بنویسید. برنامه افزودنی Polygot
(https://github.com/takari/polyglot-maven) این امکان را فراهم می‌کند. برای تست کردن
فقط `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` اجرا کنید و در
چند میلی ثانیه، فایل ساخت شما ترجمه می‌شود. متأسفم که هیچ مترجم قابل اعتماد Maven <> Gradle وجود ندارد :(.
بله، فایل‌های ساخت Maven بزرگ هستند، اما بسیار آسان فهم هستند. بهبودی ها یا عیب یابی در چرخیدن دست
انجام می‌شوند.

### سن فقط یک عدد است - پایداری و تکامل ماون

باید اعتراف کنم، میون (Maven) مدت زیادی وجود دارد و زیبایی آن شاید با استانداردهاى روز نسبت داده نشود. با این حال، طول
عمر میون امکان اقتدال و توسعه مجدد را فراهم کرده است. میون بطور مستقل از پروژه شما کار می کند. فایل های ساخت می توانند
به راحتی دوباره استفاده شوند. پلاگین ها در یک Sandbox اجرا می شوند و به صورت مستقل از یکدیگر و بصورت مستقل از نسخه Java
یا Maven هستند. این طراحی استقرار و قابلیت پیش بینی را تشویق می کند و آن را ساده می کند تا فرآیندهای ساخت پیچیده را بدون
درگیر شدن در تضادات غیر منتظره مدیریت کند.

### نتیجه‌گیری

امروزه محیط توسعه با بسیاری از وظایف و فناوری‌ها برای توسعه‌دهندگان از آن پر شده است. در جست‌وجوی سادگی و اتوماسیون،
Gradle به عنوان ابزار ساخت مدرن به حضور رسیده است اما مشکلات خود را با خود آورده است. بدون شک، کاربرد Gradle خوب است!
اما در برابر پیچیدگی و زمانی که در ساخت اسکریپت‌های Gradle سرمایه‌گذاری می‌شود، سوال پیش می‌آید که آیا گسترش دادن Maven
ساده‌تر نبوده است. با پلاگین‌ها و افزونه‌ها، می‌توان هر زمان Maven را بازسازی و ساده کرد. آیا گسترش نسبت به پرش از یک
فناوری به فناوری دیگر، جذاب‌تر و پایدارتر نبوده است؟

### لینک ها

* [برگشت از Gradle به maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### تماس

[مسائل گیتهاب](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
