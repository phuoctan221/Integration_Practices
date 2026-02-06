from flask import Flask, jsonify, render_template
from db.sql_server import connect_sql_server
from services.sync_employee import sync_employees
from services.sync_department import sync_departments

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


# 📄 Lấy danh sách employee từ HR (SQL Server)
@app.route("/api/employees")
def get_employees():
    conn = connect_sql_server()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            e.EmployeeID,
            e.FullName,
            d.DepartmentName,
            p.PositionName
        FROM dbo.Employees e
        LEFT JOIN dbo.Departments d ON e.DepartmentID = d.DepartmentID
        LEFT JOIN dbo.Positions p ON e.PositionID = p.PositionID
    """)

    data = []
    for r in cur.fetchall():
        data.append({
            "employee_id": r[0],
            "full_name": r[1],
            "department": r[2],
            "position": r[3]
        })

    conn.close()
    return jsonify(data)


# 🔄 GỘP SYNC (BƯỚC 3)
@app.route("/api/sync/all")
def sync_all():
    sync_departments()
    sync_employees()
    return {"message": "Sync Departments + Employees thành công"}


if __name__ == "__main__":
    app.run(debug=True)
