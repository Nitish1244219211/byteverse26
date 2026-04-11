from sqlalchemy import text
from app import db

def get_hospitals_by_department(dept_id):

    result = db.session.execute(
        text("""
            SELECT h.hospital_id,
                   h.hospital_name,
                   d.department_name
            FROM hospital_department hd
            JOIN hospitals h ON h.hospital_id = hd.hospital_id
            JOIN departments d ON d.department_id = hd.department_id
            WHERE hd.department_id = :dept_id
        """),
        {"dept_id": dept_id}
    )

    hospitals = []

    for row in result:
        hospitals.append({
            "id": row[0],
            "name": row[1],
            "department": row[2]
        })

    return hospitals