import pandas as pd

file_path = "Dataset.csv"
df = pd.read_csv(file_path)

df.head()

import matplotlib.pyplot as plt
import numpy as np

lats = df['Latitude'].values
lons = df['Longitude'].values

plt.figure(figsize=(8, 6))
plt.scatter(lons, lats, alpha=0.5, s=10, c='blue')
plt.title("Restaurant Locations")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()


