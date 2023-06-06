---
title: Testebenen: Tìm thấy sự cân bằng đúng đắn
date: 2023-05-31
author: "Nova Annabella"
slug: test_level
tags: [ Testing, Software Testing, Test Levels, Mock Tests, Unit Tests, Integration Tests, Component Tests, Contract Tests, End-to-End Tests ]
categories: [ Technology, Software Development, Quality Assurance ]
description: Tìm thấy sự cân bằng thích hợp trong việc chọn các cấp độ kiểm thử phù hợp cho phần mềm.
draft: false
images:
  - "/images/content/martin_fowler_testing.png"
card: "summary_large_image"
---


# Test Levels: Tìm cân bằng đúng

Test Levels là một phương pháp kiểm tra được sử dụng để đảm bảo chất lượng và độ tin cậy của phần mềm. Nhưng sự tăng cường của các bình dân phải cân đối với các tiêu chuẩn chất lượng và thời gian sử dụng. Trong bài viết này, chúng tôi sẽ tìm hiểu về các cấp độ kiểm tra khác nhau và làm thế nào để tìm ra sự cân bằng đúng giữa các loại kiểm tra khác nhau.

[![testebenen](/images/content/martin_fowler_testing.png)](https://martinfowler.com/articles/microservice-testing/)

### Giới thiệu

Chủ đề Kiểm thử dường như vẫn là lãnh vực chưa được khám phá rộng rãi với nhiều không gian để diễn giải cho đến ngày
nay. Hình kim cương kiểm thử truyền thống đã bị đặt dấu hỏi và các hình kim cương kiểm thử mới đã được tạo ra. Theo ý
kiến của tôi, không cần phải có hình kim cương kiểm thử, mà cần phải hiểu rõ những gì cần phải kiểm tra. Những bài kiểm
tra ở các cấp độ thấp thường ít có ý nghĩa. Trọng tâm nên được đặt vào việc kiểm tra hành vi, để đảm bảo rằng API hoặc
UI hoạt động như mong muốn. Thông tin chi tiết về các loại kiểm thử có thể được tìm thấy tại đây: [Martin Fowler
Testing](https://martinfowler.com/articles/microservice-testing/).

### Cấp độ 1 - Kiểm tra giả lập & Kiểm tra đơn vị

Mục tiêu: Thực hiện các phần mềm nhỏ nhất có thể trong ứng dụng để xác định liệu chúng hoạt động đúng như mong đợi hay
không. Mock-Tests và Unit-Tests có thể gây phản tác dụng và thường gây trở ngại trong quá trình phát triển. Những bài
kiểm tra này thường không liên quan đến ngữ cảnh và không liên quan đến thực tế. Chúng thường chỉ đóng vai trò duy trì
các chức năng không cần thiết thông qua các Unit-Tests hiện có. Khi các Mocks được thêm vào, nó trở thành tự phục vụ.
Kết quả được mong đợi của các bài kiểm tra Mock bị giới hạn bởi điều được xác định trong Mock gốc. Người dùng cuối không
quan tâm đến các chức năng nội bộ. Ví dụ, trong kịch bản đăng nhập `loginUser (tên, mật khẩu, thuật toán bảo mật)`. Nếu
Unit-Test thực hiện kiểm tra Null cho tham số `securityAlgorithm`, quá nhiều thứ được kiểm tra, vì người dùng không thể
thiết lập tham số `securityAlgorithm`.

### Cấp độ 2 - Kiểm thử tích hợp

Mục đích: Kiểm tra các kênh giao tiếp và tương tác giữa các thành phần để phát hiện các lỗi giao diện. Kiểm thử tích
hợp cung cấp những hiểu biết quý giá về hiệu suất và sự độc lập của các phần khác nhau của ứng dụng. Với ít Mock hơn,
các bài kiểm tra trở nên dễ hiểu hơn. Tuy nhiên, chúng vẫn thiếu bối cảnh và có nguy cơ kiểm thử tích hợp chỉ là các bài
kiểm thử đơn vị được ẩn đi với ít hơn các Mock.

### Cấp độ 3 - Kiểm tra thành phần

Mục đích: Giới hạn phạm vi của phần mềm được kiểm thử trên một phần của hệ thống được kiểm tra, điều khiển hệ thống
thông qua các interface mã nội bộ và sử dụng Testdoubles để cô lập mã được kiểm tra từ các thành phần khác.  Kiểm tra
thành phần cung cấp nhiều thông tin về chất lượng và hiệu suất của ứng dụng. Thay vì sử dụng Mock, bạn cuối cùng đã kiểm
tra ứng dụng của mình. Giới hạn giữa kiểm tra thành phần và kiểm tra End-to-End không quan trọng. Với một môi trường
kiểm tra tốt, giới hạn giữa chúng thường được mờ nhạt, cho phép kiểm tra hành vi thực tế thay vì các chức năng cô lập và
không có ngữ cảnh. Tuy nhiên, việc tạo ra các lớp kiểm thử bổ sung như Komponenten-Stubs, Fakes và Mocks trong mã sản
phẩm có thể gây ra thêm công việc bảo trì.

### Level 4 - Kiểm tra hợp đồng

Mục đích của khối mã này là kiểm tra tương tác với một dịch vụ bên ngoài và đảm bảo rằng nó đáp ứng yêu cầu hợp đồng của
một dịch vụ tiêu thụ. Kiểm thử hợp đồng thường tương tự như kiểm thử thành phần, và khác biệt giữa chúng là tối thiểu.
Một số nhà phát triển liên kết các kiểm thử này với kiểm thử Pact, các kiểm thử này thực tế là Unittests với một máy
chủ. Tuy nhiên, việc duy trì các kiểm thử này có thể không đáng giá. Ví dụ, kiểm thử Pact có thể kiểm tra REST-API
`loginUser?name=aa&password=bb)` và mong đợi một phản hồi theo JSON-Schema, đã được tải lên trước đó lên máy chủ Pact.
Mẫu này là tĩnh và dễ bị sai lệch như định dạng ngày tháng hoặc múi giờ sai trong phản hồi API. Những tác động tiêu cực
có thể rất lớn.

### Level 5 - Kiểm tra end-to-end (còn được gọi là kiểm tra Black-Box)

Mục đích: Kiểm tra xem hệ thống có đáp ứng yêu cầu bên ngoài và đạt được mục tiêu của mình bằng cách thử nghiệm toàn bộ
hệ thống từ đầu đến cuối. Kiểm thử End-to-End là đáng tin cậy và mạnh mẽ. Sau khi vượt qua được các khó khăn trong việc
thiết lập môi trường kiểm thử, công sức tiêu tốn sẽ được đền đáp. Những kiểm thử này mô phỏng hành vi thực tế và loại bỏ
nhu cầu sử dụng phần mô phỏng. Lỗi xảy ra ít hơn và dễ tái hiện ở cấp độ địa phương. Việc gỡ lỗi phức tạp và theo dõi
biên bản sản xuất được tránh nhiều hơn, cũng như các sự cố hiếm gặp. Nhà phát triển ít khi làm việc với dữ liệu sản
xuất, điều này làm giảm trách nhiệm và tăng tập trung. Ngoài ra, những phần tự động như các cập nhật phần mềm tự động
làm cho việc thực hiện dễ dàng hơn, vì hành vi đã được kiểm thử trước đó. Có nhiều lợi ích khác nữa! Khi những kiểm thử
được viết dưới dạng có thể tái sử dụng, chúng có thể được tích hợp vào kiểm thử tải để có được hình ảnh toàn diện về
chức năng. Những kiểm thử này cũng có thể được thực hiện liên tục trong môi trường sản xuất và cung cấp cái nhìn thời
gian thực về trạng thái các luồng công việc khác nhau. Nếu một phần hệ thống, chẳng hạn như một dịch vụ REST bên ngoài,
bị ngừng hoạt động, người dùng có thể xác định ngay lập tức các luồng công việc nào bị ảnh hưởng.

### Kết luận

Tóm lại, kiểm thử là một khía cạnh quan trọng của phát triển phần mềm, và việc lựa chọn các cấp độ kiểm thử phụ thuộc
vào các yêu cầu và mục tiêu cụ thể của ứng dụng. Trong khi các kiểm thử giả định và kiểm thử đơn vị có thể bị giới hạn
về hiệu quả, các kiểm thử tích hợp và kiểm thử thành phần cung cấp thông tin quý giá về hành vi và hiệu suất của ứng
dụng. Các kiểm thử hợp đồng giúp kiểm tra tương tác với các dịch vụ bên ngoài, nhưng phân biệt giữa chúng và kiểm thử
thành phần có thể rất nhỏ. Cuối cùng, các kiểm thử toàn bộ hệ thống cung cấp mức độ tin cậy cao nhất vào tính năng của
hệ thống và cho phép kiểm thử toàn diện của toàn bộ ứng dụng. Bằng cách lựa chọn các cấp độ kiểm thử phù hợp và kết hợp
chúng một cách hiệu quả, các nhà phát triển có thể đảm bảo chất lượng, độ tin cậy và sự đáng tin cậy của phần mềm của
mình.

### Liên hệ

[GitHub Issues](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).
