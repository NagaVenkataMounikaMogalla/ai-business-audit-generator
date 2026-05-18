# 🚀 AI Business Audit Generator

## Overview

AI Business Audit Generator is a Streamlit-based automation tool that analyzes company websites using AI and generates personalized business audit reports in PDF format.

The application performs:
- Website scraping
- AI-powered business analysis
- Automated PDF generation
- Email delivery of reports

---

## Features

- Website content extraction
- AI-generated business insights
- Personalized recommendations
- PDF report generation
- Automated email sending
- Streamlit web interface

---

## Tech Stack

- Python
- Streamlit
- BeautifulSoup
- Requests
- OpenAI API
- FPDF
- SMTP Email Automation

---

## Workflow

1. User submits company details
2. Website content is scraped
3. AI generates business insights
4. PDF report is created
5. Report is downloaded and emailed

---

## Installation

```bash
pip install -r requirements.txt
python -m streamlit run app.py
```

---

## API Setup

Before running the project:

1. Add your OpenRouter API key inside `ai_insights.py`

2. Add your Gmail app password inside `email_sender.py`

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python -m streamlit run app.py
```

---

## Project Structure

```text
simplifiq-project/
│
├── app.py
├── scraper.py
├── ai_insights.py
├── report_generator.py
├── email_sender.py
├── requirements.txt
├── README.md
└── generated_reports/
```

---

## Future Improvements

- Better PDF templates
- Async email queue system
- Dashboard analytics
- Multi-language support
- Advanced website analytics

---

## Limitations

Some websites may block scraping due to:
- Anti-bot protection
- CAPTCHA
- Dynamic rendering

SMTP email delivery may occasionally be delayed because of Gmail rate limits.

---

## Author

Mounika Mogalla