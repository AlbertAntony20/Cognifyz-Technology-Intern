import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Dataset.csv")

price_counts = df['Price range'].value_counts().sort_index()
print("The price range distribution:",price_counts)

plt.figure(figsize=(6,4))
plt.bar(price_counts.index, price_counts.values, color='skyblue', edgecolor='black')
plt.xlabel('Price Range')
plt.ylabel('Number of Restaurants')
plt.title('Distribution of Price Ranges among Restaurants')
plt.xticks(price_counts.index)
plt.show()
