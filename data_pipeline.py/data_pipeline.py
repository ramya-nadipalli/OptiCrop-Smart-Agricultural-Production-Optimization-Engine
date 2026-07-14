import os
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

FEATURE_COLUMNS = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]
MODEL_DIR = os.path.join(os.path.dirname(__file__), "models")


def load_dataset(path):
    df = pd.read_csv(path)
    df = df.dropna()
    return df


def build_features(df):
    X = df[FEATURE_COLUMNS]
    y = df["crop"]
    return X, y


def train_best_model(X, y):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42, stratify=y)

    model = RandomForestClassifier(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))

    return model, scaler


def save_model(model, scaler):
    os.makedirs(MODEL_DIR, exist_ok=True)
    with open(os.path.join(MODEL_DIR, "crop_recommendation_model.pkl"), "wb") as f:
        pickle.dump(model, f)
    with open(os.path.join(MODEL_DIR, "scaler.pkl"), "wb") as f:
        pickle.dump(scaler, f)


if __name__ == "__main__":
    df = load_dataset(os.path.join(os.path.dirname(__file__), "dataset.csv"))
    X, y = build_features(df)
    model, scaler = train_best_model(X, y)
    save_model(model, scaler)
