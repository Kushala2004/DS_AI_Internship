import pandas as pd
data = pd.read_csv("task1.csv")
print(data)
print(data.describe())
print(data.head())
print(data.tail())
print(data.info())
print(data.shape)