import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the emotion data
df = pd.read_csv("nike_emotion_sentiment.csv")

# Count emotions
emotion_counts = df["emotion"].value_counts()

# Create a more professional-looking chart
plt.figure(figsize=(12, 8))

# Set style for professional look
plt.style.use('default')
sns.set_palette("husl")

# Create bar chart
bars = plt.bar(emotion_counts.index, emotion_counts.values, 
               color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD'])

# Customize the chart
plt.title('Nike Customer Emotion Analysis\n174 YouTube Comments Analyzed', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Emotion Type', fontsize=12, fontweight='bold')
plt.ylabel('Number of Comments', fontsize=12, fontweight='bold')

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}',
             ha='center', va='bottom', fontweight='bold')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Add grid for better readability
plt.grid(axis='y', alpha=0.3, linestyle='--')

# Calculate percentages for insight
total_comments = emotion_counts.sum()
top_emotion = emotion_counts.index[0]
top_percentage = (emotion_counts.iloc[0] / total_comments) * 100

# Add subtitle with key insight
plt.figtext(0.5, 0.02, f'Key Insight: {top_percentage:.1f}% of comments show "{top_emotion}" emotion', 
            ha='center', fontsize=10, style='italic')

# Adjust layout
plt.tight_layout()

# Save the chart
plt.savefig('nike_emotion_chart.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')

print("✅ Emotion chart created successfully!")
print(f"📊 Saved as: nike_emotion_chart.png")
print(f"📈 Top emotion: {top_emotion} ({top_percentage:.1f}%)")
print(f"📊 Emotion distribution:")
for emotion, count in emotion_counts.items():
    percentage = (count / total_comments) * 100
    print(f"   {emotion}: {count} comments ({percentage:.1f}%)")

plt.show()
