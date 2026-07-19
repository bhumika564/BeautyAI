import streamlit as st
from components.ui import get_image_base64

def hero():
    left, right = st.columns([1.05, 0.95], gap="large")

    with left:
        st.markdown(
            """
            <div style="margin-top: 32px;">
                <div class="hero-badge">
                    AI-Powered Beauty Recommendation Engine
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <h1 class="hero-title">
                Discover Your Perfect<br>
                <span>Beauty Products</span>
            </h1>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <p class="hero-subtitle">
            Get personalized product recommendations, analyze customer sentiments,
            and explore insights from 100K+ Amazon Beauty reviews.
            </p>
            """,
            unsafe_allow_html=True,
        )

        with st.container():
            button_col1, button_col2 = st.columns([1, 1])

            with button_col1:
                if st.button("Explore Products", key="explore_btn", use_container_width=True):
                    st.switch_page("pages/recommendation.py")

            with button_col2:
                if st.button("Analyze Reviews", key="analytics_btn", use_container_width=True):
                    st.switch_page("pages/sentiment.py")

        st.markdown("<br>", unsafe_allow_html=True)

        avatar_col, text_col = st.columns([0.35, 0.65])

        with avatar_col:
            st.image(
                "assets/avatars.png",
                use_container_width=True,
            )

        with text_col:
            st.markdown(
                """
                <div class="users-text">
                Trusted by <strong>millions</strong><br>
                of customers
                </div>
                """,
                unsafe_allow_html=True,
            )

    with right:
        # We use HTML for the floating product card to achieve the glassmorphism and hover effects
        featured_img = get_image_base64("assets/featured_product.png")
        
        st.markdown(f"""
        <div class="hero-product-card">
            <div class="hero-product-badge">Recommended Today</div>
            <img src="data:image/jpeg;base64,{featured_img}" alt="Featured Product">
            <div class="hero-product-title">derma e Soothing Skin Treatment</div>
            <div class="hero-product-stars"><span style="color:#6D6D6D; font-size:14px; font-weight:400;">4.8 (2,314)</span></div>
            <div class="hero-product-score">AI Match Score 96%</div>
            <div class="hero-product-footer">Bestseller</div>
        </div>
        """, unsafe_allow_html=True)
