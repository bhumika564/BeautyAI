import streamlit as st

# A curated list of elegant Google Fonts for the beauty industry
GOOGLE_FONTS = [
    "Inter",
    "Lora",
    "Playfair Display",
    "Montserrat",
    "Roboto",
    "Open Sans",
    "Lato",
    "Poppins",
    "Oswald",
    "Raleway",
    "Nunito",
    "Cinzel",
    "Cormorant Garamond",
    "Outfit",
    "Manrope"
]

def render_appearance_studio():
    """Renders the Appearance Studio inside a Streamlit expander on the main page."""
    with st.expander("✨ Appearance Studio (Live Typography Preview)", expanded=False):
        st.markdown(
            """
            <p style="font-size: 13px; color: var(--text-light); margin-bottom: 24px;">
                Experiment with live typography changes. Select a font below to see it instantly applied across the entire UI.
            </p>
            """,
            unsafe_allow_html=True
        )
        
        # Primary Font Selection (Body, Buttons, Nav)
        st.selectbox(
            "Primary Font (Body, Buttons)",
            options=GOOGLE_FONTS,
            key="theme_font_primary",
            help="This font applies to paragraphs, navigation links, buttons, and general UI text."
        )
        
        # Heading Font Selection (H1-H6, Hero)
        st.selectbox(
            "Heading Font (Titles, Hero)",
            options=GOOGLE_FONTS,
            key="theme_font_heading",
            help="This font applies to all major headings and large text displays."
        )
        
        st.markdown(
            """
            <div style="margin-top: 32px; padding: 16px; background: var(--card); border: 1px solid var(--border);">
                <p style="font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: var(--text-light); margin-bottom: 12px;">Live Preview</p>
                <h4 style="margin-top: 0; margin-bottom: 8px;">The quick brown fox</h4>
                <p style="font-size: 13px; margin: 0;">jumps over the lazy dog.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
