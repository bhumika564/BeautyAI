import pandas as pd
import sys

def check_parquet(filepath):
    try:
        print(f"--- {filepath} ---")
        df = pd.read_parquet(filepath)
        print("Shape:", df.shape)
        print("Columns:", list(df.columns))
        print("Head (2 rows):")
        print(df.head(2).to_dict(orient='records'))
        print()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")

check_parquet('d:/Amazon_Beauty_Recommendation_System/data/processed/recommend_products.parquet')
check_parquet('d:/Amazon_Beauty_Recommendation_System/data/processed/amazon_nlp.parquet')
check_parquet('d:/Amazon_Beauty_Recommendation_System/data/processed/amazon_sentiment.parquet')
