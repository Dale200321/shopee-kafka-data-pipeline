import json
import psycopg2
from kafka import KafkaConsumer

# 1. Kết nối tới Postgres (Cái kho)
conn = psycopg2.connect(
    host="localhost",
    database="shopee_data",
    user="ivan_admin",
    password="password123",
    port="5432"
)
cursor = conn.cursor()

# 2. Kết nối tới Kafka (Cái băng chuyền)
consumer = KafkaConsumer(
    'shopee_orders',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("🕵️ Consumer đang đợi hốt đơn hàng từ Kafka... Nhấn Ctrl+C để dừng.")

try:
    for message in consumer:
        order = message.value
        
        # 3. Đổ dữ liệu vào bảng orders
        insert_query = """
            INSERT INTO orders (customer_name, product_name, price) 
            VALUES (%s, %s, %s)
        """
        cursor.execute(insert_query, (order['customer_name'], order['product_name'], order['price']))
        conn.commit()
        
        print(f"✅ Đã lưu vào Postgres: {order['customer_name']} mua {order['product_name']}")

except KeyboardInterrupt:
    cursor.close()
    conn.close()
    print("🛑 Đã dừng gắp hàng.")