import pandas as pd

def get_trending_products():
    """
    Fetches the top 4 trending products from the recommendation dataset.
    Falls back to mock data if the dataset is unavailable.
    """
    try:
        df = pd.read_parquet("data/processed/recommend_products.parquet")
        real_titles = df['product_title'].head(4).tolist()
    except Exception:
        real_titles = ["Product 1", "Product 2", "Product 3", "Product 4"]

    def truncate(title, length=45):
        return title[:length] + "..." if len(title) > length else title

    return [
        {
            "name": truncate(real_titles[0]),
            "rating": "4.8",
            "reviews": "12.4K",
            "category": "Skin Care",
            "image": "assets/products/facewash.png"
        },
        {
            "name": truncate(real_titles[1]),
            "rating": "4.6",
            "reviews": "8.1K",
            "category": "Face Wash",
            "image": "assets/products/serum.png"
        },
        {
            "name": truncate(real_titles[2]),
            "rating": "4.9",
            "reviews": "24K",
            "category": "Makeup",
            "image": "assets/products/cream.png"
        },
        {
            "name": truncate(real_titles[3]),
            "rating": "4.7",
            "reviews": "15.2K",
            "category": "Hair Care",
            "image": "assets/products/sunscreen.png"
        }
    ]
