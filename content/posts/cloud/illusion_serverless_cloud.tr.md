---
title: "Illusion Serverless & Bulut"
date: 2023-05-24
author: "Nova Annabella"
slug: illusion_serverless_cloud
tags: [ Development, Serverless, Cloud, Microservices, Scalability, Architecture, Infrastructure ]
categories: [ Technology, Software, Cloud ]
description: "Bulut içindeki sunucusuz fonksiyonların zorlukları ve gerçekleri. Buluta göç düşünen şirketler için değerli içgörüler."
draft: false
images:
  - "/images/content/onprem_vs_cloud.png"
card: "summary_large_image"
---


# Bulut'taki Serverless Fonksiyonların İllüzyonu

![aws_costs_twitter_1](/images/content/onprem_vs_cloud.png)

### Giriş

Pazarlamanın genellikle sağduyu üzerinde ne kadar sık galip geldiği konusunda hayal kırıklığına uğradım. Birçok yönetici kendilerinin
kendi uzmanlarından - yani geliştiricilerden - daha üstün olduğunu düşünür. Bu, buluta geçiş için de geçerlidir. Spoiler: Paranı tasarruf etmen gerekiyorsa, buluttan kaçınmalısın. Çünkü bulutun yeni moda kelimesi "Serverless" şu anlama gelir: Sen yazılımla ilgilenirsin, biz donanımla ilgileniriz. Ancak yetenekli, motive olmuş ve meraklı bir yöneticisi olan kişi, Serverless'i kendi başına da işletebilir (örneğin, [KNative](https://knative.dev)).

![aws_costs_twitter_1](/images/content/aws_costs_twitter_1.png)

### Serverless Fonksiyonlar vs Mikroservisler:



#### Mikroservisler

Tipik bir durumsuz Mikroservis, belirli bir işlev / alanla ilgilenir ve bir 
Konteyner Orkestrasyon ortamında dağıtılır. Bu ortam, altyapı, güvenlik, güvenlik duvarı,
Günlük tutma, metrikler, sırlar, ağ, yedeklemeler ve daha birçok şey hakkında endişelenir. Büyük bir avantajı, bir Mikroservis'in yerel olarak
az
Kaynaklar entegre bir şekilde test edilebilir ve Bulut / Sunucu-agnostik (her yerde kullanılabilir) olmasıdır.


#### Serverless Fonksiyonlar

Öncelikle küçük bir şaka: Paradoks, ama doğru - Serverless fonksiyonlar, sunucu ortamına büyük ölçüde bağımlıdır. :)
Tipik bir Serverless fonksiyonu da sadece belirli bir fonksiyon / alanla ilgilenir ve bir çerçeve olmadan
daha hızlı olması için saf kodda yazılır (MicroServices için de iyi bir pratiktir). Büyük bir
avantaj, Serverless fonksiyonların otomatik olarak ölçeklendirilmesidir. Ancak, her Serverless fonksiyonu belirgin bir miktar GlueCode gerektirir, bunlar altyapıyı tanımlar - Güvenlik, Güvenlik Duvarı, Ağ, Günlük Kaydı, Metrikler,
Sırlar, Önbellekleme, Yedeklemeler ve daha fazlası.  
Bu nedenle, bir dosyayı kopyalama gibi basit bir işlev, API dahil, hızlıca 1500 satır kod (IaC dahil)
içerebilir.
Yönetim maliyetleri, yönetimden gelişime, 1: N oranında (1'den Serverless'e
Fonksiyonlar). Bilgi ve uygulamalar artık
bir arada ve hızla istikrarsız hale gelebilir. Artan bakım maliyetleri de mevcuttur.  
Serverless ile gerçek entegratif testler nadiren veya büyük bir çabayla yapılır.
Sonuçta, Serverless fonksiyonlarının karmaşıklığı, tek bir Mikroservis'ten çok daha yüksektir.
Daha yüksek karmaşıklık, aynı zamanda daha düşük sürdürülebilirlik anlamına gelir. Yeni ekip üyelerinin işi daha zor olur ve önemli ölçüde
daha fazla önbilgi gereklidir.


### Serverless ve Genel olarak Bulut

Çoğu bulut teknolojisi en son durumda değil. Örneğin, Node.js, Java, Python ve diğer
diller veya teknolojiler genellikle kolayca güncellenemez, genellikle sabırla beklemek işe yarar.
Ayrıca MongoDB, MySQL, Kafka, NATS, RabbitMQ, Redis, Prometheus, InfluxDB, Grafana,
Kibana, Elastic Search vb. gibi modern ve standart teknolojiler ya mevcut değildir ya da aşırı pahalıdır.
Böyle standart hizmetler olmadan, genellikle kişi sanal taş devrindendir ve eski çözümleri kullanır, örn.
dışarıya iletişim için web kancaları. Bunlara, regülasyon konularında hareket kabiliyetinin kısıtlı olması,
uyumluluk, gizlilik ve hata toleransı eklenir.

