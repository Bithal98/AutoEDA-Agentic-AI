import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, r2_score
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

def run_automl(df: pd.DataFrame):
    """
    Simple AutoML agent:
    - Detect problem type
    - Train baseline models
    """

# Detect target column

    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    target = numeric_cols[-1]

    X = df.drop(columns=[target])
    y = df[target]

    # Keep numeric features only
    X = X.select_dtypes(include="number")

 
 # Detect problem type

    if y.nunique() <= 10:
        problem_type = "classification"
    else:
        problem_type = "regression"

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    results = {}


# Train models

    if problem_type == "classification":
        models = {
            "Logistic Regression": LogisticRegression(max_iter=1000),
            "Random Forest": RandomForestClassifier()
        }

        for name, model in models.items():
            model.fit(X_train, y_train)
            preds = model.predict(X_test)
            results[name] = accuracy_score(y_test, preds)

    else:
        models = {
            "Linear Regression": LinearRegression(),
            "Random Forest": RandomForestRegressor()
        }

        for name, model in models.items():
            model.fit(X_train, y_train)
            preds = model.predict(X_test)
            results[name] = r2_score(y_test, preds)

    return {
        "target": target,
        "problem_type": problem_type,
        "model_performance": results
    }
