import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load scraped comments
df = pd.read_csv("nike_youtube_comments.csv")

# Initialize VADER
analyzer = SentimentIntensityAnalyzer()

# Function to classify sentiment
def get_sentiment(text):
    score = analyzer.polarity_scores(text)["compound"]
    if score >= 0.05:
        return "positive"
    elif score <= -0.05:
        return "negative"
    else:
        return "neutral"

# Apply sentiment scoring
df["sentiment"] = df["comment"].apply(get_sentiment)

# Save results
df.to_csv("nike_sentiment.csv", index=False)

# Print sentiment counts
print("✅ Sentiment analysis complete!")
print(df["sentiment"].value_counts())
