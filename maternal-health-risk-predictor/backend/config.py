class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database/maternal_health.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MODEL_PATH = 'ml/maternal_risk_model.pkl'
