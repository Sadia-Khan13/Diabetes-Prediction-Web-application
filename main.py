
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import sklearn

model = joblib.load("SVM Model.pkl")
scaler = joblib.load("ss.pkl")

app = FastAPI(title="Diabetes prediction API")

class user_input(BaseModel):
    Pregnancies: int
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

@app.post("/prediction")
def diabetes_prediction(data: user_input):

    user_data = pd.DataFrame([{
        "Pregnancies": data.Pregnancies ,
        "Glucose": data.Glucose ,
        "BloodPressure": data.BloodPressure ,
        "SkinThickness": data.SkinThickness ,
        "Insulin": data.Insulin ,
        "BMI": data.BMI ,
        "DiabetesPedigreeFunction": data.DiabetesPedigreeFunction ,
        "Age": data.Age
     }])
    
    scaled_data = scaler.transform(user_data)

    Prediction = model.predict(scaled_data)[0]


    result = "The person is diabetic" if Prediction == 1 else "The Person is Not Diabetic"
    
    return {"prediction" : int(Prediction) , "message": result}



