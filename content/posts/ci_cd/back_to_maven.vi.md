---
title: "Quay trở lại Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "Việc tìm kiếm khó khăn về sự đơn giản và một chuyến đi ngắn để khám phá lại sức mạnh của Maven."
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# Quay lại Maven?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

## 10 năm Gradle. Đang tìm kiếm sự nhẹ nhàng và một chuyến đi ngắn để phát hiện lại sức mạnh của Maven.



### Tối đa hóa tiềm năng của các nhà phát triển - Chúng tôi cần nhiều công cụ tiết kiệm thời gian hơn

Các chủ đề thường bị bỏ qua hoặc ít khi được thảo luận thì làm tôi quan tâm. Thường xuyên có những công nghệ tuyệt vời
đang được sử dụng, nhưng ít ai nói về những vấn đề liên quan đến nó. Phát triển phần mềm ngày nay đã trở nên rất tốn
kém. Với những từ ngữ thời thượng như "Serverless", "Low Code", "IaC", "Big Data", "Cloud", "DevOps", "You Build it You
run it" v.v. các nhà phát triển đã phải đối mặt với nhiều nhiệm vụ phụ hơn. Thêm nhiệm vụ, có nghĩa là hầu như không còn
các chuyên gia nào và luôn có một cái gì đó bị lơ là để tập trung vào. Do đó, việc tự động hóa và tiết kiệm thời gian
cực kỳ quan trọng. "Đừng khiến tôi phải nghĩ" và "Hoạt động ngay tức thì" đã là những chỉ tiêu chất lượng tốt, mà tôi
chưa thấy ở Gradle . Để công bằng, Gradle không phải là công cụ hiện đại duy nhất làm cho chúng ta phải làm việc, thay
vì giảm bớt công việc.

### Cuộc tìm kiếm ảo giác về sự đơn giản và tự động hóa

Kể từ SOAP, tôi có một sự phản đối sâu sắc đối với cấu hình dựa trên XML. Với Gradle, tôi đã hy vọng, việc viết các
script bind sẽ trở nên dễ dàng. Thật không may, hy vọng và động lực của tôi lần này đến lần khác ngày càng ít đi. Gradle
hướng đến sự linh hoạt và hy sinh tự động và chất lượng để đạt được điều đó. Các nhà phát triển theo đuổi xu hướng một
cách mù quáng mà không quan tâm đến hậu quả đối với sự đáng tin cậy của phần mềm. Để giữ cho Gradle Script build đơn
giản và ít cần bảo dưỡng, điều đó đòi hỏi một kỷ luật mạnh mẽ. Một kỷ luật như vậy hiếm khi tìm thấy trong mã nguồn và
do đó, nó còn ít xuất hiện hơn nhiều trong các script build.

### Bản dịch và giải pháp tạm thời - Khi các script xây dựng trở thành một thách thức

Gradle hoạt động trong nền không khác nhiều so với Maven. Do đó, một số bản dịch là cần thiết. Các tính năng như Catalog
phụ thuộc, Plugin phát hành Maven, Dependabot và nhiều hơn nữa thực sự là các giải pháp tạm thời để giải quyết các chức
năng cơ bản mà Maven đã mang lại. Với sự linh hoạt của Gradle, thường xuyên xuất hiện các cấu hình xây dựng phức tạp,
những điều khó để duy trì. Gradle Plugins thường gặp vấn đề về tương thích, giới hạn hoặc phát triển hạn chế. Những vấn
đề này xuất hiện do bản chất phát triển của hệ sinh thái Gradle, sự đa dạng của các môi trường mà Gradle được triển khai
được và công sức cụ thể cần thiết để triển khai và bảo dưỡng cho mỗi Plugin. Mọi thứ đều liên quan đến nhau.

### Hiệu ứng Domino của Gradle - Một kịch bản ác mộng trong thế giới thực

Tôi đã thấy nhiều Microservices chỉ có vài năm tuổi và đã không thể bảo dưỡng được nữa chỉ vì Gradle.
Điều quan trọng cần nhắc đến là đây không phải lần đầu tiên tôi thấy điều như vậy, và không, chúng không phải
là Devs Junior.

**Nhiệm vụ của tôi là thực hiện nâng cấp từ Spring Boot 2.x lên 2.7**. Spoiler: Tôi đã từ bỏ sau một năm!
Vấn đề chỉ ngắn gọn như sau:

* File build của Gradle yêu cầu -> Hạ cấp phiên bản Java cục bộ của tôi xuống 11 (WTF) (Thông thường Java
  tương thích ngược - cũng có các công cụ workaround như SdkMan...)
