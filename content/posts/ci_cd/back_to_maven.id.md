---
title: "Kembali ke Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "Cari yang sulit untuk dimengerti tentang kesederhanaan dan perjalanan singkat untuk menemukan kembali kekuatan Maven."
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# Kembali ke Maven?

```
[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)


``` 

diterjemahkan menjadi:

```
[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)


```

## 10 Tahun Gradle. Mencari Kemudahan dan Perjalanan Singkat Menuju Penemuan Kembali Keunggulan dari Maven.

Tidak ada teks tampilan di sini.

### Maksimalkan Potensi Pengembang - Kami Membutuhkan Lebih Banyak Alat yang Menghemat Waktu

Topik-topik yang sering terlewatkan atau jarang dibahas menarik minat saya. Sering kali teknologi canggih digunakan,
tapi hampir tidak ada yang membicarakan masalah yang terkait.
Pengembangan saat ini telah menjadi sangat rumit.
Dengan buzzword keren seperti "Serverless", "Low Code", "IaC", "Big Data", "Cloud", "DevOps", "You Build it You run it"
dan sebagainya, pengembang sudah memiliki lebih dari cukup tugas tambahan untuk dihadapi. Lebih banyak tugas berarti hampir tidak ada
ahli dan ia akan selalu mengambil sesuatu untuk diabaikan. Oleh karena itu, otomatisasi dan penghematan waktu sangat penting. "Jangan pikirkan saya" dan "Bekerja langsung" sudah menjadi tanda-tanda kualitas yang baik, yang belum bisa saya lihat di Gradle. Untuk adilnya, Gradle bukanlah satu-satunya alat modern yang membuat pekerjaan kita sulit, bukan mudah.

### Pencarian ilusif akan Kesederhanaan dan Otomatisasi

Sejak SOAP, saya memiliki ketidak sukaan yang sangat mendalam terhadap konfigurasi yang berbasis XML. Saya berharap
dengan Gradle, menulis skrip ikatan menjadi sangat mudah. Namun, semakin lama harapan dan motivasi saya semakin
mengecil. Gradle mengejar fleksibilitas dan mengorbankan otomatisasi dan kualitas. Pengembang mengikuti tren tanpa
mempertimbangkan dampaknya pada keandalan perangkat lunak. Untuk membuat skrip Gradle Build mudah dan mudah dipelihara,
diperlukan disiplin yang kuat. Disiplin seperti itu jarang ditemukan dalam kode sumber dan oleh karena itu lebih jarang
ditemukan dalam skrip Build.

### Terjemahan dan Solusi - Ketika Build-Skrip Menjadi Tantangan

Gradle bekerja di balik layar tidak jauh berbeda dengan Maven. Oleh karena itu, beberapa terjemahan diperlukan. Fitur seperti Dependency Catalog, Maven Release Plugin, Dependabot, dan banyak lagi sebenarnya adalah workarounds untuk fitur dasar yang sudah dimiliki oleh Maven. Dengan fleksibilitas dari Gradle, seringkali menyebabkan konfigurasi build yang kompleks dan sulit untuk dipelihara. 

Plugins Gradle sering mengalami masalah kompatibilitas, batasan atau pengembangan terbatas. Masalah-masalah ini muncul karena sifat berkembangnya ekosistem Gradle, keanekaragaman lingkungan di mana Gradle digunakan, dan tuntutan implementasi dan perawatan khusus untuk setiap plugin. Semuanya saling terhubung.

### Efek Domino dari Gradle - Suatu Skenario Mimpi Buruk di Dunia Nyata

Saya telah melihat banyak Microservices yang baru berumur beberapa tahun dan sudah tidak dapat dipelihara lagi karena Gradle. Penting untuk disebutkan bahwa ini bukan pertama kalinya saya melihat hal seperti ini, dan tidak, itu bukan dari Junior Devs.

Tugas saya adalah untuk melakukan upgrade Spring Boot 2.x ke 2.7. Spoiler: Saya menyerah setelah satu tahun! Masalahnya di antaranya:

