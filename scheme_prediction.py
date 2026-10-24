
import pandas as pd
import numpy as np

np.random.seed(42)
n = 100_000

age = np.random.randint(18, 81, n)
annual_income = np.random.randint(30000, 1000001, n)
family_size = np.random.randint(1, 11, n)
is_rural = np.random.randint(0, 2, n)
has_agricultural_land = np.random.randint(0, 2, n)

# Synthetic demo rule, not official scheme criteria
eligible = (
    (annual_income <= 250000) &
    (age >= 18) &
    (has_agricultural_land == 1)
).astype(int)

df = pd.DataFrame({
    "age": age,
    "annual_income": annual_income,
    "family_size": family_size,
    "is_rural": is_rural,
    "has_agricultural_land": has_agricultural_land,
    "eligible": eligible
})

df.to_csv("scheme_data.csv", index=False)

print("Dataset created successfully!")
print("Total records:", len(df))
print("\nFirst 5 rows:")
print(df.head())
print("\nEligibility distribution:")
print(df["eligible"].value_counts())
print("\nSaved as scheme_data.csv")
