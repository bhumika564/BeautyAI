import streamlit as st

def navbar(active_page="Home"):
    # 1. Thin Dark Banner (Like Image 2)
    st.markdown('<div style="background-color: #3B3B3B; height: 16px; width: 100%; margin-top: -60px; margin-bottom: 10px;"></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="navbar-wrapper" style="background-color: #F8F8F8; padding: 10px 20px; border-bottom: 1px solid #EAEAEA;">', unsafe_allow_html=True)
    
    # We use Streamlit columns to create the exact layout from Image 2
    cols = st.columns([1.8, 0.8, 0.9, 0.9, 0.9, 0.8, 2.0, 1.2], gap="small", vertical_alignment="center")
    
    from utils import get_image_base64
    logo_b64 = get_image_base64("assets/logo.png")
    with cols[0]:
        st.markdown(f'<div class="logo"><img src="data:image/png;base64,{logo_b64}" style="width:100%; max-width:140px; height:auto; object-fit:contain;"></div>', unsafe_allow_html=True)
        
    nav_items = [
        ("Home", "pages/home.py"),
        ("Products", "pages/recommendation.py"),
        ("Reviews", "pages/sentiment.py"),
        ("Analytics", "pages/analytics.py"),
        ("About", "pages/about.py")
    ]
    
    for i, (label, path) in enumerate(nav_items):
        with cols[i+1]:
            if active_page == label:
                st.markdown(f'<div class="nav-active" style="color: #000; font-size: 15px; font-weight: 500;">{label}</div>', unsafe_allow_html=True)
            else:
                if st.button(label, key=f"nav_{label}", use_container_width=True, type="tertiary"):
                    st.switch_page(path)
            
    with cols[6]:
        st.markdown('<div style="text-align: right; font-weight: 600; font-size: 15px; color: #000; padding-top: 8px;">+447947387369</div>', unsafe_allow_html=True)
        
    with cols[7]:
        if st.button("ANALYZE", key="nav_cta", use_container_width=True, type="primary"):
            st.switch_page("pages/sentiment.py")
            
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Page Title Mapping
    page_titles = {
        "Home": "Intelligent Beauty Curation",
        "Products": "Explore AI Recommendations",
        "Reviews": "Sentiment Analysis",
        "Analytics": "Market Analytics",
        "About": "The BeautyAI Platform"
    }
    header_title = page_titles.get(active_page, "Intelligent Beauty Curation")
    
    # 1. Thin Black Banner
    # 2. Large Beige Page Header
    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500&display=swap');
    </style>
    <div style="background-color: #000000; color: #FFFFFF; text-align: center; padding: 10px 0; font-size: 11px; font-weight: 500; letter-spacing: 1.5px; text-transform: uppercase;">
        <span style="color: #FF9C71;">Data-Driven</span> Recommendations &bull; <span style="color: #FF9C71;">Expert</span> Beauty Intelligence
    </div>
    <div style="background-color: #E8E2D9; padding: 70px 20px; text-align: center; margin-bottom: 40px; border-bottom: 1px solid #D8D2C9;">
        <h1 style="font-family: 'Playfair Display', serif; font-size: 54px; color: #2C3E50; font-weight: 400; letter-spacing: 0.06em; margin: 0;">{header_title}</h1>
    </div>
    """, unsafe_allow_html=True)
