import pymysql

# Sửa lại phù hợp với cấu hình MySQL của từng bạn rồi test thử kết nối được chưa nhé
def connect_mysql():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="123456",
        database="payroll",
        port=3307,
        cursorclass=pymysql.cursors.DictCursor
    )

