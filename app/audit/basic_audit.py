import pandas as pd


def generate_basic_audit(df):

    audit_report = {}

    # Shape
    audit_report["rows"] = df.shape[0]
    audit_report["columns"] = df.shape[1]

    # Null values
    audit_report["null_values"] = df.isnull().sum()

    # Duplicates
    audit_report["duplicates"] = df.duplicated().sum()

    # Data types
    audit_report["dtypes"] = df.dtypes

    return audit_report