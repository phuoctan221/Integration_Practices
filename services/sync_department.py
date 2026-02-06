from db.sql_server import connect_sql_server
from db.mysql_db import connect_mysql

def sync_departments():
    sql_conn = connect_sql_server()
    mysql_conn = connect_mysql()

    sc = sql_conn.cursor()
    mc = mysql_conn.cursor()

    sc.execute("""
        SELECT
            DepartmentID,
            DepartmentName
        FROM dbo.Departments
    """)

    departments = sc.fetchall()

    for dept in departments:
        mc.execute("""
            INSERT INTO departments_payroll (
                DepartmentID,
                DepartmentName
            )
            VALUES (%s, %s)
            ON DUPLICATE KEY UPDATE
                DepartmentName = VALUES(DepartmentName),
                SyncedAt = CURRENT_TIMESTAMP
        """, (
            dept[0],
            dept[1]
        ))

    mysql_conn.commit()

    sc.close()
    mc.close()
    sql_conn.close()
    mysql_conn.close()

    print("✅ Sync Departments HR → Payroll thành công")
