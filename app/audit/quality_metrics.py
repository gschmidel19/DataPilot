import pandas as pd


def calculate_quality_metrics(df):

    metrics = {}

    # =====================================
    # Basic info
    # =====================================

    total_rows = df.shape[0]
    total_columns = df.shape[1]

    metrics["rows"] = total_rows
    metrics["columns"] = total_columns

    # =====================================
    # Missing values
    # =====================================

    missing_values = df.isnull().sum()

    missing_percentage = (
        df.isnull().sum() / total_rows * 100
    ).round(2)

    metrics["missing_values"] = missing_values
    metrics["missing_percentage"] = missing_percentage

    # =====================================
    # Duplicate rows
    # =====================================

    duplicate_rows = df.duplicated().sum()

    duplicate_percentage = round(
        (duplicate_rows / total_rows) * 100,
        2
    )

    metrics["duplicate_rows"] = duplicate_rows
    metrics["duplicate_percentage"] = duplicate_percentage

    # =====================================
    # Data types
    # =====================================

    metrics["dtypes"] = df.dtypes

    # =====================================
    # Cardinality
    # =====================================

    cardinality = df.nunique()

    metrics["cardinality"] = cardinality

    # =====================================
    # Quality score
    # =====================================

    total_missing_percent = missing_percentage.mean()

    quality_score = 100

    quality_score -= total_missing_percent
    quality_score -= duplicate_percentage

    quality_score = max(0, round(quality_score, 2))

    metrics["quality_score"] = quality_score

    return metrics