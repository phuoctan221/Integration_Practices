import pyodbc

# Sửa lại phù hợp với cấu hình SQL Server của từng bạn rồi test thử kết nối được chưa nhé

def connect_sql_server():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=PHUOCTAN\\MSSQLSERVER07;"
        "DATABASE=Human;"
        "UID=sa;"
        "PWD=123456"
    )
