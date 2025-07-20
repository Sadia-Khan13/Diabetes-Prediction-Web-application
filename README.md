This project is a Diabetes Prediction Web Application built with a FastAPI backend and a Streamlit frontend. The backend serves a Support Vector Machine (SVM) machine learning model trained on a diabetes dataset, while the frontend provides an interactive UI to input patient data and receive real-time predictions.

Features:

FastAPI backend providing a API for diabetes prediction.

Streamlit frontend for easy user interaction.

SVM machine learning model for diabetes classification.

Real-time prediction results.

Installation and Setup:

git clone https://github.com/yourusername/diabetes-prediction-webapp.git
cd diabetes-prediction-webapp

Setup Backend:

python -m venv myenv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload

The backend will run at http://127.0.0.1:8000

Setup Frontend:

python -m venv myenv

venv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py

The frontend will run at http://localhost:8501

Usage:

Open the Streamlit app in your browser.

Enter health parameters such as glucose level, BMI, age, etc.

Submit the form.

The frontend sends the data to the FastAPI backend.

Backend predicts diabetes risk using the SVM model.

Prediction result is displayed on the frontend.

Author:

Your Name — Sadia Khan (khansadii003@gmail.com)

GitHub: https://github.com/Sadia-Khan13
