import os
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

DATA_PATH = os.path.join(os.path.dirname(__file__), "dataset.csv")
MODEL_DIR = os.path.join(os.path.dirname(__file__), "models")
FEATURE_COLUMNS = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]

if __name__ == "__main__":
    df = pd.read_csv(DATA_PATH).dropna()
    X = df[FEATURE_COLUMNS]
    y = df["crop"]

    scaler = StandardScaler().fit(X)
    X_scaled = scaler.transform(X)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_scaled, y)

    os.makedirs(MODEL_DIR, exist_ok=True)
    with open(os.path.join(MODEL_DIR, "crop_recommendation_model.pkl"), "wb") as f:
        pickle.dump(model, f)
    with open(os.path.join(MODEL_DIR, "scaler.pkl"), "wb") as f:
        pickle.dump(scaler, f)
