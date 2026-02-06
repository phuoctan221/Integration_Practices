from db.mysql_db import connect_mysql

try:
    conn = connect_mysql()
    print("MySQL connected successfully!")
    conn.close()
except Exception as e:
    print("Error:", e)
