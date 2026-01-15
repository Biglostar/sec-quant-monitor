# sec-quant-monitor
📊 SEC Real-Time Quant Monitor
An Applied Mathematics approach to capturing market Alpha through automated SEC Filing analysis.

🔍 Project Overview
This project is a Quant Analysis Pipeline designed to monitor SEC (U.S. Securities and Exchange Commission) EDGAR filings in real-time. It identifies key corporate events and strategic shifts—such as changes in asset composition or management pivots—to capture investment opportunities before they are fully priced into the market.

The inspiration for this project stems from a successful investment in Strive (Asset Entities Inc.), where analyzing SEC filings revealed a strategic pivot to Bitcoin-based treasury management, resulting in significant alpha. This tool formalizes that manual process into an automated data engineering and mathematical modeling system.

🛠 Tech Stack
Language: Python 3.x

Data Ingestion: SEC RSS Feeds, secedgar library, EDGAR API

Processing: BeautifulSoup (HTML/XML Parsing), Pandas (Data Transformation)

Analysis: Natural Language Processing (NLP) for Sentiment Analysis, Statistical Backtesting

Notification: Slack/Discord Webhook API for real-time alerts

🚀 Key Features
Real-Time Monitoring: Scans SEC RSS feeds at 1-minute intervals to ingest the latest 8-K, 10-K, 10-Q, and Form 4 filings.

Strategic Keyword Filtering: Automatically filters for high-impact keywords such as "Bitcoin", "Digital Asset", "M&A", and "Restructuring".

Quantitative Event Study: Statistically analyzes the impact of specific filing types on historical stock price volatility and returns.

Automated Alerting System: Dispatches instant notifications to mobile/desktop via Webhooks when a high-probability signal is detected.

📈 Mathematical Framework (Applied Math Focus)
Event Study Methodology: Using a t=0 event window to calculate Cumulative Abnormal Returns (CAR) and validate the statistical significance of filing-driven signals.

Risk Optimization: Implementing Mean-Variance Optimization to adjust portfolio weights based on the confidence score of the extracted signals.

NLP Scoring: Assigning numerical weights to qualitative text data to transform "Management Discussion and Analysis (MD&A)" into actionable quantitative inputs.

📂 Project Structure
Plaintext
├── src/
│   ├── ingestion/      # SEC RSS Scraper & API Handler
│   ├── processing/     # Text parsing & Keyword extraction logic
│   └── analytics/      # Statistical backtesting & Math models
├── data/               # Historical filing metadata & Backtest results
├── tests/              # Unit tests for scraper reliability
└── README.md
💡 Future Roadmap
Integrate LLM-based summarization (GPT/Claude API) for complex 10-K filings.

Develop a Streamlit Dashboard for visual tracking of real-time signals.

Expand coverage to include Insider Trading (Form 4) sentiment correlation.
