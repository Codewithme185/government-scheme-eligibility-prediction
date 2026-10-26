# Government Scheme Eligibility Prediction System

## Overview

The **Government Scheme Eligibility Prediction System** is a machine learning project that demonstrates how classification algorithms can predict sample eligibility labels using demographic and household-related attributes.

The project uses synthetic data to demonstrate the complete machine learning workflow, including data preparation, model training, evaluation, and prediction.

## Disclaimer

**This project is an educational prototype and is not an official government eligibility checker.**

The dataset and eligibility labels are synthetic and generated using a simplified demonstration rule. Predictions must not be used to determine eligibility for any real government scheme or to make decisions affecting individuals.

For accurate eligibility information, always refer to the official government scheme guidelines and authorized portals.

## Features

- Generates and uses synthetic data for model training.
- Implements Logistic Regression and Random Forest classification algorithms.
- Evaluates model performance using classification metrics.
- Generates model evaluation visualizations.
- Saves the trained model for future predictions.
- Accepts user inputs through a command-line interface.
- Demonstrates an end-to-end machine learning workflow.

## Input Features

The model uses the following sample input features:

| Feature | Description |
|---|---|
| Age | Age of the applicant |
| Annual Income | Applicant's annual income |
| Family Size | Number of family members |
| Rural/Urban | Indicates residential location |
| Agricultural Land | Indicates agricultural land ownership |

## Technologies Used

- **Programming Language:** Python
- **Data Manipulation:** Pandas, NumPy
- **Machine Learning:** Scikit-learn
- **Data Visualization:** Matplotlib
- **Model Serialization:** Joblib / Pickle

## Project Structure

```text
Government-Scheme-Eligibility-Prediction/
│
├── train_model.py
├── predict_eligibility.py
├── scheme_data.csv
├── scheme_model.pkl
├── confusion_matrix.png
├── roc_curve.png
└── README.md
```

*Note: Some files may be generated during execution or may not be included in the repository.*

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Codewithme185/Government-Scheme-Eligibility-Prediction.git
cd Government-Scheme-Eligibility-Prediction
```

Replace the repository URL with your actual GitHub repository URL if the repository name differs.

### 2. Create a Virtual Environment

```bash
python3 -m venv .venv
```

### 3. Activate the Environment

**macOS / Linux**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
python3 -m pip install pandas numpy scikit-learn matplotlib joblib
```

## Train the Model

Run the following command to train and evaluate the machine learning models:

```bash
python3 train_model.py
```

The script trains the classification models and evaluates their performance. Depending on the implementation, it may also save the trained model and generate evaluation plots.

## Run the Prediction Demo

Execute the prediction script:

```bash
python3 predict_eligibility.py
```

Follow the terminal prompts to enter the applicant's sample demographic and household information and view the model's predicted label.

## Model Evaluation

The project demonstrates model evaluation using classification metrics and visualizations, which may include:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- ROC Curve

Performance results should be interpreted carefully. High test scores on synthetic data do not establish real-world predictive accuracy, fairness, or reliability.

## Future Improvements

- Incorporate verified and lawfully obtained datasets where appropriate.
- Implement documented, official scheme eligibility criteria.
- Add robust input validation and error handling.
- Evaluate performance using independent and representative datasets.
- Assess fairness, potential bias, and false-positive and false-negative rates.
- Improve prediction explanations and document model limitations.
- Develop a user-friendly web interface for demonstration purposes.

## Learning Outcomes

Through this project, the following concepts are demonstrated:

- Synthetic dataset generation and data preparation.
- Supervised machine learning and classification.
- Training and comparing machine learning models.
- Model evaluation and visualization.
- Saving and loading trained models.
- Building a basic prediction interface.

## Author

**Codewithme185**

GitHub: [@Codewithme185](https://github.com/Codewithme185)

---

*Developed for educational and machine learning demonstration purposes only.*
