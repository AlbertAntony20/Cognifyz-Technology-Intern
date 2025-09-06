import pandas as pd

df = pd.read_csv("Dataset.csv")
df.head()
df_cuisines = df[['Cuisines', 'Aggregate rating']].dropna()
df_cuisines['Cuisines'] = df_cuisines['Cuisines'].str.lower().str.strip()
df_cuisines['Cuisine Combo'] = df_cuisines['Cuisines'].apply(
    lambda x: ", ".join(sorted([c.strip() for c in x.split(",")]))
)
combo_counts = df_cuisines['Cuisine Combo'].value_counts().head(10)

print(combo_counts)

import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(12, 8))
top_8 = combo_counts.head(8)
others_count = combo_counts.iloc[8:].sum()
pie_data = list(top_8.values) + [others_count]
pie_labels = list(top_8.index) + ['Others']

plt.pie(pie_data, labels=pie_labels, autopct='%1.1f%%', startangle=90)
plt.title("Distribution of Top Cuisine Combinations", fontsize=14)
plt.axis('equal')
plt.tight_layout()
plt.show()
