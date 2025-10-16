# Thoughtful AI Support Agent

A simple customer support chatbot that answers questions about Thoughtful AI's automation agents using BM25 search and tag matching.

## Features

- BM25 text matching for semantic search
- Tag-based keyword matching for better accuracy
- Clean Streamlit chat interface
- Clickable example questions

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

Or directly:
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Files

- `knowledge_base.json` - Q&A data with tags
- `agent.py` - BM25 and tag matching logic
- `app.py` - Streamlit UI
- `main.py` - Entry point
- `requirements.txt` - Dependencies