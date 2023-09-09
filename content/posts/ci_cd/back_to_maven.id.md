---
title: "Kembali ke Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "Pencarian yang sulit dipahami mencari kesederhanaan dan perjalanan singkat untuk menemukan kembali kekuatan dari Maven."
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# Kembali ke Maven?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

## 10 Tahun Gradle. Dalam Pencarian Kemudahan dan Perjalanan Singkat untuk Menemukan Kembali Kekuatan Maven.



### Maksimalkan Potensi Para Pengembang - Kami Membutuhkan Lebih Banyak Alat Penghemat Waktu

Tema-tema yang sering diabaikan atau jarang dibahas menarik bagi saya. Seringkali teknologi keren digunakan,
namun hampir tidak ada yang berbicara tentang masalah yang terkait dengannya.
Pengembangan sekarang ini menjadi sangat rumit.
Dengan kata-kata keren seperti "Serverless", "Low Code", "IaC", "Big Data", "Cloud", "DevOps", "You Build it You run it"
dll. para pengembang sudah memiliki lebih dari cukup tugas tambahan untuk ditangani. Lebih banyak tugas berarti, hampir tidak ada
lagi ahli dan selalu ada sesuatu yang diabaikan untuk fokus. Oleh karena itu, otomatisasi dan penghematan waktu sangat
penting. "Don't make me think" dan "Works out of the Box" sudah menjadi ciri kualitas yang baik, yang saya belum bisa lihat dalam Gradle.
Untuk jujur, Gradle bukan satu-satunya alat modern yang membuat kita bekerja, bukan mempermudahnya.

### Pencarian ilusi atas Kesederhanaan dan Otomatisasi

Sejak SOAP, saya memiliki keengganan yang sangat terhadap konfigurasi berbasis XML. Dengan Gradle, saya berharap,
menulis skrip bind akan menjadi mudah. Sayangnya, harapan dan motivasi saya semakin berkurang dari waktu ke waktu.
Gradle mengutamakan fleksibilitas dan mengorbankan otomatisasi dan kualitas. Pengembang mengikuti tren secara buta tanpa
mempertimbangkan dampaknya terhadap keandalan perangkat lunak. Untuk membuat Skrip build Gradle sederhana dan
pemeliharaan rendah, dibutuhkan disiplin yang kuat. Disiplin semacam itu sudah jarang ditemukan dalam kode sumber dan
oleh karena itu, lebih jarang lagi dalam skrip build.

### Terjemahan dan Solusi Alternatif - Ketika Skrip Build Menjadi Sebuah Tantangan

Gradle bekerja di latar belakang tidak jauh berbeda dari Maven. Oleh karena itu, beberapa terjemahan diperlukan. Fitur
seperti Katalog Dependensi, Plugin Rilis Maven, Dependabot dan banyak lagi sebenarnya adalah solusi untuk fungsi dasar
yang sudah dibawa oleh Maven. Dengan fleksibilitas Gradle, seringkali muncul konfigurasi build yang kompleks, yang sulit
untuk dirawat. Plugin Gradle sering memiliki masalah kompatibilitas, batasan atau pengembangan terbatas. Masalah ini
muncul karena sifat alamiah dari ekosistem Gradle yang terus berkembang, keanekaragaman lingkungan di mana Gradle
digunakan, dan upaya implementasi dan pemeliharaan spesifik untuk setiap plugin. Semuanya saling terhubung.

### Efek Domino dari Gradle - Skenario Mimpi Buruk di Dunia Nyata

Saya telah melihat banyak Microservices yang hanya berumur beberapa tahun dan sudah tidak dapat dipertahankan lagi karena Gradle.
Penting untuk disebutkan bahwa ini bukan pertama kalinya saya melihat hal seperti ini, dan tidak, mereka bukan
Junior Devs.

Tugas saya adalah untuk **melakukan upgrade Spring Boot 2.x ke 2.7**. Spoiler: saya menyerah setelah satu tahun
! Berikut adalah masalah-masalahnya secara singkat:

* File build Gradle membutuhkan -> Penurunan versi Java lokal saya ke 11 (WTF) (Biasanya Java
  kompatibel mundur - di sini juga ada alat pengganti seperti SdkMan...)
