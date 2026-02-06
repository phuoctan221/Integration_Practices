from db.sql_server import connect_sql_server

conn = connect_sql_server()
print("SQL Server connected!")
conn.close()
