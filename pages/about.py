import streamlit as st
from utils import render_layout

def about_content():
    # SECTION 1 - HERO
    st.markdown("""
    <div class="page-header" style="margin-bottom: 24px;">
        <div class="page-badge">
        <span class="icon">💖</span> About BeautyAI
        </div>
        <h1>AI-Powered Beauty Recommendation Platform</h1>
    </div>
    """, unsafe_allow_html=True)
    
    # SECTION 2 - MISSION
    st.markdown("""
    <div class="chart-card" style="text-align: center; max-width: 800px; margin: 0 auto 40px auto;">
        <p style="color: var(--text-light); font-size: 18px; line-height: 1.8;">
        BeautyAI was developed to help users discover beauty products through intelligent recommendations and review analysis. By combining Natural Language Processing, Machine Learning, and interactive analytics, the platform transforms thousands of customer reviews into actionable insights.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # BONUS SECTION - ACHIEVEMENTS
    st.markdown("<h2 style='text-align: center; margin-bottom: 24px;'><span class='icon'>🏆</span> Project Achievements</h2>", unsafe_allow_html=True)
    cols = st.columns([1, 0.08, 1, 0.08, 1])
    achievements = [
        {"icon": "<span class='icon'>📈</span>", "title": "100K+ Reviews Processed", "desc": "Cleaned and vectorized"},
        {"icon": "<span class='icon'>🎯</span>", "title": "88.66% Sentiment Accuracy", "desc": "Logistic Regression Model"},
        {"icon": "<span class='icon'>🛍️</span>", "title": "56K+ Products", "desc": "Analyzed and recommended"}
    ]
    for i, item in enumerate(achievements):
        with cols[i*2]:
            st.markdown(f"""
            <div class="chart-card" style="text-align: center; height: 100%;">
                <div style="font-size: 40px; margin-bottom: 16px;">{item['icon']}</div>
                <h4 style="color: var(--text); margin-bottom: 8px;">{item['title']}</h4>
                <p style="color: var(--text-light); font-size: 14px;">{item['desc']}</p>
            </div>
            """, unsafe_allow_html=True)
            
    st.markdown("<br><hr style='border:1px solid var(--border); margin: 32px 0;'><br>", unsafe_allow_html=True)
    
    # SECTION 3 - KEY FEATURES
    st.markdown("<h2 style='text-align: center; margin-bottom: 24px;'><span class='icon'>✨</span> Key Features</h2>", unsafe_allow_html=True)
    f_cols = st.columns([1, 0.08, 1, 0.08, 1])
    features = [
        {"icon": "<span class='icon'>🤖</span>", "title": "AI Recommendation", "desc": "Find products similar to your favorite beauty items using TF-IDF and cosine similarity."},
        {"icon": "<span class='icon'>😊</span>", "title": "Sentiment Analysis", "desc": "Analyze customer reviews to understand how users feel about a product."},
        {"icon": "<span class='icon'>📊</span>", "title": "Analytics Dashboard", "desc": "Explore trends, ratings, customer behaviour and business insights."}
    ]
    for i, item in enumerate(features):
        with f_cols[i*2]:
            st.markdown(f"""
            <div class="chart-card" style="height: 100%; border-top: 4px solid var(--primary);">
                <div style="font-size: 32px; margin-bottom: 16px;">{item['icon']}</div>
                <h3 style="color: var(--text); margin-bottom: 12px; font-size: 20px;">{item['title']}</h3>
                <p style="color: var(--text-light); line-height: 1.6;">{item['desc']}</p>
            </div>
            """, unsafe_allow_html=True)
            
    st.markdown("<br>", unsafe_allow_html=True)
    
    # SECTION 4 - TECH STACK
    st.markdown("""
    <div class="chart-card" style="text-align: center;">
        <h2 style="margin-bottom: 24px;"><span class="icon">⚙️</span> Technology Stack</h2>
        <div style="display: flex; gap: 12px; flex-wrap: wrap; justify-content: center;">
            <span class="category-badge">Python</span>
            <span class="category-badge">Streamlit</span>
            <span class="category-badge">Scikit-Learn</span>
            <span class="category-badge">Pandas</span>
            <span class="category-badge">NumPy</span>
            <span class="category-badge">Plotly</span>
            <span class="category-badge">TF-IDF</span>
            <span class="category-badge">NLP</span>
            <span class="category-badge">Machine Learning</span>
            <span class="category-badge">Git & GitHub</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # SECTION 5 - ML PIPELINE
    st.markdown("""
    <div class="chart-card">
        <h2 style="text-align: center; margin-bottom: 32px;"><span class="icon">🧠</span> Machine Learning Pipeline</h2>
        <div style="display: flex; flex-wrap: wrap; gap: 16px; justify-content: center; align-items: center;">
            <div style="background: var(--primary-light); padding: 12px 24px; border-radius: 999px; color: var(--primary); font-weight: 600;">Dataset</div>
            <div style="color: var(--text-light);">➜</div>
            <div style="background: var(--primary-light); padding: 12px 24px; border-radius: 999px; color: var(--primary); font-weight: 600;">Cleaning</div>
            <div style="color: var(--text-light);">➜</div>
            <div style="background: var(--primary-light); padding: 12px 24px; border-radius: 999px; color: var(--primary); font-weight: 600;">Preprocessing</div>
            <div style="color: var(--text-light);">➜</div>
            <div style="background: var(--primary-light); padding: 12px 24px; border-radius: 999px; color: var(--primary); font-weight: 600;">TF-IDF</div>
            <div style="color: var(--text-light);">➜</div>
            <div style="background: var(--primary-light); padding: 12px 24px; border-radius: 999px; color: var(--primary); font-weight: 600;">Cosine Similarity</div>
            <div style="color: var(--text-light);">➜</div>
            <div style="background: var(--primary-light); padding: 12px 24px; border-radius: 999px; color: var(--primary); font-weight: 600;">Recommendation Engine</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # SECTION 7 - DEVELOPER
    st.markdown("""
    <div class="chart-card" style="text-align: center; padding: 48px 24px;">
        <div style="font-size: 48px; margin-bottom: 16px;"><span class="icon">👩‍💻</span></div>
        <h2 style="margin-bottom: 8px; color: var(--text);">Bhumika Sharma</h2>
        <h4 style="margin-bottom: 24px; color: var(--primary);">AI & Data Science Student</h4>
        
        <div style="display: flex; gap: 12px; justify-content: center; margin-bottom: 32px;">
            <span style="background: #f1f5f9; padding: 6px 16px; border-radius: 999px; font-size: 14px; color: #475569; font-weight: 500;">Full Stack Development</span>
            <span style="background: #f1f5f9; padding: 6px 16px; border-radius: 999px; font-size: 14px; color: #475569; font-weight: 500;">Data Analytics</span>
            <span style="background: #f1f5f9; padding: 6px 16px; border-radius: 999px; font-size: 14px; color: #475569; font-weight: 500;">Artificial Intelligence</span>
        </div>
        
        <div style="display: flex; justify-content: center; gap: 16px;">
            <a href="https://github.com" target="_blank" style="background: var(--text); color: var(--card); padding: 12px 32px; border-radius: 999px; font-weight: 600; text-decoration: none; transition: opacity 0.2s;">GitHub</a>
            <a href="https://linkedin.com" target="_blank" style="background: #0077b5; color: var(--card); padding: 12px 32px; border-radius: 999px; font-weight: 600; text-decoration: none; transition: opacity 0.2s;">LinkedIn</a>
            <a href="#" style="background: var(--primary); color: var(--card); padding: 12px 32px; border-radius: 999px; font-weight: 600; text-decoration: none; transition: opacity 0.2s;">Resume</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

def main():
    render_layout(about_content, "About")

if __name__ == "__main__":
    main()
