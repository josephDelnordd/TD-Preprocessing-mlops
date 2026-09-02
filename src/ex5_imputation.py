import pandas as pd

origin_Data = pd.read_csv(
    "data/melb_data.csv"
)

def missing_columns(originDB):

    colsWithMissing = [
        col
        for col in originDB.columns
        if originDB[col]
           .isnull()
           .any()
    ]

    reduced_original_data = (
        originDB.drop(
            colsWithMissing,
            axis=1
        )
    )

    return (
        colsWithMissing,
        reduced_original_data
    )

print(
    origin_Data.isnull().sum()
)
