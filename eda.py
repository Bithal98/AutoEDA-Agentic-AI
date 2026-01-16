import pandas as pd

def run_eda(df: pd.DataFrame):
    """
    Perform basic exploratory data analysis
    """

# Data Quality
    data_quality = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "duplicates": int(df.duplicated().sum()),
        "missing_values": df.isnull().sum().to_dict()
    }


# Statistical Summary
    statistics = df.describe().T

   
# Detect target column
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    target_col = numeric_cols[-1] if numeric_cols else None

  
# Correlation with target
    if target_col:
        correlation = (
            df.corr(numeric_only=True)[target_col]
            .sort_values(ascending=False)
            .to_frame(name="correlation")
        )
    else:
        correlation = pd.DataFrame()

   
# Return all results
    return {
        "data_quality": data_quality,
        "statistics": statistics,
        "correlation": correlation,
        "target": target_col
    }
