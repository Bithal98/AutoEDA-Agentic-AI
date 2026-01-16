import pandas as pd
from datetime import datetime

def export_report(
    eda_result: dict,
    cleaning_report: dict | None = None,
    automl_result: dict | None = None,
    file_name: str = "eda_report"
):
    """
    Export EDA, cleaning, and AutoML results to a CSV report
    """

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_file = f"{file_name}_{timestamp}.csv"

    rows = []

    # EDA Results
    
    rows.append({"Section": "EDA", "Key": "Target Column", "Value": eda_result.get("target")})

    for key, value in eda_result["data_quality"].items():
        rows.append({"Section": "Data Quality", "Key": key, "Value": str(value)})


    # Cleaning Results
 
    if cleaning_report:
        for col, action in cleaning_report.items():
            rows.append({"Section": "Cleaning", "Key": col, "Value": action})

 
    # AutoML Results
  
    if automl_result:
        rows.append({"Section": "AutoML", "Key": "Problem Type", "Value": automl_result["problem_type"]})

        for model, score in automl_result["model_performance"].items():
            rows.append({"Section": "AutoML", "Key": model, "Value": score})

  
    # Save report
  
    report_df = pd.DataFrame(rows)
    report_df.to_csv(report_file, index=False)

    return report_file
