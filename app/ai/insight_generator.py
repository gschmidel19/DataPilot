def generate_insights(metrics):

    insights = []

    # =====================================
    # Quality Score
    # =====================================

    quality_score = metrics["quality_score"]

    if quality_score >= 90:
        insights.append(
            "The dataset has excellent overall quality."
        )

    elif quality_score >= 70:
        insights.append(
            "The dataset has good overall quality, but some improvements can be made."
        )

    else:
        insights.append(
            "The dataset contains significant quality issues that may impact analysis."
        )

    # =====================================
    # Missing Values
    # =====================================

    missing_percentages = metrics["missing_percentage"]

    high_missing = missing_percentages[
        missing_percentages > 15
    ]

    if len(high_missing) > 0:

        for column, value in high_missing.items():

            insights.append(
                f"The column '{column}' contains {value}% missing values."
            )

    else:

        insights.append(
            "Missing-value presence is low across the dataset."
        )

    # =====================================
    # Duplicate Rows
    # =====================================

    duplicate_rows = metrics["duplicate_rows"]

    if duplicate_rows > 0:

        insights.append(
            f"The dataset contains {duplicate_rows} duplicate rows."
        )

    else:

        insights.append(
            "No duplicate rows were detected."
        )

    # =====================================
    # High Cardinality
    # =====================================

    cardinality = metrics["cardinality"]

    high_cardinality = cardinality[
        cardinality > 50
    ]

    if len(high_cardinality) > 0:

        for column, value in high_cardinality.items():

            insights.append(
                f"The column '{column}' has high cardinality with {value} unique values."
            )

    # =====================================
    # Numeric Columns
    # =====================================

    numeric_columns = metrics["dtypes"][
        metrics["dtypes"] != "object"
    ]

    if len(numeric_columns) > 0:

        insights.append(
            "Numeric columns were detected and are ready for statistical analysis."
        )

    return insights