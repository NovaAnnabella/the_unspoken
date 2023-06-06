---
title: "Trở lại Maven?"
date: 2023-05-01
author: "Nova Annabella"
slug: back_to_maven
tags: [ Development, Gradle, Maven, CI_CD ]
categories: [ Technology, Software ]
description: "Die schwer fassbare Suche nach Einfachheit und eine kurze Reise zur Wiederentdeckung der Macht von Maven"
draft: false
images:
  - "/images/content/maven_vs_gradle.png"
card: "summary_large_image"
---



# Quay lại Maven chăng?

[![maven_vs_gradle](/images/content/maven_vs_gradle.png)](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

## 10 năm của Gradle. Trên tìm kiếm sự dễ dàng và chuyến đi ngắn để tìm lại sức mạnh của Maven.

# Willkommen bei meinem Blog Ich heiße Max und bin 25 Jahre alt. In diesem Blog schreibe ich über meine Erfahrungen mit
dem Reisen, dem Leben im Ausland und anderen interessanten Themen. ## Meine Reiseerfahrungen Ich habe bisher in 20
Ländern auf fünf Kontinenten gereist. Meine Lieblingsländer sind Japan, Thailand und Kanada. In meinem Blog teile ich
meine Erfahrungen und gebe Tipps für deine nächste Reise. ## Das Leben im Ausland Ich habe für ein Jahr in Australien
gelebt und gearbeitet. Dort habe ich viele neue Freunde gefunden und viel über mich selbst gelernt. In meinem Blog
findest du Tipps für das Leben im Ausland und wie du am besten Freunde findest. ## Andere interessante Themen
Abgesehen von Reisen und dem Leben im Ausland schreibe ich auch über andere Themen wie Fotografie, Musik und Filme.

### Tối đa hóa tiềm năng của nhà phát triển - Chúng ta cần nhiều công cụ tiết kiệm thời gian hơn

Các chủ đề thường bị bỏ qua hoặc ít được thảo luận là những thứ tôi quan tâm. Thường có các công nghệ hay được sử dụng,
nhưng hầu như không ai nói về các vấn đề liên quan đến chúng. Phát triển là một việc rất tốn kém vào ngày nay. Với những
Buzzword hấp dẫn như “Không có máy chủ”, “Mã nguồn thấp”, “IaC”, “Dữ liệu lớn”, “Đám mây”, “DevOps”, “Bạn xây dựng nó
Bạn chạy nó"vân vân, các nhà phát triển đã có nhiều nhiệm vụ bổ sung để giải quyết. Nhiều nhiệm vụ đồng nghĩa với việc
hiếm có các chuyên gia và luôn bỏ lỡ cái gì đó để tập trung. Do đó, tự động hóa và tiết kiệm thời gian rất quan trọng.
"Đừng buộc tôi suy nghĩ" và "Hoạt động ngay khi lấy ra khỏi hộp" đã là những tiêu chí chất lượng tốt, mà tôi chưa thấy ở
Gradle. Phải công bằng, Gradle không phải là công cụ hiện đại duy nhất khiến chúng ta phải làm việc nhiều hơn là đơn
giản hóa công việc.

### Tìm kiếm hư ảo sự đơn giản và tự động hóa

Kể từ khi có SOAP, tôi có một sự không ưa sâu sắc đối với các cấu hình dựa trên XML. Với Gradle, tôi đã hy vọng viết các
kịch bản ràng buộc sẽ dễ dàng hơn. Thật không may, hy vọng và động lực của tôi đã giảm dần qua từng lần thử. Gradle
hướng đến tính linh hoạt và hy sinh sự tự động và chất lượng. Các nhà phát triển tuân theo xu hướng mù quáng mà không
quan tâm đến tác động đến tính đáng tin cậy của phần mềm. Để giữ cho kịch bản xây dựng Gradle đơn giản và dễ bảo trì,
cần phải có một kỷ luật mạnh mẽ. Một kỷ luật như vậy hiếm khi được tìm thấy trong mã nguồn và do đó hiếm gặp hơn nhiều
trong các kịch bản xây dựng.

### Dịch và các giải pháp tạm thời - Khi các tập lệnh Build gây thách thức

Gradle hoạt động nền tảng không khác nhiều so với Maven. Do đó, một số bản dịch là cần thiết. Các tính năng như
Dependency Catalog, Maven Release Plugin, Dependabot và nhiều tính năng khác thực chất là các giải pháp tạm thời cho các
chức năng cơ bản, mà Maven đã có sẵn. Với tính linh hoạt của Gradle, thường tạo ra các cấu hình Build phức tạp, khó bảo
trì. Các Plugins của Gradle thường gặp vấn đề về tính tương thích, giới hạn hoặc phát triển hạn chế. Những vấn đề này
phát sinh do sự phát triển của hệ sinh thái Gradle, đa dạng của môi trường mà Gradle được triển khai, và chi phí cụ thể
về hiện thực và bảo trì cho mỗi Plugin. Mọi thứ đều liên quan đến nhau.

### Tác động nhiễu động từ của Gradle - Kịch bản ác mộng trên thực tế

Tôi đã thấy nhiều Microservices chỉ vài năm tuổi nhưng đã không thể bảo trì nữa do Gradle. Quan trọng phải nhắc rằng đây
không phải lần đầu tiên tôi thấy điều này và không, đó không phải là do những lập trình viên mới. Nhiệm vụ của tôi là
nâng cấp Spring Boot 2.x lên 2.7. Nhưng sau một năm, tôi đã bỏ cuộc! Các vấn đề ngắn gọn như sau: - Gradle Build-File
yêu cầu down version Java của tôi xuống phiên bản 11 (WTF) (thông thường Java tương thích xuống  version - đó cũng là
lí do tại sao lại có các công cụ Workaround như SdkMan...) - Cập nhật Spring Boot yêu cầu cập nhật Gradle (WTF) - Cập
nhật Gradle yêu cầu cập nhật Plugin - Cập nhật Plugin yêu cầu cập nhật Groovy (WTF) - Cập nhật Groovy yêu cầu cập nhật
Test-Framework và Test-Updates (WTF) - Cập nhật Test-Framework yêu cầu cập nhật Dependencies - \[...\]  Ngoài ra, một
số Plugin không hoạt động với Gradle phiên bản mới hơn, một số không tiếp tục phát triển, không tương thích với các
Plugin khác, chỉ hoạt động với Gradle KTS, không hoạt động với Gradle Groovy hoặc chỉ có giới hạn. Ngay cả Plugin từ các
nhà cung cấp lớn như Spring cũng có tính năng bị giới hạn so với các Plugin của Maven. Cuối cùng, tôi có một tệp Gradle-
Build ngắn gọn, mỗi người đều không thể bảo trì, ngay cả các nhà phát triển đã viết nó và họ vẫn yêu Gradle. Tôi chỉ
biết vài người hiểu rõ và có thể viết script của Gradle.

### Khám phá lại sức mạnh của Maven - Sử dụng phép thuật của Maven

Đây là những tính năng yêu thích của tôi trong Maven: Các plugin có thể được khởi chạy và cấu hình trực tiếp từ dòng
lệnh mà không cần được xác định trước. Hơn nữa, chúng độc lập khá nhiều so với các cấu hình Plugin khác. | Lệnh mẫu
| Mô tả
| Liên kết                                | |-----------------------------|-------------
------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------|------------------------------------------------------------------------
| | `mvn versions:use -latest-versions`  | Cập nhật phiên bản - ai cần Dependabot? Đúng, các dự án của tôi đã được cập
nhật lên phiên bản mới nhất trong nhiều năm mà không cần phải nhìn chung qua các yêu cầu hợp nhất khó chịu |
https://www.mojohaus.org/versions/versions-maven-plugin/plugin-info.html | | `mvn versions:set -DnewVersion=1.0.0` | Xác
định phiên bản dự án ...
| https://www.mojohaus.org/versions/versions-maven-plugin/index.html    | | `mvn license:add-third-party`     |
Liệt kê sự phụ thuộc và hiển thị giấy phép của chúng (thậm chí có thể thất bại trong trường hợp các giấy phép bị loại
bỏ)                       | https://www.mojohaus.org/license-maven-plugin/index.html
|  Danh sách này có thể được kéo dài vô tận. Nó khiến tôi nhớ đến các bước Workflow trên GitHub.
![maven_plugin_command_line_args](/images/content/maven_plugin_command_line_args.png)

### Bạn không thích XML sao?

Không vấn đề gì! Viết File Build của bạn bằng `ruby`, `groovy`, `scala`, `yaml`, `atom` hoặc `Java`. Tiện ích Polygot
(https://github.com/takari/polyglot-maven) sẽ giúp bạn. Để thử nghiệm, chỉ cần chạy `mvn io.takari.polyglot: polyglot-
translate-plugin: translate -Dinput = pom.xml -Doutput = pom.yaml` và sau vài mili giây, File Build của bạn sẽ được
dịch. Thật đáng tiếc là không có bộ dịch Maven <> Gradle đáng tin cậy :( Đúng vậy, các tệp Build Maven rất lớn, nhưng
cũng rất dễ hiểu. Các chỉnh sửa hoặc Debugging được thực hiện trong nháy mắt.

### Tuổi tác chỉ là một con số - Sự ổn định và tiến hóa của Maven

Thật ra, Maven đã có từ một thời gian dài và thẩm mỹ của nó có lẽ không phù hợp với các tiêu chuẩn hiện nay. Nhưng sự
bền vững của Maven đã cho phép nó thích nghi và tiếp tục phát triển. Maven làm việc độc lập với dự án của bạn. Các tệp
Build có thể được tái sử dụng dễ dàng. Các plugin chạy trong một môi trường đóng hộp và không phụ thuộc lẫn nhau hoặc
phiên bản Java hoặc Maven. Thiết kế này thúc đẩy tính ổn định và dự đoán và dễ dàng quản lý quy trình Build phức tạp mà
không gây ra xung đột không mong đợi.

### Kết luận

Hiện nay, môi trường phát triển đầy nhiều nhiệm vụ và công nghệ đối với các nhà phát triển. Tìm kiếm đơn giản hóa và tự
động hóa, Gradle đã xuất hiện như một công cụ xây dựng hiện đại, nhưng nó cũng đưa ra những thách thức của riêng nó.
Không có câu hỏi, khái niệm của Gradle là tốt! Nhưng đối với sự phức tạp và thời gian được đầu tư vào các kịch bản xây
dựng Gradle, câu hỏi là liệu nó có đơn giản hóa hơn nếu mở rộng Maven. Với các plugin và extension, Maven có thể được
cập nhật và đơn giản hóa bất cứ lúc nào. Việc phát triển tiếp theo không phải là hấp dẫn và bền vững hơn, thay vì nhảy
từ một công nghệ sang công nghệ khác?

### Liên kết

* [Chuyển từ Gradle sang Maven](https://phauer.com/2018/moving-back-from-gradle-to-maven/)

### Liên hệ

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
