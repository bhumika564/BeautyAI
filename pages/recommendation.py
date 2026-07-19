import streamlit as st
from utils import render_layout, load_data, recommend_products
from components.ui import recommendation_card, selected_product_card

def recommendation_content():
    st.markdown("""
    <div class="page-header">
        <div class="page-badge">
            <span class="icon">🤖</span> AI Powered
        </div>
        <h1>
            Smart Product Recommendation
        </h1>
        <p style="color: var(--text-light); font-size: 18px;">
            Discover similar beauty products using Machine Learning.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load dataset to get product list
    try:
        _, indices = load_data()
        product_list = indices.index.tolist()
    except Exception:
        product_list = ["Example Product 1", "Example Product 2"]
        
    selected = st.selectbox(
        "",
        product_list,
        index=None,
        placeholder="⌕ Search Beauty Product..."
    )
    
    if selected:
        st.markdown("<hr style='border:1px solid var(--border); margin: 40px 0;'>", unsafe_allow_html=True)
        st.markdown("<h3 style='margin-bottom: 24px; color: var(--text);'>Selected Product</h3>", unsafe_allow_html=True)
        
        # In a real app we'd fetch actual image/rating from a DB. We use mocks for UI perfection.
        selected_product_card(
            image="assets/featured_product.png",
            title=selected,
            rating="4.6",
            reviews="2,143",
            category="Skin Care"
        )
        
        with st.spinner("Finding similar beauty products..."):
            try:
                recs_df = recommend_products(selected, top_n=4)
                
                if isinstance(recs_df, str):
                    st.error(recs_df)
                else:
                    # Calculate average match for the bonus strip
                    matches = []
                    for row in recs_df.itertuples():
                        score = getattr(row, '_2') if hasattr(row, '_2') else row[2] if len(row) > 2 else 0.90
                        matches.append(score)
                    
                    avg_match = int((sum(matches) / len(matches)) * 100) if matches else 94
                    
                    # AI Recommendation Summary Strip
                    st.markdown(f"""
                    <div class="summary-strip">
                        <div style="color: var(--text); font-weight: 600; font-size: 16px;">
                            <span class="icon">🤖</span> AI found {len(recs_df)} similar products
                        </div>
                        <div style="color: var(--primary); font-weight: 700; font-size: 18px;">
                            Average Match: {avg_match}%
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Recommendation Grid
                    cols = st.columns([1, 0.08, 1, 0.08, 1, 0.08, 1])
                    content_cols = [cols[0], cols[2], cols[4], cols[6]]
                    
                    placeholder_images = [
                        "assets/products/facewash.png",
                        "assets/products/serum.png",
                        "assets/products/cream.png",
                        "assets/products/sunscreen.png"
                    ]
                    
                    for i, row in enumerate(recs_df.itertuples()):
                        with content_cols[i]:
                            score = getattr(row, '_2') if hasattr(row, '_2') else row[2] if len(row) > 2 else 0.90
                            ai_match = int(score * 100)
                            
                            title = row.product_title
                            if len(title) > 35:
                                title = title[:35] + "..."
                            
                            recommendation_card(
                                image=placeholder_images[i % len(placeholder_images)],
                                title=title,
                                ai_score=ai_match,
                                category="Beauty Pick"
                            )
            except Exception as e:
                st.error(f"Error generating recommendations: {e}")

def main():
    render_layout(recommendation_content, "Products")

if __name__ == "__main__":
    main()
