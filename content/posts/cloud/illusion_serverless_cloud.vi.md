---
title: "Illusion Serverless & Cloud"
date: 2023-05-24
author: "Nova Annabella"
slug: illusion_serverless_cloud
tags: [ Development, Serverless, Cloud, Microservices, Scalability, Architecture, Infrastructure ]
categories: [ Technology, Software, Cloud ]
description: Herausforderungen und Realitäten von Serverless-Funktionen in der Cloud. Wertvolle Einblicke für Unternehmen, die eine Migration zur Cloud in Erwägung ziehen
draft: false
images:
  - "/images/content/onprem_vs_cloud.png"
card: "summary_large_image"
---



# Sự ảo tưởng của các chức năng không có máy chủ trên đám mây

![aws_costs_twitter_1](/images/content/onprem_vs_cloud.png)

### Giới thiệu

Tôi thất vọng về việc Marketing thắng trí lý của con người quá nhiều. Nhiều quản lý bỏ qua chuyên gia của riêng mình -
những nhà phát triển. Điều đó cũng đúng khi chúng ta chuyển đổi sang đám mây. Tiết lộ: Ai phải tiết kiệm tiền thì nên
tránh đám mây. Bởi vì từ mới "Serverless" trên đám mây có nghĩa là: Bạn quan tâm đến phần mềm, chúng tôi quan tâm đến
phần cứng. Tuy nhiên, nếu có một quản trị viên tài năng, đầy nhiệt huyết và tò mò thì anh ấy cũng có thể tự vận hành
Serverless (ví dụ: [KNative](https://knative.dev)). ![aws_costs_twitter_1](/images/content/aws_costs_twitter_1.png)

### Serverless Funktionen vs Microservices:

### Willkommen bei unserem Online-Shop Wir freuen uns, Sie hier auf unserem Online-Shop begrüßen zu dürfen. Hier finden
Sie alle Produkte, die Sie brauchen, um Ihr Leben einfacher und angenehmer zu machen. #### Unsere Produkte Unser
Sortiment umfasst eine breite Palette von Produkten, darunter Elektronik, Kleidung, Haushaltsartikel und vieles mehr.
Wir sind stolz darauf, nur Produkte von höchster Qualität anzubieten, die von Experten auf ihrem Gebiet sorgfältig
ausgewählt wurden. #### Versand Wir bieten weltweite Lieferungen für alle unsere Produkte an. Die Versandkosten
variieren je nach Standort und Größe der Bestellung. Bitte beachten Sie, dass internationale Bestellungen Zölle und
Gebühren enthalten können. #### Kundendienst Unser Kundendienst-Team steht Ihnen jederzeit zur Verfügung, um Ihre
Fragen zu beantworten und Ihnen bei Problemen zu helfen. Wir möchten sicherstellen, dass Sie mit Ihrem Einkauf bei uns
vollständig zufrieden sind. Vielen Dank, dass Sie unseren Online-Shop besucht haben. Wir hoffen, dass Sie genau das
finden, was Sie suchen, und freuen uns darauf, Ihnen dabei zu helfen, das Leben einfacher und angenehmer zu gestalten.

#### Microservices

Một Microservice không trạng thái điển hình chịu trách nhiệm cho một chức năng / miền nhất định và được triển khai trong
một môi trường triển khai Container. Môi trường này chịu trách nhiệm về cơ sở hạ tầng, bảo mật, tường lửa, logging,
metriks, Secret, networks, backups và nhiều hơn nữa. Một lợi thế lớn là Microservice có thể được tích hợp và kiểm tra
địa phương chỉ với vài tài nguyên và có thể sử dụng trên mọi địa điểm đám mây / máy chủ.

#### Chức năng không có máy chủ (Serverless)

Một lời đùa nhỏ trước: Nghịch lý, nhưng đúng - Các chức năng Serverless phụ thuộc mạnh vào môi trường máy chủ. :) Một
chức năng Serverless điển hình cũng chỉ quan tâm đến một chức năng / miền cụ thể và được viết bằng mã nguồn tinh khiết
mà không cần Framework để nhanh hơn một Microservice (cũng là một bài tập tốt cho MicroServices). Một lợi thế lớn là các
chức năng Serverless được tự động điều chỉnh quy mô. Tuy nhiên, mỗi chức năng Serverless đều cần một lượng lớn GlueCode
để xác định cơ sở hạ tầng - Bảo mật, Tường lửa, Mạng, Nhật ký, Chỉ số, Bí mật, Bộ nhớ đệm, Sao lưu và nhiều hơn nữa. Vì
vậy, một chức năng đơn giản như sao chép một tệp có thể nhanh chóng tăng lên tới 1500 dòng mã (bao gồm IaC). Chi phí
quản trị dịch chuyển từ Quản trị sang Phát triển với tỷ lệ 1: N (1 đến Chức năng Serverless). Do đó, kiến thức và thực
hiện không được tập trung nữa và có thể trở nên không ổn định nhanh chóng. Bên cạnh đó là chi phí bảo trì tăng lên. Kể
cả khi làm các bài kiểm tra tích hợp thực sự, đối với Serverless thì hiếm gặp hoặc chỉ có thể thực hiện với nỗ lực lớn.
Cuối cùng, độ phức tạp của chức năng Serverless cao hơn nhiều so với một Microservice đơn lẻ. Độ phức tạp cao cũng có
nghĩa là khả năng bảo trì thấp hơn. Những thành viên mới trong đội có thể gặp khó khăn hơn và cần có nhiều kiến thức
tiên quyết hơn.

### Serverless và Điện toán đám mây nói chung

Hầu hết các công nghệ Cloud không được cập nhật đầy đủ. Ví dụ, Node.js, Java, Python và các ngôn ngữ hoặc công nghệ khác
thường khó cập nhật, thường chỉ có thể đợi đến khi mới có cập nhật mới. Các công nghệ hiện đại và chuẩn như MongoDB,
MySQL, Kafka, NATS, RabbitMQ, Redis, Prometheus, InfluxDB, Grafana, Kibana, Elastic Search vv cũng không có sẵn hoặc quá
đắt. Nếu thiếu các dịch vụ chuẩn này, ta thường sử dụng các giải pháp lỗi thời như Webhooks để giao tiếp bên ngoài. Thêm
vào đó, phạm vi hoạt động bị giới hạn đáng kể trong các vấn đề như việc đáp ứng quy định, tuân thủ quy định, bảo vệ dữ
liệu và khả năng chịu lỗi. Vì vậy, Cloud nên được vận hành độc lập, để có thể dễ dàng chuyển đổi giữa AWS, Azure,
Google và On-Premise và so sánh chi phí. Giới hạn cũng thường xảy ra trong Cloud, dẫn đến các giải pháp tạm thời sáng
tạo, làm tăng độ phức tạp. Testing kết hợp cũng có thể trở nên đắt đỏ, vì mỗi nhà phát triển cần một môi trường phát
triển riêng trong Cloud, vì nhiều dịch vụ Cloud khó hoặc không thể được kiểm tra địa phương. Tuy nhiên, Cloud cũng đắt
đỏ mà không cần kiểm tra. Trong khi các hệ thống On-Premise chủ yếu tính tới chi phí phần cứng, thì trong Cloud bạn cũng
phải trả thêm cho lưu lượng mạng, một số dịch vụ chuẩn và thậm chí cả các thuế. Bên cạnh đó, bạn dễ bị mất quan sát
trong Cloud, vì nó không phải là về trải nghiệm người dùng mà là về tiền bạc. Chi phí được giấu kín đến mức bạn chỉ nhận
ra nó khi quá muộn. Các nguyên tắc cơ bản về kiến trúc và cơ sở hạ tầng phải được tái phát minh trong Cloud và đặc biệt
là trong lĩnh vực Serverless, vì việc triển khai tùy thuộc rất nhiều vào các chức năng có sẵn. Luôn khi tôi thiết kế
kiến trúc, tôi nghĩ: "Đó có thể là một dịch vụ đơn." Đối với tôi, Serverless là một ý tưởng thú vị và có khả năng mở
rộng tốt, nhưng không phải làm giảm chi phí. Ngược lại, nó đòi hỏi nhiều kiến thức và thời gian phát triển hơn.
Serverless hoặc Cloud đều đòi hỏi một kỷ luật và kiến thức trước. Nếu không có kiến thức về hệ thống On-Premise, thì sẽ
không dễ dàng hơn khi cần liên quan đến Cloud. Làm thế nào các nhà phát triển có thể thu thập kiến thức về cơ sở hạ tầng
bổ sung? Tôi sẽ lựa chọn một Kubernetes Cluster được quản lý tốt để thay thế cho Kiến trúc Cloud. Các nhân viên không
phát triển. Nhiều nhà phát triển không có kỷ luật khi viết mã. Rất tiếc, điều này lại áp dụng cho 80% nhà phát triển. Vì
vậy, làm thế nào những nhà phát triển này có thể phục vụ Cloud? Quan trọng là doanh nghiệp hiểu rõ thách thức và tác
động của kiến trúc Serverless Cloud. Điều này đòi hỏi không chỉ kiến thức kỹ thuật, mà còn cần tiếp cận chiến lược. Việc
di chuyển sang Cloud không đáp ứng được một cách không suy nghĩ có thể dẫn đến sự phức tạp, chi phí cao và làm cho những
nhà phát triển bị áp lực. Tóm lại, Serverless trong Cloud là một khái niệm hứa hẹn nhưng cần được xem xét cẩn thận. Chi
phí, độ phức tạp, tính bảo trì và khả năng của đội ngũ phát triển phải được cân nhắc. Mỗi doanh nghiệp có các yêu cầu và
ưu tiên khác nhau. Bạn nên đưa ra quyết định đúng đắn, xem Serverless trong Cloud là giải pháp phù hợp hay các cách tiếp
cận khác như một Kubernetes Cluster được quản lý tốt là sự lựa chọn tốt hơn. Sự thành công của Serverless và Cloud
Computing đòi hỏi sự kết hợp giữa chuyên môn kỹ thuật, kế hoạch chiến lược và sự hiểu rõ rõ nhu cầu kinh doanh. Chỉ khi
đó, bạn mới có thể nhìn thấy qua "ảo tưởng" của Serverless và đưa ra quyết định đúng đắn cho sự phát triển phần mềm của
chính mình.

### Kết luận

Việc giới thiệu các chức năng Serverless trên nền tảng đám mây hứa hẹn tính linh hoạt, khả năng mở rộng và giải phóng
các nhà phát triển khỏi các nhiệm vụ về cơ sở hạ tầng. Tuy nhiên, không nên mắc phải ảo tưởng này. Chuyển sang đám mây
và sử dụng Serverless đem lại một loạt thách thức. Ngoài việc phát triển chính, nhà phát triển cũng phải học một "ngôn
ngữ" mới và đảm nhận nhiều trách nhiệm hơn mà không có hỗ trợ tương ứng. Tính phức tạp của Serverless thường cao hơn so
với Microservices, vì các nhà phát triển phải đảm nhận nhiều nhiệm vụ bổ sung như xác định cơ sở hạ tầng, bảo mật và mở
rộng. Kiểm tra tích hợp thực sự khó khăn và kiến thức và kinh nghiệm về vận hành rất quan trọng trên đám mây. Đám mây
cũng mang đến nhiều thách thức khác. Nhiều công nghệ đám mây không được cập nhật mới nhất và sử dụng các dịch vụ tiêu
chuẩn hiện đại có thể đắt tiền hoặc thậm chí không thể. Quy định, tuân thủ và bảo vệ dữ liệu giới hạn không gian hoạt
động. Ngoài ra, chi phí trong đám mây dễ dàng trôi ra khỏi tầm kiểm soát và việc theo dõi chi tiêu có thể nhanh chóng
mất. Tổng quan, cần cân nhắc kỹ lưỡng các ưu và nhược điểm của Serverless và đám mây. Các công ty nên xem xét các yêu
cầu cụ thể của họ, khả năng có sẵn trong nhóm và tác động dài hạn của việc di chuyển sang đám mây. Một quyết định đúng
đắn dựa trên phân tích toàn diện là quan trọng để đạt được sự thành công và hiệu quả kinh doanh của dự án. Cuối cùng,
các công ty cần hỗ trợ nhà phát triển một cách thích hợp, đánh giá thực tế về chi phí và độ phức tạp của đám mây và xem
xét các giải pháp thay thế như các cụm Kubernetes được quản lý tốt. Với chiến lược rõ ràng và sự hiểu biết sâu sắc về
nhu cầu của riêng họ, các công ty có thể tận dụng các lợi ích của đám mây và Serverless tối đa và nhìn thấy thực tế.

### Liên hệ

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
