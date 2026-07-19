import streamlit as st

def navbar(active_page="Home"):
    st.markdown('<div class="navbar-wrapper">', unsafe_allow_html=True)
    
    # We use Streamlit columns to create the navbar natively
    cols = st.columns([2, 0.8, 0.8, 0.8, 0.8, 0.8, 1.5], gap="small")
    
    from utils import get_image_base64
    logo_b64 = get_image_base64("assets/logo.png")
    with cols[0]:
        st.markdown(f'<div class="logo" style="margin-top:-8px;"><img src="data:image/png;base64,{logo_b64}" style="height:56px; object-fit:contain;"></div>', unsafe_allow_html=True)
        
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
