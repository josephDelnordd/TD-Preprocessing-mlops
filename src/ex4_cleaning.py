import pandas as pd

Clients_Data = pd.read_csv("data/Custemers.csv")

print(Clients_Data.dtypes)

if "name" in Clients_Data.columns:

    Clients_Data[
        ["firstname","lastname"]
    ] = (
        Clients_Data["name"]
        .str.split(
            " ",
            n=1,
            expand=True
        )
    )

    Clients_Data = (
        Clients_Data[
            Clients_Data[
                "lastname"
            ].str.len() > 16
        ]
    )

print(
    Clients_Data.head()
)
