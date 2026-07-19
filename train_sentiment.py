import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import os

print("Loading data...")
df = pd.read_parquet('data/processed/amazon_sentiment.parquet')

# Ensure no nulls
df = df.dropna(subset=['clean_review', 'sentiment'])

print("Vectorizing...")
v = TfidfVectorizer(max_features=5000)
X = v.fit_transform(df['clean_review'])
y = df['sentiment']

print("Training model...")
m = LogisticRegression(max_iter=500, n_jobs=-1)
m.fit(X, y)

print("Saving models...")
os.makedirs('models', exist_ok=True)
joblib.dump(v, 'models/sentiment_vectorizer.pkl')
joblib.dump(m, 'models/sentiment_model.pkl')
print("Done!")
