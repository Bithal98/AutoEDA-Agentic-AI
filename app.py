import streamlit as st
import pandas as pd

from eda import run_eda
from clean import clean_data
from chat_agent import chat_with_data
from automl import run_automl
from export import export_report

st.set_page_config(page_title="Auto EDA AI Agent", layout="wide")

st.title("📊 Auto EDA AI Agent")
st.write("Upload a CSV file and let AI analyze it end-to-end")


# Upload CSV
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    st.success("Dataset loaded successfully")


# Preview

    st.subheader("🔍 Dataset Preview")
    st.write("Shape:", df.shape)
    st.dataframe(df.head())

# EDA Agent

    st.subheader("📈 EDA Agent")
    eda_result = run_eda(df)

    st.write("🎯 Target Column:", eda_result["target"])
    st.json(eda_result["data_quality"])
    st.dataframe(eda_result["statistics"])
    st.dataframe(eda_result["correlation"])


    # Cleaning Agent
 
    st.subheader("🧹 Data Cleaning Agent")
    clean_df, cleaning_report = clean_data(df)
    st.json(cleaning_report)


    # Chat Agent
   
    st.subheader("💬 Chat with Data")
    user_question = st.text_input("Ask a question about the dataset")

    if user_question:
        answer = chat_with_data(user_question, eda_result)
        st.write("🤖 AI Answer:")
        st.write(answer)


    # AutoML Agent
  
    st.subheader("🤖 AutoML Agent")

    if st.button("Run AutoML"):
        automl_result = run_automl(clean_df)
        st.json(automl_result)

   
    # Export Agent
 
    st.subheader("📤 Export Report")

    if st.button("Export Report"):
        report_file = export_report(
            eda_result=eda_result,
            cleaning_report=cleaning_report,
            automl_result=automl_result if "automl_result" in locals() else None
        )
        st.success(f"Report saved as {report_file}")
