---
title: "Ilusi Tanpa Server & Cloud"
date: 2023-05-24
author: "Nova Annabella"
slug: illusion_serverless_cloud
tags: [ Development, Serverless, Cloud, Microservices, Scalability, Architecture, Infrastructure ]
categories: [ Technology, Software, Cloud ]
description: "Tantangan dan realitas kemampuan tanpa server di cloud. Wawasan berharga bagi perusahaan yang mempertimbangkan migrasi ke cloud".
draft: false
images:
  - "/images/content/onprem_vs_cloud.png"
card: "summary_large_image"
---



# Ilusi fungsi tanpa server di awan

![aws_costs_twitter_1](/images/content/onprem_vs_cloud.png)

### Pendahuluan

Saya kecewa dengan betapa seringnya pemasaran mengalahkan akal sehat. Banyak manajer menempatkan diri mereka sendiri di
atas para ahli mereka sendiri - para pengembang. Hal ini juga berlaku untuk migrasi ke cloud. Spoiler: Jika Anda perlu
menghemat uang perlu menghemat uang harus menghindari cloud. Karena kata kunci baru "tanpa server" di cloud berarti:
Anda mengurus perangkat lunak, kami mengurus perangkat keras. Anda mengurus perangkat lunak, kami akan mengurus
perangkat kerasnya. Namun, jika Anda memiliki administrator yang cakap, termotivasi, dan penuh rasa ingin tahu, Anda
bisa juga dapat beroperasi tanpa server sendiri (misalnya [KNative] (https://knative.dev)).
![aws_costs_twitter_1](/images/content/aws_costs_twitter_1.png)

### Fungsi tanpa server vs layanan mikro:



#### Layanan Mikro

Layanan mikro tanpa kewarganegaraan yang khas menangani fungsi/domain tertentu dan digunakan dalam lingkungan orkestrasi
kontainer. Lingkungan ini menangani infrastruktur, keamanan, firewall, pencatatan, metrik, rahasia, jaringan,
pencadangan, dan lainnya. Keuntungan besarnya adalah layanan mikro dapat digunakan secara lokal dengan sedikit sumber
daya dan bersifat cloud/server agnostik (dapat digunakan di mana saja).

#### Fungsi tanpa server

Sedikit lelucon sebelumnya: Paradoks, tetapi benar - fungsi tanpa server sangat bergantung pada lingkungan server. :)
Fungsi serverless yang khas juga hanya menangani satu fungsi/domain tertentu dan ditulis dalam kode murni tanpa kerangka
kerja agar lebih cepat daripada layanan mikro. kode agar lebih cepat daripada layanan mikro (juga merupakan latihan yang
baik untuk Layanan Mikro). Sebuah besar adalah bahwa fungsi-fungsi Serverless berskala secara otomatis. Namun, setiap
fungsi tanpa server membutuhkan a sejumlah besar GlueCode untuk mendefinisikan infrastruktur - keamanan, firewall,
jaringan, pencatatan, metrik, rahasia, caching, cadangan, dan banyak lagi. Oleh karena itu, fungsi sederhana seperti
menyalin file termasuk API dapat dengan cepat melibatkan 1500 baris kode (termasuk IaC). dapat dilibatkan. Biaya
administrasi bergeser dari administrasi ke pengembangan dengan rasio 1: N (1 ke Serverless). fungsi). Oleh karena itu,
pengetahuan dan implementasinya tidak lagi dibundel dan dapat dengan cepat menjadi tidak stabil. Selain itu, ada
peningkatan biaya pemeliharaan. Pengujian integratif yang sebenarnya juga jarang dilakukan dengan serverless, atau hanya
mungkin dilakukan dengan usaha keras. Pada akhirnya, kompleksitas fungsi tanpa server secara signifikan lebih tinggi
daripada layanan mikro tunggal. Kompleksitas yang lebih tinggi juga berarti pemeliharaan yang lebih rendah. Anggota tim
baru memiliki waktu yang lebih sulit dan membutuhkan lebih banyak pengetahuan sebelumnya.

### Tanpa server dan cloud secara umum

