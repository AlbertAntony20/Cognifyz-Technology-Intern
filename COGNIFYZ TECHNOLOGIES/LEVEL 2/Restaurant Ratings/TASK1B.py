import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Dataset.csv")
df = df.drop_duplicates()
df = df.dropna(subset=['Votes'])
df['Votes'] = pd.to_numeric(df['Votes'], errors='coerce')
df = df.dropna(subset=['Votes'])

avg_votes = df['Votes'].mean()
print(f"Average number of votes received by restaurants: {avg_votes:.2f}")

df = df.dropna(subset=['Price range'])
votes_price = df.groupby('Price range')['Votes'].sum()

plt.figure(figsize=(7,7))
votes_price.plot(kind='pie', autopct='%1.1f%%', startangle=140, shadow=True)
plt.title("Share of Total Votes by Price Range")
plt.ylabel("") 
plt.show()
