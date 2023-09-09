---
title: "Maven'a Geri Dön?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "Zorlukla anlaşılan basitlik arayışı ve Maven'ın gücünü yeniden keşfetme üzerine kısa bir seyahat."
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# Maven'a Geri Dönüş?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

## Gradle'in 10. Yılı. Kolaylık Arayışı ve Maven'in Gücünün Kısa Bir Yeniden Keşfi.



### Geliştiricilerin Potansiyelini Maksimize Etme - Daha Fazla Zaman Tasarrufu Sağlayan Araçlara İhtiyacımız Var

Sıklıkla göz ardı edilen veya nadiren tartışılan konular beni ilgilendirir. Genellikle harika teknolojiler kullanılıyor,
ancak neredeyse hiç kimse bununla bağlantılı sorunlardan bahsetmiyor. Geliştirme günümüzde oldukça zahmetli hale geldi.
“Serverless”, “Low Code”, “IaC”, “Big Data”, “Cloud”, “DevOps”, “You Build it You run it” vb. gibi havalı moda laflarla
geliştiricilerin zaten aşılmaları gereken bir sürü ek görevleri vardır. Daha fazla görev, bunun neredeyse hiç uzman
kalmadığı ve her zaman odaklanmak için bir şeylerin ihmal edileceği anlamına gelir. Bu yüzden otomasyonlar ve zaman
tasarrufu mega önemlidir. “Don’t make me think” ve “Works out of the box” kalite belirtisi olarak iyi kelimelerdir,
ancak ben bunları Gradle'da henüz göremiyorum. Adil olmak gerekirse, Gradle bize iş yükü olan tek modern araç değil,
tersine işleri kolaylaştırır.

### İllüzyonun Basitlik ve Otomasyon Arayışı

SOAP'tan beri XML tabanlı yapılandırmalara karşı derinlemesine bir hoşnutsuzluğum var. Gradle ile Bind scriptlerinin
yazılmasının çocuk oyuncağı olacağını ummuştum, ne yazık ki umutlarım ve motivasyonum zamanla azaldı. Gradle, esnekliği
hedefler ve bunun için otomasyonu ve kaliteyi feda eder. Geliştiriciler, trendi takip ederken yazılımın güvenilirliği
üzerindeki etkileri göz ardı ederler. Gradle Build scriptlerini basit ve bakımı kolay tutmak için güçlü bir disipline
ihtiyaç vardır. Böyle bir disiplin hali hazırda kaynak kodunda nadiren bulunur ve bu yüzden build scriptlerinde çok daha
az bulunur.

### Çeviriler ve Geçici Çözümler - Yapı Skriptleri Bir Meydan Okumaya Dönüştüğünde

Gradle, arka planda Maven'dan çok farklı çalışmaz. Bu yüzden bazı çevirilere ihtiyaç vardır. Dependency Catalog, Maven
Release Plugin, Dependabot ve daha fazlası aslında Maven’in zaten sunduğu temel özellikler için geçici çözümlerdir.
Gradle'nin esnekliği ile sık sık karmaşık build yapılandırmaları oluşur, ki bunlar bakımı zor olabilir. Gradle
eklentileri sık sık uyumluluk sorunları, limitler veya sınırlı gelişimle karşılaşır. Bu sorunlar, Gradle ekosisteminin
gelişen doğası, Gradle'ın kullanıldığı çeşitli ortamlar ve her eklenti için spesifik uygulama ve bakım çabası nedeniyle
oluşur. Her şey birbiriyle bağlantılıdır.

### Gradle'nin Domino Etkisi - Gerçek Dünyada Bir Kabus Senaryosu

Birçok Mikroservis gördüm ki bunların yalnızca birkaç yıl ömrü olmuş ve zaten Gradle nedeniyle bakımları yapılamaz hale gelmişler.
Belirtmek önemlidir ki, bu benim gördüğüm ilk örnek değil ve hayır, bunların hiçbiri çaylak geliştiriciler değildi.

Benim **görevim, bir Spring Boot 2.x'ten 2.7'ye yükseltme işlemi gerçekleştirmekti**. Spoiler: Bir yılın sonunda
vazgeçtim! İşte kısaca yaşanan sorunlar:

