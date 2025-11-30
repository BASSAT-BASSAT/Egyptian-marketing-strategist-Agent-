import os
from typing import List, Dict

import requests
from ddgs import DDGS
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


def translate_to_english(text: str) -> str:
    try:
        import google.generativeai as genai
        
        genai.configure(api_key=GOOGLE_API_KEY)
        model = genai.GenerativeModel("gemini-2.0-flash")
        
        prompt = f"""Translate the following Arabic business description to English search keywords.
Focus on: business type, industry, products/services.
Add "Egypt" or "Egyptian" to make the search Egypt-specific.
Only return the English search query, nothing else.

Arabic text: {text}

Example: "مطعم مشاوي في القاهرة" → "Egyptian grill restaurant Cairo competitors" """
        
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"خطأ في الترجمة: {e}")
        return text


def competitor_search(query: str, max_results: int = 5) -> List[Dict]:
    try:
        english_query = translate_to_english(query)
        print(f"🔍 البحث بـ: {english_query}")
        
        ddgs = DDGS()
        results = ddgs.text(f"{english_query} Egypt competitors", max_results=max_results * 2, region="ar-XA")
        
        out = []
        for r in results:
            title = r.get("title", "")
            href = r.get("href", "")
            body = r.get("body", "")
            
            if not body or len(body) < 20:
                continue
                
            out.append({"title": title, "href": href, "body": body[:300]})
            
            if len(out) >= max_results:
                break
        
        if len(out) < 3:
            results = ddgs.text(f"{english_query} Egyptian market", max_results=max_results * 3, region="ar-XA")
            for r in results:
                title = r.get("title", "")
                href = r.get("href", "")
                body = r.get("body", "")
                
                if body and len(body) > 20:
                    if not any(item["href"] == href for item in out):
                        out.append({"title": title, "href": href, "body": body[:300]})
                        if len(out) >= max_results:
                            break
        
        return out[:max_results]
    except Exception as e:
        print(f"خطأ في البحث: {e}")
        return []


def fetch_page_text(url: str, timeout: int = 6) -> str:
    try:
        r = requests.get(url, timeout=timeout, headers={"User-Agent": "marketing-agent/1.0"})
        return r.text[:60_000]
    except Exception:
        return ""


def generate_catchphrase(business_name: str, business_desc: str, num_phrases: int = 5) -> List[str]:
    try:
        import google.generativeai as genai
        
        genai.configure(api_key=GOOGLE_API_KEY)
        model = genai.GenerativeModel("gemini-2.0-flash")
        
        prompt = f"""انت كاتب إعلانات مصري محترف. اكتب {num_phrases} شعارات تسويقية قصيرة وجذابة بالعامية المصرية.

اسم البيزنس: {business_name}
وصف البيزنس: {business_desc}

المتطلبات:
- كل شعار من 3-7 كلمات بس
- استخدم لغة مصرية عصرية وشبابية
- خليها سهلة الحفظ والمشاركة
- حط الترجمة الإنجليزية في قوسين

اكتب الشعارات بس، شعار في كل سطر."""
        
        response = model.generate_content(prompt)
        phrases = [p.strip() for p in response.text.split('\n') if p.strip()]
        return phrases[:num_phrases]
    except Exception as e:
        print(f"خطأ في إنشاء الشعارات: {e}")
        return []


def analyze_product_image(image_bytes: bytes, business_name: str, business_desc: str) -> Dict:
    try:
        import google.generativeai as genai
        import base64
        
        genai.configure(api_key=GOOGLE_API_KEY)
        model = genai.GenerativeModel("gemini-2.0-flash")
        
        image_data = base64.b64encode(image_bytes).decode('utf-8')
        
        prompt = f"""انت خبير تسويق ومصمم مصري محترف. حلل الصورة دي للمنتج/البيزنس وقدم تقييم شامل بالعامية المصرية.

اسم البيزنس: {business_name}
وصف البيزنس: {business_desc}

قدم التحليل ده:

## 🎨 تقييم الصورة
- جودة الصورة (إضاءة، وضوح، زاوية التصوير)
- هل الصورة احترافية ولا محتاجة تحسين؟
- تقييم من 10

## 🏷️ التوافق مع البراند
- هل الصورة بتعبر عن اسم البيزنس "{business_name}"؟
- هل بتوصل الرسالة الصح للعملاء؟
- إيه اللي ممكن يتحسن؟

## 📱 جاهزية السوشيال ميديا
- هل الصورة تنفع للإنستجرام والفيسبوك؟
- اقتراحات للتعديل أو الفلاتر
- أفكار لأنواع صور تانية تنفع للبيزنس

## 💡 نصايح للتحسين
- 5 نصايح عملية لتحسين صور المنتجات
- أفكار لجلسات تصوير جديدة

## ⚠️ تحذيرات
- أي حاجة ممكن تأثر سلباً على البيزنس في الصورة

خلي الكلام عملي ومفيد وبالمصري."""

        response = model.generate_content([
            prompt,
            {"mime_type": "image/jpeg", "data": image_data}
        ])
        
        analysis = response.text
        
        score_prompt = f"""بناءً على تحليلك للصورة، اعطي تقييم رقمي من 1-10 لكل عنصر. رد بالأرقام فقط مفصولة بفاصلة:
جودة الصورة, التوافق مع البراند, جاهزية السوشيال ميديا

مثال: 7, 8, 6"""
        
        score_response = model.generate_content([
            score_prompt,
            {"mime_type": "image/jpeg", "data": image_data}
        ])
        
        try:
            scores = [int(s.strip()) for s in score_response.text.split(',')]
            if len(scores) >= 3:
                scores_dict = {
                    "image_quality": scores[0],
                    "brand_fit": scores[1],
                    "social_ready": scores[2],
                    "overall": round(sum(scores) / 3, 1)
                }
            else:
                scores_dict = {"image_quality": 5, "brand_fit": 5, "social_ready": 5, "overall": 5}
        except:
            scores_dict = {"image_quality": 5, "brand_fit": 5, "social_ready": 5, "overall": 5}
        
        return {
            "analysis": analysis,
            "scores": scores_dict
        }
        
    except Exception as e:
        print(f"خطأ في تحليل الصورة: {e}")
        return {
            "analysis": f"حصل خطأ في تحليل الصورة: {str(e)}",
            "scores": {"image_quality": 0, "brand_fit": 0, "social_ready": 0, "overall": 0}
        }