* File Build-Gradle memerlukan -> downgrade versi Java lokal saya ke 11 (WTF) (Biasanya Java backwards compatible - ada juga alat workaround seperti SdkMan...)
* Pembaruan Spring Boot memerlukan -> Pembaruan Gradle (WTF)
* Pembaruan Gradle memerlukan -> Pembaruan Plugin
* Pembaruan Plugin memerlukan -> Pembaruan Groovy (WTF)
* Pembaruan Groovy memerlukan -> Pembaruan Kerangka Uji dan Pembaruan Uji (WTF)
* Pembaruan Kerangka Uji memerlukan -> Pembaruan Ketergantungan
* \[...]
  Selain itu, beberapa plugin tidak berfungsi dengan versi Gradle yang lebih baru, beberapa tidak lagi dikembangkan, tidak kompatibel dengan plugin lain, hanya berfungsi dengan Gradle KTS, tidak dengan Gradle Groovy, atau memiliki batasan sederhana. Bahkan plugin dari vendor besar seperti Spring mempunyai fungsi terbatas dibandingkan dengan plugin Maven mereka. Pada akhirnya, saya memiliki file pembangunan Gradle yang keren dan pendek, yang tidak bisa dipelihara dengan benar oleh siapa pun, bahkan oleh para pengembang yang menulisnya, dan mereka masih mencintai Gradle. Saya hanya mengenal sedikit orang yang benar-benar memahami atau dapat menulis script Gradle secara serius.

### Penemuan Kembali Kekuatan Maven - Memanfaatkan Sihir Maven

Berikut adalah fitur favorit saya dari Maven:
Plugin dapat langsung dimulai dan dikonfigurasi dari baris perintah tanpa harus didefinisikan terlebih dahulu. Selain itu, mereka secara besar-besaran independen dari konfigurasi Plugin lainnya.

| Perintah Contoh | Deskripsi | Tautan |
| --- | --- | --- |
| `mvn versions:use -latest-versions` | memperbarui versi - Siapa yang membutuhkan Dependabot? Ya, proyek-proyek saya telah diperbarui ke versi terbaru selama bertahun-tahun tanpa permintaan penggabungan yang merepotkan. | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0` | Menetapkan versi proyek ... | https://www.mojohaus.org/versions/versions-maven-plugin/index.html |
| `mvn license:add-third-party` | Daftar dependensi dan menampilkan lisensinya (bahkan dapat gagal pada lisensi yang dikecualikan) | https://www.mojohaus.org/license-maven-plugin/index.html |

Daftar ini bisa terus berlanjut. Ini mengingatkan saya pada Langkah-langkah Alur Kerja GitHub.

![maven_plugin_command_line_args] (/images/content/maven_plugin_command_line_args.png)

### Kamu Tidak Suka XML?

Tidak masalah! Tulis saja Build File kamu dalam `ruby`, `groovy`, `scala`, `yaml`, `atom`, atau `Java`. Ekstensi Polygot (https://github.com/takari/polyglot-maven) membuatnya menjadi mungkin. Untuk mencobanya, cukup jalankan `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` dan dalam beberapa milidetik, Build File kamu akan terjemahkan. Sayangnya, tidak ada terjemahan Maven <> Gradle yang dapat diandalkan :( Ya, Build File Maven memang besar, tapi sangat mudah dipahami. Penyesuaian atau debugging dapat diselesaikan dengan cepat.

### Usia Hanya Sebuah Angka - Stabilitas dan Evolusi Mavens

Diberikan, Maven sudah ada sejak lama dan estetikanya mungkin tidak sesuai dengan standar saat ini. Namun,
keberlangsungan Maven telah memungkinkannya untuk beradaptasi dan berkembang. Maven berfungsi secara mandiri dari proyek
Anda. File build dapat dengan mudah digunakan kembali. Plugin dijalankan di dalam sandbox dan mandiri satu sama lain dan
mandiri dari versi Java atau Maven. Desain ini mendorong stabilitas dan prediktabilitas dan membuat mudah mengelola
proses build kompleks tanpa konflik yang tidak diinginkan.

### Kesimpulan

Saat ini, lingkungan pengembangan penuh dengan tugas dan teknologi yang membebani para pengembang. Untuk mencari kesederhanaan dan otomatisasi, Gradle muncul sebagai alat bangun modern, tetapi membawa tantangan tersendiri. Tidak diragukan lagi, konsep Gradle baik! Namun, mengingat kompleksitas dan waktu yang diinvestasikan dalam skrip bangun Gradle, muncul pertanyaan apakah tidak lebih mudah untuk memperluas Maven. Dengan plugin dan ekstensi, Maven dapat di-refresh dan disederhanakan kapan saja. Apakah pengembangan lebih menarik dan juga berkelanjutan daripada melompat dari satu teknologi ke teknologi lainnya?

### Tautan

* [Kembali ke Maven dari Gradle](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### Kontak

[Isu GitHub] (https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).```
