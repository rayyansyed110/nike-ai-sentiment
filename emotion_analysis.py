import pandas as pd
from transformers import pipeline
from tqdm import tqdm

# Load your dataset
df = pd.read_csv("nike_sentiment.csv")

# Load emotion classifier pipeline
classifier = pipeline("text-classification", 
                      model="j-hartmann/emotion-english-distilroberta-base", 
                      top_k=1)

# Analyze emotions for each comment
tqdm.pandas()  # show progress bar

def detect_emotion(text):
    try:
        result = classifier(text)[0][0]["label"]
    except:
        result = "error"
    return result

df["emotion"] = df["comment"].progress_apply(detect_emotion)

# Save to new file
df.to_csv("nike_emotion_sentiment.csv", index=False)
print("✅ Emotion analysis complete. Results saved to nike_emotion_sentiment.csv")

import matplotlib.pyplot as plt

emotion_counts = df["emotion"].value_counts()

plt.figure(figsize=(8, 6))
emotion_counts.plot(kind="bar", color="skyblue")
plt.title("Emotion Distribution in Nike Comments")
plt.xlabel("Emotion")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("emotion_distribution.png")
plt.show()
