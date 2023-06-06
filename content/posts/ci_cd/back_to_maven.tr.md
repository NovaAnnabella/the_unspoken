---
title: "Maven'a geri dönmek mi?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "Sadelik için zor bir arayış ve Maven'ın gücünü yeniden keşfetmek için kısa bir yolculuk"
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---



# Maven'a geri mi döndün?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

## Gradle'ın 10 yılı. Rahatlama arayışı ve Maven'in gücünü yeniden keşfetmek için kısa bir yolculuk.



### Geliştiricilerin potansiyelini en üst düzeye çıkarmak - daha fazla zaman kazandıran araca ihtiyacımız var

Genellikle göz ardı edilen veya nadiren tartışılan konular ilgimi çekiyor. Genellikle kullanılan harika teknolojiler
var, ancak neredeyse hiç kimse bunlarla ilgili sorunlardan bahsetmiyor. Geliştirme bugünlerde çok maliyetli hale geldi.
"Sunucusuz", "düşük kod", "IaC", "büyük veri", "bulut", "DevOps", "sen kur, sen çalıştır" vb. gibi havalı sözcüklerle,
geliştiriciler zaten yeterince uğraştı. vs. derken, geliştiricilerin zaten uğraşması gereken gereğinden fazla ek görevi
var. Daha fazla görev, neredeyse hiç görev olmadığı anlamına gelir. uzmanlar ve odak için her zaman bir şeyler ihmal
edilir. İşte bu yüzden otomasyon ve zaman tasarrufu çok önemlidir. önemli. "Beni düşündürme" ve "Kutudan Çıkar çıkmaz
çalışır" zaten Gradle'da henüz göremediğim kaliteli özellikler. Henüz göremiyorum. Adil olmak gerekirse, Gradle işimizi
yapmak yerine kolaylaştıran tek modern araç değil. kolaylaştırır.

### Basitlik ve otomasyon için hayali arayış

SOAP'tan beri XML tabanlı yapılandırmalara karşı köklü bir isteksizliğim var. Gradle ile, ummuştum ki bağlama
senaryoları yazmanın çocuk oyuncağı olacağını düşünmüştüm. Ne yazık ki, umutlarım ve motivasyonum azaldı her seferinde
azaldı. Gradle esneklik için çabalar ve bunun için otomasyon ve kaliteyi feda eder. Geliştiriciler körü körüne
geliştiriciler, yazılımın güvenilirliği üzerindeki etkisini dikkate almadan trendi körü körüne takip ediyor. Gradle'ı
yapmak için Basit ve az bakım gerektiren senaryolar oluşturmak güçlü bir disiplin gerektirir. Böyle bir disiplin zaten
nadir kaynak kodu ve bu nedenle derleme komut dosyalarında daha da nadirdir.

### Çeviriler ve geçici çözümler - Derleme komut dosyaları zorlandığında

Gradle arka planda Maven'dan çok farklı çalışmaz. Bu nedenle bazı çeviriler gereklidir. Aşağıdaki gibi özellikler
Dependency Catalog, Maven Release Plugin, Dependabot ve daha pek çoğu aslında temel çözümler için geçici çözümlerdir.
Maven'ın zaten getirdiği işlevler. Gradle'ın esnekliği genellikle karmaşık derleme yapılandırmalarını da beraberinde
getirir, bakımı zor olan eklentilerdir. Gradle eklentilerinin genellikle uyumluluk sorunları, sınırları veya sınırlı
ilerlemeleri vardır. Bu sorunlar ortaya çıkar Gradle ekosisteminin gelişen doğası nedeniyle, Gradle'ın kullanıldığı
ortamların çeşitliliği ve her bir eklenti için gereken özel uygulama ve bakım çabası. Her şey birbiriyle bağlantılıdır.

### Gradle domino etkisi - Gerçek dünyada bir kabus senaryosu

Sadece birkaç yaşında olan ve Gradle nedeniyle artık sürdürülemeyen birçok mikro hizmet gördüm. Gradle yüzünden. Böyle
bir şeyi ilk kez görmediğimi belirtmek isterim ve hayır, bunlar Junior Devs. Benim **görevim Spring Boot 2.x'ten 2.7'ye
yükseltme** yapmaktı. Spoiler: Bir yıl sonra vazgeçtim Pes ettim! Kısaca sorunlar: * Gradle derleme dosyası şunları
gerektirir -> Yerel Java sürümümü 11'e düşürün (WTF) (Normalde Java  Aşağı doğru uyumlu - yine, SdkMan gibi geçici
çözüm araçları var ...) * Spring Boot güncellemesi -> Gradle güncellemesi gerektirir (WTF) * Gradle güncellemesi ->
Eklenti güncellemesi gerektirir * Eklenti güncellemesi -> Groovy güncellemesi gerektirir (WTF) * Groovy güncellemesi ->
Test çerçevesi ve test güncellemeleri (WTF) gerektirir * Test çerçevesi güncellemesi gerektirir -> Bağımlılık
güncellemeleri. * \[...]  Ek olarak, bazı eklentiler daha yeni Gradle sürümleriyle çalışmaz, bazıları artık
geliştirilmez, bazıları diğer Gradle sürümleriyle uyumsuzdur, bazıları artık geliştirilmez, bazıları diğer Gradle
sürümleriyle uyumsuzdur.  diğer eklentilerle uyumsuzdur, yalnızca Gradle KTS ile çalışır, Gradle Groovy ile çalışmaz
veya basitçe  basitçe sınırları vardır. Spring gibi büyük tedarikçilerin eklentileri bile Maven eklentilerine kıyasla
sınırlı işlevselliğe sahiptir.  Sınırlı işlevsellik. Sonunda kimsenin gerçekten koruyamayacağı havalı, kısa bir Gradle
derleme dosyası elde ediyorum,  onu yazan geliştiriciler bile değil ve onlar hala Gradle'ı seviyorlar. Çok az insan
tanıyorum  Gradle betiklerini anlamak, onları ciddi bir şekilde yazmak.

