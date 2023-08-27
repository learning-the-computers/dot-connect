"""Example for dot_connect usage with Streamlit and Snowpark."""

import ibis
import streamlit as st

import dot_connect

# Create a Snowpark session with dot_connect.
session = dot_connect.snowpark.connect()

# Read the Titanic dataset using Ibis with a DuckDB backend and write to Snowflake table.
titanic = ibis.read_csv(
    "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
)
df = session.create_dataframe(titanic.to_pandas())
df.write.save_as_table("TITANIC", mode="overwrite")

# View the DataFrame in application. Streamlit can evaluate Snowpark DataFrames.
st.dataframe(session.table("TITANIC"))
