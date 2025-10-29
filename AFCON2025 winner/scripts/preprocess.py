# scripts/preprocess.py
import pandas as pd

def preprocess_data(file_path):
    data = pd.read_csv(file_path)
    
    # Aggregate team statistics
    team_stats = data.groupby("Team").agg({
        "Matches_Played": "sum",
        "Wins": "sum",
        "Draws": "sum",
        "Losses": "sum",
        "Goals_For": "sum",
        "Goals_Against": "sum",
        "Goal_Difference": "sum",
        "Points": "sum",
        "FIFA_Ranking": "mean"
    }).reset_index()

    # Create derived features
    team_stats["Win_Rate"] = team_stats["Wins"] / team_stats["Matches_Played"]
    team_stats["Attack_Strength"] = team_stats["Goals_For"] / team_stats["Matches_Played"]
    team_stats["Defense_Strength"] = team_stats["Goals_Against"] / team_stats["Matches_Played"]
    team_stats["FIFA_Score"] = 1 / team_stats["FIFA_Ranking"]

    return team_stats

