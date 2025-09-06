import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Dataset.csv")

avg_ratings = df.groupby('City')['Aggregate rating'].mean().sort_values(ascending=False)

print("Average rating for restaurants in each city:")
print(avg_ratings)

plt.figure(figsize=(10,5))
plt.scatter(avg_ratings.index[:10], avg_ratings.values[:10], color='orange', s=100)
plt.title("Top 10 Cities by Average Restaurant Rating")
plt.xlabel("City")
plt.ylabel("Average Rating")
plt.xticks(rotation=45)
plt.ylim(0, 5)
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
