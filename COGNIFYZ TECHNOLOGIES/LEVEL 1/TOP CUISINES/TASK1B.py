import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")
df.drop_duplicates(inplace=True)
df = df.dropna(subset=['Cuisines'])
df['Cuisines'] = df['Cuisines'].str.strip().str.lower()

all_cuisines = df['Cuisines'].str.split(',').explode().str.strip()
top_cuisines = all_cuisines.value_counts().head(3)

total_restaurants = len(df)
percentages = (top_cuisines / total_restaurants) * 100

percentages_df = pd.DataFrame({
    'Cuisines': top_cuisines.index,
    'Percentage': percentages.values
})

print(percentages_df)

plt.bar(percentages_df['Cuisines'], percentages_df['Percentage'], color='skyblue', edgecolor='black')
plt.xlabel('Cuisines')
plt.ylabel('Percentage of Restaurants')
plt.title('Top 3 Cuisines and Their Percentages')
plt.show()
