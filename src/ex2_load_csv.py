import pandas as pd

Clients_Data = pd.read_csv("data/Custemers.csv")

print(Clients_Data.shape)
print(Clients_Data.columns)
print(Clients_Data.head())
