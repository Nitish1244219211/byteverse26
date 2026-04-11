from app import db
from datetime import datetime

class patients(db.Model):
    sno=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(99), nullable=False)
    age=db.Column(db.Integer, nullable=False)
    mobile=db.Column(db.Integer, nullable=False)
    sex=db.Column(db.String(25), nullable=False)
    desc=db.Column(db.String(500), nullable=True)
    date=db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.name}"#represent the entries

class Symptoms(db.Model):
    __tablename__ = "symptom_table"   # important symptoms

    symptom = db.Column(db.String(200), nullable=False)
    symptom_id = db.Column(db.Integer, primary_key=True)


# rest of the tables are imported in csv form using DBeaver in project.db of instance folder
