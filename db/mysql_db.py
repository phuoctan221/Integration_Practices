import pymysql

def connect_mysql():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="123456",
        database="payroll",
        port=3307,
        cursorclass=pymysql.cursors.DictCursor
    )