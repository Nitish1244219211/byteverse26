from flask import Blueprint, render_template, request, redirect, url_for
from app.models import patients, Symptoms
from app import db

main = Blueprint("main", __name__)

# Root
@main.route("/", methods=['GET', 'POST'])
def hello_world():

    if request.method == 'POST':
        name = request.form.get("name")
        age = request.form.get("age")
        sex = request.form.get("sex")
        desc = request.form.get("Symptoms")
        mobile = request.form.get("mobile")

        insta = patients(
            name=name,
            age=age,
            sex=sex,
            desc=desc,
            mobile=mobile,
        )

        db.session.add(insta)
        db.session.commit()


    entries = patients.query.all()
    symptoms = [s.symptom for s in Symptoms.query.all()]

    return render_template(
        "index.html",
        symptoms=symptoms
    )

