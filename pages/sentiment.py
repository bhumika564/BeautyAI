import streamlit as st
from utils import render_layout, predict_sentiment
import string

def get_sentiment_ui(sentiment):
    if sentiment.lower() == "positive":
        return {
            "emoji": "😊",
            "title": "Positive",
            "color": "#34C759",
            "insight": "Customers expressed strong satisfaction and appreciated the product quality."
        }
    elif sentiment.lower() == "negative":
        return {
            "emoji": "😔",
            "title": "Negative",
            "color": "#FF4D4F",
            "insight": "Customers reported dissatisfaction and highlighted issues with quality or performance."
        }
    else:
        return {
            "emoji": "😐",
            "title": "Neutral",
            "color": "#F4C542",
            "insight": "The review contains mixed opinions without a strong emotional sentiment."
        }

def sentiment_content():
    st.markdown("""
    <div class="page-header">
        <div class="page-badge">
            <span class="icon">😊</span> AI Powered
        </div>
        <h1>
            AI Review Analyzer
        </h1>
        <p style="color: var(--text-light); font-size: 18px; max-width: 600px; margin: 0 auto;">
            Understand customer emotions using Artificial Intelligence
            and Natural Language Processing.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    review = st.text_area(
        "Paste Customer Review",
        placeholder="Example: This serum worked wonders for my skin...",
        height=180
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # We use columns to center the button slightly or keep it full width
    cols = st.columns([1, 2, 1])
    with cols[1]:
        analyze = st.button("✨ Analyze Review", use_container_width=True)
        
    if analyze and review:
        with st.spinner("Analyzing sentiment..."):
            try:
                prediction, confidence = predict_sentiment(review)
                
                # Setup UI configuration
                ui_config = get_sentiment_ui(prediction)
                confidence_percent = confidence * 100
                
                # Mock Keyword Extraction (Removing basic punctuation for cleaner look)
                clean_review = review.translate(str.maketrans('', '', string.punctuation))
                keywords = [word.capitalize() for word in clean_review.split()[:5]]
                keyword_str = " • ".join(keywords) if keywords else "None"
                
                st.markdown(f"""
                <div class="sentiment-card" style="border-left: 8px solid {ui_config['color']};">
                    <h2 style="font-size: 32px; margin-bottom: 8px; color: var(--text);">
                        {ui_config['emoji']} {ui_config['title']}
                    </h2>
                    <div class="confidence">
                        Confidence
                        <div style="font-size: 32px; color: var(--primary); margin-top: 8px;">{confidence_percent:.1f}%</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Progress bar
                st.progress(float(confidence))
                
                # Insights
                st.markdown(f"""
                <div style="margin-top: 32px; background: var(--card); padding: 24px; border-radius: var(--radius); border: 1px solid var(--border);">
                    <h4 style="color: var(--text); margin-bottom: 12px;"><span class="icon">🔑</span> Extracted Keywords</h4>
                    <p style="color: var(--primary); font-weight: 600; font-size: 18px;">{keyword_str}</p>
                    <hr style="border:1px solid var(--border); margin: 24px 0;">
                    <h4 style="color: var(--text); margin-bottom: 12px;"><span class="icon">🧠</span> AI Insight</h4>
                    <p style="color: var(--text-light); font-size: 16px; line-height: 1.6;">{ui_config['insight']}</p>
                </div>
                """, unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"Error predicting sentiment: {e}")

def main():
    render_layout(sentiment_content, "Reviews")

if __name__ == "__main__":
    main()
