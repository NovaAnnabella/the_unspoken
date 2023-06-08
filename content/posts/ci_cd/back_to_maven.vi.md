---
title: "Quay lại Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "Tìm kiếm sự đơn giản không dễ dàng và một chuyến đi ngắn để khám phá lại sức mạnh của Maven."
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---


# Trở lại với Maven?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

Đoạn văn trên là mã đánh dấu.

## 10 năm của Gradle. Trên tìm kiếm sự dễ dàng và một chuyến đi ngắn để khám phá lại sức mạnh của Maven.

Không có văn bản để dịch.

### Tối đa hóa tiềm năng của nhà phát triển - Chúng ta cần nhiều công cụ tiết kiệm thời gian hơn

Các chủ đề thường bị bỏ qua hoặc ít được thảo luận là những chủ đề mà tôi quan tâm. Thường thì các công nghệ tuyệt vời
được sử dụng nhưng ít ai nói về các vấn đề liên quan đến chúng. Việc phát triển ngày nay đã trở nên rất tốn kém. Với
những từ khóa thú vị như "Serverless", "Low Code", "IaC", "Big Data", "Cloud", "DevOps", "You Build it You run it",
v.v., các nhà phát triển đã có đủ nhiều nhiệm vụ phụ để xử lý. Nhiều nhiệm vụ đồng nghĩa với việc ít chuyên gia hơn và
luôn có điều gì đó bị bỏ qua để tập trung vào cái gì khác. Vì vậy, việc tự động hóa và tiết kiệm thời gian là rất quan
trọng. "Đừng làm tôi phải suy nghĩ" và "Hoạt động ngay khi được mở ra" đã là những đặc điểm chất lượng tốt, nhưng tôi
không thấy chúng trong Gradle. Để công bằng, Gradle không phải là công cụ hiện đại duy nhất gây khó khăn cho chúng ta,
thay vì giúp cho công việc trở nên dễ dàng hơn.

### Sự tìm kiếm ảo giác của sự đơn giản và tự động hóa

Kể từ khi có SOAP, tôi có một sự không thích với các cấu hình dựa trên XML. Với Gradle, tôi hy vọng viết các kịch bản
ràng buộc sẽ dễ dàng hơn. Nhưng hy vọng của tôi đã ngày càng giảm dần. Gradle đặt sự linh hoạt lên hàng đầu và hy sinh
tự động hóa và chất lượng để đạt được điều đó. Nhà phát triển đang làm theo xu hướng mù quáng mà không quan tâm đến tác
động lên độ tin cậy của phần mềm. Để giữ cho các kịch bản dựng Gradle đơn giản và dễ bảo trì, cần có một kỷ luật rất
mạnh. Một kỷ luật như vậy hiếm khi được tìm thấy trong mã nguồn và vì vậy nó còn ít thấy hơn trong các kịch bản dựng.

### Phiên dịch và các giải pháp tạm thời - Khi tập lệnh build trở thành một thách thức

Gradle không khác nhiều so với Maven khi hoạt động ở phía sau. Vì vậy, một số bản dịch là cần thiết. Một số tính năng
như Dependency Catalog, Maven Release Plugin, Dependabot và nhiều thứ khác đều là những giải pháp tạm thời cho các chức
năng cơ bản mà Maven đã có sẵn. Với tính linh hoạt của Gradle, thường có những cấu hình Build phức tạp khó để bảo trì.
Các plugin trong Gradle thường gặp vấn đề về tính tương thích, giới hạn hoặc sự phát triển hạn chế. Những vấn đề này
phát sinh do tính đa dạng của môi trường sử dụng Gradle, các yếu tố đặc thù của từng plugin và chi phí thực hiện và bảo
trì cụ thể. Tất cả đều liên kết với nhau.

### Hiệu ứng Domino của Gradle - Kịch bản ác mộng trong thế giới thực.

Tôi đã thấy nhiều dịch vụ siêu nhỏ chỉ mới vài năm tuổi nhưng đã không thể bảo trì được nữa do Gradle. Cần nhấn mạnh rằng đây không phải là lần đầu tiên tôi nhìn thấy điều này và không, không phải là các nhà phát triển trẻ tuổi.

**Nhiệm vụ của tôi là thực hiện việc nâng cấp Spring Boot 2.x lên phiên bản 2.7**. Một lời b spoilers: Tôi đã từ bỏ sau một năm! Những vấn đề tóm tắt:

