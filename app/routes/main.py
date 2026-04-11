from flask import Blueprint, render_template, request, redirect, url_for
from app.models import patients, Symptoms
from app.services.disease import get_top_diseases
from app import db
import secrets #to create token for usr

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
        token = secrets.token_urlsafe(16)

        insta = patients(
            name=name,
            age=age,
            sex=sex,
            desc=desc,
            mobile=mobile,
            access_token=token
        )

        db.session.add(insta)
        db.session.commit()

        return redirect(url_for('main.book_appointment', token=token))

    entries = patients.query.all()
    symptoms = [s.symptom for s in Symptoms.query.all()]

    return render_template(
        "index.html",
        entriesUsingJinga2=entries,
        symptoms=symptoms
    )


@main.route("/update/<int:sno>", methods=['GET', 'POST'])#get the sno
def update(sno):
    if request.method=='POST':
        # print(request.form.get('name'))
        name=request.form.get("name")
        desc=request.form["Symptoms"]
        updateInsta=patients.query.filter_by(sno=sno).first()# fetch old instance to alter it
        updateInsta.name=name# new data replace
        updateInsta.desc=desc
        db.session.add(updateInsta)
        # updateInsta.verified = True
        db.session.commit()
        return redirect("/")
    updateInsta=patients.query.filter_by(sno=sno).first()# fetch old instance to fill the form
    return render_template("/update.html", updateUsingJinga2=updateInsta)# send the entries in this var 4 terminal


@main.route("/delete/<int:sno>")
def delete(sno):
    entry2delete = patients.query.filter_by(sno=sno).first() #give none for 0 n 1st for xle
    # entry2delete = db.session.execute(db.select(patients).filter_by(sno=sno)).scalar_one()#scalar no req* give error if 0 or more than 1 record found

    db.session.delete(entry2delete)
    db.session.commit()
    return redirect("/")

@main.route("/book_appointment/<token>")
def book_appointment(token):

    patient = patients.query.filter_by(access_token=token).first()

    if not patient:
        return "Invalid or expired link"

    symptom_list = patient.desc.split(",")
    top_diseases = get_top_diseases(symptom_list)

    return render_template(
        "book_appointment.html",
        patient=patient,
        top_diseases=top_diseases
    )

