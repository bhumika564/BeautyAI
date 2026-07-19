import streamlit as st

def navbar(active_page="Home"):
    from utils import get_image_base64
    logo_b64 = get_image_base64("assets/logo.png")
    
    # 1. Native Streamlit Navbar Row (This is the FIRST element on the page)
    # We use 10 columns to match the Myntra layout exactly (Logo, 5 Links, Search, 3 Icons)
    cols = st.columns([1.5, 0.7, 0.9, 0.8, 0.9, 0.7, 2.5, 0.8, 0.8, 0.6], gap="small", vertical_alignment="center")
    
    with cols[0]:
        # Inject CSS directly into the first column to guarantee it styles the parent row without being stripped
        st.markdown("""
        <style>
            /* Hide default Streamlit header */
            header[data-testid="stHeader"] {
                display: none !important;
            }
            
            /* Remove top padding of the main container */
            .block-container {
                padding-top: 0 !important;
                padding-left: 0 !important;
                padding-right: 0 !important;
                max-width: 100% !important;
            }
            
            /* Fix the very first element (our st.columns row) to the top of the viewport */
            .block-container > div[data-testid="stVerticalBlock"] > div:first-child {
                position: fixed !important;
                top: 0 !important;
                left: 0 !important;
                right: 0 !important;
                background-color: #ffffff !important;
                box-shadow: 0 4px 12px 0 rgba(0,0,0,.05) !important;
                z-index: 999999 !important;
                padding: 10px 2% !important;
                margin: 0 !important;
            }
            
            /* Strip default button styling to make them look like clean Myntra text links */
            .block-container > div[data-testid="stVerticalBlock"] > div:first-child button {
                background-color: transparent !important;
                border: none !important;
                box-shadow: none !important;
                color: #282c3f !important;
                font-weight: 700 !important;
                font-size: 12px !important;
                text-transform: uppercase !important;
                letter-spacing: .3px !important;
                height: auto !important;
                padding: 10px 0 !important;
                min-height: 0 !important;
            }
            .block-container > div[data-testid="stVerticalBlock"] > div:first-child button:hover {
                color: #ee5f73 !important;
            }
            
            /* Style the search bar input */
            .block-container > div[data-testid="stVerticalBlock"] > div:first-child div[data-baseweb="input"] {
                background-color: #f5f5f6 !important;
                border: 1px solid #f5f5f6 !important;
                border-radius: 4px !important;
            }
        </style>
        """, unsafe_allow_html=True)
        st.markdown(f'<img src="data:image/png;base64,{logo_b64}" style="width:100%; min-width:200px; max-width:300px; height:auto; object-fit:contain; margin-left:0px; margin-top: 5px;">', unsafe_allow_html=True)
        
    nav_items = [
        ("Home", "pages/home.py"),
        ("Products", "pages/recommendation.py"),
        ("Reviews", "pages/sentiment.py"),
        ("Analytics", "pages/analytics.py"),
        ("About", "pages/about.py")
    ]
    
    # Render the 5 navigation links
    for i, (label, path) in enumerate(nav_items):
        with cols[i+1]:
            if active_page == label:
                # Active state with pink underline
                st.markdown(f'<div style="color: #ee5f73; font-weight: 700; font-size: 12px; text-transform: uppercase; text-align: center; border-bottom: 3px solid #ee5f73; padding-bottom: 5px; margin-top: 10px; letter-spacing: .3px;">{label}</div>', unsafe_allow_html=True)
            else:
                if st.button(label, key=f"nav_{label}", use_container_width=True):
                    st.switch_page(path)
                    
    # Render the Search Bar
    with cols[6]:
        st.text_input("Search", placeholder="Search for products, brands and more", label_visibility="collapsed")
        
    # Render the 3 right-side icons as text links
    with cols[7]:
        st.button("PROFILE", key="nav_profile", use_container_width=True)
    with cols[8]:
        st.button("WISHLIST", key="nav_wish", use_container_width=True)
    with cols[9]:
        st.button("BAG", key="nav_bag", use_container_width=True)

    # 2. Spacer to push the page content exactly below the 80px fixed navbar
    st.markdown('<div style="height: 75px; width: 100%;"></div>', unsafe_allow_html=True)
    
    # Page Title Mapping
    page_titles = {
        "Home": "Intelligent Beauty Curation",
        "Products": "Explore AI Recommendations",
        "Reviews": "Sentiment Analysis",
        "Analytics": "Market Analytics",
        "About": "The BeautyAI Platform"
    }
    header_title = page_titles.get(active_page, "Intelligent Beauty Curation")
    
    # 3. Thin Black Banner & Large Beige Page Header
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
