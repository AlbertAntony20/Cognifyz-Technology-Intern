import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = "Dataset.csv"
df = pd.read_csv(file_path)

chain_counts = df['Restaurant Name'].value_counts()
chains = chain_counts[chain_counts > 1]

chain_analysis = (
    df[df['Restaurant Name'].isin(chains.index)]
    .groupby('Restaurant Name')
    .agg({
        'Aggregate rating': 'mean',
        'Votes': 'sum',
        'Restaurant ID': 'count'
    })
    .rename(columns={'Restaurant ID': 'Number of Outlets'})
    .reset_index()
    .sort_values(by="Number of Outlets", ascending=False)
)

print("Top 10 Chains Analysis:")
print(chain_analysis.head(10))

top_10_chains = chain_analysis.head(10)

plt.figure(figsize=(12, 6))
bars = plt.bar(range(len(top_10_chains)), top_10_chains['Aggregate rating'], 
               color='lightgreen', edgecolor='black')
plt.xticks(range(len(top_10_chains)), top_10_chains['Restaurant Name'], rotation=45, ha='right')
plt.title("Average Ratings of Restaurant Chains (Top 10 by Outlets)", fontsize=14, fontweight='bold')
plt.xlabel("Restaurant Chain")
plt.ylabel("Average Rating")
plt.ylim(0, 5)
plt.grid(axis='y', alpha=0.3)

for i, v in enumerate(top_10_chains['Aggregate rating']):
    plt.text(i, v + 0.05, f'{v:.2f}', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.show()
