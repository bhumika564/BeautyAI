import streamlit as st
import base64
import os

def get_image_base64(image_path):
    if not os.path.exists(image_path):
        return ""
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def section_title(title, subtitle=None):
    st.markdown(f'<div class="section-title">{title}</div>', unsafe_allow_html=True)
    if subtitle:
        st.markdown(f'<div class="section-subtitle">{subtitle}</div>', unsafe_allow_html=True)

def metric_card(value, title):
    st.markdown(f"""
    <div class="card" style="text-align:center;">
        <h1 style="color:#F45B8C; font-size:48px; margin:0; line-height: 1;">{value}</h1>
        <p style="color:#6D6D6D; font-size:17px; margin:8px 0 0 0; font-weight: 500;">{title}</p>
    </div>
    """, unsafe_allow_html=True)

def feature_card(icon, title, description, bg_color, icon_color):
    st.markdown(f"""
    <div class="card">
        <div class="stat-icon" style="background:{bg_color}; color:{icon_color};">{icon}</div>
        <div class="card-title">{title}</div>
        <div class="card-body">{description}</div>
    </div>
    """, unsafe_allow_html=True)

def product_card(image, title, rating, reviews, category):
    img_b64 = get_image_base64(image)
    st.markdown(f"""
    <div class="product-card">
        <img src="data:image/jpeg;base64,{img_b64}" class="product-image">
        <div class="product-title">
            {title}
        </div>
        <div class="product-rating">
            ⭐ {rating} ({reviews} reviews)
        </div>
        <div class="category-badge">
            {category}
        </div>
    </div>
    """, unsafe_allow_html=True)

def selected_product_card(image, title, rating="4.6", reviews="2,143", category="Skin Care"):
    img_b64 = get_image_base64(image)
    
    st.markdown(f"""
    <div class="selected-card">
        <img src="data:image/jpeg;base64,{img_b64}" class="selected-image">
        <div>
            <div class="category-badge" style="margin-top:0; margin-bottom:12px;">{category}</div>
            <div class="selected-title">{title}</div>
            <div class="rating">⭐ {rating} <span style="color:var(--text-light); font-weight:400;">({reviews} Reviews)</span></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def recommendation_card(image, title, ai_score, category="Skin Care"):
    img_b64 = get_image_base64(image)
    
    st.markdown(f"""
    <div class="recommend-card">
        <img src="data:image/jpeg;base64,{img_b64}" class="product-image" style="height: 160px;">
        <div class="product-title" style="margin-bottom: 8px; height: 44px; font-size:16px;">
            {title}
        </div>
        <div class="rating" style="margin-bottom: 12px; font-size: 14px;">
            ⭐⭐⭐⭐⭐ <span style="color:var(--text-light); font-weight:400;">(Top Match)</span>
        </div>
        <div class="ai-badge">
            <span class="icon">🤖</span> AI Match {ai_score}%
        </div>
        <div class="why-recommended">
            <div class="why-recommended-title">Why Recommended?</div>
            ✓ Similar ingredients<br>
            ✓ Customer review overlap<br>
            ✓ Shared product category
        </div>
        <div class="save-btn"></div>
    </div>
    """, unsafe_allow_html=True)
