---
title: "```Maven'e geri dönüş?```"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "# Markdown Metni```Basitliği Arama ve Maven'in Gücünü Yeniden Keşfetmek İçin Kısa Bir Yolculuk```"
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# Maven'e Geri Dönüş?

```
[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)


``` 
Bu metin Markdown olarak verilmiştir ve çevirisinde herhangi bir format veya içerik değişikliği yapılmamaktadır.

## 10 Yıl Gradle. Kolaylaştırma arayışında ve Maven'in gücünün yeniden keşfi için kısa bir yolculuk.

``` ```

### Geliştiricilerin potansiyelinin maksimuma çıkarılması - Daha fazla zaman tasarrufu sağlayan araçlara ihtiyacımız var

Beni ilgilendiren, genellikle göz ardı edilen veya nadiren tartışılan konular var. Sık sık harika teknolojiler
kullanılır, ancak çoğu kişi bununla ilişkili sorunlar hakkında konuşmaz. Geliştirme günümüzde çok zahmetli hale geldi.
"Serverless", "Low Code", "IaC", "Big Data", "Cloud", "DevOps", "You Build it You run it" vb. gibi harika moda
kelimeleri, geliştiricilerin zaten üstesinden gelmeleri gereken yeterince ek görevleri var. Daha fazla görev, neredeyse
hiç uzman olmaması anlamına gelir ve odaklanmanın her zaman ihmal edilen bir şeyi vardır. Bu nedenle, otomasyonlar ve
zaman tasarrufu çok önemlidir. "Düşünmemi sağlama" ve "Hemen kullanılabilir" gibi kalite özellikleri, Gradle'da
göremediğim iyi özelliklerdir. Adaletli olmak gerekirse, Gradle işleri kolaylaştırmak yerine zorlaştırmayacak tek modern
araç değil.

### Basitlik ve Otomasyon Arayışındaki İllüzyonik Arama

SOAP'tan beri XML tabanlı yapılandırmalara karşı kökten bir antipati geliştirdim. Gradle ile bağlama betikleri yazmanın
kolay olacağını ummuştum. Ne yazık ki, umutlarım ve motivasyonum her seferinde azaldı. Gradle esneklik peşinde koşar ve
bunun için otomasyondan ve kaliteden ödün verir. Geliştiriciler, yazılımın güvenilirliği üzerindeki etkilerine bakmadan
trendi kör bir şekilde takip ederler. Gradle yapılandırma betiklerini basit ve bakımı kolay tutmak için güçlü bir
disiplin gereklidir. Bu disiplin kaynak kodunda bile nadirdir ve yapılandırma betiklerinde daha da nadirdir.```

### Çeviriler ve Çözümler - Derleme Komut Dosyaları Zor Hale Geldiğinde

Gradle, Maven'dan çok farklı olmayarak arka planda çalışır. Bu nedenle bazı çeviriler gereklidir. Bağımlılık Kataloğu,
Maven Yayın Eklentisi, Dependabot ve daha birçok özellik aslında Maven'in zaten getirdiği temel işlevler için birer
çalışma takımıdır. Gradle'in esnekliğiyle birlikte genellikle bakımı zor olan karmaşık bir yapılandırmalar ortaya
çıkabilir. Gradle eklentileri sıklıkla uyumluluk sorunları, sınırlamalar veya sınırlı gelişimlerle karşılaşır. Bu
sorunlar, Gradle ekosisteminin gelişen doğası, Gradle'nin kullanıldığı çeşitli ortamların çeşitliliği ve her eklentinin
özel uygulama ve bakım çabası nedeniyle ortaya çıkar. Her şey birbiriyle bağlantılıdır.

### Gradle'nin Domino Etkisi - Gerçek Dünyadaki Kâbus Senaryosu

Çok sayıda Gradle nedeniyle bakımsız hale gelen sadece birkaç yıllık Microservisler gördüm. Bu tür bir şeyi gördüğüm ilk defa değil ve hayır, bu Junior Dev'ler değildi.

**Görevim, Spring Boot 2.x to 2.7 Upgrade'ini gerçekleştirmekti**. Sürpriz: Bir yıl sonra vazgeçtim! Sorunlar kısaca:

* Gradle Build dosyası -> yerel Java sürümümü 11'e indirgeme gerektirir (WTF) (Normalde Java geriye doğru uyumlu olduğundan burada da SdkMan gibi çalışma araçları var ...)
* Spring Boot Güncellemesi -> Gradle güncellemesi gerektirir (WTF)
* Gradle Güncellemesi -> Eklenti Güncellemesi gerektirir
* Eklenti Güncellemesi -> Groovy Güncellemesi gerektirir (WTF)
* Groovy Güncellemesi -> Test Framework ve Test Güncellemeleri gerektirir (WTF)
* Test Framework Güncellemesi -> Bağımlılık Güncellemeleri gerektirir
* \[...\]
  Ayrıca, bazı eklentiler daha yeni Gradle sürümleriyle çalışmaz, bazıları daha fazla geliştirilmez, diğer eklentilerle uyumsuzdur, Gradle KTS ile çalışırken Gradle Groovy ile çalışmaz veya sadece sınırlamalara sahiptir. Büyük sağlayıcılar tarafından daha önce yazılmış Maven eklentilerine kıyasla sınırlı işlevselliğe sahiptirler. Sonunda, yazan geliştiriciler bile doğru şekilde bakamayan harika bir kısa Gradle Build dosyam var ve hala Gradle'ı seviyorlar. Gradle betiklerini gerçekten anlayabilen veya yazabilen az sayıda insan tanıyorum.

### Maven'in Gücünün Yeniden Keşfi - Maven'in Büyü Güçlerini Kullanma

İşte Maven'in sevdiğim özellikleri:
Eklentiler, bunları önceden tanımlamanıza gerek olmadan doğrudan komut satırından başlatılıp yapılandırılabilirler. Ayrıca, diğer eklenti yapılandırmalarından büyük ölçüde bağımsızdırlar.

| Örnek Komut                             | Açıklama                                                                                                                                        | Link                                                                     |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`     | Sürümleri güncelle - Dependabot'a kim ihtiyaç duyar? Evet, projelerim yıllardır en son sürüme sorunsuz bir şekilde güncellendi, herhangi bir birleştirme isteği olmadan | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0`   | Proje sürümünü ayarla...                                                                                                                       | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`           | Bağımlılıkları listele ve lisanslarını göster (hatta hariç tutulan lisanslarda bile başarısız olabilir)                                          | https://www.mojohaus.org/license-maven-plugin/index.html                 | 

