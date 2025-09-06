import pandas as pd

file_path = "Dataset.csv"
df = pd.read_csv(file_path)

df.head()

import matplotlib.pyplot as plt
import numpy as np

lats = df['Latitude'].values
lons = df['Longitude'].values

plt.figure(figsize=(8, 6))
plt.hexbin(lons, lats, gridsize=40, cmap='Reds', alpha=0.7)
plt.colorbar(label="Density of Restaurants")
plt.title("Clusters of Restaurants")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()
