"""Example for dot_connect usage with Streamlit and Snowpark."""

import streamlit as st

import dot_connect

snowpark_session = dot_connect.snowpark.connect()

st.table(snowpark_session.table("AMAZING").to_pandas())
