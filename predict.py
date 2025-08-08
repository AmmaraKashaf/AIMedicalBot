import joblib

# Model load karo
model = joblib.load("heart_model.pkl")

# User se input lene ke liye function
def get_user_input():
    print("Please enter the following details:")

    age = int(input("Age: "))
    sex = int(input("Sex (1 = male, 0 = female): "))
    cp = int(input("Chest pain type (0-3): "))
    trestbps = int(input("Resting blood pressure: "))
    chol = int(input("Serum cholesterol in mg/dl: "))
    fbs = int(input("Fasting blood sugar > 120 mg/dl (1 = true, 0 = false): "))
    restecg = int(input("Resting electrocardiographic results (0-2): "))
    thalach = int(input("Maximum heart rate achieved: "))
    exang = int(input("Exercise induced angina (1 = yes, 0 = no): "))
    oldpeak = float(input("ST depression induced by exercise relative to rest: "))
    slope = int(input("Slope of the peak exercise ST segment (0-2): "))
    ca = int(input("Number of major vessels (0-3) colored by fluoroscopy: "))
    thal = int(input("Thalassemia (1 = normal, 2 = fixed defect, 3 = reversible defect): "))

    return [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]

def main():
    user_data = get_user_input()
    prediction = model.predict(user_data)

    if prediction[0] == 1:
        print("⚠️ High risk of heart disease.")
    else:
        print("✅ Low risk of heart disease.")

if __name__ == "__main__":
    main()
