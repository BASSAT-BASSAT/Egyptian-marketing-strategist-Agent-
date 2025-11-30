# 🇪🇬 وكيل التسويق المصري | Egyptian Marketing Agent

An AI-powered marketing strategist that speaks Egyptian Arabic! Get competitor analysis, marketing strategies, catchy slogans, and product image analysis - all in authentic Egyptian dialect.

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.20+-red)
![Gemini](https://img.shields.io/badge/Google%20Gemini-2.0%20Flash-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## ✨ Features

### 🔍 Competitor Analysis
- Searches for competitors in the **Egyptian market**
- Automatically translates Arabic queries to English for better search results
- Returns relevant competitor links and summaries

### 📊 Marketing Strategy Generation
- Complete 6-week marketing plan
- Channel recommendations (Social Media, Delivery Apps, Local Marketing)
- Budget estimates
- Content ideas (10+ post/video ideas)
- KPIs and success metrics

### 💬 Egyptian Arabic Slogans
- 5 catchy marketing catchphrases in **Egyptian dialect (العامية المصرية)**
- Includes English translations
- Ready to use on social media

### 📸 Product Image Analysis (NEW!)
- Upload product photos or logos
- Get scores for:
  - 🎨 Image Quality (1-10)
  - 🏷️ Brand Fit (1-10)
  - 📱 Social Media Readiness (1-10)
- Detailed improvement suggestions
- Photography tips

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/BASSAT-BASSAT/Egyptian-marketing-strategist-Agent-.git
cd Egyptian-marketing-strategist-Agent-
```

### 2. Create virtual environment
```powershell
# Windows PowerShell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

```bash
# Linux/Mac
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Set up your API key
Create a `.env` file:
```env
GOOGLE_API_KEY=your-google-gemini-api-key
```

Get your free API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

### 4. Run the app
```bash
streamlit run app.py
```

---

## 💡 What You Get

| Feature | Description | Output Language |
|---------|-------------|-----------------|
| **Competitor Research** | Find Egyptian market competitors | English links, Arabic analysis |
| **Marketing Strategy** | Complete 6-week plan | Egyptian Arabic |
| **Slogans/Catchphrases** | 5 catchy taglines | Egyptian Arabic + English |
| **Image Analysis** | Product photo feedback | Egyptian Arabic |

---

## 📱 Example Usage

### Input:
```
اسم البيزنس: مشاوي الحارة
المجال: مطاعم
الوصف: مطعم مشاوي مصري في القاهرة. كباب وكفتة وفراخ مشوية.
العملاء: عائلات وشباب من 20-50 سنة.
الأسعار: 150-300 جنيه للوجبة.
الهدف: 5000 أوردر شهرياً.
```

### Output:
- ✅ Competitor analysis with links to similar Egyptian restaurants
- ✅ 6-week marketing strategy in Egyptian Arabic
- ✅ Slogans like: "اشويي يا شويش، طعم اللي بيحوش!" (Eshweey ya Shweesh, taste that satisfies!)
- ✅ Budget recommendations
- ✅ Social media content calendar

---

## 🛠️ Tech Stack

| Technology | Purpose | Cost |
|------------|---------|------|
| **Google Gemini 2.0 Flash** | LLM for strategy & analysis | Free tier available |
| **DuckDuckGo Search** | Competitor research | Free |
| **Streamlit** | Web UI | Free |
| **Python** | Backend | Free |

---

## 📁 Project Structure

```
├── app.py                    # Streamlit web interface
├── marketing_agent/
│   ├── __init__.py
│   ├── agent.py              # Main agent logic
│   └── tools.py              # Search, translation, image analysis
├── requirements.txt          # Dependencies
├── test_agent.py            # Test script
└── .env                     # API keys (create this)
```

---

## 🔑 API Key Setup

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Add it to your `.env` file

**Free tier includes:**
- 15 requests per minute
- 1,500 requests per day
- Perfect for small businesses!

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

---

## 📄 License

MIT License - feel free to use for your own projects!

---

## 👨‍💻 Author

Made with ❤️ for Egyptian entrepreneurs and small businesses.

**يلا نكبر البيزنس بتاعك! 🚀🇪🇬**



