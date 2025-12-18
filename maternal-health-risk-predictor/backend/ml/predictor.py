import joblib
import os
import numpy as np
from sklearn.linear_model import LogisticRegression

MODEL_PATH = 'ml/maternal_risk_model.pkl'

def load_model():
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)

    # fallback model
    X = np.array([
        [25,120,80,6.5,98,80],
        [38,150,95,9,101,110]
    ])
    y = np.array([0,2])

    model = LogisticRegression()
    model.fit(X,y)
    joblib.dump(model, MODEL_PATH)
    return model
