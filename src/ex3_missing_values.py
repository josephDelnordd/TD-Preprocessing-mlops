import pandas as pd

Clients_Data = pd.read_csv("data/Custemers.csv")

print(
    Clients_Data.isnull().sum()
)

if "name" in Clients_Data.columns:
    print(
        Clients_Data[
            Clients_Data["name"].isnull()
        ]
    )
