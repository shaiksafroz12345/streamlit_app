""" Streamlit package - Streamlit is an open-source Python library that makes it easy 
to create and share custom web apps for machine learning and data science projects"""

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# adds a large title to the app
st.title("📊 CSV Data Explorer")
# Lets users upload files
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Preview of the Dataset")
    st.write(df)

    st.subheader("Basic Information")
    st.write(f"Number of Rows: {df.shape[0]}") # prints no. of rows
    st.write(f"Number of Columns: {df.shape[1]}") # prints no. of columns

    if st.checkbox("Show Summary Statistics"):
        st.write(df.describe())

    if st.checkbox("Show Missing Values"):
        st.write(df.isnull().sum())

    st.subheader("Column Selection for Visualization")
    numeric_columns = df.select_dtypes(
        include=['float64', 'int64']).columns.tolist()

    column = st.selectbox(
        "Choose a numeric column to plot histogram", numeric_columns)

    if column:
        fig, ax = plt.subplots()
        sns.histplot(df[column], kde=True, ax=ax)
        st.pyplot(fig)

    if st.checkbox("Show Correlation Heatmap"):
        fig2, ax2 = plt.subplots()
        sns.heatmap(df[numeric_columns].corr(),
                    annot=True, cmap='coolwarm', ax=ax2)
        st.pyplot(fig2)
else:
    st.info("👈 Upload a CSV file to get started")