Bulut, AWS, Azure, Google, On-Premise vb. arasında hızlı bir şekilde değişebilmek ve
maliyetleri karşılaştırabilmek için agnostik bir şekilde çalıştırılmalıdır.
Sınırlar bulutta da sıkça mevcuttur, bu da karmaşıklığı
artıran yaratıcı çözüm yollarına yol açar. Ayrıca entegratif testler pahalı hale gelebilir, çünkü her geliştiricinin bulutta kendi geliştirme ortamına
ihtiyacı vardır, çünkü birçok bulut hizmeti yerel olarak pek veya hiç test edilemez.
Ancak testler olmaksızın bile bulut pahalıdır. On-Premise sistemlerde özellikle
donanım maliyetleri oluşurken, bulutta ek olarak trafik, bazı standart hizmetler ve hatta çoğu zaman
çifte vergilendirme için ödeme yapılması gerekir. Ayrıca, bulutta kolayca genel bakışı kaybedersiniz, çünkü mesele
kullanıcı dostu olmak değil, para kazanmaktır. Maliyetler öyle gizlidir ki, onları ancak çok geç olduğunda fark edersiniz.

Mimari ve altyapı temelleri bulutta ve özellikle sunucusuz alanında
yeniden icat edilmeli, çünkü uygulama mevcut işlevlere büyük ölçüde bağlıdır.
Mimariyi tasarladıktan her zaman sonra, "Bu bir hizmet olabilirdi" diye düşünürüm.

Benim için sunucusuz, ilginç bir fikir ve iyi ölçeklenebilir, ancak maliyeti düşürmez. Tam
aksine, geliştirme sürecinde daha fazla bilgi ve zaman gerektirir. Sunucusuz veya bulut, disiplin ve
ön bilgi gerektirir.
On-Premise sistemler için bilgi yoksa, bulutla daha kolay olmaz.
Geliştiriciler ek olarak altyapı bilgisi nasıl edinebilir?

Bir bulut mimarisi yerine iyi yönetilen bir Kubernetes kümesini tercih ederim.
Çalışanlar ölçeklenmiyor. Birçok geliştiricinin kod yazma disiplini yok.
Maalesef bu durum geliştiricilerin %80'ine uygundur. Peki bu geliştiriciler nasıl bulutu yönetebilirler?

Şirketlerin sunucusuz mimari ve bulutun zorluklarını ve etkilerini tam anlamıyla anlamaları önemlidir. Bu sadece teknik bilgiyi değil, aynı zamanda stratejik bir yaklaşımı gerektirir. Düşünmeden yapılmış bir buluta geçiş, karmaşıklığa, daha yüksek maliyetlere ve geliştiricilerin aşırı yüklenmesine yol açabilir.

Özetle, bulutta sunucusuz bir olasılık, ancak dikkatlice
incelenmelidir. Maliyet, karmaşıklık, sürdürülebilirlik ve geliştirme ekibinin yetenekleri
göz önünde bulundurulmalıdır.
Her şirketin farklı gereksinimleri ve öncelikleri vardır. Bulutta sunucusuzun doğru çözüm olup olmadığına veya alternatif yaklaşımların - 
örneğin iyi bir Kubernetes kümesinin - daha iyi bir seçenek olup olmadığına dikkatli bir karar verilmelidir.

Sunucusuz ve bulut bilişimin başarılı uygulaması, teknik uzmanlık
stratejik planlama ve iş gereksinimlerinin net anlaşılması kombinasyonunu gerektirir. Sadece bu şekilde sunucusuzun illüzyonunu görebilir ve kendi yazılım geliştirmesi için doğru kararı verebilirsiniz.


### Sonuç

Sunucusuz işlevlerin Buluta tanıtılması esneklik, ölçeklenebilirlik ve alıcıyı altyapı görevlerinden kurtarma sözü
verir. Ancak, bu yanılsamadan kör olunmamalı. Buluta geçiş ve sunucusuz işlevlerin kullanımı bir dizi zorluk getirir.
Geliştiriciler asıl geliştirmenin yanı sıra yeni bir "dil" öğrenmeli ve uygun destek olmadan daha fazla sorumluluk
almalıdır. Sunucusuz işlevlerin karmaşıklığı, geliştiricilerin birçok ek görevler gibi altyapı tanımı, güvenlik ve
ölçeklendirme aldıklarından, mikro hizmetlerden daha sıklıkla yüksektir. Gerçek entegrasyon testleri zordur ve bulutta
operasyon için önceden bilgi ve deneyim daha da önemlidir. Bulut kendi kendine daha fazla zorluk getiriyor. Birçok
bulut teknolojisi en son ve modern standart hizmetleri kullanmak pahalı veya imkansız olabilir. Düzenleyici
gereklilikler, uyumluluk ve veri koruma hareket alanını kısıtlar. Ayrıca, bulutta maliyetler kolaylıkla kontrol dışına
çıkar, ve harcamaların genel görünümü hızla kaybolur. Genel olarak, Sunucusuz ve Bulut'un avantajları ve dezavantajları
dikkatlice değerlendirilmelidir. Şirketler, belirli gereksinimlerini, ekibindeki mevcut bilgi birikimini ve buluta bir
göçün uzun vadeli etkilerini göz önünde bulundurmalıdır. Kapsamlı bir analize dayalı bilinçli bir karar, projenin
başarısı ve karlılık için hayati öneme sahiptir. Sonuçta, şirketlerin, geliştiricilerini uygun şekilde desteklemesi,
bulutun maliyetini ve karmaşıklığını gerçekçi bir şekilde değerlendirmesi ve iyi yönetilen Kubernetes kümesi gibi
alternatif çözümleri düşünmesi gerekir. Net bir strateji ve kendi ihtiyaçlarının sağlam bir anlayışı ile şirketler,
bulutun ve sunucusuz işlevlerin avantajlarını en iyi şekilde kullanabilir ve yanılsamayı görebilirler.

### İletişim

[GitHub Sorunları](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
