---
title: "Kembali ke Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "Pencarian yang sulit dipahami akan kesederhanaan dan perjalanan singkat untuk menemukan kembali kekuatan Maven".
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---



# Kembali ke Maven?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

## 10 tahun Gradle. Mencari kelegaan dan perjalanan singkat untuk menemukan kembali kekuatan Maven.



### Memaksimalkan potensi pengembang - kami membutuhkan lebih banyak alat bantu yang menghemat waktu

Topik-topik yang sering diabaikan atau jarang dibahas menarik minat saya. Sering kali ada teknologi keren yang
digunakan, tetapi hampir tidak ada yang membicarakan masalah yang terkait dengannya. Pengembangan telah menjadi sangat
mahal akhir-akhir ini. Dengan kata kunci keren seperti "tanpa server", "kode rendah", "IaC", "data besar", "cloud",
"DevOps", "Anda yang membuat, Anda yang menjalankan", dll., para pengembang sudah merasa cukup. dll., pengembang sudah
memiliki lebih dari cukup tugas tambahan untuk ditangani. Lebih banyak tugas berarti hampir tidak ada ahli dan ada
sesuatu yang selalu terabaikan untuk fokus. Itulah mengapa otomatisasi dan penghematan waktu sangat penting. "Jangan
membuat saya berpikir" dan "Bekerja di luar kotak" sudah merupakan fitur berkualitas baik yang belum saya lihat di
Gradle. belum bisa melihat. Sejujurnya, Gradle bukan satu-satunya alat modern yang membuat pekerjaan kita menjadi lebih
mudah. membuatnya lebih mudah.

### Pencarian ilusi untuk kesederhanaan dan otomatisasi

Sejak SOAP, saya memiliki keengganan yang mengakar terhadap konfigurasi berbasis XML. Dengan Gradle, saya berharap bahwa
menulis skrip pengikatan akan sangat mudah. Sayangnya, harapan dan motivasi saya berkurang berkurang dari waktu ke
waktu. Gradle mengupayakan fleksibilitas dan mengorbankan otomatisasi dan kualitas untuk itu. Pengembang secara membabi
buta mengikuti tren pengembang secara membabi buta mengikuti tren tanpa memperhatikan dampaknya terhadap keandalan
perangkat lunak. Untuk membuat Gradle membangun skrip yang sederhana dan pemeliharaan yang rendah membutuhkan disiplin
yang kuat. Kedisiplinan seperti itu sudah jarang terjadi di kode sumber dan oleh karena itu lebih jarang lagi dalam
skrip build.

### Terjemahan dan solusi - Ketika membangun skrip menjadi sebuah tantangan

Gradle tidak bekerja jauh berbeda di latar belakang daripada Maven. Oleh karena itu, beberapa terjemahan diperlukan.
Fitur-fitur seperti Katalog Ketergantungan, Plugin Rilis Maven, Dependabot, dan banyak lagi sebenarnya adalah solusi
untuk dasar yang sudah dibawa oleh Maven. Dengan fleksibilitas Gradle, sering kali muncul konfigurasi build yang
kompleks, yang sulit untuk dipelihara. Plugin Gradle sering kali memiliki masalah kompatibilitas, batasan, atau kemajuan
yang terbatas. Masalah-masalah ini muncul karena sifat ekosistem Gradle yang terus berkembang, keragaman lingkungan
tempat Gradle berada digunakan, dan upaya implementasi dan pemeliharaan khusus yang diperlukan untuk setiap plugin.
Semuanya saling berhubungan.

### Efek domino Gradle - Skenario mimpi buruk di dunia nyata

Saya telah melihat banyak layanan mikro yang baru berumur beberapa tahun dan sudah tidak dapat dipertahankan lagi karena
Gradle. karena Gradle. Penting untuk disebutkan bahwa ini bukan pertama kalinya saya melihat hal seperti ini, dan tidak,
mereka bukan Junior Devs. Tugas saya adalah melakukan upgrade Spring Boot 2.x ke 2.7**. Spoiler: Saya menyerah setelah
satu tahun Saya menyerah! Masalahnya secara singkat: * File build Gradle membutuhkan -> Turunkan versi Java lokal saya
ke 11 (WTF) (Biasanya Java adalah  kompatibel ke bawah - sekali lagi, ada alat bantu untuk mengatasi masalah ini
seperti SdkMan...) * Pembaruan Spring Boot membutuhkan -> Pembaruan Gradle (WTF) * Pembaruan Gradle membutuhkan ->
Pembaruan plugin * Pembaruan plugin membutuhkan -> pembaruan Groovy (WTF) * Pembaruan Groovy membutuhkan -> Pembaruan
kerangka kerja pengujian dan pengujian (WTF) * Pembaruan kerangka kerja pengujian membutuhkan -> Pembaruan
ketergantungan. * \[...]  Selain itu, beberapa plugin tidak bekerja dengan versi Gradle yang lebih baru, beberapa tidak
lagi dikembangkan, beberapa tidak kompatibel dengan versi Gradle lainnya, beberapa tidak lagi dikembangkan, beberapa
tidak kompatibel dengan versi Gradle lainnya.  tidak kompatibel dengan plugin lain, hanya bekerja dengan Gradle KTS,
bukan dengan Gradle Groovy, atau hanya memiliki  hanya memiliki batasan. Bahkan plugin dari vendor besar seperti Spring
memiliki fungsionalitas yang terbatas dibandingkan dengan plugin Maven mereka.  Fungsionalitas yang terbatas. Saya
berakhir dengan file build Gradle yang keren dan pendek yang tidak bisa dipelihara oleh siapa pun,  bahkan pengembang
yang menulisnya, dan mereka masih menyukai Gradle. Saya hanya mengenal sedikit orang yang  memahami skrip Gradle dengan
serius pelaku yang menulisnya.

