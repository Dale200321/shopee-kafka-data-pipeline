import json
import time
import random
from kafka import KafkaProducer

# 1. Cấu hình kết nối tới Kafka
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic_name = 'shopee_orders'

print(" Đang bắt đầu bơm đơn hàng vào Kafka... Nhấn Ctrl+C để dừng.")

# 2. Vòng lặp giả lập đơn hàng
customers = ['Ivan', 'Peter', 'Gemini', 'An', 'Binh']
products = ['Iphone 15', 'Macbook M3', 'Ban phim co', 'Chuot logitech']

try:
    while True:
        data = {
            'customer_name': random.choice(customers),
            'product_name': random.choice(products),
            'price': round(random.uniform(10, 2000), 2)
        }
        
        # Bắn dữ liệu lên băng chuyền Kafka
        producer.send(topic_name, value=data)
        print(f"📦 Đã gửi đơn hàng: {data}")
        
        time.sleep(2) # Bắn đơn hàng mỗi 2 giây
except KeyboardInterrupt:
    print("🛑 Đã dừng bơm dữ liệu.")
