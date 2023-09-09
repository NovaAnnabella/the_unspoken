---
title: "Cấp độ kiểm tra: Tìm thấy sự cân đối đúng"
date: 2023-05-31
author: "Nova Annabella"
slug: test_level
tags: [ Testing, Software Testing, Test Levels, Mock Tests, Unit Tests, Integration Tests, Component Tests, Contract Tests, End-to-End Tests ]
categories: [ Technology, Software Development, Quality Assurance ]
description: "Tìm đúng sự cân đối khi lựa chọn các cấp độ thử nghiệm phù hợp cho việc kiểm thử phần mềm"
draft: false
images:
  - "/images/content/martin_fowler_testing.png"
card: "summary_large_image"
---


# Các cấp độ kiểm thử: Tìm kiếm sự cân đối đúng

[![testebenen](/images/content/martin_fowler_testing.png)](https://martinfowler.com/articles/microservice-testing/)

### Giới thiệu

Chủ đề Kiểm thử dường như đến nay vẫn là mảnh đất mới với rất nhiều không gian cho sự giải thích. Ngọn núi kiểm thử truyền thống đã bị đặt ra câu hỏi và đã có những ngọn núi kiểm thử mới xuất hiện. Theo quan điểm của tôi, chúng ta không cần ngọn núi kiểm thử, mà chỉ cần hiểu rõ về những gì cần được kiểm thử. Các bài kiểm tra ở các cấp thấp hơn thường ít có ý nghĩa. Trọng tâm nên đặt vào việc kiểm thử hành vi, để đảm bảo rằng API hoặc giao diện người dùng hoạt động như mong đợi. Một cái nhìn toàn diện về các loại kiểm thử có thể được tìm thấy ở đây: [Martinfowler Testing](https://martinfowler.com/articles/microservice-testing/).

### Mức độ 1 - Kiểm tra giả lập & Kiểm tra đơn vị

Mục tiêu: Thực hiện các phần phần mềm có thể kiểm tra nhỏ nhất trong ứng dụng để xác định xem chúng có hoạt động như dự
kiến hay không. Các bài kiểm tra Mock và Unit có thể phản tác dụng và thường cản trở quá trình phát triển. Những bài
kiểm tra này thường tách rời khỏi ngữ cảnh và có ít liên quan đến thực tế. Chúng thường chỉ để duy trì các chức năng
không cần thiết thông qua các bài kiểm tra đơn vị hiện tại. Khi Mocks được thêm vào, nó trở thành một công việc tự phục
vụ. Kết quả mong đợi của các bài kiểm tra Mock chỉ giới hạn ở những gì đã được định rõ trong Mock ban đầu. Người dùng
cuối không quan tâm đến các chức năng nội bộ. Ví dụ, trong một tình huống đăng nhập `loginUser(name, password,
securityAlgorithmus)`. Nếu bài kiểm tra đơn vị thực hiện một kiểm tra Null trên tham số `securityAlgorithm`, thì đang
kiểm tra quá nhiều, vì người dùng không thể đặt tham số `securityAlgorithm`.

### Cấp độ 2 - Kiểm thử Tích hợp

Mục đích: Kiểm tra các con đường giao tiếp và tương tác giữa các thành phần để phát hiện lỗi giao diện. Các bài kiểm
tra tích hợp cung cấp thông tin quý giá về khả năng hoạt động và độc lập của các phần khác nhau của ứng dụng. Với ít hơn
các mocks, các bài kiểm tra trở nên dễ hiểu hơn. Tuy nhiên, họ vẫn thiếu bối cảnh, và có nguy cơ rằng các bài kiểm tra
tích hợp chỉ đơn giản là các bài kiểm tra đơn vị được cải trang với ít mocks hơn.

### Cấp độ 3 - Kiểm tra thành phần

Mục đích: Hạn chế phạm vi phần mềm được kiểm thử trên một phần của hệ thống cần kiểm tra, thao tác hệ thống qua các giao
diện mã nội bộ và sử dụng Testdoubles để cô lập mã cần kiểm tra khỏi các thành phần khác. Các kiểm thử thành phần cung
cấp một lượng lớn thông tin về chất lượng và khả năng hoạt động của ứng dụng. Thay vì sử dụng Mocks, bạn cuối cùng đang
kiểm tra ứng dụng của mình. Biên giới giữa kiểm thử thành phần và kiểm thử từ đầu đến cuối không đáng kể. Với một môi
trường kiểm thử tốt, biên giới giữa chúng thường mờ nhạt, do đó việc kiểm tra hành vi thực thay vì các chức năng cô lập
và không liên quan đến ngữ cảnh trở nên khả thi. Tuy nhiên, việc tạo thêm các lớp kiểm thử như các Stubs, Fakes và Mocks
trong mã sản phẩm có thể mang lại nhiều công việc bảo dưỡng bổ sung.

### Cấp độ 4 - Kiểm thử hợp đồng

Mục đích của khối mã này là để kiểm tra các tương tác ở biên giới của một dịch vụ bên ngoài và 
đảm bảo rằng nó đáp ứng yêu cầu hợp đồng của một dịch vụ tiêu thụ.

Bài kiểm tra Hợp đồng thường giống với bài kiểm tra Cầu thành, và sự khác biệt giữa chúng là tối thiểu. Một số nhà phát triển 
liên kết các bài kiểm tra này với Pact Tests, những cái hoạt động về cơ bản như các bài kiểm tra đơn vị với một máy chủ ở giữa. Tuy nhiên, 
công sức bỏ ra để duy trì những bài kiểm tra này có thể không đáng giá. Chẳng hạn, một Pact Test có thể kiểm tra 
REST API `loginUser?name=aa&password=bb)` và mong đợi một phản hồi JSON-Schema đã được tải lên máy chủ Pact trước đó. 
Lược đồ này là tĩnh và dễ bị lỗi như các định dạng ngày tháng sai hoặc múi giờ trong 
phản hồi API. Hậu quả tiêu cực có thể rất lớn.


### Cấp độ 5 - Kiểm tra End-to-End (còn được gọi là Kiểm tra Black-Box)

Mục đích: Kiểm tra xem hệ thống có đáp ứng được yêu cầu bên ngoài và đạt được mục tiêu của nó bằng cách kiểm tra toàn bộ
hệ thống từ đầu đến cuối. Các bài kiểm tra từ đầu đến cuối đáng tin cậy và vững chắc. Một khi đã vượt qua rào cản của
việc xây dựng môi trường kiểm tra, công sức bỏ ra sẽ được đền đáp. Những bài kiểm tra này mô phỏng hành vi thực tế và
loại bỏ nhu cầu của Mocks. Lỗi xảy ra ít hơn và dễ dàng tái tạo lại ở cấp độ cục bộ. Việc gỡ lỗi tốn kém và thực hiện
việc ghi log trong sản xuất phần lớn được tránh, cũng như những sự cố hiếm hoi. Các nhà phát triển ít khi làm việc với
dữ liệu sản xuất, điều này giảm bớt trách nhiệm và tăng tập trung. Hơn nữa, các quy trình tự động như cập nhật phần mềm
tự động giúp thực hiện, vì hành vi đã được kiểm tra trước đó. Có thêm nhiều lợi ích! Khi các bài kiểm tra được viết theo
một hình thức có thể tái sử dụng, chúng có thể được tích hợp vào các bài kiểm tra tải để có được hình ảnh toàn diện về
chức năng. Những bài kiểm tra này cũng có thể được thực hiện liên tục trong môi trường sản xuất và cung cấp cái nhìn
thực tế về tình trạng các quy trình làm việc khác nhau. Khi một phần hệ thống, như ví dụ như một dịch vụ REST bên ngoài,
offline, người ta có thể ngay lập tức xác định các quy trình làm việc của người dùng nào bị ảnh hưởng.

### Kết luận

Tóm lại, việc kiểm thử là một khía cạnh quan trọng của phát triển phần mềm, và việc lựa chọn các cấp độ kiểm thử phụ
thuộc vào các yêu cầu và mục tiêu cụ thể của ứng dụng. Trong khi Kiểm thử giả lập và Kiểm thử đơn vị có thể bị hạn chế
về hiệu quả, Kiểm thử tích hợp và Kiểm thử thành phần cung cấp những cái nhìn quý giá về hành vi và hiệu năng của ứng
dụng. Kiểm thử hợp đồng giúp kiểm tra các tương tác với các dịch vụ bên ngoài, nhưng sự phân biệt của nó với Kiểm thử
thành phần có thể tối thiểu. Cuối cùng, Kiểm thử từ đầu đến cuối cung cấp mức độ tin cậy cao nhất vào chức năng của hệ
thống và cho phép kiểm thử toàn diện của toàn bộ ứng dụng. Thông qua việc lựa chọn các mức độ kiểm thử phù hợp và kết
hợp chúng một cách hiệu quả, các nhà phát triển có thể đảm bảo chất lượng, độ tin cậy, và sự mạnh mẽ của phần mềm của
bạn.

### Liên hệ

[Vấn đề GitHub](https://github.com/NovaAnnabella/the_unspoken/issues/new/choose).

