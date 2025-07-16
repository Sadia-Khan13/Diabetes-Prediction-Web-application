
import streamlit as st
import requests

st.set_page_config(page_title="Diabetes prediction Model" , page_icon="🩺")
st.title("Diabetes Prediction System")
st.write("Fill in the patient data below to check the diabetes risk")

with st.form("Diabetes form"):
    Pregnancies= st.number_input("Pragnancies" , min_value=0)
    Glucose= st.number_input("Glucose", min_value=0.0)
    BloodPressure= st.number_input("Blood Pressure", min_value=0.0)
    SkinThickness= st.number_input("Skin Thickness", min_value=0.0)
    Insulin= st.number_input("Insulin", min_value=0.0)
    BMI= st.number_input("BMI", min_value=0.0)
    DiabetesPedigreeFunction= st.number_input("Diabetes Pedigree Function", min_value=0.0)
    Age= st.number_input("Age", min_value=1)

    submitted = st.form_submit_button("Predict")

    if submitted:
        input_data={
            "Pregnancies":Pregnancies,
            "Glucose": Glucose,
            "BloodPressure": BloodPressure,
            "SkinThickness": SkinThickness,
            "Insulin": Insulin,
            "BMI": BMI,
            "DiabetesPedigreeFunction": DiabetesPedigreeFunction,
            "Age": Age
        }


        response = requests.post("http://127.0.0.1:8000/prediction", json=input_data)
        prediction= response.json()["prediction"]

        if prediction == 1:
                st.error(f"🔴 The Patient is Diabetic")
        else:
               st.success(f"🟢 The Patient is not Diabetic")
        
   