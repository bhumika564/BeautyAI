import streamlit as st
import json
import os

CONFIG_PATH = "config/theme.json"

def get_default_theme():
    """Returns the original developer default theme."""
    return {
        "theme_font_primary": "Avenir Next",
        "theme_font_heading": "Avenir Next",
        "theme_color_primary": "#000000",
        "theme_color_bg": "#FFFFFF",
        "theme_color_text": "#333333",
        "theme_color_hero_bg": "#E0D7D0",
        "theme_color_hero_text": "#2C3E50",
        "theme_color_action_bg": "#FFFFFF",
        "theme_color_action_text": "#000000",
        "theme_color_card_bg": "#E0D7D0",
        "theme_color_card_text": "#333333"
    }

def load_saved_theme():
    """Reads the permanent theme configuration from JSON."""
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r") as f:
            return json.load(f)
    return get_default_theme()

def reset_developer_theme():
    """Resets the global developer theme configuration to defaults."""
    save_theme(get_default_theme())

def save_theme(theme_dict):
    """Writes the current preview configuration to JSON."""
    os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
    with open(CONFIG_PATH, "w") as f:
        json.dump(theme_dict, f, indent=4)

def init_theme_state(ls_val=None):
    """Initializes the session state variables from the saved JSON config or localStorage."""
    base_theme = load_saved_theme()
    
    # If client-side local storage data arrived and hasn't been applied yet
    if ls_val and isinstance(ls_val, dict) and not st.session_state.get("ls_theme_applied"):
        for key, val in ls_val.items():
            st.session_state[key] = val
        st.session_state["ls_theme_applied"] = True
        
    for key, val in base_theme.items():
        if key not in st.session_state:
            st.session_state[key] = val

def inject_live_theme(ls_val=None):
    """Builds and injects the dynamic CSS variables based on session state."""
    init_theme_state(ls_val)
    
    primary_font = st.session_state.theme_font_primary
    heading_font = st.session_state.theme_font_heading
    color_primary = st.session_state.theme_color_primary
    color_bg = st.session_state.theme_color_bg
    color_text = st.session_state.theme_color_text
    color_hero_bg = st.session_state.theme_color_hero_bg
    color_hero_text = st.session_state.theme_color_hero_text
    color_action_bg = st.session_state.theme_color_action_bg
    color_action_text = st.session_state.theme_color_action_text
    color_card_bg = st.session_state.theme_color_card_bg
    color_card_text = st.session_state.theme_color_card_text
    
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
            --hero-text: {color_hero_text};
            --action-bg: {color_action_bg};
            --action-text: {color_action_text};
            --card: {color_card_bg};
            --card-text: {color_card_text};
        }}
    </style>
    """
    
    st.markdown(font_import + css_vars, unsafe_allow_html=True)
