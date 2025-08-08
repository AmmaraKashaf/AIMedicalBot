from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Model load karo
model = joblib.load("heart_model.pkl")

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            # Form se data lo
            age = int(request.form["age"])
            sex = int(request.form["sex"])
            cp = int(request.form["cp"])
            trestbps = int(request.form["trestbps"])
            chol = int(request.form["chol"])
            fbs = int(request.form["fbs"])
            restecg = int(request.form["restecg"])
            thalach = int(request.form["thalach"])
            exang = int(request.form["exang"])
            oldpeak = float(request.form["oldpeak"])
            slope = int(request.form["slope"])
            ca = int(request.form["ca"])
            thal = int(request.form["thal"])

            user_data = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
            prediction = model.predict(user_data)

            if prediction[0] == 1:
                result = "⚠️ High risk of heart disease."
            else:
                result = "✅ Low risk of heart disease."

            return render_template("index.html", result=result)
        except Exception as e:
            return render_template("index.html", result=f"Error: {str(e)}")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
