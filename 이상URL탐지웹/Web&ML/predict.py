import joblib

def prediction(df):
    model = joblib.load('lgbm.pkl')
    model.fitted_=True
    pred = model.predict(df)
    return pred
