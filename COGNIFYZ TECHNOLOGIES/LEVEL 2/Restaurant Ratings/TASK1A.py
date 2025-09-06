import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Dataset.csv")
df = df.drop_duplicates()
df = df.dropna(subset=['Aggregate rating'])
df['Aggregate rating'] = pd.to_numeric(df['Aggregate rating'], errors='coerce')
df = df.dropna(subset=['Aggregate rating'])

plt.figure(figsize=(8,5))
plt.hist(df['Aggregate rating'], bins=10, edgecolor='black')
plt.xlabel("Aggregate Rating")
plt.ylabel("Number of Restaurants")
plt.title("Distribution of Restaurant Ratings")
plt.show()

rating_bins = pd.cut(df['Aggregate rating'], bins=[0,1,2,3,4,5], right=True)
common_range = rating_bins.value_counts().idxmax()

print("The most common rating range is:", common_range)
