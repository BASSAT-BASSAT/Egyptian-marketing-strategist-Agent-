# Test Examples for Marketing Agent

## Test Input 1: AI Fitness App (Recommended - Simple)
```
Name: AI Fitness App
Business Info:
AI-powered fitness app. Personalized workouts using ML. Target: busy professionals 25-45. 
Subscription: $9.99/month. Goal: 50k users in 6 months.
```

## Test Input 2: Eco-Friendly Packaging
```
Name: GreenPack Solutions
Business Info:
Sustainable biodegradable packaging for e-commerce. Compostable materials, competitive pricing.
Target: SME online retailers. Goal: 100 retail partnerships in year 1.
```

## Test Input 3: Mental Wellness App
```
Name: MindFlow
Business Info:
AI-powered meditation and therapy app. Affordable mental health access. Target: Gen Z & millennials.
Price: $7.99/month. Goal: 100k downloads in first year, 10k active daily users.
```

## Test Input 4: Code Learning Platform
```
Name: CodeBridge Academy
Business Info:
Interactive coding bootcamp. Project-based Python and JavaScript learning. Career placement.
Target: career changers and students. Price: $500/course. Goal: 5k students enrolled in Y1.
```

## Test Input 5: Niche SaaS (Most Interesting)
```
Name: ContentFlow Pro
Business Info:
AI content calendar and social media planning tool for small agencies. Auto-generates posts, 
schedules content, tracks engagement. Target: digital marketing agencies 5-50 employees.
Pricing: $199/month. Goal: 200 agencies subscribed, $40k MRR in 12 months.
```

---

## How to Test:
1. Open http://localhost:8501 in your browser
2. Copy one of the test inputs above
3. Paste into the "Business name" and "Describe your business..." fields
4. Click "Run agent"
5. Wait 30-60 seconds for results

## Expected Output:
- Competitor analysis (5-10 relevant companies)
- Marketing strategy (positioning, channels, 6-week plan, KPIs, budget)
- AI-generated logo (or purple placeholder if APIs unavailable)
- Direct links to competitor websites

---

## Troubleshooting:

**Logo not generating?**
- HF API might be rate-limited (free tier has limits)
- Replicate free tier: max 6 requests/min
- Fallback to purple placeholder is normal - it still shows a nice gradient

**Competitors not found?**
- DuckDuckGo search works offline, might need more specific input
- Try business type + keywords (e.g., "SaaS project management tool")

**Strategy seems generic?**
- Gemini works best with specific business details
- Add target audience, pricing, and goals for better results

**Empty responses?**
- Check that GOOGLE_API_KEY is set in .env
- Restart the Streamlit app: http://localhost:8501

