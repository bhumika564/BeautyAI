import pandas as pd

df = pd.read_parquet('d:/Amazon_Beauty_Recommendation_System/data/processed/amazon_nlp.parquet')
unique_products = df['product_id'].nunique()
print(f"Total Unique Products: {unique_products}")

# Top 1000 products
top_products = df.groupby(['product_id', 'product_title']).size().reset_index(name='review_count')
top_products = top_products.sort_values(by='review_count', ascending=False).head(1000)
print(f"Top 1000 products min review count: {top_products['review_count'].min()}")
print(f"Top 1000 products max review count: {top_products['review_count'].max()}")
