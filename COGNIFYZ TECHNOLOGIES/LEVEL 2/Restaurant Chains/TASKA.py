
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = "Dataset.csv"
df = pd.read_csv(file_path)

chain_counts = df['Restaurant Name'].value_counts()
chains = chain_counts[chain_counts > 1]
top_chains = chains.head(10)

print("Top 10 Restaurant Chains:")
print(top_chains)

plt.figure(figsize=(12, 6))
plt.bar(range(len(top_chains)), top_chains.values, color='skyblue', edgecolor='black')
plt.xticks(range(len(top_chains)), top_chains.index, rotation=45, ha='right')
plt.title("Number of Outlets per Restaurant Chain (Top 10)", fontsize=14, fontweight='bold')
plt.xlabel("Restaurant Chain")
plt.ylabel("Number of Outlets")
plt.grid(axis='y', alpha=0.3)

for i, v in enumerate(top_chains.values):
    plt.text(i, v + 0.1, str(v), ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.show()
