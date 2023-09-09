---
title: "Máy chủ ảo không tồn tại & Đám mây"
date: 2023-05-24
author: "Nova Annabella"
slug: illusion_serverless_cloud
tags: [ Development, Serverless, Cloud, Microservices, Scalability, Architecture, Infrastructure ]
categories: [ Technology, Software, Cloud ]
description: "Thách thức và thực tế của các chức năng không máy chủ trong đám mây. Những cái nhìn quý giá cho các doanh nghiệp đang xem xét việc di chuyển đến đám mây"
draft: false
images:
  - "/images/content/onprem_vs_cloud.png"
card: "summary_large_image"
---


# Ảo tưởng về Chức năng Serverless trong Cloud

![aws_costs_twitter_1](/images/content/onprem_vs_cloud.png)

### Giới thiệu

Tôi thất vọng với việc quảng cáo thắng trên lý trí quá nhiều lần. Nhiều người quản lý coi thường chuyên gia của họ - những nhà phát triển. Điều này cũng đúng với việc chuyển đổi sang đám mây. Spoiler: Ai cần tiết kiệm tiền nên tránh đám mây. Bởi vì từ khóa mới "Serverless" trong đám mây có nghĩa là: Bạn lo về phần mềm, chúng tôi lo về phần cứng. Tuy nhiên, ai có quản trị viên giỏi, đầy động lực và tò mò, họ có thể tự vận hành serverless (ví dụ: [KNative](https://knative.dev)).

![aws_costs_twitter_1](/images/content/aws_costs_twitter_1.png)

### Các chức năng không máy chủ vs Microservices:



#### Microservices

Một Microservice không trạng thái tiêu chuẩn chăm sóc một chức năng / lĩnh vực cụ thể và được triển khai trong một môi
trường điều phối container. Môi trường này chăm sóc cơ sở hạ tầng, bảo mật, tường lửa, logging, số liệu, bí mật, mạng,
sao lưu và nhiều hơn nữa. Một lợi ích lớn là rằng một dịch vụ micro có thể được kiểm tra tích hợp tại chỗ với ít tài
nguyên và đảm bảo không phụ thuộc vào Cloud / Server (có thể sử dụng ở mọi nơi).

#### Chức năng không máy chủ


Một câu chuyện cười nhỏ trước: Mâu thuẫn, nhưng đúng - Các hàm Serverless phụ thuộc nhiều vào môi trường máy chủ. :)
Một hàm Serverless điển hình cũng chỉ chăm sóc cho một chức năng / lĩnh vực cụ thể và được viết bằng
mã thuần túy, để nhanh hơn một Microservice (Cũng là một bài tập tốt cho MicroServices). Một lợi thế lớn
là Các chức năng Serverless tự động căn chỉnh. Tuy nhiên, mỗi chức năng Serverless đều cần một
lượng GlueCode đáng kể để xác định cơ sở hạ tầng - Bảo mật, tường lửa, mạng lưới, ghi lô, số liệu,
Bí mật, Bộ nhớ đệm, Sao lưu và nhiều thứ khác nữa.
Vì vậy, một chức năng đơn giản như sao chép một tệp bao gồm API có thể nhanh chóng chiếm đến 1500 dòng mã (bao gồm IaC)
chiếm.
Chi phí quản trị được chuyển từ quản trị sang phát triển theo tỷ lệ 1:N (1 so với
Các chức năng Serverless). Kiến thức và cài đặt không còn được
tập trung và có thể nhanh chóng trở nên không ổn định. Đi kèm với đó là chi phí bảo dưỡng tăng.
Các bài kiểm tra tích hợp thực sự cũng là hiếm khi hoặc chỉ liên quan đến Serverless với nhiều công sức.
Cuối cùng, độ phức tạp của các hàm Serverless đáng kể cao hơn so với một Microservices đơn lẻ.
Độ phức tạp cao hơn cũng có nghĩa là khả năng bảo dưỡng thấp hơn. Các thành viên mới trong đội sẽ gặp khó khăn hơn và cần nhiều
kiến thức trước.

### Serverless và Cloud nói chung

Hầu hết các công nghệ Điện toán Đám mây không được cập nhật mới nhất. Ví dụ, Node.js, Java, Python và các ngôn ngữ hoặc công nghệ khác thường không dễ dàng cập nhật, phần lớn chỉ có thể chờ đợi.
Công nghệ tiên tiến và chuẩn như MongoDB, MySQL, Kafka, NATS, RabbitMQ, Redis, Prometheus, InfluxDB, Grafana,
Kibana, Elastic Search vv. hoặc không có hoặc quá đắt.
Không có những dịch vụ chuẩn như vậy, bạn thường rơi vào thời đại đồ đá ảo và sử dụng các giải pháp lỗi thời, ví dụ,
Webhooks để giao tiếp ra ngoài. Thêm vào đó, quyền hành hành động liên quan đến các vấn đề như quy định,
Tuân thủ, bảo mật dữ liệu và đảm bảo an toàn khi mất dòng lớn nằm trong phạm vi hạn chế.

Đám mây nên do đó được vận hành theo cách trung lập, để có thể nhanh chóng chuyển đổi giữa AWS, Azure, Google, On-Premise vv. so sánh và
So sánh chi phí.
Giới hạn cũng thường xuất hiện trong Đám mây, dẫn đến các giải pháp vòng qua, làm tăng độ phức tạp
tăng lên. Cả việc kiểm tra tích hợp cũng có thể trở nên đắt đỏ, vì mỗi nhà phát triển cần một môi trường phát triển riêng trong Đám mây
cần, vì nhiều dịch vụ Đám mây hầu như không thể hoặc không thể thử nghiệm tại chỗ.
Nhưng cả việc không có thử nghiệm cũng khiến Đám mây tốn kém. Trong khi với hệ thống On-Premise trước hết
Chi phí phần cứng phát sinh, trong Đám mây bạn phải trả thêm cho Traffic, một số Dịch vụ chuẩn và thậm chí cho
Thuế đánh thuế nhiều lần. Ngoài ra, bạn dễ mất kiểm soát trong Đám mây, bởi điều quan trọng không phải là
Tính thân thiện với người dùng, mà là về tiền. Chi phí được ẩn đi đến mức bạn chỉ nhận ra khi đã quá muộn
là.

Cần phải tạo mới những nền tảng kiến trúc và cơ sở hạ tầng trong Đám mây và đặc biệt là trong lĩnh vực của Serverless
, vì việc triển khai phụ thuộc nhiều vào các chức năng có sẵn.
Mỗi khi tôi thiết kế kiến trúc, tôi lại nghĩ: "Điều này cũng có thể là một dịch vụ duy nhất".

Đối với tôi, Serverless là một ý tưởng thú vị và có thể mở rộng tốt, nhưng nó không giảm chi phí. Thay vào đó, nó yêu cầu nhiều kiến thức và thời gian hơn trong việc phát triển. Serverless hoặc Đám mây yêu cầu kỷ luật và kiến thức trước.
Nếu không có kiến thức về hệ thống On-Premise, việc sử dụng Đám mây sẽ không dễ dàng hơn.
Làm thế nào mà các nhà phát triển nên nắm bắt thêm kiến thức về cơ sở hạ tầng?

Tôi sẽ ưu tiên một Kubernetes Cluster quản lý tốt hơn so với Kiến trúc Đám mây.
Nhân viên không thể mở rộng. Nhiều nhà phát triển không có kỷ luật trong việc viết mã.
Thật không may, điều này áp dụng cho 80 phần trăm các nhà phát triển. Vậy vì sao những nhà phát triển này lại có thể vận hành Đám mây
có thể?

Điều quan trọng là doanh nghiệp nên hiểu rõ những thách thức và tác động của Kiến trúc không máy chủ và Đám mây
toàn diện. Điều này không chỉ yêu cầu kiến thức kỹ thuật mà còn cần có một phương pháp chiến lược. Một
Chuyển đổi không cẩn thận vào Đám mây có thể gây ra sự phức tạp, chi phí cao hơn và làm quá sức các nhà phát triển.

Tóm lại, có thể nói rằng Serverless trong Đám mây là một khái niệm đầy hứa hẹn, nhưng cần được xem xét cẩn thận.
Chi phí, độ phức tạp, khả năng duy trì và khả năng của nhóm phát triển phải
được xem xét.
Mỗi doanh nghiệp có những yêu cầu và ưu tiên khác nhau. Bạn nên đưa ra quyết định có căn cứ, liệu có
Serverless trong Đám mây là giải pháp đúng hay không hoặc lựa chọn thay thế như
ví dụ, Kubernetes Cluster tốt là lựa chọn tốt hơn.

Sử dụng thành công Serverless và Điện toán Đám mây yêu cầu sự kết hợp giữa kỹ thuật chuyên môn
kế hoạch chiến lược và một sự hiểu rõ rõ ràng về yêu cầu kinh doanh. Chỉ cần nhuận mạo về Serverless
nhìn rõ và đưa ra quyết định đúng cho phát triển phần mềm của riêng bạn.


### Kết luận

Việc giới thiệu chức năng Serverless trong Cloud mang lại sự linh hoạt, khả năng mở rộng và giảm tải cho các nhà phát
triển từ nhiệm vụ cơ sở hạ tầng. Tuy nhiên, không nên bị mê hoặc bởi ảo tưởng này. Việc chuyển đổi sang Cloud và sử dụng
các chức năng Serverless mang lại một loạt thách thức. Các nhà phát triển phải học một "ngôn ngữ" mới ngoài việc phát
triển thực tế và tự chịu trách nhiệm nhiều hơn mà không có sự hỗ trợ thích hợp. Độ phức tạp của các chức năng Serverless
thường cao hơn so với Microservices, vì các nhà phát triển phải đảm nhận nhiều nhiệm vụ bổ sung như xác định cơ sở hạ
tầng, bảo mật và mở rộng. Việc thử nghiệm tích hợp thực sự là khó khăn và kiến thức tiền đề cũng như kinh nghiệm cho
việc vận hành càng quan trọng hơn trong Cloud. Chính Cloud đem lại thêm nhiều thách thức. Nhiều công nghệ Cloud không
được cập nhật mới và việc sử dụng dịch vụ chuẩn hiện đại có thể đắt đỏ hoặc thậm chí không thể. Quy định quản lý, tuân
thủ và bảo vệ dữ liệu giới hạn khả năng chơi. Ngoài ra, chi phí trong Cloud dễ dàng ra khỏi tầm kiểm soát, và cái nhìn
tổng quan về chi tiêu nhanh chóng mất đi. Tổng thể, cần cân nhắc kỹ lưỡng ưu và nhược điểm của Serverless và Cloud. Các
doanh nghiệp nên xem xét yêu cầu cụ thể của mình, kiến thức hiện có trong nhóm và những ảnh hưởng dài hạn của việc di
chuyển sang Cloud. Việc đưa ra quyết định dựa trên một phân tích toàn diện là quan trọng đối với sự thành công và khả
năng sinh lợi của dự án. Cuối cùng, nó phụ thuộc vào các doanh nghiệp để hỗ trợ đúng mức cho nhà phát triển của họ,
đánh giá một cách thực tế chi phí và độ phức tạp của Cloud và cân nhắc đến các giải pháp thay thế như nhóm Kubernetes
được quản lý tốt. Với một chiến lược rõ ràng và sự hiểu biết vững chắc về nhu cầu của mình, các doanh nghiệp có thể tận
dụng tối đa lợi ích của Cloud và chức năng Serverless và nhìn thấu ảo tưởng.

### Liên hệ

[Vấn đề GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
