# Marketing Agent — Streamlit + Google Gemini

A free marketing strategy generator using Google Gemini LLM and web search.

**Features:**

- AI-powered competitor research (DuckDuckGo search)
- Marketing strategy generation with Gemini 2.0 Flash
- Competitor analysis and summary
- Purple-themed Streamlit UI
- Completely free (only requires GOOGLE_API_KEY)

**Quick start (Windows PowerShell):**

1. Create a virtual environment and activate it

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
pip install -r "requirements.txt"
```

2. Set your Google Gemini API key

```powershell
$env:GOOGLE_API_KEY = 'your-google-gemini-key'
```

Or create `.env` from `.env.example` and fill in the key.

3. Run the Streamlit app

```powershell
streamlit run app.py
```

**What You Get:**

| Feature | Technology | Cost |
|---------|-----------|------|
| **LLM** | Google Gemini 2.0 Flash | Free (daily limit) |
| **Competitor Search** | DuckDuckGo | Free |
| **Web UI** | Streamlit | Free |
| **Logo** | Purple gradient placeholder | Free |

**API Key Setup:**

Get your free GOOGLE_API_KEY from [Google AI Studio](https://makersuite.google.com/app/apikey)

Free tier includes:
- 15 requests per minute
- Unlimited requests per day
- Perfect for development and testing

**Test Inputs:**

See `TEST_INPUTS.md` for example business descriptions to test.



