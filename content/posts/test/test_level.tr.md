---
title: "Test Seviyeleri: Doğru Dengeyi Bulma"
date: 2023-05-31
author: "Nova Annabella"
slug: test_level
tags: [ Testing, Software Testing, Test Levels, Mock Tests, Unit Tests, Integration Tests, Component Tests, Contract Tests, End-to-End Tests ]
categories: [ Technology, Software Development, Quality Assurance ]
description: "Yazılım testleri için uygun test seviyelerini seçerken doğru dengeyi bulma"
draft: false
images:
  - "/images/content/martin_fowler_testing.png"
card: "summary_large_image"
---


# Test Seviyeleri: Doğru Dengeyi Bulmak

[![testebenen](/images/content/martin_fowler_testing.png)](https://martinfowler.com/articles/microservice-testing/)


### Giriş

Test konusu bugüne kadar hala keşfedilmemiş çok fazla yorum alanına sahip olmaya devam ediyor gibi görünüyor. Geleneksel
test piramidi sorgulandı ve yeni test piramitleri oluşturuldu. Bana göre, bir test piramidi değil, neyin test edilmesi gerektiği konusunda net bir anlayışa ihtiyaç var. Daha düşük seviyelerdeki testler genellikle
daha az açıklayıcıdır. Odak, özellikle davranışın test edilmesi üzerinde olmalıdır, API'nin
veya UI'nin istendiği gibi çalıştığını garantilemek için. Olası test türleri hakkında kapsamlı bir genel bakışı burada bulabilirsiniz:
[Martinfowler Testi](https://martinfowler.com/articles/microservice-testing/).


### Seviye 1 - Alay Sınavları & Birim Testleri

Hedef: Uygulamadaki en küçük test edilebilir yazılım parçalarını çalıştırmak ve beklenildiği gibi çalışıp
çalışmadıklarını belirlemek. Mock testler ve ünite testler çoğu zaman ters tepebilir ve geliştirme sürecini engeller.
Bu testler genellikle bağlamdan bağımsızdır ve gerçeklikle fazla bir ilgisi olmaz. Çoğunlukla sadece, var olan unit
testler üzerinde gereksiz fonksiyonları sürdürmeye yararlar. Mocklar eklendiğinde, bu bir kendi kendine meşguliyete
dönüşür. Mock testlerin beklenen sonuçları, orijinal mock'ta tanımlananlara sınırlıdır. Son kullanıcılar, iç
fonksiyonlarla ilgilenmiyorlar. Örneğin, bir giriş senaryosunda `loginUser(name, password, securityAlgorithmus)`. Unit
test, `securityAlgorithm` parametresinde bir null kontrolü yaparsa, kullanıcıların `securityAlgorithm` parametresini
ayarlayamadığından, çok fazla test edilmiş olur.

### Seviye 2 - Entegrasyon Testi

Amaç: Bileşenler arasındaki iletişim yollarını ve etkileşimleri kontrol ederek arayüz hatalarını tespit etme.
Entegrasyon testleri, uygulamanın çeşitli parçalarının performans ve bağımsızlığı hakkında değerli bilgiler sunar. Daha
az mock ile testler daha anlaşılır hale gelir. Ancak, hala bir bağlam eksikliği vardır ve entegrasyon testlerinin sadece
daha az mock ile gizlenmiş birim testler olduğu riski vardır.

### Seviye 3 - Bileşen Testi

Amaç: Test edilen yazılımın kapsamını sistemin test edilecek bir kısmına sınırlamak, sistemi iç kod arayüzleri üzerinden
manipüle etmek ve test doubles'ın test edilecek kodu diğer bileşenlerden izole etmek için kullanılır. Bileşen testleri,
uygulamanın kalitesi ve performansı hakkında bir dizi bilgi sağlar. Nihayetinde uygulamanızı mocklar yerine test
edersiniz. Bileşen testleri ile uçtan uca testler arasındaki sınır belirgin değildir. İyi bir test ortamı ile, onlar
arasındaki sınırlar genellikle bulanıklaşır, bu da gerçek davranışın izole ve bağlamsız işlevler yerine test edilmesini
mümkün kılar. Ancak, ek test sınıfları oluşturmak, prodüksiyon kodunda bileşen stubs, sahte ve mocklar gibi, ek bakım
yükü getirebilir.

### Seviye 4 - Sözleşme Testi

Bu kod bloğunun amacı, bir dış hizmetin sınırındaki etkileşimleri kontrol etmek ve 
tüketen bir hizmetin sözleşme taleplerine uyduğundan emin olmaktır.

Sözleşme Testleri genellikle Bileşen Testlerine benzer ve aralarındaki fark minimaldir. Bazı geliştiriciler 
bu testleri Pact Testleri ile ilişkilendirir, temelde bir sunucu arasındaki birim testleri olarak işlev görürler. Ancak, 
bu testleri sürdürme maliyeti karşılığını vermeyebilir. Örneğin, bir Pact Testi 
REST-API `loginUser?name=aa&password=bb)`ı test edebilir ve daha önce Pact sunucusuna 
yüklenmiş, bir JSON Şema yanıtı bekler. Bu şema statik ve API yanıtındaki yanlış tarih formatları 
veya saat dilimleri gibi hatalara açıktır. Negatif etkileri oldukça büyük olabilir.


### Seviye 5 - Uçtan Uca Testler (aynı zamanda Kara Kutu Testleri olarak da adlandırılır)

Amaç: Bir sistemin dış gereklilikleri karşıladığını ve hedeflerine ulaştığını, sistemin tümünün baştan sona test
edilmesi ile kontrol etmek. Uçtan uca testler güvenilir ve sağlamdır. Test ortamı kurulum zorlukları aşıldığında, çaba
karşılığını verir. Bu testler, gerçek davranışları simüle eder ve sahte özelliklerin gerekliliğini ortadan kaldırır.
Hatalar daha az sıklıkla ortaya çıkar ve yerel olarak daha kolay çoğaltılabilirler. Karmaşık hata ayıklama ve üretimde
günlük kaydı tutma çoğunlukla önlenir, nadir olaylar da aynı şekilde. Geliştiriciler, sorumluluğu azaltan ve odaklanmayı
artıran veri üretimiyle daha az uğraşırlar, eğer hiç uğraşırlarsa. Ayrıca, otomatik yazılım güncellemeleri gibi
otomatikleştirmeler uygulamayı kolaylaştırır, çünkü davranış zaten test edilmiştir. Daha fazla avantaj var! Testler bir
kere yeniden kullanılabilir bir forma yazıldığında, bir işlevsellik hakkında kapsamlı bir resim elde etmek için yük
testlerine entegre edilebilirler. Bu testler ayrıca sürekli olarak üretim ortamında yürütülebilir ve çeşitli çalışma
akışlarının durumu hakkında gerçek zamanlı bilgi sağlar. Bir alt sistem, örneğin bir dış REST hizmeti, çevrimdışı
olursa, etkilenen kullanıcı iş akışlarının hemen tanımlanabilmesi mümkün olur.

### Sonuç

Özetlemek gerekirse, test etme yazılım geliştirmenin vazgeçilmez bir yönüdür ve test seviyelerinin seçimi uygulamanın
spesifik gereksinimlerine ve hedeflerine bağlıdır. Mock testler ve birim testler etkinliklerinde sınırlı olabilirler,
entegrasyon testleri ve bileşen testleri uygulamanın davranışı ve performansı hakkında değerli bilgiler sunar. Sözleşme
testleri, dış hizmetlerle olan etkileşimleri kontrol etmeye yardımcı olur, ancak senin bileşen testleri ile
sınırlandırılması minimal olabilir. Sonuç olarak, uçtan uca testler sistemin işlevselliğine olan en yüksek düzeyde
güveni sağlar ve tüm uygulamanın kapsamlı testlerini sağlar. Uygun test seviyelerini seçmek ve etkili bir şekilde
birleştirmek, geliştiricilerin kalite, güvenilirlik ve sağlamlığını garanti eder yazılımı.

### İletişim

[GitHub Sorunları](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).

