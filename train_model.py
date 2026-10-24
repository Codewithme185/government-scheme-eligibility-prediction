
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report
import joblib

# Load dataset
df = pd.read_csv("scheme_data.csv")

X = df.drop("eligible", axis=1)
y = df["eligible"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Random Forest": RandomForestClassifier(
        n_estimators=100, random_state=42, class_weight="balanced"
    )
}

best_model = None
best_accuracy = -1

for name, model in models.items():
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions, zero_division=0)
    recall = recall_score(y_test, predictions, zero_division=0)

    print(f"\n{name}")
    print(f"Accuracy:  {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall:    {recall:.4f}")

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = model

joblib.dump(best_model, "scheme_model.pkl")
print("\nBest model saved as scheme_model.pkl")

import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay, RocCurveDisplay

# Confusion Matrix
ConfusionMatrixDisplay.from_estimator(
    best_model, X_test, y_test
)
plt.title("Government Scheme Eligibility - Confusion Matrix")
plt.tight_layout()
plt.savefig("confusion_matrix.png", dpi=300)
plt.close()

# ROC Curve
RocCurveDisplay.from_estimator(
    best_model, X_test, y_test
)
plt.title("Government Scheme Eligibility - ROC Curve")
plt.tight_layout()
plt.savefig("roc_curve.png", dpi=300)
plt.close()

print("Charts saved: confusion_matrix.png, roc_curve.png")
