import pandas as pd
import joblib
import streamlit as st
from sklearn.metrics.pairwise import linear_kernel

@st.cache_resource
def load_models():
    tfidf_matrix = joblib.load("models/tfidf_matrix.pkl")
    sentiment_model = joblib.load("models/sentiment_model.pkl")
    sentiment_vectorizer = joblib.load("models/sentiment_vectorizer.pkl")
    return tfidf_matrix, sentiment_model, sentiment_vectorizer

@st.cache_data
def load_data():
    recommend_df = pd.read_parquet("data/processed/recommend_products.parquet")
    
    # Create product index
    indices = pd.Series(
        recommend_df.index,
        index=recommend_df["product_title"]
    ).drop_duplicates()
    
    return recommend_df, indices

def recommend_products(product_name, top_n=5):
    tfidf_matrix, _, _ = load_models()
    recommend_df, indices = load_data()
    
    if product_name not in indices:
        return "Product not found."

    idx = indices[product_name]
    sim_scores = linear_kernel(tfidf_matrix[idx], tfidf_matrix).flatten()
    similar_indices = sim_scores.argsort()[::-1][1:top_n+1]

    recommendations = recommend_df.iloc[similar_indices][["product_title"]].copy()
    recommendations["Similarity Score"] = sim_scores[similar_indices].round(4)
    return recommendations.reset_index(drop=True)

def predict_sentiment(review):
    _, sentiment_model, sentiment_vectorizer = load_models()
    
    review_vector = sentiment_vectorizer.transform([review])
    prediction = sentiment_model.predict(review_vector)[0]
    confidence = sentiment_model.predict_proba(review_vector).max()
    
    return prediction, confidence

def load_css():
    import os
    css_files = [f for f in os.listdir("styles") if f.endswith(".css")]
    combined_css = ""
    for file in css_files:
        with open(f"styles/{file}", encoding="utf-8") as f:
            combined_css += f.read() + "\n"
    if combined_css:
        st.markdown(f"<style>{combined_css}</style>", unsafe_allow_html=True)

def render_footer():
    st.markdown("""
    <hr style="border-color: #E5E7EB; margin-top: 40px;">
    <center style="color: #777; font-size: 14px; margin-bottom: 20px;">
    Made with by <b>Bhumika Sharma</b><br>
    Python • Streamlit • NLP • Scikit-Learn
    </center>
    """, unsafe_allow_html=True)

import base64
def get_image_base64(image_path):
    import os
    if not os.path.exists(image_path):
        return ""
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def render_layout(page_function, active_page="Home"):
    from components.navbar import navbar
    from components.footer import footer
    from components.chatbot import render_chatbot
    from theme_engine import inject_live_theme
    from components.appearance_studio import render_appearance_studio
    import json
    
    # 1. Read client-side theme from URL (100% native, no custom components to break)
    ls_val = None
    if "theme" in st.query_params:
        try:
            ls_val = json.loads(st.query_params["theme"])
        except:
            pass
    
    # 2. Inject Dynamic Theme Variables First
    inject_live_theme(ls_val)
    
    # 2. Load CSS and components
    load_css()
    navbar(active_page)
    
    # 3. Render the Appearance Studio below the headers
    render_appearance_studio()
    
    page_function()
    render_chatbot()
    footer()
