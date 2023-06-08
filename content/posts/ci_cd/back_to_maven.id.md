---
title: "Kembali ke Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "Menerjemahkan teks Markdown ke bahasa Indonesia:

```
Mencari kesederhanaan yang sulit ditemukan dan perjalanan singkat untuk mengingat kembali kekuatan Maven. 
```"
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# Kembali ke Maven?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/kembali-dari-gradle-ke-maven/)

## 10 Tahun Gradle. Mencari Kemudahan dan Perjalanan Singkat Menuju Penemuan Kembali Keunggulan Maven.

Saya minta maaf, tetapi perintah "`` ` ```" tidak dapat diterjemahkan ke dalam bahasa Indonesia karena hanya digunakan
untuk memberikan format dan tidak memiliki arti atau makna tertentu dalam bahasa Indonesia. Mohon maaf atas
ketidaknyamanannya.

### Maksimalkan Potensi Pengembang - Kami Membutuhkan Lebih Banyak Alat yang Hemat Waktu

Topik yang sering terabaikan atau jarang dibahas menarik minat saya. Seringkali teknologi keren digunakan, namun sedikit yang membicarakan masalah yang terkait dengan hal itu. Pengembangan telah menjadi sangat rumit pada masa kini. Dengan buzzword keren seperti "Serverless", "Low Code", "IaC", "Big Data", "Cloud", "DevOps", "You Build it You run it", dan sebagainya, pengembang telah memiliki cukup banyak tugas tambahan untuk dihadapi. Lebih banyak tugas berarti banyak ahli yang kurang tersedia dan selalu ada yang diabaikan dalam fokus. Oleh karena itu, otomatisasi dan penghematan waktu sangat penting. "Don't make me think" dan "Works out of the Box" adalah tanda kualitas yang baik, yang belum terlihat pada Gradle. Untuk adil, Gradle bukanlah satu-satunya alat modern yang membuat pekerjaan kita sulit, bukan mudah.

### Pencarian Illusif untuk Kesederhanaan dan Otomatisasi

Sejak SOAP, saya memiliki rasa tidak suka yang kuat terhadap konfigurasi berbasis XML. Dengan Gradle, saya berharap
menulis skrip binding akan menjadi mudah. Namun sayangnya, harapan dan motivasi saya semakin menurun dari waktu ke
waktu. Gradle mengejar fleksibilitas dan mengorbankan otomatisasi dan kualitas. Pengembang mengikuti tren tanpa
memperhatikan dampaknya pada keandalan perangkat lunak. Untuk menjaga skrip build Gradle sederhana dan mudah dipelihara,
diperlukan disiplin yang kuat. Disiplin seperti itu jarang ditemukan dalam kode sumber dan oleh karena itu sangat jarang
ditemukan dalam skrip build.

### Terjemahan dan Workaround - Ketika Skrip Build menjadi Tantangan

Gradle bekerja di latar belakang tidak jauh berbeda dengan Maven. Oleh karena itu, beberapa terjemahan diperlukan. Fitur-fitur seperti Katalog Dependency, Plugin Rilis Maven, Dependabot, dan banyak lagi sebenarnya adalah workarounds untuk fungsi dasar yang dimiliki oleh Maven. Dengan fleksibilitas Gradle, sering kali terjadi konfigurasi Build yang kompleks dan sulit untuk dipelihara. 

Plugin Gradle seringkali memiliki masalah kompatibilitas, batasan, atau pembatasan pengembangan. Masalah-masalah ini disebabkan oleh sifat evolusi dari ekosistem Gradle, keragaman lingkungan di mana Gradle digunakan, dan kompleksitas implementasi dan pemeliharaan untuk setiap plugin. Semuanya saling terhubung.

### Dampak Domino Gradle - Skenario Mimpi Buruk di Dunia Nyata

Saya telah melihat banyak Microservices yang berusia hanya beberapa tahun dan sudah tidak dapat dipelihara lagi karena Gradle. Penting untuk dicatat bahwa ini bukan kali pertama saya melihat sesuatu seperti itu, dan tidak, itu bukan Junior Devs.

**Tugas saya adalah melakukan upgrade Spring Boot 2.x ke 2.7**. Spoiler: Saya menyerah setelah setahun! Masalahnya dalam beberapa poin:

