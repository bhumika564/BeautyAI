import streamlit as st

features_data = [
    {
        "icon": "",
        "title": "Smart Recommendations",
        "desc": "Find similar beauty products using machine learning.",
        "bg": "pink"
    },
    {
        "icon": "",
        "title": "Review Sentiment Analysis",
        "desc": "Analyze customer reviews using advanced NLP.",
        "bg": "yellow"
    },
    {
        "icon": "",
        "title": "Analytics Dashboard",
        "desc": "Explore insights, trends & patterns from 100K+ reviews.",
        "bg": "purple"
    }
]

def feature_card(item):
    st.markdown(
        f"""
        <div class="feature-card">
            <div class="feature-left">
                <div class="feature-icon {item['bg']}">
                    {item['icon']}
                </div>
                <div>
                    <div class="feature-title">
                        {item['title']}
                    </div>
                    <div class="feature-desc">
                        {item['desc']}
                    </div>
                </div>
            </div>
            <div class="feature-arrow">
                ➜
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def features():
    st.markdown(
        """
        <div class="section-heading">
            <div class="section-badge">
                </div>
            <h2>What You Can Do</h2>
            <p>
            Explore powerful features to make smarter beauty choices.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    cols = st.columns(3)
    
    routes = [
        {"label": "Try Smart Recommendations", "page": "pages/recommendation.py", "key": "feat_rec"},
        {"label": "Analyze a Review", "page": "pages/sentiment.py", "key": "feat_sent"},
        {"label": "View Dashboard", "page": "pages/analytics.py", "key": "feat_ana"}
    ]

    for col, item, route in zip(cols, features_data, routes):
        with col:
            feature_card(item)
            if st.button(route["label"], key=route["key"], use_container_width=True):
                st.switch_page(route["page"])
