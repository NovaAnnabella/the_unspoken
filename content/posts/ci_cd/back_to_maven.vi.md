---
title: "Quay lại Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "Tìm kiếm tính đơn giản khó nắm bắt và một chuyến đi ngắn đến việc khám phá lại sức mạnh của Maven."
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# Quay trở lại Maven?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

(Nhấn vào hình để đọc bài viết về sự khác biệt giữa Maven và Gradle)

## 10 Năm Gradle. Trên tìm kiếm sự dễ dàng và một chuyến đi ngắn để khám phá lại sức mạnh của Maven.

Không có nội dung cần dịch.

### Tối đa hóa tiềm năng của nhà phát triển - Chúng ta cần nhiều công cụ tiết kiệm thời gian hơn

Các chủ đề thường bị bỏ qua hoặc ít được thảo luận thu hút tôi. Thường thì các công nghệ độc đáo được sử dụng, nhưng ít
người nói về các vấn đề liên quan. Sự phát triển hiện nay đã trở nên rất tốn kém. Với các cụm từ hấp dẫn như
"Serverless", "Low Code", "IaC", "Big Data", "Cloud", "DevOps", "You Build it You run it" vv. các nhà phát triển đã có
quá nhiều nhiệm vụ phụ để giải quyết. Việc có nhiều nhiệm vụ phụ trong công việc cũng có ý nghĩa rằng chúng ta gần như
không còn chuyên gia nào cả và luôn có điều gì đó bị bỏ quên. Do đó, việc tự động hóa và tiết kiệm thời gian rất quan
trọng. "Đừng làm tôi nghĩ" và "Hoạt động ngay từ đầu" đã là các đặc điểm chất lượng tốt, mà tôi chưa thấy được trong
Gradle. Để công bằng, Gradle không phải là công cụ hiện đại duy nhất làm cho chúng tôi phải làm việc thay vì làm cho
việc của chúng tôi dễ dàng hơn.

### Tìm kiếm hình tượng dễ hiểu và tự động hóa là một ảo tưởng

Kể từ khi sử dụng SOAP, tôi có một sự ghê tởm sâu sắc đối với các cấu hình dựa trên XML. Với Gradle, tôi đã hy vọng viết
các kịch bản liên kết sẽ dễ dàng hơn. Nhưng đáng tiếc, hi vọng và động lực của tôi đã ngày càng suy giảm. Gradle luôn
tìm kiếm tính linh hoạt và đánh đổi sự tự động hóa và chất lượng để đạt được mục đích đó. Các nhà phát triển đang theo
một xu hướng mà không quan tâm đến tác động đến tính đáng tin cậy của phần mềm. Để giữ cho các kịch bản Gradle Build đơn
giản và dễ bảo trì, cần có disclipine mạnh mẽ. Loại kỷ luật này hiếm khi được tìm thấy trong mã nguồn và nó càng hiếm
trong các kịch bản Build.

### Dịch và khắc phục - Khi các tập lệnh xây dựng trở thành thách thức

Gradle hoạt động ở nền tảng không khác gì Maven nhiều. Do đó, một số bản dịch là cần thiết. Như Dependency Catalog,
Maven Release Plugin, Dependabot và nhiều tính năng khác, thực chất là các giải pháp tạm thời cho các chức năng cơ bản
mà Maven đã có sẵn. Với tính linh hoạt của Gradle, thường tạo ra các cấu hình Build phức tạp, khó bảo trì.  Các Plugin
của Gradle thường gặp vấn đề về tương thích, giới hạn hoặc hạn chế trong việc phát triển tiếp theo. Những vấn đề này
phát sinh do tính chất của hệ sinh thái Gradle đang phát triển, đa dạng của các môi trường sử dụng Gradle và các chi phí
cài đặt và bảo trì đặc thù cho từng Plugin. Tất cả đều có liên quan với nhau.

### Tác động lan truyền của Gradle - Một kịch bản ác mộng trong thế giới thực

Tôi đã nhìn thấy nhiều Microservices chỉ mới mấy năm tuổi nhưng đã không thể được sửa chữa do Gradle. Đáng chú ý là đây không phải là lần đầu tiên tôi thấy điều này và không, không phải là lập trình viên mới.

**Nhiệm vụ của tôi là nâng cấp một Spring Boot 2.x lên 2.7**. Spoiler: Sau một năm tôi đã từ bỏ! Những vấn đề tóm tắt ngắn gọn như sau:

