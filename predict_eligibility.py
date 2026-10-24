
import pandas as pd
import joblib

# Load trained model
model = joblib.load("scheme_model.pkl")

print("Government Scheme Eligibility Demo")
print("-" * 35)

age = int(input("Enter age: "))
income = float(input("Enter annual family income (Rs): "))
family_size = int(input("Enter family size: "))
rural = int(input("Rural area? (1=Yes, 0=No): "))
land = int(input("Agricultural land available? (1=Yes, 0=No): "))

# Validate inputs
if not (18 <= age <= 100):
    print("Age must be between 18 and 100.")
elif income < 0 or family_size < 1:
    print("Income cannot be negative and family size must be at least 1.")
elif rural not in (0, 1) or land not in (0, 1):
    print("Enter only 1 or 0 for rural and land.")
else:
    applicant = pd.DataFrame([{
        "age": age,
        "annual_income": income,
        "family_size": family_size,
        "is_rural": rural,
        "has_agricultural_land": land
    }])

    prediction = model.predict(applicant)[0]
    probability = model.predict_proba(applicant)[0][1]

    print("\n--- Prediction Result ---")
    print("Demo prediction:", "Eligible" if prediction == 1 else "Not Eligible")
    print(f"Model eligibility score: {probability:.2%}")
    print("Note: Synthetic-data demo only, not an official eligibility decision.")
