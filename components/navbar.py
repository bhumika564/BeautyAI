import streamlit as st

def navbar(active_page="Home"):
    from utils import get_image_base64
    logo_b64 = get_image_base64("assets/logo.png")
    
    # Generate the active class dynamically
    def is_active(page_name):
        return "active" if active_page == page_name else ""
        
    html_content = f"""
    <style>
        /* Hide the native Streamlit header */
        header[data-testid="stHeader"] {{
            display: none !important;
        }}
        
        /* Remove default vertical padding but add 4% horizontal padding for breathing room */
        .block-container,
        [data-testid="stMainBlockContainer"],
        [data-testid="stAppViewBlockContainer"],
        .main {{
            padding-top: 80px !important;
            margin-top: 0 !important;
            padding-left: 4% !important;
            padding-right: 4% !important;
            max-width: 100% !important;
            overflow-x: hidden !important;
        }}
        
        /* CSS hack to force banners to break out of the 4% padding and span the full screen */
        .full-bleed-banner {{
            margin-left: -50vw !important;
            margin-right: -50vw !important;
            padding-left: 50vw !important;
            padding-right: 50vw !important;
        }}
        
        /* Force remove margins from markdown element containers at the top */
        div.element-container:nth-child(1),
        div.element-container:nth-child(2) {{
            margin-top: 0 !important;
            margin-bottom: 0 !important;
            padding-top: 0 !important;
            padding-bottom: 0 !important;
        }}
        
        /* The Fixed Myntra Header */
        .myntra-header {{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            height: 80px;
            background-color: #ffffff;
            box-shadow: 0 4px 12px 0 rgba(0,0,0,.05);
            z-index: 999999;
            display: flex;
            align-items: center;
            padding: 0 4%;
            min-width: 1000px;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }}
        
        /* Logo */
        .myntra-logo {{
            margin-right: 40px;
            display: flex;
            align-items: center;
        }}
        .myntra-logo img {{
            height: 58px;
            width: auto;
            max-width: 220px;
            object-fit: contain;
        }}
        
        /* Navigation Links */
        .myntra-nav {{
            display: flex;
            height: 100%;
            align-items: center;
        }}
        .myntra-nav a {{
            text-decoration: none;
            color: #282c3f;
            font-size: 14px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: .3px;
            height: 100%;
            display: flex;
            align-items: center;
            padding: 0 17px;
            border-bottom: 4px solid transparent;
            transition: all 0.2s ease;
        }}
        .myntra-nav a:hover, .myntra-nav a.active {{
            border-bottom: 4px solid #C4A484;
        }}
        
        /* Search Bar */
        .myntra-search {{
            flex-grow: 1;
            max-width: 500px;
            margin: 0 40px;
            position: relative;
            display: flex;
            align-items: center;
        }}
        .myntra-search input {{
            width: 100%;
            background-color: #f5f5f6;
            border: 1px solid #f5f5f6;
            border-radius: 4px;
            padding: 10px 10px 10px 45px;
            font-size: 14px;
            color: #696e79;
            outline: none;
            transition: all 0.2s ease;
        }}
        .myntra-search input:focus {{
            background-color: #ffffff;
            border: 1px solid #eaeaec;
        }}
        .myntra-search svg {{
            position: absolute;
            left: 15px;
            width: 16px;
            height: 16px;
            fill: #696e79;
        }}
        
        /* Icons (Profile, Wishlist, Bag) */
        .myntra-icons {{
            display: flex;
            gap: 25px;
            align-items: center;
            margin-left: auto;
        }}
        .myntra-icon-item {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            text-decoration: none;
            color: #000;
        }}
        .myntra-icon-item svg {{
            width: 20px;
            height: 20px;
            stroke: #000;
            fill: none;
            stroke-width: 1.5;
            margin-bottom: 5px;
            transition: all 0.2s ease;
        }}
        .myntra-icon-item span {{
            font-size: 12px;
            font-weight: 600;
            color: #000;
            transition: all 0.2s ease;
        }}
        .myntra-icon-item:hover svg, .myntra-icon-item:hover span {{
            color: #ee5f73;
            stroke: #ee5f73;
        }}
    </style>

    <div class="myntra-header">
        <div class="myntra-logo">
            <a href="./" target="_self">
                <img src="data:image/png;base64,{logo_b64}" alt="Logo">
            </a>
        </div>
        <div class="myntra-nav">
            <a href="./" target="_self" class="{is_active('Home')}">HOME</a>
            <a href="recommendation" target="_self" class="{is_active('Products')}">PRODUCTS</a>
            <a href="sentiment" target="_self" class="{is_active('Reviews')}">REVIEWS</a>
            <a href="analytics" target="_self" class="{is_active('Analytics')}">ANALYTICS</a>
            <a href="about" target="_self" class="{is_active('About')}">ABOUT</a>
        </div>
        <div class="myntra-search">
            <svg viewBox="0 0 24 24"><path d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0 0 16 9.5 6.5 6.5 0 1 0 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"></path></svg>
            <input type="text" placeholder="Search for products, brands and more">
        </div>
        <div class="myntra-icons">
            <a href="#" class="myntra-icon-item">
                <svg viewBox="0 0 24 24"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
                <span>Profile</span>
            </a>
            <a href="#" class="myntra-icon-item">
                <svg viewBox="0 0 24 24"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
                <span>Wishlist</span>
            </a>
            <a href="#" class="myntra-icon-item">
                <svg viewBox="0 0 24 24"><path d="M6 2L3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4z"></path><line x1="3" y1="6" x2="21" y2="6"></line><path d="M16 10a4 4 0 0 1-8 0"></path></svg>
                <span>Bag</span>
            </a>
        </div>
    </div>
    """
    
    # Page Title Mapping
    page_titles = {
        "Home": "Intelligent Beauty Curation",
        "Products": "Explore AI Recommendations",
        "Reviews": "Sentiment Analysis",
        "Analytics": "Market Analytics",
        "About": "The BeautyAI Platform"
    }
    header_title = page_titles.get(active_page, "Intelligent Beauty Curation")

    html_content += f"""
    <div class="full-bleed-banner" style="margin-top: 0 !important; background-color: #000000; color: #FFFFFF; text-align: center; padding: 10px 0; font-size: 11px; font-weight: 500; letter-spacing: 1.5px; text-transform: uppercase;">
        <span style="color: #FF9C71;">Data-Driven</span> Recommendations &bull; <span style="color: #FF9C71;">Expert</span> Beauty Intelligence
    </div>
    <div class="full-bleed-banner hero-banner-bg">
        <h1 class="hero-banner-title">{header_title}</h1>
    </div>
    """
    
    st.markdown(html_content, unsafe_allow_html=True)
