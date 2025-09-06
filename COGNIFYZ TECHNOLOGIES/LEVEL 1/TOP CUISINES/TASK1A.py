import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")
df.drop_duplicates(inplace=True)
df = df.dropna(subset=['Cuisines'])
df['Cuisines'] = df['Cuisines'].str.strip().str.lower()

all_cuisines = df['Cuisines'].str.split(',').explode().str.strip()
top_cuisines = all_cuisines.value_counts().head(3)

print("Top 3 Cuisines:")
print(top_cuisines)

plt.bar(top_cuisines.index, top_cuisines.values, color='blue', edgecolor='black')
plt.xlabel("Cuisines")
plt.ylabel("Count")
plt.title("top 3 cuisines ")
plt.show()