Sebagian besar teknologi cloud tidak mutakhir. Sebagai contoh, Node.js, Java, Python, dan bahasa atau teknologi lainnya
bahasa atau teknologi sering kali tidak mudah untuk diperbarui, biasanya hanya menunggu saja. Bahkan teknologi yang
modern dan standar seperti MongoDB, MySQL, Kafka, NATS, RabbitMQ, Redis, Prometheus, InfluxDB, Grafana, Kibana, Elastic
Search, dll. tidak tersedia atau terlalu mahal. Tanpa layanan standar seperti itu, seseorang sering kali berada di zaman
batu virtual dan menggunakan solusi yang sudah ketinggalan zaman, misalnya webhook untuk komunikasi eksternal. Selain
itu, ruang untuk bermanuver pada masalah seperti regulasi, kepatuhan, perlindungan data, dan keamanan kegagalan sangat
terbatas. Oleh karena itu, cloud harus dijalankan secara agnostik agar dapat beralih dengan cepat antara AWS, Azure,
Google, on-premise, dll. dan untuk membandingkan biaya. Keterbatasan juga umum terjadi di cloud, yang mengarah pada
solusi kreatif, yang pada gilirannya meningkatkan kompleksitas. meningkat. Pengujian integratif juga bisa menjadi mahal,
karena setiap pengembang membutuhkan lingkungan pengembangan mereka sendiri di cloud karena banyak layanan cloud yang
hampir tidak atau sama sekali tidak dapat diuji secara lokal. Tetapi bahkan tanpa pengujian pun, cloud sudah mahal.
Sedangkan dengan sistem on-premise, hal ini terutama biaya perangkat keras, di cloud Anda juga harus membayar lalu
lintas, beberapa layanan standar dan bahkan sering kali untuk beberapa dan seringkali bahkan untuk beberapa pajak.
Selain itu, mudah untuk kehilangan jejak hal-hal di cloud, karena ini bukan tentang ini bukan tentang keramahan
pengguna, tetapi tentang uang. Biayanya sangat tersembunyi sehingga Anda baru menyadarinya ketika sudah terlambat. sudah
terlambat. Dasar-dasar arsitektur dan infrastruktur harus diciptakan kembali di cloud dan terutama di serverless harus
diciptakan kembali, karena implementasinya sangat bergantung pada fitur yang tersedia. Setiap kali saya merancang
arsitektur, saya berpikir: "Ini bisa saja menjadi layanan tunggal". bisa saja". Bagi saya, serverless adalah ide yang
menarik dan skalanya bagus, tetapi tidak mengurangi biaya. Sebaliknya Sebaliknya, hal ini membutuhkan lebih banyak
pengetahuan dan waktu dalam pengembangannya. Serverless atau cloud membutuhkan disiplin dan pengetahuan sebelumnya. Jika
pengetahuan tersebut tidak ada pada sistem on-premise, maka tidak akan lebih mudah dengan cloud. Bagaimana cara
pengembang memperoleh pengetahuan infrastruktur tambahan? Saya lebih memilih cluster Kubernetes yang dikelola dengan
baik daripada arsitektur cloud. Orang-orangnya tidak berskala. Banyak pengembang yang tidak disiplin dalam menulis kode.
Sayangnya, hal ini terjadi pada 80 persen pengembang. Jadi, bagaimana para pengembang ini dapat menjalankan cloud?
cloud? Penting bagi organisasi untuk memahami sepenuhnya tantangan dan implikasi dari arsitektur tanpa server dan
cloud. memahami sepenuhnya tantangan dan implikasi dari arsitektur tanpa server dan cloud. Hal ini tidak hanya
membutuhkan pengetahuan teknis, tetapi juga pendekatan strategis. A Migrasi ke cloud yang tidak dipertimbangkan dengan
baik dapat menyebabkan kerumitan, biaya yang lebih tinggi, dan membebani pengembang. Singkatnya, tanpa server di cloud
adalah konsep yang menjanjikan, tetapi harus dipertimbangkan dengan hati-hati. harus dipertimbangkan dengan hati-hati.
Biaya, kompleksitas, pemeliharaan, dan keterampilan tim pengembangan perlu dipertimbangkan. harus diperhitungkan. Setiap
perusahaan memiliki persyaratan dan prioritas yang berbeda. Keputusan yang tepat harus dibuat mengenai apakah Serverless
di cloud adalah solusi yang tepat atau apakah pendekatan alternatif seperti misalnya Kubernetes Cluster adalah pilihan
yang lebih baik. Keberhasilan penerapan komputasi tanpa server dan cloud membutuhkan kombinasi keahlian teknis
perencanaan strategis dan pemahaman yang jelas tentang persyaratan bisnis. Hanya dengan begitu ilusi tanpa server dapat
dan membuat keputusan yang tepat untuk pengembangan perangkat lunak Anda sendiri.

### Fazit

Pengenalan fungsi tanpa server di cloud menjanjikan fleksibilitas, skalabilitas, dan keringanan dari tugas-tugas
infrastruktur. membebaskan pengembang dari tugas-tugas infrastruktur. Namun, jangan sampai kita dibutakan oleh ilusi
ini. Perpindahan pindah ke cloud dan penggunaan fungsi tanpa server membawa sejumlah tantangan. Pengembang harus
mempelajari "bahasa" baru selain pengembangan yang sebenarnya dan mengambil lebih banyak tanggung jawab tanpa dukungan
yang sesuai. mengambil lebih banyak tanggung jawab. Kompleksitas fungsi tanpa server sering kali lebih tinggi daripada
layanan mikro, karena pengembang harus melakukan banyak tugas tambahan, seperti pengembang harus melakukan banyak tugas
tambahan seperti definisi infrastruktur, keamanan, dan penskalaan. Pengujian integratif yang sebenarnya adalah sulit dan
pengetahuan serta pengalaman sebelumnya untuk operasi bahkan lebih penting di cloud. Awan itu sendiri membawa tantangan
lebih lanjut. Banyak teknologi cloud yang tidak mutakhir dan menggunakan layanan modern yang siap pakai bisa jadi mahal
atau bahkan tidak mungkin. Persyaratan peraturan, kepatuhan dan perlindungan data membatasi ruang lingkup. Selain itu,
biaya di cloud dengan mudah menjadi tidak terkendali, dan gambaran umum biaya dengan cepat hilang. Secara keseluruhan,
keuntungan dan kerugian dari serverless dan cloud perlu dipertimbangkan dengan cermat. Perusahaan harus mempertimbangkan
kebutuhan spesifik mereka, keahlian yang ada dalam tim, dan efek jangka panjang dari migrasi ke cloud. dari migrasi ke
cloud. Keputusan yang tepat berdasarkan analisis yang komprehensif sangat penting untuk keberhasilan dan profitabilitas
proyek. dari proyek tersebut. Pada akhirnya, terserah perusahaan untuk mendukung pengembang mereka secara memadai,
menilai biaya dan kompleksitas cloud secara realistis dan mempertimbangkan solusi alternatif seperti cluster Kubernetes
yang dikelola dengan baik. Dengan strategi yang jelas dan pemahaman yang baik tentang kebutuhan mereka sendiri,
perusahaan dapat memanfaatkan manfaat dari cloud dan kemampuan tanpa server dan melihat melalui ilusi.

### Kontak

[Masalah GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
