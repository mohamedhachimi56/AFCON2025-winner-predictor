# scripts/visualize.py
import matplotlib.pyplot as plt

def plot_predictions(predictions):
    top10 = predictions.head(10)
    plt.figure(figsize=(10, 6))
    plt.barh(top10["Team"], top10["Win_Probability"], color='gold')
    plt.gca().invert_yaxis()
    plt.title("AFCON 2025 Winning Probability (Top 10)", fontsize=14)
    plt.xlabel("Win Probability")
    plt.ylabel("Team")
    plt.show()

