---
title: "Tingkat Tes: Menemukan Keseimbangan yang Tepat"
date: 2023-05-31
author: "Nova Annabella"
slug: test_level
tags: [ Testing, Software Testing, Test Levels, Mock Tests, Unit Tests, Integration Tests, Component Tests, Contract Tests, End-to-End Tests ]
categories: [ Technology, Software Development, Quality Assurance ]
description: "Menemukan keseimbangan yang tepat dalam memilih tingkat tes yang sesuai untuk pengujian perangkat lunak"
draft: false
images:
  - "/images/content/martin_fowler_testing.png"
card: "summary_large_image"
---


# Tingkat Pengujian: Menemukan Keseimbangan yang Tepat

[![testebenen](/images/content/martin_fowler_testing.png)](https://martinfowler.com/articles/microservice-testing/)


### Pendahuluan

Tema Pengujian tampaknya hingga hari ini masih merupakan wilayah baru dengan banyak ruang untuk interpretasi. Piramida pengujian tradisional dipertanyakan dan piramida pengujian baru muncul. Menurut pendapat saya, kita tidak memerlukan piramida pengujian, tetapi pemahaman yang jelas tentang apa yang harus diuji. Pengujian pada level yang lebih rendah seringkali kurang informatif. Fokus harus terutama pada pengujian perilaku untuk memastikan bahwa 
API 
atau UI berfungsi sesuai keinginan. Ikhtisar komprehensif tentang jenis-jenis pengujian yang mungkin dapat ditemukan di sini: 
[Martinfowler Testing](https://martinfowler.com/articles/microservice-testing/).


### Level 1 - Ujian Coba & Ujian Unit

Tujuan: Melakukan bagian perangkat lunak yang dapat diuji terkecil dalam aplikasi untuk menentukan apakah mereka berfungsi sesuai yang diharapkan.

Mock-tests dan Unit-tests bisa kontraproduktif dan seringkali menghambat proses pengembangan. Tes ini seringkali terlepas dari konteks dan memiliki sedikit kaitan dengan kenyataan. Mereka seringkali hanya digunakan untuk mempertahankan fungsi yang tidak perlu melalui Unit-tests yang ada. Begitu Mock ditambahkan, maka menjadi kesibukan sendiri. Hasil yang diharapkan dari Mock-tests dibatasi pada apa yang didefinisikan dalam Mock asli. Pengguna akhir tidak peduli dengan fungsi internal. Misalnya, dalam skenario login `loginUser(name, password, securityAlgorithmus)`. Jika Unit-test melakukan pengecekan Null pada parameter `securityAlgorithm`, ini adalah tes yang berlebihan, karena pengguna tidak bisa mengatur parameter `securityAlgorithm`.


### Level 2 - Uji Integrasi

Tujuan: Memeriksa jalur komunikasi dan interaksi antara komponen untuk mendeteksi kecacatan antarmuka. Tes integrasi
memberikan wawasan berharga tentang kinerja dan independensi berbagai bagian dari aplikasi. Dengan lebih sedikit mock,
tes menjadi lebih mudah dimengerti. Namun, mereka masih kekurangan konteks, dan ada risiko bahwa tes integrasi hanyalah
tes unit yang terselubung dengan lebih sedikit mock.

### Level 3 - Uji Komponen

Tujuan: Membatasi lingkup perangkat lunak yang diuji menjadi sebagian dari sistem yang harus dites, manipulasi sistem
melalui antarmuka kode internal dan penggunaan Testdoubles untuk mengisolasi kode yang diuji dari komponen lain.

Tes komponen memberikan banyak informasi tentang kualitas dan kinerja aplikasi. Alih-alih
Mocks, kau akhirnya menguji aplikasimu. Batas antara tes komponen dan tes ujung-ke-ujung tidak
signifikan. Dengan lingkungan tes yang baik, batas antara mereka seringkali menjadi kabur, sehingga pengujian perilaku nyata
daripada fungsi terisolasi dan tanpa konteks menjadi mungkin. Namun, pembuatan tambahan
kelas tes seperti Komponen-Stubs, Fakes dan Mocks dalam kode produksi dapat membawa biaya pemeliharaan tambahan.

### Level 4 - Tes Kontrak

Tujuan dari blok kode ini adalah untuk memeriksa interaksi di perbatasan layanan eksternal dan
memastikan bahwa ia memenuhi persyaratan kontrak dari layanan konsumen.

Pengujian Kontrak sering kali mirip dengan Pengujian Komponen, dan perbedaan antara keduanya sangat minimal. Beberapa pengembang
mengasosiasikan pengujian ini dengan Pact-Tests, yang pada dasarnya berfungsi sebagai unit tests dengan server di antaranya. Namun,
upaya untuk mempertahankan pengujian ini mungkin tidak sepadan. Sebagai contoh, Pact-Test bisa
menguji REST-API `loginUser?name=aa&password=bb)` dan mengharapkan respon JSON Schema yang sebelumnya telah diunggah ke server Pact.
Skema ini adalah statis dan rentan terhadap kesalahan seperti format tanggal yang salah atau zona waktu dalam
respon API. Dampak negatifnya bisa sangat besar.

### Level 5 - Uji End-to-End (juga disebut Uji Black-Box)

Tujuan: Melakukan pemeriksaan apakah suatu sistem memenuhi persyaratan eksternal dan mencapai tujuan-tujuannya dengan menguji seluruh sistem dari
awal hingga akhir.

Tes End-to-End adalah tepercaya dan kokoh. Setelah hambatan pembangunan lingkungan tes diatasi, upaya tersebut akan memberikan hasil. Tes ini mensimulasikan perilaku nyata dan menghilangkan kebutuhan akan mock. Kesalahan lebih jarang
terjadi dan lebih mudah direproduksi secara lokal. Debugging yang rumit dan pencatatan di produksi
sebagian besar dihindari, begitu pula insiden yang jarang terjadi. Pengembang jarang bekerja, jika ada, dengan
data produksi, yang mengurangi tanggung jawab dan meningkatkan fokus. Selain itu, otomatisasi seperti
pembaruan perangkat lunak otomatis memudahkan pelaksanaan, karena perilakunya sudah diuji. Ada banyak keuntungan lainnya! Begitu
tes ditulis dalam bentuk yang dapat digunakan kembali, mereka bisa diintegrasikan ke dalam tes beban untuk mendapatkan gambaran
secara komprehensif tentang fungsionalitas. Tes ini juga bisa dijalankan secara kontinu di lingkungan produksi
dan memberikan wawasan real-time tentang status berbagai alur kerja. Jika subsistem, seperti
layanan REST eksternal, offline, dapat segera diidentifikasi alur kerja pengguna mana yang
terpengaruh.

### Kesimpulan

Secara keseluruhan, pengujian adalah aspek penting dalam pengembangan perangkat lunak, dan pemilihan tingkat pengujian tergantung pada
persyaratan dan tujuan spesifik dari aplikasi. Meski Pengujian Mock dan Unit mungkin memiliki keterbatasan dalam efektivitasnya,
pengujian integrasi dan pengujian komponen memberikan wawasan berharga tentang perilaku dan
kinerja aplikasi. Pengujian kontrak membantu memeriksa interaksi dengan layanan eksternal, tetapi pembatasan anda
dengan pengujian komponen mungkin minim. Pada akhirnya, Pengujian End-to-End memberikan tingkat kepercayaan tertinggi dalam
fungsionalitas sistem dan memungkinkan pengujian menyeluruh dari aplikasi secara keseluruhan. Dengan memilih tipe
pengujian yang tepat dan kombinasi efektif dari mereka, pengembang dapat menjamin kualitas, keandalan, dan ketahanan perangkat lunak anda.

### Kontak

[Isu GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
