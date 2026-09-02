import pandas as pd

def analyse_dataset(path):

    print(
        f"\nAnalyse : {path}"
    )

    df = pd.read_csv(path)

    print(df.shape)

    print(df.info())

    print(
        df.isnull().sum()
    )

    print(
        df.duplicated().sum()
    )

    df.drop_duplicates(
        inplace=True
    )

    df.dropna(
        how="all",
        inplace=True
    )

    return df

olympics = analyse_dataset(
    "data/olympics.csv"
)

flicker = analyse_dataset(
    "data/flicker.csv"
)