* Gradle-Build-File đòi hỏi -> Giảm phiên bản Java cục bộ của tôi xuống cấp 11 (WTF) (Thông thường, Java là tương thích ngược - ở đây cũng có các công cụ Workaround như SdkMan ...)
* Cập nhật Spring Boot đòi hỏi -> Cập nhật Gradle (WTF)
* Cập nhật Gradle đòi hỏi -> Cập nhật Plugin
* Cập nhật Plugin đòi hỏi -> Cập nhật Groovy (WTF)
* Cập nhật Groovy đòi hỏi -> Cập nhật Test-Framework (khung thử nghiệm) và Test-Updates (WTF)
* Cập nhật Test-Framework đòi hỏi -> Cập nhật phụ thuộc
* \[...\]
  Ngoài ra, một số plugin không hoạt động với các phiên bản Gradle mới hơn, một số không được phát triển tiếp theo, không tương thích với các plugin khác, chỉ hoạt động với Gradle KTS, không với Gradle Groovy hoặc có giới hạn đơn giản. Ngay cả các plugin từ các nhà cung cấp lớn như Spring cũng có tính năng giới hạn so với Maven-Plugins của họ. Cuối cùng, tôi có một tệp Gradle-Build ngắn gọn và đầy cá tính, mà không ai có thể bảo trì đúng, ngay cả các nhà phát triển đã viết nó và họ vẫn yêu Gradle. Tôi chỉ biết vài người có thể hiểu và viết đối với Gradle Script một cách nghiêm túc.

### Phát hiện lại sức mạnh của Maven - Sử dụng phép thuật của Maven

Đây là những tính năng yêu thích của tôi trong Maven:
Các Plugin có thể được khởi động và cấu hình trực tiếp từ dòng lệnh mà không cần được xác định trước. Ngoài ra, chúng rất độc lập với các cấu hình Plugin khác.

| Lệnh ví dụ | Mô tả | Liên kết |
|------------|-------------------------------------------|--------------------------|
| `mvn versions:use -latest-versions` | Cập nhật phiên bản - ai còn cần Dependabot? Vâng, dự án của tôi đã được cập nhật thành phiên bản mới nhất trong nhiều năm qua mà không cần những yêu cầu hợp nhất phiền toái | https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html |
| `mvn versions:set -DnewVersion=1.0.0` | Thiết lập phiên bản dự án ... | https://www.mojohaus.org/versions/versions-maven-plugin/index.html |
| `mvn license:add-third-party` | Liệt kê các phụ thuộc và hiển thị giấy phép của chúng (thậm chí có thể bị thất bại với các giấy phép bị loại trừ) | https://www.mojohaus.org/license-maven-plugin/index.html |

Danh sách này có thể kéo dài mãi mãi. Nó làm tôi nhớ đến các bước làm việc của GitHub Workflow.

![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

### Bạn không thích XML sao?

Không vấn đề gì! Chỉ cần viết các tệp Build của bạn bằng `ruby`, `groovy`, `scala`, `yaml`, `atom` hoặc `Java`. Tiện ích Polygot (https://github.com/takari/polyglot-maven) làm điều đó trở thành hiện thực. Chỉ cần thử nghiệm bằng cách chạy `mvn io.takari.polyglot:polyglot-translate-plugin:translate -Dinput=pom.xml -Doutput=pom.yaml` và chỉ trong vài mili giây, tệp Build của bạn sẽ được dịch. Rất tiếc là hiện tại chưa có trình dịch đổi ngược đáng tin cậy từ Maven sang Gradle :(
Vâng, các tệp Build của Maven rất lớn, nhưng cũng rất dễ hiểu. Việc sửa chữa hoặc gỡ lỗi có thể được thực hiện chỉ trong vài giây.

### Tuổi tác chỉ là con số - Sự ổn định và Tiến hoá của Maven

Thừa nhận, Maven đã tồn tại trong một thời gian khá lâu và thẩm mỹ của nó có thể không phù hợp với các tiêu chuẩn hiện
đại. Tuy nhiên, sự lâu dài của Maven đã cho phép nó thích nghi và tiếp tục phát triển. Maven hoạt động độc lập với dự án
của bạn. Tệp xây dựng có thể được tái sử dụng một cách dễ dàng. Các plugin chạy trong một sandbox và độc lập lẫn nhau và
độc lập với phiên bản Java hoặc Maven. Thiết kế này thúc đẩy tính ổn định và dự báo và làm cho nó dễ dàng để quản lý các
quy trình xây dựng phức tạp mà không gặp xung đột không mong muốn.

### Kết luận

Ngày nay, môi trường phát triển bị quá tải với nhiều nhiệm vụ và công nghệ cho các nhà phát triển. Trong tìm kiếm sự đơn
giản và tự động hóa, Gradle đã xuất hiện như một công cụ xây dựng hiện đại, nhưng đem đến những thách thức riêng của nó.
Không thể phủ nhận, khái niệm của Gradle là tốt! Tuy nhiên, với sự phức tạp và thời gian đầu tư vào các kịch bản xây
dựng Gradle, câu hỏi đặt ra là liệu việc mở rộng Maven có không giản đơn hơn. Với các trình cắm và tiện ích mở rộng,
Maven có thể được cập nhật và đơn giản hóa bất cứ lúc nào. liệu rằng một việc tiếp tục phát triển có không thú vị và bền
vững hơn là chuyển từ một công nghệ sang khác?

### Liên kết

* [Chuyển từ Gradle về Maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### Liên lạc

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
```

Dịch sang tiếng Việt:

```
[Các vấn đề trên GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
```
