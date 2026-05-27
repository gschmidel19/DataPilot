import streamlit as st
import pandas as pd

from app.audit.quality_metrics import calculate_quality_metrics
from app.ai.insight_generator import generate_insights

# =====================================
# Page Config
# =====================================

st.set_page_config(
    page_title="DataPilot",
    page_icon="🚀",
    layout="wide"
)

# =====================================
# Header
# =====================================

st.title("🚀 DataPilot")
st.subheader("AI Copilot for Data Auditing")

# =====================================
# File Upload
# =====================================

uploaded_file = st.file_uploader(
    "Upload your CSV file",
    type=["csv"]
)

# =====================================
# Main App
# =====================================

if uploaded_file is not None:

    # Read CSV
    df = pd.read_csv(uploaded_file)

    st.success("Dataset loaded successfully!")

    # =====================================
    # Dataset Preview
    # =====================================

    st.write("## Dataset Preview")
    st.dataframe(df.head())

    # =====================================
    # Calculate Metrics
    # =====================================

    metrics = calculate_quality_metrics(df)

    # =====================================
    # Generate Insights
    # =====================================

    insights = generate_insights(metrics)

    # =====================================
    # Quality Score
    # =====================================

    st.write("## Data Quality Score")

    st.metric(
        label="Quality Score",
        value=f"{metrics['quality_score']}%"
    )

    # =====================================
    # Dataset Shape
    # =====================================

    st.write("## Dataset Shape")

    col1, col2 = st.columns(2)

    col1.metric(
        "Rows",
        metrics["rows"]
    )

    col2.metric(
        "Columns",
        metrics["columns"]
    )

    # =====================================
    # Duplicate Rows
    # =====================================

    st.write("## Duplicate Rows")

    col1, col2 = st.columns(2)

    col1.metric(
        "Duplicate Rows",
        metrics["duplicate_rows"]
    )

    col2.metric(
        "Duplicate %",
        f"{metrics['duplicate_percentage']}%"
    )

    # =====================================
    # Missing Values
    # =====================================

    st.write("## Missing Values")

    missing_df = pd.DataFrame({
        "Missing Values": metrics["missing_values"],
        "Missing %": metrics["missing_percentage"]
    })

    st.dataframe(missing_df)

    # =====================================
    # Cardinality
    # =====================================

    st.write("## Cardinality")

    cardinality_df = pd.DataFrame({
        "Unique Values": metrics["cardinality"]
    })

    st.dataframe(cardinality_df)

    # =====================================
    # Column Types
    # =====================================

    st.write("## Column Types")

    dtypes_df = pd.DataFrame({
        "Data Type": metrics["dtypes"]
    })

    st.dataframe(dtypes_df)

    # =====================================
    # Smart Insights
    # =====================================

    st.write("## 🧠 Smart Insights")

    for insight in insights:
        st.info(insight)