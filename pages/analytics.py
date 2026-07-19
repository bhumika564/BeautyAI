import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from utils import render_layout
from components.ui import recommendation_card

@st.cache_data
def load_analytics_data():
    cols_to_load = [
        'star_rating', 'product_category', 'verified_purchase', 
        'product_id', 'product_title', 'review_date', 
        'review_body', 'review_headline'
    ]
    clean_df = pd.read_parquet("data/processed/amazon_beauty_sampled.parquet", columns=cols_to_load)
    sentiment_df = pd.read_parquet("data/processed/amazon_sentiment.parquet", columns=['sentiment'])
    return clean_df, sentiment_df

def generate_wordcloud(text):
    wc = WordCloud(width=800, height=400, background_color='white', colormap='PiYG').generate(text)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wc, interpolation='bilinear')
    ax.axis("off")
    return fig

def analytics_content():
    st.markdown("""
    <div class="page-header">
        <div class="page-badge">
        Data Analytics
        </div>
        <h1>Beauty Analytics Dashboard</h1>
        <p style="color: var(--text-light); font-size: 18px; max-width: 600px; margin: 0 auto;">
        Explore insights from thousands of Amazon Beauty Reviews.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    clean_df, sentiment_df = load_analytics_data()
    
    # --- BONUS: Interactive Filters ---
    st.markdown("<h3 style='margin-bottom: 16px;'>Global Filters</h3>", unsafe_allow_html=True)
    filter_cols = st.columns(3)
    
    with filter_cols[0]:
        selected_rating = st.selectbox("Rating", ["All", "5 Stars", "4 Stars", "3 Stars", "2 Stars", "1 Star"])
    with filter_cols[1]:
        categories = ["All"] + sorted(clean_df['product_category'].unique().tolist())
        selected_category = st.selectbox("Category", categories)
    with filter_cols[2]:
        verified_only = st.selectbox("Verified Purchase", ["All", "Verified Only"])
        
    # Apply Filters
    filtered_df = clean_df.copy()
    if selected_rating != "All":
        filtered_df = filtered_df[filtered_df['star_rating'] == selected_rating[0]] # '5' from '5 Stars'
    if selected_category != "All":
        filtered_df = filtered_df[filtered_df['product_category'] == selected_category]
    if verified_only == "Verified Only":
        filtered_df = filtered_df[filtered_df['verified_purchase'] == 'Y']
        
    st.markdown("<hr style='border:1px solid var(--border); margin: 32px 0;'>", unsafe_allow_html=True)
    
    # --- KPIs ---
    total_reviews = len(filtered_df)
    unique_products = filtered_df["product_id"].nunique()
    
    # Calculate Avg Rating safely (convert str to int for calculation if necessary)
    if 'star_rating' in filtered_df.columns:
        filtered_df['rating_num'] = pd.to_numeric(filtered_df['star_rating'], errors='coerce')
        avg_rating = filtered_df['rating_num'].mean()
    else:
        avg_rating = 4.2
        
    stats_data = [
        {"icon": "", "value": f"{total_reviews//1000}K+" if total_reviews > 1000 else str(total_reviews), "title": "Reviews", "desc": "Analyzed records", "class": "reviews-card"},
        {"icon": "", "value": f"{unique_products//1000}K+" if unique_products > 1000 else str(unique_products), "title": "Products", "desc": "Unique items", "class": "products-card"},
        {"icon": "", "value": f"{avg_rating:.1f}", "title": "Avg Rating", "desc": "Across platform", "class": "accuracy-card"},
        {"icon": "", "value": "88.6%", "title": "ML Accuracy", "desc": "Sentiment precision", "class": "nlp-card"}
    ]
    
    cols = st.columns([1, 0.08, 1, 0.08, 1, 0.08, 1])
    content_cols = [cols[0], cols[2], cols[4], cols[6]]
    
    for col, item in zip(content_cols, stats_data):
        with col:
            st.markdown(f"""
                <div class="stats-card {item['class']}">
                    <div class="stats-icon">{item['icon']}</div>
                    <div class="stats-content">
                        <h2>{item['value']}</h2>
                        <h4>{item['title']}</h4>
                        <p>{item['desc']}</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- CHARTS ---
    chart_col1, gap, chart_col2 = st.columns([1, 0.08, 1])
    
    with chart_col1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        st.markdown("<h3 style='margin-bottom:16px;'>Rating Distribution</h3>", unsafe_allow_html=True)
        rating_counts = filtered_df['star_rating'].value_counts().reset_index()
        rating_counts.columns = ['Rating', 'Count']
        rating_counts = rating_counts.sort_values('Rating')
        
        fig = px.bar(rating_counts, x="Rating", y="Count", color_discrete_sequence=['#F45B8C'])
        fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', margin=dict(t=0, b=0, l=0, r=0))
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with chart_col2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        st.markdown("<h3 style='margin-bottom:16px;'>Sentiment Distribution</h3>", unsafe_allow_html=True)
        # Using sentiment_df for sentiment distribution
        sentiment_counts = sentiment_df['sentiment'].value_counts().reset_index()
        sentiment_counts.columns = ['Sentiment', 'Count']
        
        fig2 = px.pie(sentiment_counts, values="Count", names="Sentiment", hole=.65, 
                     color_discrete_sequence=['#34C759', '#FF4D4F', '#F4C542'])
        fig2.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', margin=dict(t=0, b=0, l=0, r=0))
        st.plotly_chart(fig2, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    # --- TIMELINE ---
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown("<h3 style='margin-bottom:16px;'>Reviews Over Time</h3>", unsafe_allow_html=True)
    
    if 'review_date' in filtered_df.columns:
        filtered_df['date'] = pd.to_datetime(filtered_df['review_date'], errors='coerce')
        timeline_df = filtered_df.groupby(filtered_df['date'].dt.to_period('M')).size().reset_index(name='Count')
        timeline_df['date'] = timeline_df['date'].dt.to_timestamp()
        
        fig3 = px.line(timeline_df, x="date", y="Count", color_discrete_sequence=['#F45B8C'])
        fig3.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', margin=dict(t=0, b=0, l=0, r=0))
        st.plotly_chart(fig3, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # --- WORD CLOUD ---
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    st.markdown("<h3 style='margin-bottom:16px;'>Most Common Words</h3>", unsafe_allow_html=True)
    if not filtered_df.empty and 'review_body' in filtered_df.columns:
        text = " ".join(filtered_df['review_body'].dropna().head(1000).astype(str).tolist())
        if text:
            wordcloud_fig = generate_wordcloud(text)
            st.pyplot(wordcloud_fig)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # --- TOP PRODUCTS ---
    st.markdown("<br><h2 style='margin-bottom: 24px;'>Top Products</h2>", unsafe_allow_html=True)
    top_products = filtered_df['product_title'].value_counts().head(4).index.tolist()
    
    cols = st.columns([1, 0.08, 1, 0.08, 1, 0.08, 1])
    content_cols = [cols[0], cols[2], cols[4], cols[6]]
    
    placeholder_images = [
        "assets/products/facewash.png",
        "assets/products/serum.png",
        "assets/products/cream.png",
        "assets/products/sunscreen.png"
    ]
    
    for i, product in enumerate(top_products):
        with content_cols[i]:
            title = product[:35] + "..." if len(product) > 35 else product
            recommendation_card(
                image=placeholder_images[i % len(placeholder_images)],
                title=title,
                ai_score=98 - i,
                category="Top Rated"
            )
            
    # --- SEARCH & DOWNLOAD ---
    st.markdown("<hr style='border:1px solid var(--border); margin: 40px 0;'>", unsafe_allow_html=True)
    st.markdown("<h3 style='margin-bottom:16px;'>Recent Customer Reviews</h3>", unsafe_allow_html=True)
    
    search_query = st.text_input("", placeholder="Search Reviews...", label_visibility="collapsed")
    display_df = filtered_df[['product_title', 'star_rating', 'review_headline', 'review_body']].head(50)
    
    if search_query:
        display_df = display_df[display_df['review_body'].str.contains(search_query, case=False, na=False)]
        
    st.dataframe(display_df, use_container_width=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    csv = filtered_df.head(1000).to_csv(index=False).encode('utf-8')
    st.download_button(
        label="⤓ Download CSV Report",
        data=csv,
        file_name="beauty_reviews_analytics.csv",
        mime="text/csv",
    )

def main():
    render_layout(analytics_content, "Analytics")

if __name__ == "__main__":
    main()