* Gradle-Build-File yêu cầu -> Giảm phiên bản Java cục bộ của tôi xuống cấp 11 (WTF) (Thường thì Java là tương thích ngược - cũng có những công cụ workaround như SdkMan ...)
* Spring Boot-Update đòi hỏi -> Cập nhật Gradle (WTF)
* Gradle-Update yêu cầu -> Plugin-Update
* Plugin-Update yêu cầu -> Groovy-Update (WTF)
* Groovy-Update yêu cầu -> Test-Framework- và Test-Updates (WTF)
* Test-Framework-Update yêu cầu -> Cập nhật phụ thuộc
* \[...]
Ngoài ra, một số plugin không hoạt động với các phiên bản Gradle mới hơn, một số plugin không được tiếp tục phát triển, không tương thích với các plugin khác, chỉ hoạt động với Gradle KTS, không hoạt động với Gradle Groovy, hoặc có giới hạn đơn giản. Ngay cả các plugin của các nhà cung cấp lớn như Spring cũng có tính năng bị hạn chế so với các plugin Maven của họ. Cuối cùng tôi có một tệp Gradle-Build ngắn gọn và "đẹp đẽ", mà chẳng ai có thể bảo trì một cách đúng đắn, không cả những nhà phát triển đã viết nó, nhưng họ vẫn yêu Gradle. Tôi chỉ biết ít người hiểu và viết kịch bản Gradle một cách nghiêm túc.

### Sự khám phá lại sức mạnh của Maven - Sử dụng phép thuật của Maven

Đây là các tính năng yêu thích của Maven của tôi:
Các plugin có thể được khởi động và cấu hình trực tiếp từ dòng lệnh mà không cần phải xác định trước. Ngoài ra, chúng độc lập khá với các cấu hình plugin khác.

| Lệnh ví dụ                          | Mô tả                                                                                                                                                              | Liên kết                                                                |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| `mvn versions:use -latest-versions` | Cập nhật các phiên bản mới nhất - ai cần Dependabot? Vâng, các dự án của tôi đã được cập nhật lên phiên bản mới nhất mà không có yêu cầu ghép lệnh phiền toái | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0`| Thiết lập phiên bản dự án...                                                                                                                                         | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`       | Liệt kê các phụ thuộc và hiển thị giấy phép của chúng (thậm chí có thể thất bại khi bị loại bỏ khỏi giấy phép)                                                      | https://www.mojohaus.org/license-maven-plugin/index.html                |

Danh sách này có thể kéo dài mãi mãi. Nó làm tôi nhớ đến bước làm việc của GitHub.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)
```

### Bạn không thích XML?

Không vấn đề gì! Chỉ cần bạn viết Tệp Build của mình bằng `ruby`, `groovy`, `scala`, `yaml`, `atom` hoặc `Java`. Tiện ích đa ngôn ngữ (https://github.com/takari/polyglot-maven) có thể làm được điều đó. Để thử nghiệm, chỉ cần chạy `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` và chỉ trong vài mili giây, Tệp Build của bạn sẽ được dịch. Thật đáng tiếc là không có bộ dịch Maven <> Gradle đáng tin cậy nào :(
Đúng vậy, Tệp Build của Maven lớn, nhưng cũng rất dễ hiểu. Sửa chữa hoặc gỡ lỗi được thực hiện chỉ trong vài giây.

### Tuổi tác chỉ là một con số - Tính ổn định và tiến hóa của Mavens

Thừa nhận rằng, Maven đã tồn tại khá lâu và vẻ đẹp của nó có thể không phù hợp với các tiêu chuẩn hiện đại. Tuy nhiên,
độ bền của Maven đã cho phép nó thích nghi và phát triển tiếp. Maven hoạt động độc lập với dự án của bạn. Tập tin Build
có thể tái sử dụng dễ dàng. Trình cắm sẽ chạy trong một Sandbox và độc lập với nhau và độc lập với phiên bản Java hoặc
Maven. Thiết kế này thúc đẩy tính ổn định và dự đoán và làm cho nó dễ dàng để quản lý các quy trình Build phức tạp mà
không gặp phải xung đột bất ngờ.

### Kết luận

Hiện nay, môi trường phát triển đã quá tải với nhiều nhiệm vụ và công nghệ cho các nhà phát triển. Tìm kiếm sự đơn giản
và tự động hoá, Gradle đã xuất hiện như một công cụ xây dựng hiện đại nhưng đưa ra những thách thức riêng của nó. Không
nghi ngờ gì, khái niệm Gradle là tốt! Nhưng trước sự phức tạp và thời gian đầu tư cho kịch bản Gradle, câu hỏi đặt ra là
liệu có dễ dàng hơn không khi mở rộng Maven. Với các plugin và phần mở rộng, Maven có thể được cập nhật và đơn giản hóa
bất cứ lúc nào. Việc phát triển tiếp theo có phải là thú vị và bền vững hơn không, thay vì chuyển đổi từ công nghệ này
sang công nghệ khác?

### Liên kết

* [Chuyển từ Gradle về lại Maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### Liên hệ

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).

Đầu tưược traducteur

