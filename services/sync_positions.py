from db.sql_server import connect_sql_server
from db.mysql_db import connect_mysql

def sync_positions():
    sql_conn = connect_sql_server()
    mysql_conn = connect_mysql()

    sc = sql_conn.cursor()
    mc = mysql_conn.cursor()

    # 1️⃣ Lấy dữ liệu từ HR (SQL Server)
    sc.execute("""
        SELECT
            PositionID,
            PositionName
        FROM dbo.Positions
    """)

    positions = sc.fetchall()

    # 2️⃣ Đồng bộ sang Payroll (MySQL)
    for pos in positions:
        mc.execute("""
            INSERT INTO positions_payroll (
                PositionID,
                PositionName
            )
            VALUES (%s, %s)
            ON DUPLICATE KEY UPDATE
                PositionName = VALUES(PositionName),
                SyncedAt = CURRENT_TIMESTAMP
        """, (
            pos.PositionID,
            pos.PositionName
        ))

    mysql_conn.commit()

    sc.close()
    mc.close()
    sql_conn.close()
    mysql_conn.close()

    print("✅ Sync Positions HR → Payroll thành công")
