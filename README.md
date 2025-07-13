# TextSummarizer

A simple web app that summarizes user-inputted text using basic NLP heuristics. Returns a 3-sentence summary.
![Input UI and summary example](<Screenshot 2025-07-12 at 8.18.53 PM.png>)

## Features
- Extractive summary of paragraphs
- Real-time interaction with Flask backend
- Built using TextBlob (lexical heuristics)

## Tech Stack
- Python 3.7+
- Flask
- TextBlob
- HTML, JS (frontend)

## Installation

```bash
git clone https://github.com/blackberryjam876/TextSummarizer.git
cd TextSummarizer
pip install -r requirements.txt
python app.py
```

Then visit: `http://localhost:5000`

## 📄 License
MIT (for the usage of TextBlob).
