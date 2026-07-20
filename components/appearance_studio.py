import streamlit as st
from theme_engine import save_theme, reset_developer_theme, get_default_theme
import json

# A curated list of elegant Google Fonts for the beauty industry
GOOGLE_FONTS = [
    "Avenir Next", "Inter", "Lora", "Playfair Display", "Montserrat", "Roboto",
    "Open Sans", "Lato", "Poppins", "Oswald", "Raleway",
    "Nunito", "Cinzel", "Cormorant Garamond", "Outfit", "Manrope"
]

def color_picker_with_undo(label, key):
    """Wraps st.color_picker to include an Undo (↺) button with a history stack."""
    history_key = f"{key}_history"
    
    # Initialize history stack with the current value
    if history_key not in st.session_state:
        st.session_state[history_key] = [st.session_state[key]]
        
    def on_color_change():
        new_val = st.session_state[key]
        if st.session_state[history_key][-1] != new_val:
            st.session_state[history_key].append(new_val)
            
    def perform_undo():
        if len(st.session_state[history_key]) > 1:
            st.session_state[history_key].pop()  # Remove current
            st.session_state[key] = st.session_state[history_key][-1]  # Set to previous
            
    col_picker, col_undo = st.columns([0.85, 0.15])
    
    with col_picker:
        st.color_picker(label, key=key, on_change=on_color_change)
        
    with col_undo:
        st.markdown("<div style='margin-top: 28px;'></div>", unsafe_allow_html=True)
        can_undo = len(st.session_state[history_key]) > 1
        st.button("↺", key=f"undo_{key}", help="Revert to previous color", disabled=not can_undo, use_container_width=True, on_click=perform_undo)

def get_current_theme_dict():
    return {
        "theme_font_primary": st.session_state.theme_font_primary,
        "theme_font_heading": st.session_state.theme_font_heading,
        "theme_color_primary": st.session_state.theme_color_primary,
        "theme_color_bg": st.session_state.theme_color_bg,
        "theme_color_text": st.session_state.theme_color_text,
        "theme_color_hero_bg": st.session_state.theme_color_hero_bg,
        "theme_color_hero_text": st.session_state.theme_color_hero_text,
        "theme_color_action_bg": st.session_state.theme_color_action_bg,
        "theme_color_action_text": st.session_state.theme_color_action_text,
        "theme_color_card_bg": st.session_state.theme_color_card_bg,
        "theme_color_card_text": st.session_state.theme_color_card_text
    }

def render_appearance_studio():
    """Renders the Appearance Studio inside a Streamlit expander on the main page."""
    

    
    if st.query_params.get("studio") != "open":
        return

    with st.container():
        col_title, col_close = st.columns([0.85, 0.15])
        with col_title:
            st.markdown("### ✨ Appearance Studio (Live Theme Editor)")
        with col_close:
            if st.button("❌ Close", key="close_studio"):
                del st.query_params["studio"]
                st.rerun()
        st.markdown(
            """
            <p style="font-size: 13px; color: var(--text-light); margin-bottom: 24px;">
                Experiment with live typography and color changes. Select options below to see them instantly applied across the entire UI.
            </p>
            """,
            unsafe_allow_html=True
        )
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Typography**")
            st.selectbox("Primary Font (Body)", options=GOOGLE_FONTS, key="theme_font_primary")
            st.selectbox("Heading Font (Titles)", options=GOOGLE_FONTS, key="theme_font_heading")
            
        with col2:
            st.markdown("**Color Palette**")
            color_picker_with_undo("Primary Accent Color", key="theme_color_primary")
            color_picker_with_undo("App Background Color", key="theme_color_bg")
            color_picker_with_undo("Main Text Color", key="theme_color_text")
            
            st.markdown("**Components Background & Font Color**")
            color_picker_with_undo("Hero Section Background", key="theme_color_hero_bg")
            color_picker_with_undo("Hero Section Font Color", key="theme_color_hero_text")
            color_picker_with_undo("Action Buttons Background", key="theme_color_action_bg")
            color_picker_with_undo("Action Buttons Font Color", key="theme_color_action_text")
            color_picker_with_undo("Info & Feature Cards Background", key="theme_color_card_bg")
            color_picker_with_undo("Info & Feature Cards Font Color", key="theme_color_card_text")
            
        st.markdown(
            """
            <div style="margin-top: 32px; padding: 16px; background: var(--card); border: 1px solid var(--border);">
                <p style="font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: var(--text-light); margin-bottom: 12px;">Live Preview</p>
                <h4 style="margin-top: 0; margin-bottom: 8px; font-family: var(--font-heading); color: var(--text);">The quick brown fox</h4>
                <p style="font-size: 13px; margin: 0; font-family: var(--font-primary); color: var(--text);">jumps over the lazy dog.</p>
                <button style="margin-top: 12px; background: var(--primary); color: #fff; border: none; padding: 8px 16px; cursor: pointer; font-family: var(--font-primary); font-weight: 600;">Sample Button</button>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.markdown("---")
        
        btn_col1, btn_col2, btn_col3 = st.columns(3)
        
        def handle_restore():
            defaults = get_default_theme()
            for key, val in defaults.items():
                st.session_state[key] = val
                if f"{key}_history" in st.session_state:
                    st.session_state[f"{key}_history"] = [val]
            if "theme" in st.query_params:
                del st.query_params["theme"]
            st.session_state["trigger_ls_clear"] = True
            
        def handle_dev_reset():
            reset_developer_theme()
            st.session_state["trigger_dev_reset_msg"] = True
            
        with btn_col1:
            st.button("Restore Original Theme", use_container_width=True, on_click=handle_restore)
                
        with btn_col2:
            if st.button("Save Theme Changes", type="primary", use_container_width=True):
                theme_dict = get_current_theme_dict()
                st.query_params["theme"] = json.dumps(theme_dict)
                st.success("✨ Theme successfully saved to URL!")
                
        with btn_col3:
            st.button("Developer Reset (Global)", help="Resets the global server-side theme", use_container_width=True, on_click=handle_dev_reset)
            
        # Handle deferred triggers from callbacks safely
        if st.session_state.get("trigger_ls_clear"):
            st.session_state["trigger_ls_clear"] = False
            st.success("✨ Original theme restored!")
            
        if st.session_state.get("trigger_dev_reset_msg"):
            st.success("✅ Global developer theme reset!")
            st.session_state["trigger_dev_reset_msg"] = False
