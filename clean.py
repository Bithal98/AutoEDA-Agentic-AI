import pandas as pd

def clean_data(df: pd.DataFrame):
    """
    Basic data cleaning agent
    """

    cleaning_report = {}


# Handle missing values
    missing = df.isnull().sum()

    for col in missing.index:
        if missing[col] > 0:
            if df[col].dtype == "object":
                df[col] = df[col].fillna(df[col].mode()[0])
                cleaning_report[col] = "Filled missing values with mode"
            else:
                df[col] = df[col].fillna(df[col].median())
                cleaning_report[col] = "Filled missing values with median"


# Remove duplicates
    before = df.shape[0]
    df = df.drop_duplicates()
    after = df.shape[0]

    if before != after:
        cleaning_report["duplicates"] = f"Removed {before - after} duplicate rows"

    return df, cleaning_report
