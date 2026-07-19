import streamlit as st
import time
import base64
import os

def get_bot_response(user_input):
    text = user_input.lower()
    
    # Simple Rule-Based NLP Engine
    if "dry" in text or "moisturiz" in text or "hydrate" in text:
        return "Based on our product database, here are the best matches for dry skin:\n• CeraVe Moisturizing Cream\n• COSRX Snail Mucin Essence\n• Cetaphil Moisturizing Lotion"
    
    elif "acne" in text or "pimple" in text or "breakout" in text or "salicylic" in text:
        return "For acne-prone skin, our AI engine highly recommends:\n• Minimalist 2% Salicylic Acid Face Wash\n• Paula's Choice 2% BHA Liquid Exfoliant\n• The Ordinary Niacinamide 10% + Zinc 1%"
        
    elif "sun" in text or "spf" in text or "uv" in text:
        return "Here are the top-rated sunscreens in our dataset:\n• Beauty of Joseon Relief Sun : Rice + Probiotics\n• Isntree Hyaluronic Acid Watery Sun Gel\n• EltaMD UV Clear Broad-Spectrum SPF 46"
        
    else:
        return "I'm your BeautyAI Assistant! 💄 I can recommend products for **dry skin**, **acne**, or **sun protection**. \n\nFor more advanced searches, head over to the **Recommendations** page!"

@st.cache_data
def get_chatbot_icon_b64():
    img_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "chatbot_icon.png")
    if os.path.exists(img_path):
        with open(img_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

def render_chatbot():
    # Load the uploaded real image
    img_b64 = get_chatbot_icon_b64()
            
    bg_css = f'background: url("data:image/png;base64,{img_b64}") center center / cover no-repeat !important;' if img_b64 else 'background: linear-gradient(135deg, var(--primary), #FF7FA6) !important;'

    # Inject Custom CSS to make the Popover float in the bottom right corner
    css = f"""
    <style>
    /* Float the popover button container */
    div[data-testid="stPopover"] {{
        position: fixed !important;
        bottom: 30px !important;
        right: 30px !important;
        z-index: 99999 !important;
        width: 64px !important;
        height: 64px !important;
    }}
    
    /* Style the popover trigger button to be a premium circular avatar */
    div[data-testid="stPopover"] button {{
        width: 64px !important;
        height: 64px !important;
        min-width: 64px !important;
        max-width: 64px !important;
        border-radius: 50% !important;
        padding: 0 !important;
        margin: 0 !important;
        
        /* Premium Image Background */
        {bg_css}
        
        border: none !important;
        box-shadow: 0 10px 25px rgba(0,0,0, 0.2) !important;
        transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.3s ease !important;
        
        /* Make any residual text completely invisible */
        color: transparent !important;
        font-size: 0px !important;
    }}
    
    /* Force hide ALL inner content (label, chevron SVG, etc.) */
    div[data-testid="stPopover"] button * {{
        display: none !important;
        opacity: 0 !important;
        visibility: hidden !important;
    }}
    
    div[data-testid="stPopover"] button:hover {{
        transform: scale(1.08) translateY(-4px) !important;
        box-shadow: 0 15px 35px rgba(0,0,0, 0.3) !important;
    }}
    
    /* Expand the chat window inside the popover */
    div[data-testid="stPopoverBody"] {{
        width: 380px !important;
        height: 550px !important;
        border-radius: 24px;
        border: 1px solid var(--border);
        box-shadow: 0 20px 50px rgba(0,0,0,0.1);
        padding: 20px 20px 0 20px;
        background: var(--card);
        display: flex;
        flex-direction: column;
    }}
    
    /* Streamlit chat inputs naturally stick to the bottom, but we can ensure the container scrolls */
    div[data-testid="stPopoverBody"] > div:first-child {{
        overflow-y: auto;
        flex-grow: 1;
        padding-bottom: 20px;
    }}
    
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi! I'm your AI Beauty Assistant. How can I help you today?"}
        ]

    # Render Popover
    with st.popover("💬 BeautyAI Assistant", use_container_width=False):
        
        st.markdown("<h3 style='margin-top:0; margin-bottom: 16px; font-size: 18px; border-bottom: 1px solid var(--border); padding-bottom: 12px;'>💬 BeautyAI Assistant</h3>", unsafe_allow_html=True)
        
        # Create a container for messages to scroll properly
        chat_container = st.container(height=360, border=False)
        
        # Display chat messages
        with chat_container:
            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

        # Accept user input
        if prompt := st.chat_input("Ask me anything..."):
            # Add user message
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            # Show user message instantly
            with chat_container:
                with st.chat_message("user"):
                    st.markdown(prompt)
                
                # Show assistant response with spinner
                with st.chat_message("assistant"):
                    with st.spinner("Thinking..."):
                        response = get_bot_response(prompt)
                        st.markdown(response)
                        
            # Save assistant response
            st.session_state.messages.append({"role": "assistant", "content": response})
            
            st.rerun()
