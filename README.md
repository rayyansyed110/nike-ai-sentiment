# 🧠 Nike AI Sentiment Analysis

An advanced AI-powered sentiment analysis system that analyzes YouTube comments about Nike products using CrewAI multi-agent framework and OpenAI's GPT-4 to generate actionable business insights.

## 🚀 Features

- **Multi-Agent AI System**: Uses CrewAI framework with specialized agents for analysis and strategy
- **Aspect-Based Sentiment Analysis**: Advanced NLP using spaCy for granular opinion mining
- **YouTube Comment Analysis**: Processes real customer feedback from Nike product videos
- **Dual Analysis Modes**: Both online (API-based) and offline (network-independent) capabilities
- **Strategic Recommendations**: Generates actionable business insights for brand improvement
- **Professional Business Reports**: Executive-level summaries with impact forecasts
- **Comprehensive Reporting**: Multiple output formats for different stakeholders

## 🛠️ Tech Stack

- **Python**: Core programming language
- **CrewAI**: Multi-agent AI orchestration framework
- **OpenAI GPT-4**: Large language model for analysis
- **spaCy**: Advanced natural language processing and aspect extraction
- **scikit-learn**: Machine learning for clustering and pattern recognition
- **Pandas**: Data manipulation and analysis
- **YouTube Data API**: Comment extraction (via separate scraper)

## 📊 Project Structure

```
nike-ai-sentiment/
├── scrape_nike_comments.py          # YouTube comment scraper
├── analyze_sentiment.py             # Basic sentiment analysis
├── generate_insights.py             # AI-powered insight generation (CrewAI)
├── aspect_sentiment.py              # Advanced aspect-based analysis (spaCy)
├── generate_report.py               # OpenAI API report generator
├── generate_comprehensive_report.py # Offline business report generator
├── nike_youtube_comments.csv        # Raw scraped comments
├── nike_sentiment.csv               # Processed sentiment data
├── nike_emotion_sentiment.csv       # Enhanced emotion analysis data
├── aspect_sentiment_summary.csv     # Aspect-based analysis results
├── final_output.txt                 # CrewAI multi-agent insights
├── nike_comprehensive_report.txt    # Executive business report
├── requirements.txt                 # Python dependencies
├── .env.example                     # Environment variables template
└── README.md                        # Project documentation
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
- **Distinct Aspects Identified**: 112 unique customer discussion points
- **Overall Sentiment**: 50.6% positive, 39.1% neutral, 10.3% negative
- **AI Model Used**: GPT-4 for strategic insights
- **Analysis Date**: August 6-7, 2025
- **Analysis Methods**: Multi-agent AI + Aspect-based NLP + Clustering
- **Key Products Mentioned**: Mars Yard, ACG line, Jordan models

## � Analysis Capabilities

### 1. **Multi-Agent AI Analysis** (`generate_insights.py`)
- Uses CrewAI framework with specialized AI agents
- Customer Insight Analyst + Brand Strategist collaboration
- Requires OpenAI API access
- Generates strategic business recommendations

### 2. **Aspect-Based Sentiment Analysis** (`aspect_sentiment.py`)
- Advanced NLP using spaCy for noun phrase extraction
- K-means clustering to identify discussion themes
- Granular sentiment mapping per topic/aspect
- Works offline without API dependencies

### 3. **Comprehensive Business Reports** (`generate_comprehensive_report.py`)
- Executive-level analysis and insights
- Professional formatting for stakeholder presentations
- Impact forecasts and strategic recommendations
- Network-independent operation

### 4. **Flexible Report Generation** (`generate_report.py`)
- OpenAI API-based report generation
- Customizable analysis prompts
- Fallback to offline mode if API unavailable

## �🚀 Quick Start

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

4. **Set up environment variables** (for online AI analysis)
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   OPENAI_MODEL_NAME=gpt-4
   ```
   *Note: Copy from `.env.example` and add your actual API key*

5. **Download spaCy language model**
   ```bash
   python -m spacy download en_core_web_sm
   ```

### Usage

#### **Option 1: Multi-Agent AI Analysis (Requires API)**
```bash
python generate_insights.py
```
- Real-time agent collaboration and strategic insights
- Outputs: `final_output.txt` with detailed agent analysis

#### **Option 2: Aspect-Based Analysis (Offline)**
```bash
python aspect_sentiment.py
```
- Advanced NLP without API requirements
- Outputs: `aspect_sentiment_summary.csv` with topic breakdowns

#### **Option 3: Comprehensive Business Report (Offline)**
```bash
python generate_comprehensive_report.py
```
- Executive-level business analysis
- Outputs: `nike_comprehensive_report.txt` with professional insights

#### **Option 4: Custom Report Generation**
```bash
python generate_report.py
```
- API-based custom reports with fallback capabilities
- Outputs: `nike_ai_summary_report.txt`

### 📊 **Output Files Overview**
- `final_output.txt` - Multi-agent AI strategic analysis
- `nike_comprehensive_report.txt` - Executive business report  
- `aspect_sentiment_summary.csv` - Detailed aspect analysis data
- `nike_ai_summary_report.txt` - Custom AI-generated summaries

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
