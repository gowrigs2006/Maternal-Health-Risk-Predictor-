from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    sbp = db.Column(db.Integer)
    dbp = db.Column(db.Integer)
    bs = db.Column(db.Float)
    temp = db.Column(db.Float)
    hr = db.Column(db.Integer)
    risk = db.Column(db.String(20))
