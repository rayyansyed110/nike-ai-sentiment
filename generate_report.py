import os
import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI
import ssl
import httpx

# Load your API key
load_dotenv()

# Create SSL context that doesn't verify certificates (for corporate networks)
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# Create custom httpx client with SSL settings
http_client = httpx.Client(verify=False)

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    http_client=http_client
)
model = os.getenv("OPENAI_MODEL_NAME", "gpt-3.5-turbo")

# Load sentiment summary
df = pd.read_csv("aspect_sentiment_summary.csv")
top_aspects = df.sort_values("positive", ascending=False).head(5)

# Build input text
aspect_summary = "\n".join(
    [f"- {row['main_aspect']}: {row['positive']} positive, {row['neutral']} neutral, {row['negative']} negative"
     for idx, row in top_aspects.iterrows()]
)

# Create prompt for GPT
prompt = f"""
You are a marketing insights analyst.

Based on this data from a Nike YouTube video sentiment analysis, write a 2-paragraph report summarizing the main customer perceptions and suggestions for brand strategy.

Here are the top-mentioned aspects and their sentiment:

{aspect_summary}

Write it as if you're presenting to Nike's marketing team. Be specific and use natural language. End with 3 clear, bullet-point recommendations.
"""

# Call OpenAI GPT
try:
    print(f"Using model: {model}")
    print(f"API key configured: {'Yes' if os.getenv('OPENAI_API_KEY') else 'No'}")
    
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful marketing analyst."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    
    report_text = response.choices[0].message.content
    
except Exception as e:
    print(f"Error calling OpenAI API: {e}")
    # Fallback: create a basic report from the data
    report_text = f"""
    Nike YouTube Video Sentiment Analysis Report
    ============================================
    
    Based on aspect-based sentiment analysis of customer comments, the following insights were identified:
    
    Top Customer Aspects and Sentiments:
    {aspect_summary}
    
    Key Recommendations:
    • Increase product availability to meet high demand
    • Improve communication about release quantities and timing
    • Address reseller and bot issues in the purchasing process
    
    Note: This is a simplified report due to API connectivity issues.
    """

# Save to file
with open("nike_ai_summary_report.txt", "w", encoding="utf-8") as f:
    f.write(report_text)

print("✅ Summary report saved to nike_ai_summary_report.txt")
