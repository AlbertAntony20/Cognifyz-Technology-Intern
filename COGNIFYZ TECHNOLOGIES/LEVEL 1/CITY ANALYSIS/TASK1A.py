import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Dataset.csv")

city_counts = df['City'].value_counts()

avg_ratings = df.groupby('City')['Aggregate rating'].mean().sort_values(ascending=False)

print(f"City with highest number of restaurants: {city_counts.idxmax()} — {city_counts.max()} restaurants")

# Visualization
plt.figure(figsize=(10,5))
city_counts.head(10).plot(kind='barh', color='skyblue')
plt.title("Top 10 Cities by Number of Restaurants")
plt.xlabel("Number of Restaurants")
plt.ylabel("City")
plt.gca().invert_yaxis() 
plt.show()
