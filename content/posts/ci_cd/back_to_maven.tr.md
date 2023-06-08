---
title: "```
Maven'e geri dönülecek mi?
```"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "```
Efsaneye dönüşen basitlik arayışı ve Maven'in gücünün keşfi için kısa bir yolculuk
```"
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# Maven'e Geri Mi Dönüyoruz?

```
[![maven_vs_gradle](/resimler/icerik/maven_vs_gradle.png)](https://phauer.com/2018/gradle-den-maven-e-geri-donmek/)
```

## 10 Yıl Gradle. Kolaylaştırma arayışında ve Maven'in gücünün yeniden keşfi için kısa bir yolculuk.

Markdown metnini Türkçeye çevirin:  ```

### Geliştiricilerin Potansiyelinin Maksimize Edilmesi - Daha Fazla Zamandan Tasarruf Etmek İçin Daha Fazla Araç Gerekiyor

Sıklıkla gözden kaçırılan veya nadiren tartışılan konular beni ilgilendirir. Sık sık harika teknolojiler kullanılır,
ancak bununla ilgili sorunlar hemen hemen hiçbir zaman konuşulmaz. Geliştirme günümüzde çok zahmetli hale geldi.
"Sunucusuz", "Düşük Kod", "IaC", "Büyük Veri", "Bulut", "DevOps", "Sen yaparsın Sen çalıştırırsın" gibi harika
kelimelerle geliştiricilerin üzerine yüklenen tamamen yeterli ek görevleri var. Daha fazla görev, uzmanların neredeyse
hiç olmaması anlamına gelir ve her zaman bir şeye odaklanmak zorunda kalındığından bir şeyler ihmal edilir. Bu nedenle
otomasyonlar ve zaman tasarrufları son derece önemlidir. "Beni düşündürme" ve "Kutudan çalışır" iyi kalite
özellikleridir, fakat Gradle'da bunları göremiyorum. Adil olmak gerekirse, Gradle sadece işimizi zorlaştıran modern
araçlardan biri, başka araçlar da var.

### İllüzyonik Basitlik ve Otomatizasyon Arayışı

SOAP'tan beri, XML tabanlı yapılandırmalara karşı köklü bir direnç duygusu taşıyorum. Gradle ile bağlama betikleri yazmanın kolay olacağını umdum. Ne yazık ki, umutlarım ve motivasyonum zamanla azaldı. Gradle esneklik peşinde koşar ve bunun için otomasyonu ve kaliteyi feda eder. Geliştiriciler, yazılımın güvenilirliği üzerindeki etkilere aldırmadan modaya bandwagon'a binerler. Gradle build betiklerini kolay ve bakımlı tutmak için güçlü bir disiplin gerekmektedir. Böyle bir disiplin, kaynak kodunda bile nadiren bulunur, bu nedenle Build-Betiklerinde daha da nadirdir.

### Çeviriler ve Çözümler - Yapı betikleri bir zorluk haline geldiğinde

Gradle, Maven'dan çok farklı bir arka plan üzerinde çalışmaz. Bu nedenle, bazı çevirilere ihtiyaç duyulmaktadır.
Bağımlılık Kataloğu, Maven Release Eklentisi, Dependabot ve daha birçok özellik, temel işlevlerin çalıştırılmasını
sağlamak için zaten Maven'da yer alan bir takım işlemlere dayanmaktadır. Gradle'in esnekliğiyle, genellikle bakımı zor
olan karmaşık derleme konfigürasyonları oluşturulabilir. Gradle eklentileri sıklıkla uyumluluk sorunları, sınırlamalar
veya sınırlı ilerlemelerle karşılaşır. Bu sorunlar, Gradle ekosistemindeki gelişen doğası, Gradle'in kullanıldığı
ortamların çeşitliliği ve her eklentinin özel uygulama ve bakım gereksinimlerinden kaynaklanmaktadır. Her şey birbirine
bağlıdır.

### Gradle'nin Domino Etkisi - Gerçek Dünyada Bir Kabus Senaryosu

Ich habe viele Mikro-Services gesehen, die nur wenige Jahre alt waren und aufgrund von Gradle nicht mehr gewartet werden konnten. Es ist wichtig zu erwähnen, dass dies nicht das erste Mal ist, dass ich so etwas gesehen habe und nein, es waren keine Junior Devs.

Meine Aufgabe war es, ein Upgrade von Spring Boot 2.x auf 2.7 durchzuführen. Spoiler: Ich habe nach einem Jahr aufgegeben! Die Probleme im Überblick:

* Die Gradle-Build-Datei erfordert -> Downgrade meiner lokalen Java-Version auf 11 (WTF) (Normalerweise ist Java abwärts-kompatibel - es gibt auch hier wieder Workaround-Tools wie SdkMan...)
* Das Spring Boot-Update erfordert -> Gradle-Update (WTF)
* Das Gradle-Update erfordert -> Plugin-Update
* Das Plugin-Update erfordert -> Groovy-Update (WTF)
* Das Groovy-Update erfordert -> Test-Framework und Test-Updates (WTF)
* Das Test-Framework-Update erfordert -> Abhängigkeitsupdates
* [...]
  Darüber hinaus funktionieren einige Plugins nicht mit neueren Gradle-Versionen, einige werden nicht mehr weiterentwickelt, sind inkompatibel mit anderen Plugins, funktionieren nur mit Gradle KTS, nicht mit Gradle Groovy, oder haben einfach Limits. Selbst Plugins von großen Anbietern wie Spring haben im Vergleich zu ihren Maven-Plugins eingeschränkte Funktionalität. Am Ende hatte ich eine kurze, coole Gradle-Build-Datei, die niemand richtig warten konnte, nicht einmal die Entwickler, die sie geschrieben hatten und sie lieben Gradle immer noch. Ich kenne nur wenige, die Gradle-Skripte ernsthaft verstehen oder schreiben können.

### Maven'in Gücünü Yeniden Keşfetmek: Maven'in Sihirli Güçlerini Kullanmak

İşte benim en sevdiğim Maven işlevleri:
Eklentiler önceden tanımlanmadan doğrudan komut satırından başlatılabilir ve yapılandırılabilir. Ayrıca, diğer Eklenti yapılandırmalarından büyük ölçüde bağımsızdırlar.

| Örnek Komut                           | Açıklama                                                                                                                                                            | Link                                                                     | 
|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`   | Sürümleri güncelleyin - Dependabot kim gereklidir? Evet, projelerim yıllardır en son sürüme sorunsuz bir şekilde güncellendi ve zahmetsiz birleştirme istekleri olmadan. | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0` | Proje sürümünü belirleyin...                                                                                                                                        | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`         | Bağımlılıkları ve lisanslarını listeleme (hatta dışlanmış lisanslar için başarısız olabilir)                                                                          | https://www.mojohaus.org/license-maven-plugin/index.html                 | 

Bu liste sonsuza kadar devam edebilir. Github Çalışma Akış Adımlarını bir şekilde hatırlatıyor.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

```

### XML' i sevmiyor musun?

Sorun değil! Yalnızca `ruby`, `groovy`, `scala`, `yaml`, `atom` veya `Java` biçimindeki yapınızı yazın. Polygot Extension'u (https://github.com/takari/polyglot-maven) kullanarak yapabilirsiniz. Denemek için sadece `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` komutunu çalıştırın ve inanılmaz bir şekilde, yapınız çevrilmiş olacaktır. Ne yazık ki, güvenilir bir Maven <> Gradle tercümanı yok :(. Evet, Maven Build Dosyaları büyük, ama çok kolay anlaşılır. Hataların veya hata ayıklamaların düzenlenmesi de birkaç saniye içinde yapılabilir.

### Yaş sadece bir sayıdır - Maven'in Stabilitesi ve Evrimi

Kabul edelim ki, Maven oldukça uzun bir süredir var ve estetiği belki de bugünün standartlarına uymuyor. Ancak, Maven'in
dayanıklılığı adapte olmasına ve gelişmesine olanak sağladı. Maven projenizden bağımsız çalışır. Derleme dosyaları
kolayca yeniden kullanılabilir. Eklentiler bir kum havuzunda çalışır ve birbirlerinden ve Java veya Maven sürümünden
bağımsızdır. Bu tasarım istikrarı ve öngörülebilirliği teşvik eder ve beklenmedik çatışmalar olmadan karmaşık derleme
süreçlerini yönetmeyi kolaylaştırır.

### Sonuç

Günümüzde, geliştiriciler için gerekli birçok görev ve teknoloji ile geliştirme ortamı aşırı yüklenmiştir. Basitlik ve
otomatizasyon arayışında, modern bir oluşturma aracı olarak ortaya çıkan Gradle, kendi zorluklarını da beraberinde
getirmiştir. Şüphesiz, Gradle'nin konsepti iyi! Ancak, Gradle yapı betiklerine yatırılan karmaşıklık ve zaman göz önüne
alındığında, Maven'ı genişletmek daha kolay olmaz mıydı? PLUGINS ve EXTENSIONS ile, Maven her zaman yenilenebilir ve
basitleştirilebilir. Teknolojiden teknolojiye atlamaktan ziyade, bir ilerleme daha heyecan verici ve sürdürülebilir
olmaz mıydı?

### Bağlantılar

```
* [Gradle'dan Maven'e Geri Dönüş](https://phauer.com/2018/moving-back-from-gradle-to-maven/)
```

### İletişim

[GitHub Problemleri](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
