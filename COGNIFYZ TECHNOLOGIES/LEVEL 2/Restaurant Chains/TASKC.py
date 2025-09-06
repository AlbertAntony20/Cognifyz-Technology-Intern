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

print("Chain Analysis:")
print(chain_analysis.head(10))

top_chains_by_votes = chain_analysis.sort_values(by="Votes", ascending=False).head(10)
print("\nTop 10 Chains by Popularity (Total Votes):")
print(top_chains_by_votes[['Restaurant Name', 'Votes', 'Number of Outlets', 'Aggregate rating']])

plt.figure(figsize=(12, 6))
bars = plt.bar(range(len(top_chains_by_votes)), top_chains_by_votes['Votes'], 
               color='salmon', edgecolor='black')
plt.xticks(range(len(top_chains_by_votes)), top_chains_by_votes['Restaurant Name'], 
           rotation=45, ha='right')
plt.title("Popularity of Restaurant Chains (Total Votes, Top 10)", fontsize=14, fontweight='bold')
plt.xlabel("Restaurant Chain")
plt.ylabel("Total Votes")
plt.grid(axis='y', alpha=0.3)

for i, v in enumerate(top_chains_by_votes['Votes']):
    plt.text(i, v + max(top_chains_by_votes['Votes']) * 0.01, f'{v:,}', 
             ha='center', va='bottom', fontweight='bold', fontsize=9)

plt.tight_layout()
plt.show()