* Cập nhật Spring Boot yêu cầu -> Cập nhật Gradle (WTF)
* Cập nhật Gradle yêu cầu -> Cập nhật Plugin
* Cập nhật plugin yêu cầu -> Cập nhật Groovy (WTF)
* Cập nhật Groovy yêu cầu -> Cập nhật Test-Framework và Test-Upgrades (WTF)
* Cập nhật Test-Framework yêu cầu -> Cập nhật Dependency
* \[...]
  Thêm vào đó, một số plugin không hoạt động với phiên bản Gradle mới, một số không còn được phát triển nữa,
  không tương thích với các plugin khác, chỉ hoạt động với Gradle KTS, không phải với Gradle Groovy, hoặc
  chỉ có giới hạn. Thậm chí các plugin từ các nhà cung cấp lớn như Spring so với plugin Maven của họ
  cũng có chức năng bị hạn chế. Cuối cùng, tôi có một file build Gradle ngắn gọn, mà không ai có thể duy trì đúng cách,
  ngay cả những nhà phát triển đã viết nó, và họ vẫn yêu Gradle. Tôi chỉ biết vài người
  hiểu hoặc có thể viết script Gradle một cách nghiêm túc.

### Sự tái khám phá sức mạnh của Maven - Sử dụng những sức mạnh ma thuật của Maven

Dưới đây là những tính năng yêu thích của tôi về Maven:
Các plugin có thể được khởi chạy và cấu hình trực tiếp từ dòng lệnh mà không cần phải định nghĩa trước. 
Thêm vào đó, chúng hoàn toàn độc lập với các cấu hình plugin khác.

| Lệnh ví dụ                           | Mô tả                                                                                                                                                               | Link                                                                     |
|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| `mvn versions:use -latest-versions`   | Cập nhật phiên bản - ai cần Dependabot? Đúng, dự án của tôi đã được cập nhật lên phiên bản mới nhất mà không gặp phiền phức yêu cầu ghép nối các phiên bản | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0` | Đặt phiên bản dự án...                                                                                                                                             | https://www.mojohaus.org/versions/versions-maven-plugin/index.html       |
| `mvn license:add-third-party`         | Liệt kê các yêu cầu và hiển thị giấy phép của chúng (có thể thất bại ngay cả khi có giấy phép bị loại trừ)                                                           | https://www.mojohaus.org/license-maven-plugin/index.html                 | 

Danh sách này có thể kéo dài mãi mãi. Nó gợi nhớ cho tôi về Các bước trong Workflow của GitHub.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)


### Bạn không thích XML à?

Không có vấn đề gì! Chỉ cần viết tệp xây dựng của bạn trong `ruby`, `groovy`, `scala`, `yaml`, `atom` hoặc `Java`. Phần mở rộng Polygot
(https://github.com/takari/polyglot-maven) làm cho điều này có thể thực hiện được. Để thử, hãy thực hiện 
`mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` và trong
vài mili giây, tệp xây dựng của bạn đã được dịch. Thật tiếc là không có bộ dịch Maven <> Gradle đáng tin cậy
nào: (
Có, tệp xây dựng Maven rất lớn, nhưng cũng rất dễ hiểu. Việc cải tiến hay gỡ lỗi có thể được hoàn tất trong nháy mắt.

### Tuổi tác chỉ là một con số - Sự ổn định và tiến hóa của Maven

Đúng là, Maven đã tồn tại khá lâu và phong cách của nó có thể không phù hợp với các tiêu chuẩn hiện nay. Tuy nhiên, tuổi
thọ của Maven đã cho phép nó thích nghi và phát triển. Maven hoạt động độc lập với dự án của bạn. Các tệp xây dựng có
thể được sử dụng lại một cách dễ dàng. Các plugin hoạt động trong một sandbox và độc lập với nhau cũng như độc lập với
phiên bản Java hoặc Maven. Thiết kế này thúc đẩy sự ổn định và khả năng dự đoán và làm cho việc quản lý các quá trình
xây dựng phức tạp mà không có xung đột không mong đợi trở nên dễ dàng.

### Kết luận

Ngày nay, môi trường phát triển đang chứa đầy nhiều nhiệm vụ và công nghệ cho các nhà phát triển. Trong sự tìm kiếm sự
đơn giản và tự động hóa, Gradle đã xuất hiện như một công cụ xây dựng hiện đại, nhưng cũng đã mang lại những thách thức
riêng của nó. Không có gì để chối cãi, khái niệm của Gradle là tốt! Tuy nhiên, trước sự phức tạp và thời gian được đầu
tư vào các script xây dựng Gradle, câu hỏi đặt ra là liệu có phải sẽ dễ dàng hơn nếu mở rộng Maven hay không. Với các
plugin và extension, Maven có thể được làm mới và đơn giản hóa bất cứ lúc nào. Phải chăng việc phát triển tiếp sẽ thú vị
hơn và cũng bền vững hơn, so với việc chuyển từ công nghệ này sang công nghệ khác?

### Liên kết

* [Chuyển đổi từ Gradle về maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### Liên hệ

[Vấn đề GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
