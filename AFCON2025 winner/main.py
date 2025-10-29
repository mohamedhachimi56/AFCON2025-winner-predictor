import pandas as pd
import matplotlib.pyplot as plt

print("⚙️ Loading data...")

# Load CSV file
df = pd.read_csv("AFCON2025_Qualified_Teams_with_FIFA.csv")

# Group data by team and calculate aggregated stats
team_stats = df.groupby("Team").agg({
    "Wins": "mean",
    "Draws": "mean",
    "Losses": "mean",
    "Goals_For": "mean",
    "Goals_Against": "mean",
    "Goal_Difference": "mean",
    "Points": "mean",
    "FIFA_Ranking": "mean"
}).reset_index()

# Create a performance index (lower FIFA ranking = stronger)
team_stats["Strength_Index"] = (
    (team_stats["Wins"] * 3) +
    (team_stats["Draws"] * 1) +
    (team_stats["Goal_Difference"] * 0.5) +
    (team_stats["Goals_For"] * 0.3) +
    (team_stats["Points"] * 0.8) -
    (team_stats["FIFA_Ranking"] * 0.1)
)

# Sort by strength
team_stats = team_stats.sort_values(by="Strength_Index", ascending=False)

# Display top 10
print("\n AFCON 2025 — Realistic Top 10 Predicted Teams:\n")
for i, row in enumerate(team_stats.head(10).itertuples(), start=1):
    print(f"{i}. {row.Team} — Strength Index: {row.Strength_Index:.2f}")

# Plot bar chart for top 10
plt.figure(figsize=(10,6))
plt.barh(team_stats["Team"].head(10)[::-1], team_stats["Strength_Index"].head(10)[::-1], color="gold")
plt.xlabel("Strength Index")
plt.title(" AFCON 2025 - Top 10 Predicted Teams (Realistic)")
plt.tight_layout()
plt.show()

# Use top 10 results from the calculated data
top_teams = team_stats.head(10)
teams = top_teams["Team"].tolist()
strengths = top_teams["Strength_Index"].tolist()

# Calculate total and percentage share for each team
total_strength = sum(strengths)
percentages = [(s / total_strength) * 100 for s in strengths]

# Create pie chart for winning probability
plt.figure(figsize=(8, 8))
plt.pie(percentages, labels=teams, autopct='%1.1f%%', startangle=140,
        wedgeprops={'edgecolor': 'white'}, textprops={'fontsize': 10})
plt.title(" AFCON 2025 — Winning Probability (%)", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# Predict the most likely winner
winner_index = percentages.index(max(percentages))
predicted_winner = teams[winner_index]
winner_prob = percentages[winner_index]

print(f"\ Predicted Winner: {predicted_winner} ({winner_prob:.2f}%)")
