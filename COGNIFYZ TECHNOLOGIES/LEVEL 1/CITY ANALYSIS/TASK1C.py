import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Dataset.csv")  

avg_ratings = df.groupby('City')['Aggregate rating'].mean().sort_values(ascending=False)

highest_avg_city = avg_ratings.idxmax()
highest_avg_rating = avg_ratings.max()

print(f"City with highest average rating: {highest_avg_city} — {highest_avg_rating:.2f}")

top5_cities = avg_ratings.head(5)
plt.figure(figsize=(6,6))
plt.pie(top5_cities, labels=top5_cities.index, autopct='%1.2f%%', startangle=140, colors=['green','skyblue','orange','pink','purple'])
plt.title("Top 5 Cities by Average Rating")
plt.show()