* File Build Gradle membutuhkan -> menurunkan versi Java lokal saya menjadi 11 (WTF) (biasanya Java mendukung kompatibilitas ke bawah - ada juga alat Workaround seperti SdkMan ...)
* Pembaruan Spring Boot membutuhkan -> Pembaruan Gradle (WTF)
* Pembaruan Gradle membutuhkan -> Pembaruan Plugin
* Pembaruan Plugin membutuhkan -> Pembaruan Groovy (WTF)
* Pembaruan Groovy membutuhkan -> Pembaruan Kerangka Kerja Uji dan Pembaruan Uji (WTF)
* Pembaruan Kerangka Kerja Uji membutuhkan -> pembaruan ketergantungan
* \[...]
  Selain itu, beberapa plugin tidak berfungsi dengan versi Gradle yang lebih baru, beberapa tidak lagi dikembangkan, tidak
  kompatibel dengan plugin lain, hanya berfungsi dengan Gradle KTS, bukan Gradle Groovy, atau memiliki batasan. Bahkan
  plugin dari vendor besar seperti Spring memiliki fungsi terbatas dibandingkan dengan plugin Maven mereka. Pada akhirnya,
  saya memiliki file Build Gradle yang bagus dan pendek, yang tidak bisa dipelihara dengan benar oleh siapa pun, bahkan
  oleh para pengembang yang menulisnya, dan mereka masih suka Gradle. Saya hanya tahu sedikit orang yang benar-benar memahami atau dapat menulis skrip Gradle dengan serius.

### Penemuan Kembali Kekuatan Maven - Memanfaatkan Sihir Maven

Berikut adalah fitur-fitur favorit saya dari Maven:
Plugin dapat langsung dimulai dan dikonfigurasi dari baris perintah tanpa harus didefinisikan sebelumnya. Selain itu, mereka sebagian besar independen dari konfigurasi plugin lainnya.

| Perintah Contoh                       | Deskripsi                                                                                                                                                           | Link                                                                    | 
|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`   | Memperbarui versi - siapa yang perlu Dependabot? Ya, proyek-proyek saya telah diperbarui ke versi terbaru selama bertahun-tahun tanpa permintaan penggabungan yang menjengkelkan | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0` | Menetapkan versi proyek...                                                                                                                                          | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`         | Menampilkan daftar dependensi dan lisensi mereka (dapat gagal bahkan jika lisensi telah dikecualikan)                                                               | https://www.mojohaus.org/license-maven-plugin/index.html                | 

Daftar ini bisa terus berlanjut. Ini somehow mengingatkan saya pada Langkah-langkah Alur Kerja GitHub.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

### Kamu Tidak Suka XML?

Tidak masalah! Hanya tulis Build File Anda dalam `ruby`, `groovy`, `scala`, `yaml`, `atom` atau `Java`. Ekstensi Polyglot (https://github.com/takari/polyglot-maven) membuatnya mungkin. Untuk mencoba, cukup jalankan `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` dan dalam beberapa milidetik Build File Anda akan diterjemahkan. Sayangnya, tidak ada penerjemah Maven <> Gradle yang dapat diandalkan :( Ya, Build Files Maven besar, tetapi juga sangat mudah dipahami. Penyesuaian atau debugging dapat dilakukan dengan mudah.

### Usia Hanya Sebuah Angka - Stabilitas dan Evolusi di Maven

Terlebih mengakui, bahwa Maven telah ada sejak lama dan estetikanya mungkin tidak sesuai dengan standar saat ini. Namun,
keberlanjutan Maven telah memungkinkannya untuk beradaptasi dan berkembang. Maven bekerja secara independen dari proyek
Anda. Berkas bangunan dapat dengan mudah digunakan kembali. Plugin berjalan dalam Sandbox dan independen satu sama lain
serta independen dari versi Java atau Maven. Desain ini mempromosikan stabilitas dan prediktabilitas dan membuat itu
mudah untuk mengelola proses pembangunan yang kompleks tanpa konflik yang tidak terduga.

### Kesimpulan

Saat ini, lingkungan pengembangan telah kebanjiran tugas dan teknologi bagi para pengembang. Dalam mencari kemudahan dan
otomatisasi, Gradle muncul sebagai alat build modern, namun membawa tantangan sendiri. Tidak diragukan lagi, konsep
Gradle sangat bagus! Namun, mengingat kompleksitas dan waktu yang diinvestasikan dalam skrip build Gradle, muncul
pertanyaan apakah tidak lebih mudah untuk memperluas Maven. Dengan plugin dan ekstensi, Maven dapat dimutakhirkan dan
disederhanakan kapan saja. Apakah pengembangan lebih menarik dan juga berkelanjutan daripada melompat dari satu
teknologi ke teknologi berikutnya?

### Tautan

* [Kembali dari Gradle ke Maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### Kontak

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
