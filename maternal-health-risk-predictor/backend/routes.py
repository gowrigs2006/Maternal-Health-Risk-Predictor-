from flask import Blueprint, request, jsonify
import numpy as np
from models import db, Patient
from ml.predictor import load_model

routes = Blueprint('routes', __name__)
model = load_model()

@routes.route('/predict', methods=['POST'])
def predict():
    data = request.json

    features = np.array([[
        data['age'], data['sbp'], data['dbp'],
        data['bs'], data['temp'], data['hr']
    ]])

    probs = model.predict_proba(features)[0]
    label = probs.argmax()
    score = probs.max()

    risk = ['Low Risk','Medium Risk','High Risk'][label]

    patient = Patient(**data, risk=risk)
    db.session.add(patient)
    db.session.commit()

    return jsonify({'risk': risk, 'score': round(score*100,2)})
