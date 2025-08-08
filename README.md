AI Medical Bot - Heart Disease Predictor
This project is a simple AI-based web app that predicts the risk of heart disease based on user medical data.

Features:
 Prediction using Logistic Regression model
 Real-time user input through a Flask web app
 Easy setup and local running
 
Setup:

1.Clone the repository:
    git clone https://github.com/AmmaraKashaf/AIMedicalBot.git
    cd AIMedicalBot
    
2.Create and activate a virtual environment:
    python -m venv venv
    venv\Scripts\activate
    
3.Install required packages:
    pip install flask scikit-learn joblib pandas
    
4.Run the Flask app:
    python app.py
    
5.Open your browser and visit: http://127.0.0.1:5000

File Structure:

aimedicalbot/
├── app.py              # Flask app

├── heart_model.pkl     # Trained model

├── med.py              # Data loading

├── train.py            # Model training

├── predict.py          # Console prediction script

├── templates/
│   └── index.html      # HTML form for user input

└── requirements.txt    # (Optional) Python dependencies

Dataset:

     Dataset used: Heart Disease UCI Dataset
     
Created by Ammara Kashaf  



