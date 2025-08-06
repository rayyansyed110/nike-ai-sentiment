import pandas as pd
from crewai import Crew, Agent, Task, Process
import os
from dotenv import load_dotenv
from textwrap import dedent


load_dotenv()
os.environ["OPENAI_MODEL_NAME"] = "gpt-4"


# Load comments
df = pd.read_csv("nike_sentiment.csv")

# Combine all comments into one big text block
text_data = "\n".join(df["comment"].tolist())

# Agent 1 – Insight Extractor
insight_agent = Agent(
    role="Customer Insight Analyst",
    goal="Extract themes and trends from Nike customer feedback",
    backstory="You're an expert in marketing and trend detection. You analyze customer reviews to find what they like, dislike, and repeat often.",
    allow_delegation=False,
    verbose=True
)

# Agent 2 – Brand Strategist
strategy_agent = Agent(
    role="Brand Strategist",
    goal="Provide actionable brand strategy based on feedback",
    backstory="You're a marketing strategist at Nike. Your job is to turn public sentiment into product, messaging, and experience improvements. You always provide exactly 3 numbered recommendations with clear action steps.",
    allow_delegation=False,
    verbose=True
)

task1 = Task(
    description=dedent(f"""
    Analyze the following YouTube comments about Nike products:
    -----
    {text_data[:3000]}
    -----
    Identify recurring customer opinions, product highlights, common complaints, or praise.
    """),
    agent=insight_agent,
    expected_output="A structured summary of the most common themes, positive feedback, and negative feedback mentioned in the comments."
)

# Task for Agent 2
task2 = Task(
    description=dedent("""
    You must provide exactly THREE specific, actionable recommendations for Nike based on the customer feedback analysis.
    
    Format your response as:
    1. [Recommendation title]: [Specific action Nike should take]
    2. [Recommendation title]: [Specific action Nike should take]  
    3. [Recommendation title]: [Specific action Nike should take]
    
    Focus on addressing these key customer issues:
    - Limited product availability causing frustration
    - Difficult purchasing process with bots/resellers
    - Strong demand for storytelling and craftsmanship
    """),
    agent=strategy_agent,
    expected_output="Exactly three numbered recommendations with specific, actionable steps Nike can implement to address customer concerns about availability, purchasing experience, and brand engagement.",
    context=[task1]
)

# Run crew
crew = Crew(
    agents=[insight_agent, strategy_agent],
    tasks=[task1, task2],
    process=Process.sequential
)

result = crew.kickoff()

# Save comprehensive analysis to file
with open("final_output.txt", "w", encoding="utf-8") as f:
    f.write("🧠 NIKE AI SENTIMENT ANALYSIS - COMPREHENSIVE REPORT\n")
    f.write("="*70 + "\n\n")
    
    f.write("📊 CUSTOMER INSIGHT ANALYSIS\n")
    f.write("-" * 30 + "\n")
    f.write(str(crew.tasks[0].output) + "\n\n")
    
    f.write("💡 STRATEGIC RECOMMENDATIONS\n")
    f.write("-" * 30 + "\n")
    f.write(str(result) + "\n\n")
    
    f.write("🏷️ METADATA\n")
    f.write("-" * 10 + "\n")
    f.write(f"Analysis Date: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write(f"Total Comments Analyzed: {len(df)}\n")
    f.write(f"Model Used: {os.environ.get('OPENAI_MODEL_NAME', 'gpt-4')}\n")

print("\n🧠 FINAL OUTPUT:\n")
print(result)
print("\n✅ Comprehensive analysis saved to final_output.txt")

