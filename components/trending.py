import streamlit as st
from components.ui import product_card
from data.products import get_trending_products

def trending():
    header_col1, header_col2 = st.columns([0.8, 0.2])
    
    with header_col1:
        st.markdown(
        """
        <div class="section-header" style="margin-bottom: 0;">
            <div>
                <h2>🔥 Trending Beauty Picks</h2>
                <p>Most loved products by our community</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
        )
        
    with header_col2:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("View all products ➜", key="view_all", use_container_width=True):
            st.switch_page("pages/recommendation.py")
            
    products = get_trending_products()
    
    cols = st.columns([1, 0.08, 1, 0.08, 1, 0.08, 1])
    content_cols = [cols[0], cols[2], cols[4], cols[6]]
    
    for i, product in enumerate(products):
        with content_cols[i]:
            product_card(
                image=product["image"],
                title=product["name"],
                rating=product["rating"],
                reviews=product["reviews"],
                category=product["category"]
            )
            if st.button("Explore", key=f"trend_{i}", use_container_width=True):
                st.switch_page("pages/recommendation.py")
