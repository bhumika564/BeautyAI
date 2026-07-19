import streamlit as st

def search_bar(options):
    return st.selectbox(
        "Search Beauty Product",
        options,
        index=None,
        placeholder="Start typing a product..."
    )
