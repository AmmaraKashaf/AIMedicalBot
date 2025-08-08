import pandas as pd

# 1. CSV file load karo
data = pd.read_csv("heart.csv")

# 2. Data ka shape check karo
print("Dataset shape:", data.shape)

# 3. Features (X) aur Target (y) define karo
# Target column ka naam tumhare dataset me "target" hoga
X = data.drop("target", axis=1)  # sari columns except 'target'
y = data["target"]               # sirf target column

print("Features shape:", X.shape)
print("Target shape:", y.shape)

# Optional: Top rows check karlo
print(X.head())
print(y.head())
from sklearn.linear_model import LogisticRegression
import joblib

# Model banana
model = LogisticRegression(max_iter=1000)

# Train karna
model.fit(X, y)

# Model save karna
joblib.dump(model, "heart_model.pkl")

print("Model training complete! Model saved as heart_model.pkl")
