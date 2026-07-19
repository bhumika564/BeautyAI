import streamlit as st

def init_theme_state():
    """Initializes the session state variables for the Appearance Studio."""
    if "theme_font_primary" not in st.session_state:
        st.session_state.theme_font_primary = "Inter"
    if "theme_font_heading" not in st.session_state:
        st.session_state.theme_font_heading = "Lora"

def inject_live_theme():
    """Builds and injects the dynamic CSS variables based on session state."""
    init_theme_state()
    
    primary_font = st.session_state.theme_font_primary
    heading_font = st.session_state.theme_font_heading
    
    primary_font_url = primary_font.replace(" ", "+")
    heading_font_url = heading_font.replace(" ", "+")
    
    # Fetch both fonts dynamically from Google Fonts with standard weights
    font_import = f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family={primary_font_url}:wght@300;400;500;600&family={heading_font_url}:ital,wght@0,400;0,500;0,600;1,400&display=swap');
    </style>
    """
    
    # Map them to global CSS variables
    css_vars = f"""
    <style>
        :root {{
            --font-primary: '{primary_font}', sans-serif;
            --font-heading: '{heading_font}', serif;
        }}
    </style>
    """
    
    st.markdown(font_import + css_vars, unsafe_allow_html=True)
