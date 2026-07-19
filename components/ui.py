import streamlit as st
import base64
import os
import random

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
        <h1 style="color:var(--primary); font-size:48px; margin:0; line-height: 1;">{value}</h1>
        <p style="color:var(--text-light); font-size:17px; margin:8px 0 0 0; font-weight: 500;">{title}</p>
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
    
    # Fake e-commerce data based on string hash for consistency
    seed = sum(ord(c) for c in title)
    random.seed(seed)
    price = round(random.uniform(15.0, 85.0), 2)
    mrp = round(price * random.uniform(1.2, 1.5), 2)
    discount = int((1 - price/mrp) * 100)
    
    st.markdown(f"""
    <div class="product-card">
        <div class="category-badge">{category}</div>
        <img src="data:image/png;base64,{img_b64}" class="product-image">
        <div class="product-title">{title}</div>
        <div class="product-price">
            ${price:.2f} <span class="product-mrp">${mrp:.2f}</span> <span class="product-discount">{discount}% Off</span>
        </div>
        <div class="product-rating">
            <span class="rating-count">({reviews})</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

def selected_product_card(image, title, rating="4.6", reviews="2,143", category="Skin Care"):
    img_b64 = get_image_base64(image)
    
    seed = sum(ord(c) for c in title)
    random.seed(seed)
    price = round(random.uniform(15.0, 85.0), 2)
    
    st.markdown(f"""
    <div class="selected-card">
        <img src="data:image/png;base64,{img_b64}" class="selected-image">
        <div>
            <div class="category-badge" style="position:static; display:inline-block; margin-bottom:12px;">{category}</div>
            <div class="selected-title">{title}</div>
            <div class="product-rating" style="margin-bottom:8px;">{rating} <span class="rating-count">({reviews} Reviews)</span></div>
            <div class="product-price" style="font-size:24px;">${price:.2f}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def recommendation_card(image, title, ai_score, category="Skin Care"):
    img_b64 = get_image_base64(image)
    
    seed = sum(ord(c) for c in title)
    random.seed(seed)
    price = round(random.uniform(15.0, 85.0), 2)
    mrp = round(price * random.uniform(1.2, 1.5), 2)
    discount = int((1 - price/mrp) * 100)
    
    st.markdown(f"""
    <div class="recommend-card">
        <img src="data:image/png;base64,{img_b64}" class="product-image" style="height: 180px;">
        <div class="product-title">
            {title}
        </div>
        <div class="product-price" style="font-size: 15px; margin-bottom: 6px;">
            ${price:.2f} <span class="product-mrp">${mrp:.2f}</span> <span class="product-discount" style="font-size:11px;">{discount}% Off</span>
        </div>
        <div class="product-rating" style="margin-bottom: 12px; font-size: 12px;">
            <span class="rating-count">Top Match</span>
        </div>
        <div class="ai-badge">
            AI Match {ai_score}%
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
