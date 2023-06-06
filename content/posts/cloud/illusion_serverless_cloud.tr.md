---
title: "Illusion Sunucusuz ve Bulut"
date: 2023-05-24
author: "Nova Annabella"
slug: illusion_serverless_cloud
tags: [ Development, Serverless, Cloud, Microservices, Scalability, Architecture, Infrastructure ]
categories: [ Technology, Software, Cloud ]
description: "Bulutta sunucusuz yeteneklerin zorlukları ve gerçekleri. Buluta geçmeyi düşünen şirketler için değerli bilgiler"
draft: false
images:
  - "/images/content/onprem_vs_cloud.png"
card: "summary_large_image"
---



# Bulutta sunucusuz işlevler yanılsaması

![aws_costs_twitter_1](/images/content/onprem_vs_cloud.png)

### Giriş

Pazarlamanın sağduyuya bu kadar sık galip gelmesi beni hayal kırıklığına uğratıyor. Birçok yönetici kendilerini kendi
uzmanları olan geliştiricilerden daha fazla. Bu durum buluta geçiş için de geçerlidir. Spoiler: Paradan tasarruf etmeniz
gerekiyorsa tasarruf etmesi gerekenler buluttan kaçınmalıdır. Çünkü buluttaki yeni moda sözcük "sunucusuz" şu anlama
geliyor: Siz yazılımı halledin, biz donanımı hallederiz. Siz yazılımı halledin, biz de donanımı halledelim. Ancak,
yetenekli, motive ve meraklı bir yöneticiniz varsa, şunları yapabilirsiniz kendileri de sunucusuz çalışabilir (örneğin
[KNative](https://knative.dev)). ![aws_costs_twitter_1](/images/content/aws_costs_twitter_1.png)

### Sunucusuz işlevler vs mikro hizmetler:



#### Mikro Hizmetler

Tipik bir durumsuz mikro hizmet, belirli bir işlevle/alanla ilgilenir ve bir konteyner orkestrasyon ortamı. Bu ortam
altyapı, güvenlik, güvenlik duvarı ile ilgilenir, günlük kaydı, ölçümler, sırlar, ağ oluşturma, yedeklemeler ve daha
fazlası. Büyük bir avantaj, bir mikro hizmetin yerel olarak şu şekilde dağıtılabilmesidir birkaç kaynaklar ve
bulut/sunucu agnostiktir (her yerde konuşlandırılabilir).

#### Sunucusuz işlevler

Öncesinde küçük bir şaka: Paradoksal ama gerçek - sunucusuz işlevler büyük ölçüde sunucu ortamına bağlıdır. :) Tipik bir
sunucusuz işlev de yalnızca belirli bir işlev / alanla ilgilenir ve bir mikro hizmetten daha hızlı olmak için çerçeveler
olmadan saf kodla yazılır. Bir mikro hizmetten daha hızlı olmak için kod (MicroServices için de iyi bir alıştırma).
Büyük bir avantajı, Sunucusuz işlevlerin otomatik olarak ölçeklenmesidir. Bununla birlikte, her sunucusuz işlev bir
Altyapıyı tanımlamak için önemli miktarda GlueCode - güvenlik, güvenlik duvarı, ağ, günlük kaydı, ölçümler, sırlar,
önbellekleme, yedeklemeler ve çok daha fazlası. Bu nedenle, API dahil olmak üzere bir dosyayı kopyalamak gibi basit bir
işlev hızlı bir şekilde 1500 satır kod (IaC dahil) içerebilir. dahil olabilir. Yönetim maliyetleri 1:N oranında
yönetimden geliştirmeye kayar (1'den Sunucusuz fonksiyonlar). Bu nedenle bilgi ve uygulama artık paketlenir ve hızla
istikrarsız hale gelebilir. Ayrıca bakım maliyetleri de artar. Gerçek bütünleştirici testler de sunucusuz sistemlerde
nadirdir ya da ancak büyük çabalarla mümkündür. Sonuç olarak, sunucusuz işlevlerin karmaşıklığı, tek bir mikro
hizmetinkinden önemli ölçüde daha yüksektir. Daha yüksek karmaşıklık aynı zamanda daha düşük sürdürülebilirlik anlamına
gelir. Yeni ekip üyeleri daha zor zamanlar geçirir ve önemli ölçüde daha fazla ön bilgi.

### Sunucusuz ve genel olarak bulut

Çoğu bulut teknolojisi güncel değildir. Örneğin, Node.js, Java, Python ve diğer diller veya teknolojiler dilleri veya
teknolojileri güncellemek genellikle kolay değildir, genellikle sadece beklemek yardımcı olur. MongoDB, MySQL, Kafka,
NATS, RabbitMQ, Redis, Prometheus, InfluxDB, Grafana gibi modern ve standart teknolojiler bile, Kibana, Elastic Search
vb. ya mevcut değildir ya da aşırı pahalıdır. Bu tür standart hizmetler olmadan, kişi genellikle sanal taş devrinde
kalır ve harici iletişim için web kancaları gibi modası geçmiş çözümler kullanır. harici iletişim için web kancaları.
Buna ek olarak, düzenleme gibi konularda manevra alanı, uyumluluk, veri koruma ve arıza güvenliği son derece sınırlıdır.
Bu nedenle AWS, Azure, Google, şirket içi vb. arasında hızlı geçiş yapabilmek için bulut agnostik olarak
çalıştırılmalıdır. maliyetleri karşılaştırın. Sınırlamalar da genellikle bulutta mevcuttur ve bu da yaratıcı geçici
çözümlere yol açarak karmaşıklığı artırır. Artış. Her geliştiricinin bulutta kendi geliştirme ortamına ihtiyaç duyması
nedeniyle bütünleştirici testler de pahalı hale gelebilir Çünkü pek çok bulut hizmeti yerel olarak ya hiç test
edilemiyor ya da çok az test edilebiliyor. Ancak test yapılmasa bile bulut pahalıdır. Şirket içi sistemlerde ise esas
olarak donanım maliyetleri, bulutta ayrıca trafik, bazı standart hizmetler ve hatta çoğu zaman birden fazla hizmet için
ödeme yapmanız gerekir. ve hatta çoğu zaman birden fazla vergilendirme için. Dahası, bulutta işlerin izini kaybetmek
kolaydır, çünkü söz konusu olan mesele kullanım kolaylığı değil, paradır. Maliyetler o kadar gizlidir ki ancak iş işten
geçtikten sonra fark edersiniz. çok geç. Mimari ve altyapının temelleri bulutta ve özellikle sunucusuz ortamda yeniden
keşfedilmelidir Uygulama büyük ölçüde mevcut özelliklere bağlı olduğu için yeniden keşfedilmesi gerekiyor. Mimariyi her
tasarladığımda şöyle düşünüyorum: "Bu tek bir hizmet olabilirdi". olabilirdi". Benim için sunucusuz ilginç bir fikir ve
iyi ölçekleniyor, ancak maliyetleri düşürmüyor. Üzerinde Aksine, geliştirme için çok daha fazla bilgi ve zaman
gerektirir. Sunucusuz ya da bulut disiplin gerektirir ve ön bilgi. Eğer şirket içi sistemler için bu bilgi mevcut
değilse, bulutta da daha kolay olmayacaktır. Geliştiricilerin ek altyapı bilgisini nasıl edinmeleri gerekiyor? İyi
yönetilen bir Kubernetes kümesini bulut mimarisine tercih ederim. İnsanlar ölçeklenmiyor. Birçok geliştiricinin kod
yazma konusunda disiplini yok. Ne yazık ki bu durum geliştiricilerin yüzde 80'i için geçerli. Peki bu geliştiriciler
bulutu nasıl çalıştırabilecekler? Bulutu mu? Kuruluşların sunucusuz mimari ve bulutun zorluklarını ve etkilerini tam
olarak anlaması önemlidir. Sunucusuz mimarinin ve bulutun zorluklarını ve etkilerini tam olarak anlamak. Bu sadece
teknik bilgi değil, aynı zamanda stratejik bir yaklaşım da gerektirir. A İyi düşünülmemiş bir buluta geçiş karmaşıklığa,
daha yüksek maliyetlere ve geliştiricilerin aşırı yüklenmesine yol açabilir. Özetle, bulutta sunucusuz sistem umut
verici bir kavramdır, ancak dikkatle değerlendirilmesi gerekir. dikkatlice düşünülmelidir. Maliyet, karmaşıklık,
sürdürülebilirlik ve geliştirme ekibinin becerileri göz önünde bulundurulmalıdır. dikkate alınmalıdır. Her şirketin
farklı gereksinimleri ve öncelikleri vardır. Şu konularda bilinçli bir karar verilmelidir Bulutta sunucusuz çözüm doğru
çözüm mü yoksa aşağıdaki gibi alternatif yaklaşımlar mı? örneğin Kubernetes Kümesi daha iyi bir seçimdir. Sunucusuz ve
bulut bilişimin başarılı bir şekilde uygulanması, teknik uzmanlığın bir kombinasyonunu gerektirir stratejik planlama ve
iş gereksinimlerinin net bir şekilde anlaşılması. Ancak o zaman sunucusuzluk yanılsaması ve kendi yazılım geliştirmeniz
için doğru kararı verin.

### Fazit

Bulutta sunucusuz işlevlerin kullanılmaya başlanması esneklik, ölçeklenebilirlik ve altyapı görevlerinden kurtulma vaat
ediyor. geliştiricileri altyapı görevlerinden kurtarıyor. Ancak bu yanılsamaya kapılmamak gerekir. Çünkü Buluta geçiş ve
sunucusuz işlevlerin kullanımı bir dizi zorluğu da beraberinde getiriyor. Geliştiriciler, gerçek geliştirmeye ek olarak
yeni bir "dil" öğrenmek ve uygun destek olmadan daha fazla sorumluluk almak zorundadır. Daha fazla sorumluluk almak.
Sunucusuz işlevlerin karmaşıklığı genellikle mikro hizmetlerden daha yüksektir, çünkü geliştiricilerin aşağıdakiler gibi
birçok ek görevi üstlenmesi gerekir geliştiricilerin altyapı tanımı, güvenlik ve ölçeklendirme gibi birçok ek görevi
üstlenmesi gerekir. Gerçek bütünleştirici test zor ve operasyonlar için önceden bilgi ve deneyim bulutta daha da
önemlidir. Bulutun kendisi başka zorlukları da beraberinde getirmektedir. Birçok bulut teknolojisi güncel değildir ve
modern kullanıma hazır hizmetleri kullanmak pahalı, hatta imkansız olabilir. Düzenleyici gereklilikler, uyumluluk ve
veri koruma kapsamı sınırlamaktadır. Buna ek olarak, buluttaki maliyetler kolayca kontrolden çıkabilir, ve harcamaların
genel görünümü hızla kaybolur. Sonuç olarak, sunucusuz ve bulutun avantaj ve dezavantajlarının dikkatlice tartılması
gerekir. Şirketler kendi özel gereksinimlerini, ekipteki mevcut uzmanlığı ve buluta geçişin uzun vadeli etkilerini göz
önünde bulundurmalıdır. buluta geçişin dezavantajları. Kapsamlı bir analize dayanan bilinçli bir karar, projenin
başarısı ve kârlılığı için çok önemlidir. Projenin. Nihayetinde, geliştiricilerini yeterince desteklemek, maliyetleri
ve karmaşıklığı gerçekçi bir şekilde değerlendirmek şirketlerin sorumluluğundadır. bulutu gerçekçi bir şekilde
değerlendirmeli ve iyi yönetilen Kubernetes kümeleri gibi alternatif çözümleri göz önünde bulundurmalıdır. Şirketler net
bir strateji ve kendi ihtiyaçlarına dair sağlam bir anlayışla bulutun avantajlarından en iyi şekilde faydalanabilir.
bulut ve sunucusuz yetenekler ve illüzyonun ötesini görmek.

### İletişim

[GitHub Sorunları](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
