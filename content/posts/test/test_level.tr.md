---
title: "Test seviyeleri: Doğru dengeyi bulmak"
date: 2023-05-31
author: "Nova Annabella"
slug: test_level
tags: [ Testing, Software Testing, Test Levels, Mock Tests, Unit Tests, Integration Tests, Component Tests, Contract Tests, End-to-End Tests ]
categories: [ Technology, Software Development, Quality Assurance ]
description: "Yazılım testi için uygun test seviyelerini seçerken doğru dengeyi bulmak."
draft: false
images:
  - "/images/content/martin_fowler_testing.png"
card: "summary_large_image"
---


# Test seviyeleri: Doğru dengeyi bulmak

[![testebenen](/images/content/martin_fowler_testing.png)](https://martinfowler.com/articles/microservice-testing/)

### Giriş

Test konusu hala yoruma çok açık, keşfedilmemiş bir alan gibi görünüyor. Geleneksel test piramidi sorgulanmış ve yeni
test piramitleri ortaya çıkmıştır. Benim görüşüme göre, bir test piramidine gerek yok. test piramidi değil, neyin test
edilmesi gerektiğinin net bir şekilde anlaşılmasıdır. Alt seviyelerdeki testler genellikle daha az anlamlıdır. Odak
noktası, öncelikle aşağıdakileri sağlamak için davranışı test etmek olmalıdır API veya UI istenildiği gibi çalışır.
Olası test türlerine kapsamlı bir genel bakış burada bulunabilir: [Martinfowler Testing]
(https://martinfowler.com/articles/microservice-testing/).

### Seviye 1 - Deneme Testleri ve Birim Testleri

Amaç: Uygulamadaki test edilebilir en küçük yazılım parçalarının beklendiği gibi çalışıp çalışmadığını görmek için
alıştırma yapmak. İş. Sahte testler ve birim testleri verimsiz olabilir ve genellikle geliştirme sürecini engeller. Bu
testler genellikle bağlamdan kopuktur ve gerçeklikle çok az ilişkisi vardır. Genellikle sadece mevcut işlevler
aracılığıyla gereksiz işlevlerin sürdürülmesine hizmet ederler. birim testleri. Mock'lar eklendiğinde, bu kendi kendini
yok eden bir egzersiz haline gelir. Beklenen Sahte testlerin sonuçları orijinal sahte testte tanımlananlarla sınırlıdır.
Son kullanıcılar dahili işlevlerle ilgilenmez. Örneğin, bir login senaryosu `loginUser(name, password,
securityAlgorithm)`. Eğer birim testi bir null kontrolü yaparsa parametresi kullanıldığında, kullanıcılar
`securityAlgorithm` parametresini ayarlayamadıkları için çok fazla test yapılır. 'securityAlgorithm' parametresini
ayarlayın.

### Seviye 2 - Entegrasyon Testi

Amaç: Bileşenler arasındaki iletişim yollarını ve etkileşimleri kontrol ederek arayüz kusurları. Entegrasyon testleri,
uygulamanın farklı bölümlerinin performansı ve bağımsızlığı hakkında değerli bilgiler sağlar. Uygulama. Daha az sayıda
mock ile testler daha anlaşılır hale gelir. Ancak yine de bağlamdan yoksundurlar ve şu riskler vardır Entegrasyon
testlerinin daha az mock ile kılık değiştirmiş birim testleri olduğu tehlikesi.

### Seviye 3 - İçerik Testi

Amaç: Test edilen yazılımın kapsamını test edilen sistemin bir bölümüyle sınırlamak, sistemi manipüle etmek Dahili kod
arayüzleri aracılığıyla sistem ve test edilen kodu diğer bileşenlerden izole etmek için test çiftlerinin kullanılması.
bileşenler. Bileşen testi, uygulamanın kalitesi ve performansı hakkında çok sayıda bilgi sağlar. Bunun yerine Sonunda
uygulamanızı test edersiniz. Bileşen testi ile uçtan uca test arasındaki sınır önemli. İyi bir test ortamında,
aralarındaki sınırlar genellikle bulanıklaşır, böylece gerçek testler izole ve bağlamsız işlevler yerine davranış.
Ancak, ek işlevlerin oluşturulması Ancak, üretim kodunda bileşen saplamaları, sahteler ve mock'lar gibi ek test
sınıfları oluşturmak bakım yükünü artırabilir.

### Seviye 4 - Sözleşme Testi

Bu kod bloğunun amacı, harici bir hizmetin sınırındaki etkileşimleri kontrol etmek ve tüketen bir hizmetin sözleşme
gerekliliklerine uygun olmasını sağlamak. Sözleşme testleri genellikle birim testlerine benzer ve aralarındaki fark çok
azdır. Bazı geliştiriciler Bu testleri, aralarında bir sunucu bulunan birim testleri gibi davranan Pact testleriyle
ilişkilendirin. Bu testler Ancak bu testleri sürdürmek için harcanan çabaya değmeyebilir. Örneğin, bir Pact testi
aşağıdakileri kullanabilir REST API `loginUser?name=aa&password=bb)` ve daha önce Pact sunucusuna yüklenmiş bir JSON
şema yanıtı bekleyin. sunucu. Bu şema statiktir ve yanlış tarih biçimleri veya saat dilimleri gibi hatalara açıktır. API
yanıtı. Olumsuz etkileri çok büyük olabilir.

### Seviye 5 - Uçtan uca testler (kara kutu testleri olarak da adlandırılır)

Amaç: Bir sistemin dış gereksinimleri karşıladığını ve tüm sistemi baştan sona test ederek hedeflerine ulaştığını
doğrulamak. Baştan sona. Uçtan uca test güvenilir ve sağlamdır. Test ortamını kurmanın önündeki engeller aşıldıktan
sonra çaba karşılığını verir. Bu testler gerçek davranışı simüle eder ve mock'lara olan ihtiyacı ortadan kaldırır.
Hatalar daha az sıklıkta meydana gelir ve yerel olarak yeniden üretilmesi daha kolaydır. Üretimde zaman alan hata
ayıklama ve günlüğe kaydetme işlemlerinden büyük ölçüde kaçınılır. nadir olaylar gibi büyük ölçüde önlenir.
Geliştiriciler, eğer varsa, aşağıdakilerle daha az çalışır üretim verileri, sorumluluğu azaltır ve odaklanmayı artırır.
Ayrıca, aşağıdaki gibi otomasyonlar otomatik yazılım güncellemeleri, davranış zaten test edilmiş olduğu için uygulamayı
kolaylaştırır. Başka faydaları da var! Bir kez testler yeniden kullanılabilir bir biçimde yazılırsa, kapsamlı bir test
elde etmek için yük testlerine entegre edilebilirler. işlevselliğin kapsamlı bir resmi. Bu testler üretim ortamında da
sürekli olarak çalıştırılabilir ve çeşitli iş akışlarının durumu hakkında gerçek zamanlı bilgiler sağlar. Bir alt
sistem, örneğin Örneğin REST hizmeti çevrimdışı olduğunda, hangi kullanıcı iş akışlarının etkilendiğini hemen belirlemek
mümkündür. etkilenir.

### Fazit

Özetle, test yazılım geliştirmenin önemli bir yönüdür ve test seviyelerinin seçimi aşağıdakilere bağlıdır Uygulamanın
özel gereksinimleri ve hedefleri. Sahte testler ve birim testlerinin etkinliği sınırlı olabilirken, entegrasyon testleri
ve etkinliği, entegrasyon testleri ve birim testleri uygulamanın davranışı ve performansı hakkında değerli bilgiler
sağlar. Uygulamanın performansı. Sözleşme testleri harici hizmetlerle etkileşimlerin doğrulanmasına yardımcı olur, ancak
bunların Birim testlerinden farklılaşma minimum düzeyde olabilir. Sonuç olarak, uçtan uca test, sistemin işlevselliği
konusunda en yüksek düzeyde güven sağlar ve kapsamlı testlere olanak tanır. Sistemin işlevselliği ve tüm uygulamanın
kapsamlı bir şekilde test edilmesine olanak tanır. Uygun olanı seçerek test seviyeleri ve bunları etkili bir şekilde bir
araya getirerek, geliştiriciler testlerinizin kalitesini, güvenilirliğini ve sağlamlığını sağlayabilir. yazılım.

### İletişim

[GitHub Sorunları](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
