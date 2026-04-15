"""
model.py

Handles training, evaluation, saving, loading, and prediction for the
logistic regression model. SMOTE is applied to address class imbalance
in the training data. StandardScaler normalizes features before training.

Known Limitations:
    - hours_per_week is closely tied to the completed label which may
      inflate model confidence.
    - Synthetic personality scores in training data may not reflect
      real user behavior.

Functions:
    train_model()    - Trains logistic regression model on prepared dataset.
    predict_tasks()  - Predicts completion probability for each user task.
    save_model()     - Saves trained model and scaler to disk.
    load_model()     - Loads saved model and scaler from disk.
"""

import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
from imblearn.over_sampling import SMOTE

def train_model(df):
    X = df.drop(columns=["completed"])
    y = df["completed"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    #Applying SMOTE to address imbalance
    smote = SMOTE(random_state=42)
    X_train, y_train = smote.fit_resample(X_train, y_train)

    """
    hours_per_week has high values while rating columns are 1-5
    therefore we transform every feature to have same scale
    """
    scaler = StandardScaler()
    #Learns the scale from training data
    X_train_scaled = scaler.fit_transform(X_train)
    #Applies same scale to test data
    X_test_scaled = scaler.transform(X_test)

    model = LogisticRegression()
    model.fit(X_train_scaled, y_train)

    y_pred = model.predict(X_test_scaled)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    print(f"\nModel Accuracy: {accuracy:.2%}")
    print(f"\nClassification Report:\n{report}")

    return model, scaler

def predict_tasks(model, scaler, combined):
    feature_order = ["U", "I", "Q", "S", "category", "hours_per_week", 
                     "stress", "urgency", "importance", "mental_effort"]
    
    results = []
    for task in combined:
        features = {f: [task[f]] for f in feature_order}
        features_df = pd.DataFrame(features)
        features_scaled = scaler.transform(features_df)
        probability = model.predict_proba(features_scaled)[0][1]
        
        results.append({
            "name": task["name"],
            "completion_probability": round(probability, 10)
        })
    
    results.sort(key=lambda x: x["completion_probability"], reverse=True)
    
    return results

def save_model(model, scaler, model_path="models/model.pkl", scaler_path="models/scaler.pkl"):
    joblib.dump(model, model_path)
    joblib.dump(scaler, scaler_path)
    print("Model saved.")

def load_model(model_path="models/model.pkl", scaler_path="models/scaler.pkl"):
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    print("Model loaded.")
    return model, scaler