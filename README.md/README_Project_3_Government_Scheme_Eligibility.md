# Government Scheme Eligibility Prediction System

## Overview

A machine-learning demonstration that predicts a sample eligibility
label from demographic and household attributes. It uses synthetic demo
data to demonstrate a classification workflow.

## Important Disclaimer

**This is an educational prototype, not an official government
eligibility checker.** The dataset and eligibility labels are synthetic
and based on a simplified demo rule. Predictions must not be used to
determine eligibility for any real government scheme. Always check the
official scheme guidelines and portal.

## Features

-   Generates or uses a synthetic dataset for model training.
-   Trains Logistic Regression and Random Forest classifiers.
-   Evaluates models using classification metrics.
-   Saves a trained model for prediction.
-   Accepts user inputs to demonstrate a prediction.

## Input Features

-   Age
-   Annual income
-   Family size
-   Rural/urban indicator
-   Agricultural land indicator

## Tools & Technologies

-   Python
-   Pandas
-   NumPy
-   Scikit-learn
-   Matplotlib
-   Joblib / Pickle model serialization

## Project Files

-   `train_model.py` --- trains and evaluates the models.
-   `predict_eligibility.py` --- loads the saved model and accepts
    inputs.
-   `scheme_data.csv` --- synthetic demo dataset, if included.
-   `scheme_model.pkl` --- saved model, if included.
-   `confusion_matrix.png` and `roc_curve.png` --- evaluation
    visualizations, if included.

## Setup

``` bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install pandas numpy scikit-learn matplotlib
```

## Train the Model

``` bash
python3 train_model.py
```

## Run a Prediction Demo

``` bash
python3 predict_eligibility.py
```

Follow the prompts in the terminal.

## Evaluation Notes

Very high test scores can occur because the synthetic labels are
generated from a simple rule. They do not establish real-world accuracy,
fairness, or suitability for government decisions.

## Future Improvements

-   Use verified, lawfully obtained scheme data and official eligibility
    criteria.
-   Add input validation and clearer explanations for each result.
-   Evaluate on independent, representative data.
-   Assess fairness, error rates, and model limitations before any
    real-world use.

## Author

Codewithme185
