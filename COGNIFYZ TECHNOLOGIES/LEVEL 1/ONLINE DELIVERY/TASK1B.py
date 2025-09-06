import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Dataset.csv", encoding='latin-1')

avg_ratings = df.groupby('Has Online delivery')['Aggregate rating'].mean()
print("Average Ratings (With vs Without Online Delivery):")
print(avg_ratings)

plt.figure(figsize=(6,4))
avg_ratings.plot(kind='barh', color=['skyblue', 'salmon'])
plt.ylabel('Has Online Delivery')
plt.xlabel('Average Rating')
plt.title('Average Ratings: With vs Without Online Delivery')
plt.xlim(0, 5)
plt.show()
