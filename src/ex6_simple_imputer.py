import pandas as pd

from sklearn.impute import (
    SimpleImputer
)

origin_Data = pd.read_csv(
    "data/melb_data.csv"
)

origin_Data_num = (
    origin_Data.select_dtypes(
        include=["number"]
    )
)

imputer = SimpleImputer(
    strategy="mean"
)

imputer.fit(
    origin_Data_num
)

transformed = (
    imputer.transform(
        origin_Data_num
    )
)

df_transformed = (
    pd.DataFrame(
        transformed,
        columns=origin_Data_num.columns
    )
)

print(
    df_transformed.head()
)