* Gradle-Build dosyası gerektiriyor -> Yerel Java sürümümü 11'e düşürmem gerekti (Vay canına) (Genellikle Java
ters uyumludur - burada da alternatif çözümler var, örneğin SdkMan gibi araçlar...)
* Spring Boot güncellemesi gerektiriyor -> Gradle güncellemesi (Vay canına)
* Gradle güncellemesi gerektiriyor -> Eklenti güncellemesi
* Eklenti güncellemesi gerektiriyor -> Groovy güncellemesi (Vay canına)
* Groovy güncellemesi gerektiriyor -> Test çatısı ve test güncellemeleri (Vay canına)
* Test çatısı güncellemesi gerektiriyor -> Bağımlılık güncellemeleri
* \[...]
  Ayrıca bazı eklentiler, yeni Gradle sürümleriyle çalışmaz, bazıları geliştirilmez, diğer eklentilerle uyumsuzdur, sadece Gradle KTS ile çalışır, Gradle Groovy ile değil,
  veya basitçe limitleri vardır. Büyük sağlayıcılar tarafından bile, Spring gibi, Maven eklentilerine kıyasla sınırlı işlevselliğe sahip eklentiler kullanılmış. Sonunda tam anlaşılamayan bir Gradle-Build-Datei elde ettim,
  hatta onu yazan geliştiriciler bile bunu tam anlamıyla bakımını sağlayamıyor ve hala Gradle'i seviyorlar. Gradle betiklerini gerçekten anlayabilecek veya yazabilecek sadece birkaç kişi tanıyorum.

### Maven'ın Gücünün Yeniden Keşfi - Maven'ın Sihirli Güçlerini Kullanma

İşte Maven'daki en sevdiğim özellikler:
Eklentiler, daha önce tanımlanmaları gerekmeden doğrudan komut satırından başlatılabilir ve yapılandırılabilir. Artı, diğer eklenti yapılandırmalarından büyük ölçüde bağımsızdırlar.

| Örnek Komut                        | Açıklama                                                                                                                                                                    | Bağlantı                                    | 
|-----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|--------------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`     | Sürümleri güncelle - kim Dependabot'a ihtiyaç duyar? Evet, projelerim yıllardır sorunsuz bir şekilde en yeni sürüme güncellendi, rahatsız edici birleştirme istekleri olmadan | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html|
| `mvn versions:set -DnewVersion=1.0.0` | Proje sürümünü ayarla...                                                                                                                                                  | https://www.mojohaus.org/versions/versions-maven-plugin/index.html |
| `mvn license:add-third-party`           | Bağımlılıkları listele ve lisanslarını göster (hatta hariç tutulan lisanslarda bile başarısız olabilir)                                                                    | https://www.mojohaus.org/license-maven-plugin/index.html        | 

Bu liste sonsuza kadar devam edebilir. Bana bir şekilde GitHub İş Akışı Adımlarını hatırlatıyor.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)


### XML Sevmez misin?

Hiç sorun değil! Yapılandırma dosyanızı sadece `ruby`, `groovy`, `scala`, `yaml`, `atom` veya `Java` olarak yazın. Polygot
Eklentisi (https://github.com/takari/polyglot-maven) bunu mümkün kılar. Denemek için
sadece `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` komutunu çalıştırın ve sadece
birkaç milisaniyede yapılandırma dosyanız çevrilmiş olur. Keşke güvenilir bir Maven <> Gradle çevirmeni
olsaydı :(
Evet, Maven Yapılandırma Dosyaları büyük, ancak anlaşılması çok kolay. Düzeltmeler veya hata ayıklama hızlı bir şekilde
yapılır.

### Yaş sadece bir sayıdır - Mavens'in Stabilitesi ve Evrimi

Elbette, Maven'ın üzerinden epey zaman geçti ve estetiği belki bugünkü standartlara uymuyor. Ancak Maven'ın uzun ömrü,
onun adapte olmasını ve gelişmeye devam etmesini sağladı. Maven, projenizden bağımsız olarak çalışır. Build dosyaları
kolaylıkla yeniden kullanılabilir. Eklentiler, bir kum havuzunda çalışır ve birbirlerinden ve Java veya Maven sürümünden
bağımsızdırlar. Bu tasarım, stabiliteyi ve tahmin edilebilirliği teşvik eder ve karmaşık build süreçlerini beklenmedik
çatışmalar olmadan yönetmeyi kolaylaştırır.

### Sonuç

Günümüzde, geliştirme ortamı, geliştiriciler için birçok görev ve teknoloji ile dolup taşıyor. Basitlik ve otomasyon
arayışında, Gradle modern bir yapı aracı olarak ortaya çıktı, ancak kendi zorluklarını da beraberinde getirdi. Şüphe yok
ki, Gradle'nin konsepti iyi! Ancak, Gradle Yapı betiklerine yapılan yatırım ve karmaşıklık göz önüne alındığında,
Maven'i genişletmek daha basit olmaz mıydı? Eklentiler ve uzantılarla, Maven her zaman yenilenebilir ve
basitleştirilebilir. Bir teknolojiden diğerine atlamak yerine, daha da geliştirme daha heyecan verici ve sürdürülebilir
olmaz mıydı?

### Bağlantılar

* [Gradle'den Maven'a Geri Dönüş](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### İletişim

[GitHub Sorunları](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
