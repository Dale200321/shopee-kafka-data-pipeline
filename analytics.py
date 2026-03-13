import psycopg2
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Kết nối và lấy dữ liệu
conn = psycopg2.connect(
    host="localhost", database="shopee_data",
    user="ivan_admin", password="password123", port="5432"
)
df = pd.read_sql("SELECT * FROM orders", conn)
conn.close()

# Chuẩn bị biến
y = df['price']

# Chuyển timestamp (chuỗi) sang dạng thời gian của Python
df['order_time'] = pd.to_datetime(df['order_time'])

# Tách Hour (Giờ) và DayOfWeek (Thứ trong tuần)
df['hour'] = df['order_time'].dt.hour
df['day_of_week'] = df['order_time'].dt.dayofweek

# Thử hồi quy theo Giờ
X_hour = sm.add_constant(df['hour'])
model_hour = sm.OLS(df['price'], X_hour).fit()

print("--- KẾT QUẢ HỒI QUY THEO GIỜ ---")
print(model_hour.summary())

# Vẽ phân phối giá tiền
plt.figure(figsize=(10, 6))
sns.histplot(df['price'], kde=True, color='green')
plt.title('Phân phối giá trị đơn hàng trong khung giờ thử nghiệm')
plt.xlabel('Giá tiền (USD)')
plt.ylabel('Số lượng đơn hàng')
plt.show()
