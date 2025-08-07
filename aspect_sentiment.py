import pandas as pd
import spacy
from collections import defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Load your data
df = pd.read_csv("nike_emotion_sentiment.csv")
nlp = spacy.load("en_core_web_sm")

# Extract noun chunks (aspects) from comments
def extract_aspects(text):
    doc = nlp(text)
    return [chunk.text.lower() for chunk in doc.noun_chunks if len(chunk.text) > 2]

df["aspects"] = df["comment"].apply(extract_aspects)

# Flatten all aspects into a single list
all_aspects = [aspect for sublist in df["aspects"].tolist() for aspect in sublist]

# Vectorize and Cluster aspects to find major themes
vectorizer = TfidfVectorizer(max_df=0.85, min_df=2)
X = vectorizer.fit_transform(all_aspects)

k = 6  # Number of clusters (you can tweak this)
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(X)

# Map each aspect to a cluster
cluster_map = defaultdict(list)
for idx, label in enumerate(kmeans.labels_):
    word = all_aspects[idx]
    cluster_map[label].append(word)

# Print clustered topics
print("📦 Clustered Aspect Topics:")
for label, words in cluster_map.items():
    print(f"\nCluster {label + 1}:")
    top_keywords = pd.Series(words).value_counts().head(10)
    for kw, count in top_keywords.items():
        print(f" - {kw} ({count})")

# (Optional) Combine most common aspect per comment with its sentiment
def get_main_aspect(aspect_list):
    return aspect_list[0] if aspect_list else "unknown"

df["main_aspect"] = df["aspects"].apply(get_main_aspect)
summary = df.groupby(["main_aspect", "sentiment"]).size().unstack(fill_value=0)
summary.to_csv("aspect_sentiment_summary.csv")

print("\n✅ Aspect-based sentiment summary saved to 'aspect_sentiment_summary.csv'")