Bu liste sonsuz gibi devam edebilir. Bu beni bir şekilde GitHub İş Akış Adımlarını hatırlatıyor.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

### XML'den hoşlanmıyor musun?

Sorun değil! Sadece `ruby`, `groovy`, `scala`, `yaml`, `atom` veya `Java` formatında olan Build Dosyanı yaz. Polygot 
Extension (https://github.com/takari/polyglot-maven) sayesinde mümkündür. Denemek için 
sadece `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml`
çalıştırın ve birkaç milisaniye içinde Build Dosyanız çevrilir. Maalesef güvenilir bir Maven <> Gradle çevirmen yok :(
Evet, Maven Build Dosyaları büyük ama çok anlaşılır. İyileştirmeler veya Hata Ayıklama anında hemen yapılabilir.

### Yaş sadece bir sayıdır - Maven'in Kararlılığı ve Evrimi

Kabul edelim ki, Maven uzun bir süredir var ve estetiği belki de bugünkü standartlara uymuyor. Ancak, Maven'ın
dayanıklılığı, uyum sağlamasına ve gelişmesine izin vermiştir. Maven projenizden bağımsız çalışır. Yapı dosyaları
kolayca yeniden kullanılabilir. Eklentiler bir kum havuzunda çalışır ve birbirinden bağımsızdır ve Java veya Maven
sürümünden bağımsızdır. Bu tasarım, istikrar ve öngörülebilirlik sağlar ve beklenmedik çatışmalar olmadan karmaşık yapı
süreçlerini yönetmeyi kolaylaştırır.

### Sonuç

Şu anda, Geliştiriciler için çeşitli görevler ve teknolojilerle yüklü bir geliştirme ortamı var. Basitlik ve otomatikleştirme arayışında, modern bir yapı aracı olarak ortaya çıkan Gradle, ancak kendi zorluklarını getirdi. Hiç şüphe yok ki, Gradle kavramı iyi! Ancak, Gradle yapı betiklerine yatırılan karmaşıklık ve zaman göz önüne alındığında, Maven'i genişletmenin daha kolay olup olmayacağı sorusu ortaya çıkıyor. Plug-in ve uzantılarla, Maven her zaman taze ve basitleştirilmiş olabilir. Teknolojiden teknolojiye atlamaktansa geliştirilmesi daha heyecan verici ve sürdürülebilir olmaz mıydı?

### Bağlantılar

```
* [Gradle'dan maven'e Geri Dönüş](https://phauer.com/2018/moving-back-from-gradle-to-maven/)
```

### İletişim

[GitHub Sorunları](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
