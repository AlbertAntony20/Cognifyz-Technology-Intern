import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Dataset.csv")

price_counts = df['Price range'].value_counts().sort_index()
price_percentage = (price_counts / len(df)) * 100

plt.figure(figsize=(6,6))
plt.pie(price_percentage, labels=price_percentage.index, autopct='%1.1f%%', startangle=90)
plt.title('Percentage of Restaurants in Each Price Range')
plt.show()

print("Percentage of restaurants in each price range:")
print(price_percentage)
