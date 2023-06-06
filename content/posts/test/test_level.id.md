---
title: "Menguji level: Menemukan keseimbangan yang tepat"
date: 2023-05-31
author: "Nova Annabella"
slug: test_level
tags: [ Testing, Software Testing, Test Levels, Mock Tests, Unit Tests, Integration Tests, Component Tests, Contract Tests, End-to-End Tests ]
categories: [ Technology, Software Development, Quality Assurance ]
description: "Menemukan keseimbangan yang tepat dalam memilih tingkat pengujian yang sesuai untuk pengujian perangkat lunak."
draft: false
images:
  - "/images/content/martin_fowler_testing.png"
card: "summary_large_image"
---


# Tingkat pengujian: Menemukan keseimbangan yang tepat

[![testebenen](/images/content/martin_fowler_testing.png)](https://martinfowler.com/articles/microservice-testing/)

### Pendahuluan

Topik pengujian tampaknya masih merupakan wilayah yang belum dipetakan dengan banyak ruang untuk interpretasi.
Tradisional tradisional telah dipertanyakan dan piramida pengujian baru telah muncul. Menurut pendapat saya, tidak perlu
ada piramida tes, tetapi pemahaman yang jelas tentang apa yang perlu diuji. Tes di tingkat yang lebih rendah sering kali
kurang bermakna. Fokusnya harus terutama pada pengujian perilaku untuk memastikan bahwa API atau UI berfungsi seperti
yang diinginkan. Gambaran umum yang komprehensif tentang jenis pengujian yang mungkin dapat ditemukan di sini:
[Martinfowler Testing](https://martinfowler.com/articles/microservice-testing/).

### Level 1 - Tes Tiruan & Tes Unit

Tujuan: Melatih bagian perangkat lunak terkecil yang dapat diuji dalam aplikasi untuk melihat apakah berfungsi seperti
yang diharapkan. bekerja. Uji coba dan uji coba unit dapat menjadi kontraproduktif dan sering kali menghambat proses
pengembangan. Tes-tes ini sering kali terlepas dari konteks dan memiliki sedikit hubungan dengan kenyataan. Mereka
sering kali hanya berfungsi untuk mempertahankan fungsi yang tidak perlu melalui tes unit yang ada. Setelah mock
ditambahkan, ini menjadi latihan yang merugikan diri sendiri. Yang diharapkan Hasil dari mock test terbatas pada apa
yang didefinisikan dalam mock asli. Pengguna akhir tidak tertarik dengan fungsi internal. Sebagai contoh, dalam sebuah
skenario login `loginUser(nama, kata sandi, securityAlgorithm)`. Jika uji coba unit melakukan pemeriksaan null pada
parameter `securityAlgorithm`, terlalu banyak pengujian yang dilakukan karena pengguna tidak dapat mengatur parameter
`securityAlgorithm`. mengatur parameter `securityAlgorithm`.

### Level 2 - Uji Integrasi

Tujuan: Memeriksa jalur komunikasi dan interaksi antar komponen untuk mendeteksi cacat antarmuka. Tes integrasi
memberikan wawasan berharga tentang kinerja dan kemandirian berbagai bagian aplikasi. aplikasi. Dengan lebih sedikit
tiruan, pengujian menjadi lebih mudah dipahami. Namun, mereka masih kekurangan konteks, dan ada risiko bahwa bahaya
bahwa tes integrasi hanyalah tes unit yang menyamar dengan lebih sedikit tiruan.

### Level 3 - Uji Konten

Tujuan: untuk membatasi ruang lingkup perangkat lunak yang diuji menjadi bagian dari sistem yang diuji, untuk
memanipulasi sistem sistem melalui antarmuka kode internal dan penggunaan ganda uji untuk mengisolasi kode yang diuji
dari komponen lain. komponen. Pengujian komponen memberikan banyak informasi tentang kualitas dan kinerja aplikasi.
Alih-alih mengolok-olok Anda akhirnya menguji aplikasi Anda. Batas antara pengujian komponen dan pengujian end-to-end
tidak signifikan. Dengan lingkungan pengujian yang baik, batas-batas di antara keduanya sering kali menjadi kabur,
sehingga pengujian perilaku nyata, bukannya fungsi-fungsi yang terisolasi dan tanpa konteks. Akan tetapi, pembuatan
kelas uji tambahan Namun, pembuatan kelas pengujian tambahan seperti stub komponen, fakes, dan mocks dalam kode produksi
dapat menambah biaya pemeliharaan.

### Level 4 - Tes Kontrak

Tujuan dari blok kode ini adalah untuk memeriksa interaksi pada batas layanan eksternal dan untuk memastikan bahwa itu
sesuai dengan persyaratan kontrak dari layanan konsumsi. Uji coba kontrak sering kali menyerupai uji coba unit, dan
perbedaan di antara keduanya sangat kecil. Beberapa pengembang mengasosiasikan pengujian ini dengan pengujian Pact, yang
pada dasarnya bertindak sebagai pengujian unit dengan server di antaranya. Upaya Namun, upaya mempertahankan tes ini
mungkin tidak bermanfaat. Sebagai contoh, tes Pact dapat menggunakan REST API `loginUser?name=aa&password=bb)` dan
mengharapkan respons skema JSON yang sebelumnya diunggah ke server Pact. server. Skema ini bersifat statis dan rentan
terhadap kesalahan seperti format tanggal atau zona waktu yang salah dalam Respons API. Efek negatifnya bisa sangat
besar.

### Level 5 - Tes ujung ke ujung (juga disebut tes kotak hitam)

Tujuan: Untuk memverifikasi bahwa suatu sistem memenuhi persyaratan eksternal dan mencapai tujuannya dengan menguji
keseluruhan sistem dari awal hingga akhir. dari awal hingga akhir. Pengujian dari awal hingga akhir dapat diandalkan
dan kuat. Setelah rintangan pengaturan lingkungan pengujian diatasi, maka upaya terbayar. Pengujian ini mensimulasikan
perilaku nyata dan menghilangkan kebutuhan akan tiruan. Kesalahan lebih jarang terjadi dan lebih mudah direproduksi
secara lokal. Debugging dan pencatatan yang memakan waktu dalam produksi sebagian besar dihindari, karena jarang
terjadi. sebagian besar dihindari, seperti halnya insiden yang jarang terjadi. Pengembang lebih jarang bekerja, jika
sama sekali, dengan dengan data produksi, yang mengurangi tanggung jawab dan meningkatkan fokus. Selain itu, otomatisasi
seperti pembaruan perangkat lunak otomatis membuat implementasi menjadi lebih mudah, karena perilakunya sudah teruji.
Masih ada manfaat lainnya! Sekali tes ditulis dalam bentuk yang dapat digunakan kembali, tes tersebut dapat
diintegrasikan ke dalam tes beban untuk mendapatkan yang komprehensif komprehensif tentang fungsionalitas. Pengujian ini
juga dapat dijalankan terus menerus di lingkungan produksi dan memberikan wawasan waktu nyata tentang status berbagai
alur kerja. Ketika sebuah subsistem, seperti Layanan REST, misalnya, menjadi offline, maka dimungkinkan untuk segera
mengidentifikasi alur kerja pengguna mana yang terpengaruh. terpengaruh.

### Fazit

Singkatnya, pengujian adalah aspek penting dalam pengembangan perangkat lunak, dan pilihan tingkat pengujian tergantung
pada persyaratan dan tujuan spesifik aplikasi. Meskipun uji coba dan uji coba unit mungkin terbatas dalam
keefektifannya, uji coba integrasi dan uji coba efektivitas, tes integrasi dan tes unit memberikan wawasan yang berharga
ke dalam perilaku dan kinerja aplikasi. kinerja aplikasi. Uji coba kontrak membantu memverifikasi interaksi dengan
layanan eksternal, tetapi diferensiasi dari tes unit bisa minimal. Pada akhirnya, pengujian end-to-end memberikan
tingkat kepercayaan tertinggi pada fungsionalitas sistem dan memungkinkan pengujian yang komprehensif. Pengujian end-to-
end memberikan tingkat kepercayaan tertinggi pada fungsionalitas sistem dan memungkinkan pengujian komprehensif terhadap
keseluruhan aplikasi. Dengan memilih yang sesuai tingkat pengujian yang sesuai dan menggabungkannya secara efektif,
pengembang dapat memastikan kualitas, keandalan, dan ketahanan Anda perangkat lunak.

### Kontak

[Masalah GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
