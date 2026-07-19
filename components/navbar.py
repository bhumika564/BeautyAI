import streamlit as st

def navbar(active_page="Home"):
    st.markdown('<div class="navbar-wrapper">', unsafe_allow_html=True)
    
    # We use Streamlit columns to create the navbar natively
    cols = st.columns([3, 0.7, 0.7, 0.7, 0.7, 0.7, 1.5], gap="small")
    
    from utils import get_image_base64
    logo_b64 = get_image_base64("assets/logo.png")
    with cols[0]:
        st.markdown(f'<div class="logo" style="margin-top:-16px;"><img src="data:image/png;base64,{logo_b64}" style="width:100%; max-width:280px; height:auto; object-fit:contain;"></div>', unsafe_allow_html=True)
        
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
                st.markdown(f'<div class="nav-active">{label}</div>', unsafe_allow_html=True)
            else:
                if st.button(label, key=f"nav_{label}", use_container_width=True):
                    st.switch_page(path)
            
    with cols[6]:
        if st.button("✨ Analyze Review", key="nav_cta", use_container_width=True):
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
    <div style="background-color: #000000; color: #FFFFFF; text-align: center; padding: 10px 0; font-size: 11px; font-weight: 500; letter-spacing: 1.5px; text-transform: uppercase;">
        <span style="color: #FF9C71;">Data-Driven</span> Recommendations &bull; <span style="color: #FF9C71;">Expert</span> Beauty Intelligence
    </div>
    <div style="background-color: var(--card); padding: 70px 20px; text-align: center; margin-bottom: 40px; border-bottom: 1px solid var(--border);">
        <h1 style="font-family: 'Lora', serif; font-size: 52px; color: var(--text); font-weight: 400; letter-spacing: 0.05em; margin: 0;">{header_title}</h1>
    </div>
    """, unsafe_allow_html=True)