### Maven'ın Gücünü Yeniden Keşfetmek - Maven'ın Sihrinden Yararlanmak

İşte Maven'in en sevdiğim özellikleri: Eklentiler, önceden tanımlanmalarına gerek kalmadan doğrudan komut satırından
başlatılabilir ve yapılandırılabilir. tanımlanmasına gerek yoktur. Ayrıca, diğer eklenti yapılandırmalarından büyük
ölçüde bağımsızdırlar. | Örnek Komut | Açıklama | Bağlantı | |---------------------------------------|-----------------
------------------------------------------------------------------------------------------------------------------------
----------------------------|--------------------------------------------------------------------------| | `mvn
versions:use -latest-versions` | Sürümleri güncelleyin - Dependabot'a kimin ihtiyacı var? Evet, projelerim yıllardır
sorunsuz ve can sıkıcı birleştirme istekleri olmadan en son sürüme güncellendi |
https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html | | `mvn versions:set -DnewVersion=1.0.0` |
Proje sürümünü ayarla...
| https://www.mojohaus.org/versions/versions-maven-plugin/index.html | | `mvn license:add-third-party` | Bağımlılıkları
listeler ve lisanslarını gösterir (lisanslar hariç tutulsa bile başarısız olabilir) | https://www.mojohaus.org/license-
maven-plugin/index.html | Bu liste sonsuza kadar devam edebilir. Bana biraz GitHub İş Akışı Adımlarını hatırlatıyor.
![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

### XML'i sevmiyor musun?

Hiç sorun değil! Derleme dosyanızı `ruby`, `groovy`, `scala`, `yaml`, `atom` veya `Java` dillerinde yazmanız yeterlidir.
Polygot Extension (https://github.com/takari/polyglot-maven) bunu mümkün kılıyor. Denemek için basitçe `mvn
io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` çalıştırın ve birkaç
milisaniye içinde yapınız milisaniyede derleme dosyanız çevrilir. Güvenilir bir Maven <> Gradle çeviricisinin olmaması
üzücü. :( Evet, Maven derleme dosyaları büyüktür, ancak anlaşılması da çok kolaydır. Düzeltmeler veya hata ayıklama
hemen yapılır. bitti.

### Yaş sadece bir sayıdır - Maven'ın istikrarı ve evrimi

Kuşkusuz, Maven oldukça uzun bir süredir piyasada ve estetiği günümüz standartlarını karşılamayabilir. Ancak, Maven'ın
uzun ömürlü olması uyum sağlamasına ve gelişmesine olanak tanımıştır. Maven bağımsız çalışır projenizin. Derleme
dosyaları kolayca yeniden kullanılabilir. Eklentiler bir sanal alanda çalışır ve birbirlerinden ve Java veya Maven
sürümünden bağımsızdır. Bu tasarım, kararlılığı ve öngörülebilirliği teşvik eder ve karmaşık derleme süreçlerini
beklenmedik durumlar olmadan yönetmeyi kolaylaştırır. Çatışmalar.

### Fazit

Günümüzde geliştirme ortamı, geliştiriciler için birçok görev ve teknoloji ile aşırı yüklenmiştir. Arama içinde basitlik
ve otomasyon için Gradle modern bir derleme aracı olarak ortaya çıkmıştır, ancak kendi zorluklarla karşılaştım. Gradle
konseptinin iyi olduğuna şüphe yok! Ancak karmaşıklığı ve Gradle derleme komut dosyalarına harcanan zaman, Maven'ı
genişletmenin daha basit olup olmayacağı sorusunu ortaya çıkarmaktadır. Genişletilmiş. Eklentiler ve uzantılarla Maven
her zaman yenilenebilir ve basitleştirilebilir. Bir Daha fazla gelişme, bir teknolojiden diğerine atlamaktan çok daha
heyecan verici ve aynı zamanda daha sürdürülebilir olmaz mı?

### Bağlantılar

* [Gradle'dan maven'a Geri Dönüş](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### İletişim

[GitHub Sorunları](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
