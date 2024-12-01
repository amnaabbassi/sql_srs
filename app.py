import  streamlit as st
import  pandas as pd
import duckdb


st.write("""
#SQL SRS
Spaced Repetition System SQL practice
""")

option = st.selectbox(
    "What would you like to review?",
    ("Joins", "GroupBy", "Windows Functions"),
    index=None,
    placeholder="Select a theme..."
)


st.write("You selected:", option)