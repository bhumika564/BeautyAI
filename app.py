import streamlit as st
from utils import load_css

st.set_page_config(
    page_title="BeautyAI",
    page_icon="assets/logo.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

load_css()

# Set up the multi-page router without the default sidebar
pg = st.navigation(
    [
        st.Page("pages/home.py", title="Home", default=True),
        st.Page("pages/recommendation.py", title="Recommendation Engine"),
        st.Page("pages/sentiment.py", title="Sentiment Analysis"),
        st.Page("pages/analytics.py", title="Market Analytics"),
        st.Page("pages/about.py", title="About")
    ], 
    position="hidden" # Hides the native sidebar navigation so our custom navbar shines
)

pg.run()