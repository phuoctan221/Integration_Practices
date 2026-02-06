from db.sql_server import connect_sql_server
from db.mysql_db import connect_mysql

def sync_employees():
    sql_conn = connect_sql_server()
    mysql_conn = connect_mysql()

    sc = sql_conn.cursor()
    mc = mysql_conn.cursor()

    sc.execute("""
        SELECT
            e.EmployeeID,
            e.FullName,
            e.DepartmentID,
            e.PositionID
        FROM dbo.Employees e
    """)

    employees = sc.fetchall()

    for emp in employees:
        mc.execute("""
            INSERT INTO employees_payroll (
                EmployeeID,
                FullName,
                DepartmentID,
                PositionID
            )
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                FullName = VALUES(FullName),
                DepartmentID = VALUES(DepartmentID),
                PositionID = VALUES(PositionID),
                SyncedAt = CURRENT_TIMESTAMP
        """, (
            emp[0],
            emp[1],
            emp[2],
            emp[3]
        ))

    mysql_conn.commit()

    sc.close()
    mc.close()
    sql_conn.close()
    mysql_conn.close()

    print("✅ Sync Employees HR → Payroll thành công")
