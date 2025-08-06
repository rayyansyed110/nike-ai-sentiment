# 🧠 Nike AI Sentiment Analysis

An advanced AI-powered sentiment analysis system that analyzes YouTube comments about Nike products using CrewAI multi-agent framework and OpenAI's GPT-4 to generate actionable business insights.

## 🚀 Features

- **Multi-Agent AI System**: Uses CrewAI framework with specialized agents for analysis and strategy
- **YouTube Comment Analysis**: Processes real customer feedback from Nike product videos
- **Sentiment Classification**: Identifies positive, negative, and neutral sentiments
- **Strategic Recommendations**: Generates actionable business insights for brand improvement
- **Comprehensive Reporting**: Exports detailed analysis reports

## 🛠️ Tech Stack

- **Python**: Core programming language
- **CrewAI**: Multi-agent AI orchestration framework
- **OpenAI GPT-4**: Large language model for analysis
- **Pandas**: Data manipulation and analysis
- **YouTube Data API**: Comment extraction (via separate scraper)

## 📊 Project Structure

```
nike-ai-sentiment/
├── scrape_nike_comments.py    # YouTube comment scraper
├── analyze_sentiment.py       # Basic sentiment analysis
├── generate_insights.py       # AI-powered insight generation
├── nike_youtube_comments.csv  # Raw scraped comments
├── nike_sentiment.csv         # Processed sentiment data
├── final_output.txt          # AI-generated insights report
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## 🎯 AI Analysis Results

### 📊 Customer Insight Analysis

**Key Findings:**
- **High Anticipation**: Customers show great excitement for product releases
- **Design Appreciation**: Strong positive sentiment toward aesthetics and functionality
- **Storytelling Value**: Customers appreciate Nike's narrative approach to product launches
- **Availability Frustration**: Major complaints about limited supply and reseller issues
- **Transparency Requests**: Customers want clearer communication about release quantities

**Brand Perception:**
- Nike is viewed as a high-end fashion leader with innovative designs
- Some skepticism exists about "high art" marketing targeting wealthy consumers
- Strong brand loyalty despite purchasing difficulties

### 💡 Strategic Recommendations

#### 1. **Improve Product Availability**
- Implement pre-order model for new releases
- Increase production of high-demand models
- Provide transparent release quantity information
- Create tiered release system to maintain exclusivity while improving access

#### 2. **Enhance Purchasing Process**
- Deploy advanced bot detection (CAPTCHA, OTP verification)
- Implement purchase limits per customer
- Create loyalty-based allocation system
- Prioritize rewards program members for exclusive access

#### 3. **Deepen Storytelling and Craftsmanship**
- Develop documentary content showcasing design process
- Create designer interview series
- Build augmented reality experiences for product creation
- Focus on innovation and quality narratives beyond fashion

## 📈 Analysis Metrics

- **Total Comments Analyzed**: 174
- **AI Model Used**: GPT-4
- **Analysis Date**: August 6, 2025
- **Sentiment Categories**: Positive, Negative, Neutral themes identified
- **Key Products Mentioned**: Mars Yard, ACG line, Jordan models

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- OpenAI API key
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/rayyansyed110/nike-ai-sentiment.git
   cd nike-ai-sentiment
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # or
   source venv/bin/activate  # macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   OPENAI_MODEL_NAME=gpt-4
   ```

### Usage

1. **Run the AI analysis**
   ```bash
   python generate_insights.py
   ```

2. **View results**
   - Check console output for real-time agent interactions
   - Review `final_output.txt` for comprehensive analysis report

## 🤖 AI Agents

### Customer Insight Analyst
- **Role**: Extract themes and trends from customer feedback
- **Specialty**: Marketing and trend detection
- **Output**: Structured sentiment analysis with themes identification

### Brand Strategist  
- **Role**: Transform insights into actionable business strategy
- **Specialty**: Nike marketing strategy and brand improvement
- **Output**: Three specific, actionable recommendations

## 📁 Data Sources

- **YouTube Comments**: Nike product video comments
- **Sentiment Data**: Processed customer feedback with sentiment scores
- **Analysis Reports**: AI-generated business intelligence

## 🔒 Privacy & Security

- API keys are excluded from version control (`.gitignore`)
- No personal customer data is stored
- Comments are anonymized for analysis
- Secure environment variable management

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Nike for providing inspiration for this analysis
- OpenAI for GPT-4 capabilities
- CrewAI team for the multi-agent framework
- YouTube for comment data access

## 📞 Contact

Rayyan Syed - [@rayyansyed110](https://github.com/rayyansyed110) - syedrayyanahmed1853@gmail.com

Project Link: [https://github.com/rayyansyed110/nike-ai-sentiment](https://github.com/rayyansyed110/nike-ai-sentiment)

---

*This project demonstrates the power of AI-driven sentiment analysis for business intelligence and strategic decision-making.*