* Pembaruan Spring Boot membutuhkan -> Pembaruan Gradle (WTF)
* Pembaruan Gradle membutuhkan -> Pembaruan Plugin
* Pembaruan Plugin membutuhkan -> Pembaruan Groovy (WTF)
* Pembaruan Groovy membutuhkan -> Pembaruan Test-Framework dan Test (WTF)
* Pembaruan Test-Framework membutuhkan -> Pembaruan ketergantungan
* \[...]
  Selain itu, beberapa plugin tidak bekerja dengan versi Gradle yang lebih baru, beberapa tidak lagi
  dikembangkan, tidak kompatibel dengan plugin lain, hanya bekerja dengan Gradle KTS, bukan dengan Gradle Groovy, atau
  hanya memiliki batas. Bahkan plugin dari penyedia besar seperti Spring memiliki fungsi yang dibatasi dibandingkan dengan plugin Maven-nya
  . Pada akhirnya, saya memiliki file build Gradle yang keren dan singkat, yang tidak dapat dikelola dengan benar oleh siapa pun,
  bahkan oleh pengembang yang menulisnya, dan mereka masih menyukai Gradle. Saya hanya tahu sedikit yang
  memahami atau bisa menulis skrip Gradle dengan serius.

### Penemuan Kembali Kekuatan Maven - Menggunakan Kekuatan Ajaib Maven

Berikut adalah fitur favorit saya dari Maven:
Plugin dapat langsung dijalankan dan dikonfigurasi dari baris perintah tanpa harus didefinisikan terlebih dahulu.
Plus, mereka sebagian besar independen dari konfigurasi plugin lainnya.

| Perintah Contoh                        | Deskripsi                                                                                                                                                    | Link                                                                     | 
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`    | Perbarui versi - siapa yang butuh Dependabot? Ya, proyek saya telah diperbarui ke versi terbaru tanpa masalah selama bertahun-tahun, tanpa permintaan gabungan yang merepotkan | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0`  | Tetapkan versi proyek...                                                                                                                                      | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`          | Daftar dependensi dan tampilkan lisensi mereka (bahkan bisa gagal pada lisensi yang dikecualikan)                                                            | https://www.mojohaus.org/license-maven-plugin/index.html                 | 

Daftar ini bisa berlanjut selamanya. Itu entah bagaimana mengingatkan saya pada Langkah Workflow GitHub.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

### Kamu Tidak Suka XML?

Tidak masalah! Cukup tulis File Build Anda dalam `ruby`, `groovy`, `scala`, `yaml`, `atom` atau `Java`. Ekstensi Polygot
(https://github.com/takari/polyglot-maven) membuatnya mungkin. Untuk mencoba
cukup jalankan `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` dan dalam
beberapa milidetik File Build Anda sudah diterjemahkan. Sayang sekali, tidak ada penerjemah Maven <> Gradle yang
dapat diandalkan :(
Ya, Maven Build Files besar, tetapi juga sangat mudah dipahami. Perbaikan atau Debugging dapat diselesaikan dalam sekejap
saja.

### Usia hanya sebuah angka - Stabilitas dan Evolusi Mavens

Diketahui, Maven telah ada cukup lama dan estetikanya mungkin tidak sesuai dengan standar hari ini. Namun, daya tahan
Maven telah memungkinkan untuk beradaptasi dan berkembang. Maven bekerja secara independen dari proyek Anda. File build
dapat digunakan kembali dengan mudah. Plugin berjalan dalam sandbox dan independen satu sama lain dan independen dari
versi Java atau Maven. Desain ini mendorong stabilitas dan prediktabilitas dan memudahkan pengelolaan proses build yang
kompleks tanpa konflik yang tak terduga.

### Kesimpulan

Saat ini, lingkungan pengembangan dipenuhi dengan banyak tugas dan teknologi untuk pengembang. Dalam pencarian untuk
kemudahan dan otomatisasi, Gradle muncul sebagai alat pembangunan modern, tetapi membawa tantangan tersendiri keluar
dari situ. Tanpa pertanyaan, konsep Gradle itu baik! Namun, mengingat kompleksitas dan waktu yang diinvestasikan ke
dalam skrip pembuatan Gradle, muncul pertanyaan apakah tidak lebih mudah untuk memperluas Maven lagi. Dengan plugin dan
ekstensi, Maven bisa segar dan disederhanakan kapan saja. Bukankah pengembangan lebih lanjut lebih menarik dan juga
lebih berkelanjutan, daripada melompat dari satu teknologi ke teknologi berikutnya?

### Tautan

* [Berpindah Kembali dari Gradle ke maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### Kontak

[Isu GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
