from flask import Blueprint
from app import db

api = Blueprint("api", __name__)

@api.route("/hospitals/<int:dept_id>")
def hospitals(dept_id):
# for hospital list in book appointment page
    result = db.session.execute(
        db.text("""
        SELECT h.hospital_name, d.department_name
        FROM hospital_department hd
        JOIN hospitals h ON h.hospital_id = hd.hospital_id
        JOIN departments d ON d.department_id = hd.department_id
        WHERE hd.department_id = :dept_id
    """), {"dept_id": dept_id})

    hospitals = [{"name": r[0], "dept": r[1]} for r in result.fetchall()]

    return {"hospitals": hospitals}