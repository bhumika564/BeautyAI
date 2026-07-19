import streamlit as st
from theme_engine import save_theme

# A curated list of elegant Google Fonts for the beauty industry
GOOGLE_FONTS = [
    "Avenir Next", "Inter", "Lora", "Playfair Display", "Montserrat", "Roboto",
    "Open Sans", "Lato", "Poppins", "Oswald", "Raleway",
    "Nunito", "Cinzel", "Cormorant Garamond", "Outfit", "Manrope"
]

def render_appearance_studio():
    """Renders the Appearance Studio inside a Streamlit expander on the main page."""
    with st.expander("✨ Appearance Studio (Live Theme Editor)", expanded=False):
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
            st.color_picker("Primary Accent Color", key="theme_color_primary")
            st.color_picker("App Background Color", key="theme_color_bg")
            st.color_picker("Main Text Color", key="theme_color_text")
            
            st.markdown("**Components Background & Font Color**")
            st.color_picker("Hero Section Background", key="theme_color_hero_bg")
            st.color_picker("Hero Section Font Color", key="theme_color_hero_text")
            st.color_picker("Action Buttons Background", key="theme_color_action_bg")
            st.color_picker("Action Buttons Font Color", key="theme_color_action_text")
            st.color_picker("Info & Feature Cards Background", key="theme_color_card_bg")
            st.color_picker("Info & Feature Cards Font Color", key="theme_color_card_text")
            
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
        
        if st.button("Apply & Save Changes", type="primary", use_container_width=True):
            theme_dict = {
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
            save_theme(theme_dict)
            st.success("✨ Theme successfully saved!")
