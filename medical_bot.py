import pandas as pd

# Step 1: Load CSV file
df = pd.read_csv("heart.csv")

# Step 2: Show first 5 rows
print("First 5 rows of dataset:")
print(df.head())

# Step 3: Check columns & missing data
print("\nDataset Info:")
print(df.info())

print("\nMissing Values in Each Column:")
print(df.isnull().sum())
