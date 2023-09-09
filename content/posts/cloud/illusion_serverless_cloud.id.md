---
title: "Serverless Ilusi & Cloud"
date: 2023-05-24
author: "Nova Annabella"
slug: illusion_serverless_cloud
tags: [ Development, Serverless, Cloud, Microservices, Scalability, Architecture, Infrastructure ]
categories: [ Technology, Software, Cloud ]
description: "Tantangan dan realitas fungsi Serverless di Cloud. Wawasan berharga untuk perusahaan yang mempertimbangkan migrasi ke Cloud."
draft: false
images:
  - "/images/content/onprem_vs_cloud.png"
card: "summary_large_image"
---


# Ilusi Fungsi Serverless di Cloud

![aws_costs_twitter_1](/images/content/onprem_vs_cloud.png)

### Pendahuluan

Saya kecewa dengan seberapa sering pemasaran mengalahkan akal sehat. Banyak manajer mengeksploitasi
ahli mereka sendiri - para pengembang. Ini juga berlaku untuk migrasi ke cloud. Spoiler: Siapa pun yang perlu menghemat
uang, harus menghindari cloud. Karena kata kunci baru "Serverless" di cloud berarti: Anda mengurus
perangkat lunak, kami mengurus perangkat keras. Namun, siapa pun yang memiliki administrator yang mampu, termotivasi, dan penasaran, itu
dapat mengoperasikan Serverless sendiri (mis. [KNative](https://knative.dev)).

![aws_costs_twitter_1](/images/content/aws_costs_twitter_1.png)


### Fungsi Serverless vs Microservices:



#### Mikroservis

Sebuah mikroservis tanpa keadaan yang khas bertanggung jawab atas fungsi / domain tertentu dan dikerahkan dalam
Lingkungan orkestrasi kontainer. Lingkungan ini mengatur infrastruktur, keamanan, firewall, Logging, metrik, rahasia,
jaringan, backup dan banyak lagi. Satu keuntungan besar adalah bahwa sebuah mikroservis dapat diuji secara lokal dengan
beberapa sumber daya yang terintegrasi dan agnostik Cloud / Server (dapat digunakan di mana saja).

#### Fungsi Serverless

Sebuah lelucon kecil untuk memulai: Paradoks, tetapi benar - Fungsi Serverless sangat bergantung pada lingkungan server. :)
Fungsi Serverless yang khas juga hanya menangani fungsi/domain tertentu dan ditulis dalam
kode murni tanpa kerangka kerja
untuk menjadi lebih cepat daripada microservice (Juga latihan yang baik untuk MicroServices). Keuntungan besar
adalah bahwa fungsi Serverless dapat diskalakan secara otomatis. Namun, setiap fungsi Serverless memerlukan
sejumlah besar GlueCode untuk mendefinisikan infrastruktur - Keamanan, Firewall, Jaringan, Logging, Metrik,
Rahasia, Caching, Backup dan banyak lagi.
Oleh karena itu, fungsi sederhana seperti penyalinan file termasuk API bisa cepat mencapai 1500 baris kode (termasuk IaC).
Biaya administrasi berpindah dari administrasi ke pengembangan dalam rasio 1:N (1 ke Serverless
Fungsi). Pengetahuan dan implementasi oleh karena itu tidak lagi
terkumpul dan dapat dengan cepat menjadi tidak stabil. Ditambah dengan biaya perawatan yang meningkat.
Pengujian integratif yang sebenarnya juga jarang atau hanya dengan usaha besar terkait dengan Serverless.
Pada akhirnya, kompleksitas fungsi Serverless jauh lebih tinggi daripada microservice tunggal.
Kompleksitas yang lebih tinggi juga berarti pemeliharaan yang lebih rendah. Anggota tim baru akan merasakan kesulitan dan memerlukan jauh
lebih banyak pengetahuan sebelumnya.

### Serverless dan Cloud pada umumnya

Sebagian besar teknologi cloud tidak mutakhir. Misalnya, Node.js, Java, Python, dan bahasa atau teknologi lainnya seringkali sulit untuk diperbarui, sebagian besar hanya bisa menunggu.
Teknologi modern dan standar seperti MongoDB, MySQL, Kafka, NATS, RabbitMQ, Redis, Prometheus, InfluxDB, Grafana,
Kibana, Elastic Search, dll. baik tidak tersedia atau harganya sangat mahal.
Tanpa layanan standar seperti itu, seringkali kita merasa berada di zaman batu virtual dan menggunakan solusi yang sudah ketinggalan zaman, seperti
Webhook untuk komunikasi ke luar. Ditambah lagi, ruang gerak untuk isu seperti regulasi,
kepatuhan, privasi data, dan keandalan sangat terbatas.

Cloud seharusnya dioperasikan dengan agnostik, agar dapat cepat berpindah antara AWS, Azure, Google, On-Premise, dll. dan
bisa membandingkan biaya.
Batasan juga sering ada di cloud, yang menghasilkan solusi kreatif yang pada gilirannya meningkatkan kompleksitas.
Pengujian integrasi juga bisa menjadi mahal, karena setiap pengembang membutuhkan lingkungan pengembangan sendiri di cloud
karena banyak layanan cloud tidak bisa atau bahkan sama sekali tidak bisa diuji secara lokal.
Namun, bahkan tanpa tes, cloud tetap mahal. Sementara pada sistem On-Premise terutama
biaya perangkat keras yang dikeluarkan, di cloud perlu membayar tambahan untuk lalu lintas, beberapa layanan standar dan seringkali bahkan untuk
perpajakan yang berlipat. Selain itu, di cloud mudah kehilangan gambaran keseluruhan, karena yang penting bukan
kenyamanan pengguna, tetapi uang. Biayanya sangat tersembunyi sehingga Anda baru menyadarinya ketika sudah terlambat.

Dasar-dasar arsitektur dan infrastruktur harus ditemukan kembali di cloud dan khususnya di bidang serverless
karena implementasinya sangat bergantung pada fungsi yang tersedia.
Setiap kali saya merancang arsitektur, saya berpikir: "Ini seharusnya hanya satu layanan."

Bagi saya, Serverless adalah ide yang menarik dan dapat diskalakan dengan baik, tetapi tidak mengurangi biaya. Ini malah
memerlukan lebih banyak pengetahuan dan waktu dalam pengembangan. Serverless atau cloud memerlukan disiplin dan
pengetahuan sebelumnya.
Jika pengetahuan tentang sistem On-Premise tidak ada, tidak akan lebih mudah dengan cloud.
Bagaimana pengembang dapat mempelajari pengetahuan infrastruktur tambahan?

Saya lebih memilih cluster Kubernetes yang dikelola dengan baik daripada arsitektur cloud.
Karyawan tidak bisa diskalakan. Banyak pengembang tidak memiliki disiplin dalam menulis kode.
Sayangnya, ini berlaku untuk 80 persen dari pengembang. Jadi bagaimana pengembang tersebut kemudian dapat mengoperasikan cloud?

Penting bagi perusahaan untuk memahami secara menyeluruh tantangan dan dampak arsitektur serverless dan cloud. Ini bukan hanya memerlukan pengetahuan teknis, tetapi juga pendekatan strategis. Migrasi ke cloud yang tidak dipikirkan dengan baik dapat menyebabkan kompleksitas, biaya yang lebih tinggi, dan beban pengembang.

Secara keseluruhan, serverless di cloud adalah konsep yang menjanjikan yang harus dipertimbangkan dengan hati-hati.
Biaya, kompleksitas, pemeliharaan, dan kemampuan tim pengembangan harus diperhitungkan.
Setiap perusahaan memiliki kebutuhan dan prioritas yang berbeda. Anda harus membuat keputusan yang berdasar, apakah
Serverless di cloud adalah solusi yang tepat atau pendekatan alternatif seperti
misalnya, cluster Kubernetes yang baik adalah pilihan yang lebih baik.

Penerapan sukses dari Serverless dan Cloud Computing memerlukan kombinasi dari keahlian teknis
perencanaan strategis dan pemahaman yang jelas tentang kebutuhan bisnis. Hanya dengan cara ini dapat melihat melalui ilusi dari Serverless
dan membuat keputusan yang tepat untuk pengembangan perangkat lunak sendiri.

### Kesimpulan

Pengenalan fungsi Serverless di Cloud menjanjikan fleksibilitas, skalabilitas dan pembebanan dari
Pengembang untuk tugas-tugas infrastruktur. Namun, Anda tidak boleh terpedaya oleh ilusi ini. Pindah
ke Cloud dan penggunaan fungsi Serverless membawa sejumlah tantangan.

Pengembang harus belajar "bahasa" baru di samping pengembangan itu sendiri dan tanpa dukungan yang tepat
mengambil lebih banyak tanggung jawab.
Kompleksitas fungsi Serverless seringkali lebih tinggi dibandingkan dengan layanan Micro, karena pengembang memiliki banyak tambahan
tugas seperti definisi infrastruktur, keamanan, dan skalabilitas. Tes integratif sebenarnya adalah
sulit dan pengetahuan pra-syarat serta pengalaman untuk operasi di Cloud bahkan lebih penting.

Cloud itu sendiri membawa tantangan lebih lanjut. Banyak teknologi Cloud tidak up to date
dan penggunaan layanan standar modern bisa mahal atau bahkan tidak mungkin. Aturan regulasi, kepatuhan, dan
Perlindungan data membatasi ruang untuk bernapas. Selain itu, biaya di Cloud dapat dengan mudah keluar jalur,
dan gambaran tentang pengeluaran cepat hilang.

Secara keseluruhan, manfaat dan kerugian dari Serverless dan Cloud harus dipertimbangkan dengan hati-hati.
Perusahaan harus mempertimbangkan kebutuhan spesifik mereka, pengetahuan yang ada di tim dan dampak jangka panjang
dari migrasi ke Cloud.
Keputusan yang didasarkan pada analisis yang komprehensif sangat penting untuk keberhasilan dan rentabilitas 
dari proyek.

Akhirnya, terserah kepada perusahaan untuk mendukung pengembang mereka secara layak, mengevaluasi biaya dan kompleksitas dari
Cloud secara realistis dan pertimbangkan solusi alternatif seperti cluster Kubernetes yang dikelola dengan baik.
Dengan strategi yang jelas dan pemahaman yang mantap tentang kebutuhan mereka sendiri, perusahaan dapat memanfaatkan keuntungan dari
Cloud dan fungsi Serverless secara optimal dan melihat melalui ilusi.

### Kontak

[Isu GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
