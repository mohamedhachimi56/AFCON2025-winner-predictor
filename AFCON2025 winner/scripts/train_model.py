# scripts/train_model.py
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

def train_model(team_stats, save_path="models/random_forest_model.pkl"):
    features = ["Win_Rate", "Attack_Strength", "Defense_Strength", "Points", "Goal_Difference", "FIFA_Score"]
    
    scaler = MinMaxScaler()
    X = scaler.fit_transform(team_stats[features])
    y = (team_stats["Points"] == team_stats["Points"].max()).astype(int)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    # ✅ Random Forest Model
    model = RandomForestClassifier(n_estimators=200, max_depth=6, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"✅ Model Accuracy: {acc*100:.2f}%")

    # Save model and scaler
    joblib.dump((model, scaler), save_path)
    print(f"📁 Model saved at: {save_path}")
