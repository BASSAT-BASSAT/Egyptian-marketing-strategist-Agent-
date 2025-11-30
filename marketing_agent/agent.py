import os
from typing import List

import google.generativeai as genai
from dotenv import load_dotenv

from . import tools

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


def _get_llm(temperature: float = 0.6):
    if not GOOGLE_API_KEY:
        raise ValueError("لازم تضيف GOOGLE_API_KEY في ملف .env")
    genai.configure(api_key=GOOGLE_API_KEY)
    return genai.GenerativeModel("gemini-2.0-flash")


def _call_llm(model, prompt: str, temperature: float = 0.6) -> str:
    try:
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(temperature=temperature)
        )
        return response.text
    except Exception as e:
        return f"خطأ في الاتصال: {e}"


def summarize_competitors(business: str, competitors: List[dict]) -> str:
    model = _get_llm(temperature=0.3)
    prompt = f"""انت محلل تسويق مصري محترف. اكتب تحليل للمنافسين بالعامية المصرية.

البيزنس بتاعنا: {business}

المنافسين:
"""
    for c in competitors:
        prompt += f"- {c.get('title')}: {c.get('href')}\n  {c.get('body', '')[:100]}\n"
    
    prompt += """
اكتب بالعامية المصرية:
1. ملخص سريع (2-3 فقرات) عن المنافسين دول
2. 5-6 حاجات نقدر نستفيد منها ونطبقها
3. نقاط القوة والضعف عندهم

خلي الكلام سهل وواضح زي ما بنتكلم مع صاحبنا."""
    return _call_llm(model, prompt, temperature=0.3)


def create_marketing_strategy(business_info: str, competitor_summary: str) -> str:
    model = _get_llm(temperature=0.7)
    prompt = f"""انت استراتيجي تسويق مصري خبير. اكتب خطة تسويق كاملة بالعامية المصرية.

معلومات البيزنس:
{business_info}

تحليل المنافسين:
{competitor_summary}

اكتب الخطة دي:
## 🎯 الرسالة التسويقية
جملة واحدة قوية تعبر عن البيزنس

## 📱 القنوات التسويقية (بالترتيب)
3 قنوات رئيسية مع شرح ليه اخترناهم

## 📅 خطة الـ 6 أسابيع
أسبوع أسبوع، إيه اللي هنعمله ومؤشرات النجاح

## 💡 أفكار محتوى
10 أفكار بوستات وفيديوهات

## 💰 الميزانية المقترحة
تقدير سريع للتكاليف

خلي الكلام عملي ومصري وسهل التنفيذ."""
    return _call_llm(model, prompt, temperature=0.7)


def run_full_pipeline(business_info: str):
    query = f"{business_info} competitors"
    competitors = tools.competitor_search(query)
    competitor_summary = summarize_competitors(business_info, competitors)
    strategy = create_marketing_strategy(business_info, competitor_summary)
    catchphrases = tools.generate_catchphrase(business_info.split('\n')[0], business_info, num_phrases=5)
    return {
        "competitors": competitors,
        "competitor_summary": competitor_summary,
        "strategy": strategy,
        "catchphrases": catchphrases,
    }
