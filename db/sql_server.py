import pyodbc

def connect_sql_server():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=PHUOCTAN\\MSSQLSERVER07;"
        "DATABASE=Human;"
        "UID=sa;"
        "PWD=123456"
    )
