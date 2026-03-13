Shopee Data Pipeline and Real-time Analytics
Dự án này tập trung vào việc xây dựng hệ thống xử lý dữ liệu đơn hàng theo thời gian thực và thực hiện phân tích thống kê trên tập dữ liệu thu thập được. Các thao tác được thực hiện trên VSCode và có sự hỗ trợ của AI Gemini.

1. Công nghệ sử dụng
Hệ thống: Docker, Docker-compose.

Luồng dữ liệu: Apache Kafka, Zookeeper.

Cơ sở dữ liệu: PostgreSQL.

Phân tích: Python (Pandas, Statsmodels).

2. Quy trình thực hiện
Giả lập luồng dữ liệu đơn hàng từ Shopee và đẩy vào Kafka Topic.

Sử dụng Consumer để tiếp nhận dữ liệu và lưu trữ vào cơ sở dữ liệu PostgreSQL.

Kết nối dữ liệu từ PostgreSQL vào môi trường Python để thực hiện phân tích.

3. Nội dung phân tích và Kết quả
Trong dự án này, tôi đã thực hiện mô hình hồi quy tuyến tính (OLS) để kiểm tra mối tương quan giữa thời gian giao dịch và giá trị đơn hàng.

Kết quả từ 400 quan sát cho thấy chỉ số R-squared đạt 0.00% và P-value là 0.9.

Kết luận: Giá trị đơn hàng trong cửa sổ thời gian ngắn mang tính ngẫu nhiên cao. Kết quả này là cơ sở để đề xuất việc mở rộng thêm các biến số khác như danh mục sản phẩm hoặc hành vi người dùng trong các giai đoạn tiếp theo.

