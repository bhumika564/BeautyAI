import streamlit as st
import json
import os

CONFIG_PATH = "config/theme.json"

def load_saved_theme():
    """Reads the permanent theme configuration from JSON."""
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r") as f:
            return json.load(f)
    return {
        "theme_font_primary": "Avenir Next",
        "theme_font_heading": "Avenir Next",
        "theme_color_primary": "#000000",
        "theme_color_bg": "#FFFFFF",
        "theme_color_text": "#333333",
        "theme_color_hero_bg": "#E0D7D0",
        "theme_color_action_bg": "#FFFFFF",
        "theme_color_card_bg": "#E0D7D0"
    }

def save_theme(theme_dict):
    """Writes the current preview configuration to JSON."""
    os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
    with open(CONFIG_PATH, "w") as f:
        json.dump(theme_dict, f, indent=4)

def init_theme_state():
    """Initializes the session state variables from the saved JSON config."""
    saved_theme = load_saved_theme()
    for key, val in saved_theme.items():
        if key not in st.session_state:
            st.session_state[key] = val

def inject_live_theme():
    """Builds and injects the dynamic CSS variables based on session state."""
    init_theme_state()
    
    primary_font = st.session_state.theme_font_primary
    heading_font = st.session_state.theme_font_heading
    color_primary = st.session_state.theme_color_primary
    color_bg = st.session_state.theme_color_bg
    color_text = st.session_state.theme_color_text
    color_hero_bg = st.session_state.theme_color_hero_bg
    color_action_bg = st.session_state.theme_color_action_bg
    color_card_bg = st.session_state.theme_color_card_bg
    
    primary_font_url = primary_font.replace(" ", "+")
    heading_font_url = heading_font.replace(" ", "+")
    
    font_import = ""
    if primary_font != "Avenir Next" and heading_font != "Avenir Next":
        font_import = f"""
        <style>
            @import url('https://fonts.googleapis.com/css2?family={primary_font_url}:wght@300;400;500;600&family={heading_font_url}:ital,wght@0,400;0,500;0,600;1,400&display=swap');
        </style>
        """
    elif primary_font != "Avenir Next":
        font_import = f"""
        <style>
            @import url('https://fonts.googleapis.com/css2?family={primary_font_url}:wght@300;400;500;600&display=swap');
        </style>
        """
    elif heading_font != "Avenir Next":
        font_import = f"""
        <style>
            @import url('https://fonts.googleapis.com/css2?family={heading_font_url}:ital,wght@0,400;0,500;0,600;1,400&display=swap');
        </style>
        """
    
    css_vars = f"""
    <style>
        :root {{
            --font-primary: '{primary_font}', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            --font-heading: '{heading_font}', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            --primary: {color_primary};
            --bg: {color_bg};
            --text: {color_text};
            --hero-bg: {color_hero_bg};
            --action-bg: {color_action_bg};
            --card: {color_card_bg};
        }}
    </style>
    """
    
    st.markdown(font_import + css_vars, unsafe_allow_html=True)
