import numpy as np
import joblib
from sklearn.linear_model import LogisticRegression

X = np.array([
    [22,120,80,6.5,98.4,80],
    [35,150,95,9.2,101,110],
    [28,130,85,7.5,99,90],
    [18,145,92,8.8,100.5,105],
    [30,118,76,6.0,98,75]
])

y = np.array([0,2,1,2,0])  # 0=Low, 1=Medium, 2=High

model = LogisticRegression(max_iter=1000)
model.fit(X, y)

joblib.dump(model, 'maternal_risk_model.pkl')
print("Model trained & saved.")
