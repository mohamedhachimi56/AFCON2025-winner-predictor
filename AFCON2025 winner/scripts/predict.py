# scripts/predict.py
import pandas as pd
import joblib

def predict_winner(team_stats, model_path="models/random_forest_model.pkl"):
    model, scaler = joblib.load(model_path)

    features = ["Win_Rate", "Attack_Strength", "Defense_Strength", "Points", "Goal_Difference", "FIFA_Score"]
    X = scaler.transform(team_stats[features])

    probs = model.predict_proba(X)[:, 1]
    team_stats["Win_Probability"] = probs

    results = team_stats.sort_values("Win_Probability", ascending=False)
    return results
