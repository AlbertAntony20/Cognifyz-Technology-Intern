import pandas as pd

df = pd.read_csv("Dataset.csv")
df.head()

df_cuisines = df[['Cuisines', 'Aggregate rating']].dropna()
df_cuisines['Cuisines'] = df_cuisines['Cuisines'].str.lower().str.strip()
df_cuisines['Cuisine Combo'] = df_cuisines['Cuisines'].apply(
    lambda x: ", ".join(sorted([c.strip() for c in x.split(",")]))
)
combo_counts = df_cuisines['Cuisine Combo'].value_counts().head(10)

combo_ratings = (
    df_cuisines.groupby("Cuisine Combo")['Aggregate rating']
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print(combo_ratings)

import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(12, 8))
y_pos = np.arange(len(combo_ratings))
colors = plt.cm.viridis(np.linspace(0, 1, len(combo_ratings)))

bars = plt.barh(y_pos, combo_ratings.values, color=colors)
plt.yticks(y_pos, combo_ratings.index)
plt.xlabel("Average Rating", fontsize=12)
plt.ylabel("Cuisine Combination", fontsize=12)
plt.title("Top 10 Highest Rated Cuisine Combinations", fontsize=14, fontweight='bold')
plt.grid(axis='x', alpha=0.3)

for i, value in enumerate(combo_ratings.values):
    plt.text(value + 0.02, i, f'{value:.2f}', va='center', fontsize=10)

plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

