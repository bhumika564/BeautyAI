import streamlit as st

stats_data = [
    {
        "icon": "",
        "value": "56K+",
        "title": "Products",
        "desc": "Curated beauty products",
        "class": "products-card"
    },
    {
        "icon": "",
        "value": "100K+",
        "title": "Reviews",
        "desc": "Real customer reviews",
        "class": "reviews-card"
    },
    {
        "icon": "",
        "value": "88.66%",
        "title": "Accuracy",
        "desc": "Model accuracy rate",
        "class": "accuracy-card"
    },
    {
        "icon": "",
        "value": "NLP",
        "title": "Powered",
        "desc": "Advanced AI technology",
        "class": "nlp-card"
    }
]


def stats():
    st.markdown("<br><br>", unsafe_allow_html=True)
    cols = st.columns([1, 0.08, 1, 0.08, 1, 0.08, 1])
    
    # We only want the content columns (index 0, 2, 4, 6)
    content_cols = [cols[0], cols[2], cols[4], cols[6]]

    for col, item in zip(content_cols, stats_data):
        with col:
            st.markdown(f"""
                <div class="stats-card {item['class']}">
                    <div class="stats-content">
                        <h2>{item['value']}</h2>
                        <h4>{item['title']}</h4>
                        <p>{item['desc']}</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