### Menemukan Kembali Kekuatan Maven - Memanfaatkan Keajaiban Maven

Berikut ini adalah fitur favorit saya dari Maven: Plugin bisa dimulai dan dikonfigurasi langsung dari baris perintah
tanpa harus mendefinisikannya terlebih dahulu. perlu didefinisikan. Selain itu, plugin ini sebagian besar tidak
bergantung pada konfigurasi plugin lain. | Contoh Perintah | Deskripsi | Tautan | |------------------------------------
---|--------------------------------------------------------------------------------------------------------------------
-------------------------------------------------|----------------------------------------------------------------------
----| | `mvn versions:use -latest-versions` | Perbarui versi - siapa yang membutuhkan Dependabot? Ya, proyek saya telah
diperbarui ke versi terbaru selama bertahun-tahun tanpa masalah dan tanpa permintaan penggabungan yang mengganggu |
https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html | | `mvn versions:set -DnewVersion=1.0.0` |
Tetapkan versi proyek...
| https://www.mojohaus.org/versions/versions-maven-plugin/index.html | | `mvn license:add-third-party` | Membuat daftar
dependensi dan menampilkan lisensinya (bisa gagal meskipun lisensinya tidak disertakan) |
https://www.mojohaus.org/license-maven-plugin/index.html | Daftar ini bisa berlanjut selamanya. Ini mengingatkan saya
pada Langkah-langkah Alur Kerja GitHub.
![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

### Anda tidak menyukai XML?

Tidak masalah! Tulis saja berkas build Anda dalam `ruby`, `groovy`, `scala`, `yaml`, `atom`, atau `Java`. Ekstensi
Polygot Extension (https://github.com/takari/polyglot-maven) memungkinkan hal tersebut. Untuk mencobanya cukup jalankan
`mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` dan dalam beberapa
milidetik, hasil kompilasi Anda akan menjadi milidetik file build Anda telah diterjemahkan. Sangat disayangkan tidak ada
penerjemah Maven <> Gradle yang dapat diandalkan. :( Ya, berkas build Maven memang besar, tetapi juga sangat mudah
dimengerti. Perbaikan atau debugging dilakukan dalam waktu singkat. Selesai.

### Usia hanyalah sebuah angka - Stabilitas dan evolusi Maven

Harus diakui, Maven sudah ada sejak lama dan estetikanya mungkin tidak memenuhi standar masa kini. Namun, umur panjang
Maven telah memungkinkannya untuk beradaptasi dan berevolusi. Maven bekerja secara independen dari proyek Anda. File
yang sudah dibuat dapat dengan mudah digunakan kembali. Plugin berjalan di dalam sandbox dan tidak bergantung satu sama
lain dan tidak bergantung pada versi Java atau Maven. Desain ini meningkatkan stabilitas dan prediktabilitas dan
membuatnya mudah untuk mengelola proses pembuatan yang kompleks tanpa konflik.

### Fazit

Saat ini, lingkungan pengembangan dipenuhi dengan banyak tugas dan teknologi untuk pengembang. Dalam pencarian untuk
kesederhanaan dan otomatisasi, Gradle telah muncul sebagai alat pembuatan modern, tetapi telah membawa tantangannya
sendiri tantangannya sendiri. Tidak diragukan lagi, konsep Gradle memang bagus! Tetapi mengingat kompleksitas dan waktu
yang diinvestasikan dalam skrip build Gradle, muncul pertanyaan apakah tidak lebih sederhana untuk memperluas Maven.
diperpanjang. Dengan plugin dan ekstensi, Maven dapat selalu disegarkan dan disederhanakan. Bukankah Bukankah
pengembangan lebih lanjut akan jauh lebih menarik dan juga lebih berkelanjutan daripada melompat dari satu teknologi ke
teknologi berikutnya?

### Tautan

* [Pindah Kembali dari Gradle ke maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### Kontak

[Masalah GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
