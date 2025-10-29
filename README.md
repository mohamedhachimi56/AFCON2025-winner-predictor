 — Predicted Winner Analysis

This project uses **Python (Pandas + Matplotlib)** to analyze and predict the most likely winner of the **Africa Cup of Nations 2025 (AFCON 2025)** based on real team performance data and FIFA rankings.

---

## 📊 Overview

The program loads a CSV file containing each qualified team's stats (wins, draws, losses, goals, points, and FIFA ranking), then:
1. Calculates a **Strength Index** for each team.
2. Sorts teams from strongest to weakest.
3. Displays a **bar chart** for the top 10 teams.
4. Displays a **pie chart** showing **each team’s winning probability**.

---

## 🧮 Formula Used

The **Strength Index** is calculated as follows:

\[
Strength = (Wins × 3) + (Draws × 1) + (GoalDifference × 0.5) + (GoalsFor × 0.3) + (Points × 0.8) - (FIFA_Ranking × 0.1)
\]

This formula gives more weight to performance and penalizes lower FIFA rankings.

---

## 📁 CSV File Structure

The program expects a CSV file named:
AFCON2025_Qualified_Teams_with_FIFA.csv



### Example columns:
| Team | Wins | Draws | Losses | Goals_For | Goals_Against | Goal_Difference | Points | FIFA_Ranking |
|------|------|--------|---------|------------|----------------|-----------------|--------|---------------|
| Morocco | 6 | 2 | 0 | 15 | 3 | 12 | 20 | 12 |
| Senegal | 5 | 3 | 0 | 14 | 4 | 10 | 18 | 15 |
| Egypt | 5 | 2 | 1 | 13 | 6 | 7 | 17 | 30 |

---

## 🧠 Example Output

⚙️ Loading data...

🏆 AFCON 2025 — Realistic Top 10 Predicted Teams:

1-Morocco — Strength Index: 21.77

2-Senegal — Strength Index: 20.73

3-Egypt — Strength Index: 19.40

4-Ivory Coast — Strength Index: 19.33

5-Nigeria — Strength Index: 17.37

6-Algeria — Strength Index: 15.70

7-Tunisia — Strength Index: 15.10

8-Mali — Strength Index: 13.93

9-South Africa — Strength Index: 12.57

10-Burkina Faso — Strength Index: 12.47

🏆 Predicted Winner: Morocco (12.9%)



---

## 📈 Visualizations

- **Bar Chart**: Top 10 teams based on calculated Strength Index.  
- **Pie Chart**: Percentage chance of winning for each top team.

---

## 🧩 Requirements

Make sure you have Python and the following libraries installed:

```bash
pip install pandas matplotlib
🚀 How to Run
Place your CSV file (AFCON2025_Qualified_Teams_with_FIFA.csv) in the project folder.

Run the main script:

bash
Copier le code
python main.py
View the console output and the generated charts.

💡 Notes
You can adjust the weights in the formula to reflect your own ranking logic.

The project is meant for educational and analytical purposes — not official predictions.

🧑‍💻 Author
HM Med
A data & AI enthusiast exploring football analytics through Python ⚽📊

📜 License
This project is released under the MIT License — free to use and modify with credit.


