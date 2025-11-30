#!/usr/bin/env python3
import sys
sys.path.insert(0, 'c:/Users/asus/Desktop/Projects/Marketing agent')

from marketing_agent import agent

test_cases = [
    {
        "name": "تطبيق فيتنس بالذكاء الاصطناعي",
        "input": "AI-powered fitness app that personalizes workouts using machine learning. Target: busy professionals aged 25-45. Monthly subscription $9.99. Goal: reach 50k users in 6 months."
    },
    {
        "name": "تغليف صديق للبيئة",
        "input": "Sustainable packaging solution for e-commerce businesses. Biodegradable, compostable materials. Competitive pricing vs traditional packaging. Target: SME online retailers. Goal: partner with 100 retailers."
    },
    {
        "name": "تطبيق صحة نفسية",
        "input": "Mobile app offering AI-powered therapy and meditation. Affordable access to mental health support. Target: Gen Z and millennials. Subscription $7.99/month. Goal: 100k downloads in year 1."
    },
    {
        "name": "منصة تعليم برمجة",
        "input": "Interactive coding bootcamp platform. Project-based learning for Python and JavaScript. Career placement assistance. Target: career changers and students. Price: $500 per course. Goal: 5000 students enrolled."
    }
]

print("=" * 80)
print("🇪🇬 وكيل التسويق المصري - اختبار")
print("=" * 80)

for i, test_case in enumerate(test_cases, 1):
    print(f"\n\n{'='*80}")
    print(f"اختبار {i}: {test_case['name']}")
    print(f"{'='*80}")
    print(f"\nالمدخل: {test_case['input'][:100]}...\n")
    
    try:
        print("جاري تشغيل الوكيل...")
        results = agent.run_full_pipeline(test_case['input'])
        
        print("\n--- ملخص المنافسين ---")
        print(results["competitor_summary"][:500] + "...\n")
        
        print("\n--- الاستراتيجية التسويقية ---")
        print(results["strategy"][:500] + "...\n")
        
        print("\n--- الشعارات ---")
        for phrase in results.get("catchphrases", [])[:3]:
            print(f"  • {phrase}")
        
        print("\n--- المنافسين ---")
        for c in results["competitors"][:3]:
            print(f"  • {c.get('title')}")
            print(f"    {c.get('href')}\n")
            
    except Exception as e:
        print(f"خطأ: {e}")
        import traceback
        traceback.print_exc()

print("\n" + "=" * 80)
print("✅ تم الاختبار!")
print("=" * 80)
