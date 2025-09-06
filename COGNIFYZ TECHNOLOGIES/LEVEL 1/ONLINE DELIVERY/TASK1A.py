import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Dataset.csv", encoding='latin-1')

online_counts = df['Has Online delivery'].value_counts()
online_percentage = (online_counts / len(df)) * 100
print("Percentage of Restaurants Offering Online Delivery:")
print(online_percentage)

plt.figure(figsize=(6,6))
plt.pie(online_percentage, labels=online_percentage.index, autopct='%1.1f%%', startangle=90)
plt.title('Percentage of Restaurants Offering Online Delivery')
plt.show()
