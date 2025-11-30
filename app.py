import os
import streamlit as st
from dotenv import load_dotenv
from marketing_agent import agent
from marketing_agent import tools

load_dotenv()

st.set_page_config(
    page_title="وكيل التسويق المصري 🇪🇬",
    page_icon="🇪🇬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&display=swap');

* {
    font-family: 'Cairo', sans-serif !important;
}

html, body, [data-testid="stAppViewContainer"], .main {
    direction: rtl !important;
    text-align: right !important;
}

.stApp {
    background: linear-gradient(160deg, #0c0c1e 0%, #1a1a3a 40%, #2d1f4e 70%, #1a1a3a 100%);
    min-height: 100vh;
}

[data-testid="stForm"] {
    direction: rtl;
}

.block-container {
    padding: 2rem 3rem !important;
    max-width: 1400px !important;
}

.main-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
    padding: 3rem 4rem;
    border-radius: 24px;
    margin-bottom: 2.5rem;
    text-align: center;
    box-shadow: 0 20px 60px rgba(102, 126, 234, 0.4);
    position: relative;
    overflow: hidden;
}

.main-header::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 60%);
    animation: shimmer 3s ease-in-out infinite;
}

@keyframes shimmer {
    0%, 100% { transform: translateX(-50%) translateY(-50%) rotate(0deg); }
    50% { transform: translateX(-30%) translateY(-30%) rotate(180deg); }
}

.main-header h1 {
    color: white;
    font-size: 3rem;
    font-weight: 900;
    margin: 0;
    text-shadow: 3px 3px 6px rgba(0,0,0,0.3);
    position: relative;
    z-index: 1;
}

.main-header p {
    color: rgba(255,255,255,0.95);
    font-size: 1.25rem;
    margin-top: 0.75rem;
    font-weight: 600;
    position: relative;
    z-index: 1;
}

.card {
    background: linear-gradient(145deg, rgba(255,255,255,0.08) 0%, rgba(255,255,255,0.02) 100%);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 20px;
    padding: 2rem;
    margin-bottom: 1.5rem;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
}

.card::before {
    content: '';
    position: absolute;
    top: 0;
    right: 0;
    width: 100px;
    height: 100px;
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.2) 0%, transparent 60%);
    border-radius: 0 20px 0 100px;
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0 25px 50px rgba(102, 126, 234, 0.25);
    border-color: rgba(102, 126, 234, 0.3);
}

.card-header {
    display: flex;
    align-items: center;
    justify-content: flex-start;
    gap: 12px;
    margin-bottom: 1.5rem;
    padding-bottom: 1rem;
    border-bottom: 2px solid rgba(102, 126, 234, 0.3);
}

.card-header h2 {
    background: linear-gradient(90deg, #667eea 0%, #f093fb 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    font-size: 1.5rem;
    font-weight: 800;
    margin: 0;
}

.card-content {
    color: rgba(255, 255, 255, 0.9);
    line-height: 2;
    font-size: 1.05rem;
}

.catchphrase-item {
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.15) 0%, rgba(240, 147, 251, 0.08) 100%);
    border-right: 4px solid #667eea;
    border-left: none;
    padding: 1.25rem 1.5rem;
    margin: 1rem 0;
    border-radius: 12px 0 0 12px;
    transition: all 0.3s ease;
    font-size: 1.1rem;
    color: white;
    font-weight: 600;
}

.catchphrase-item:hover {
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.25) 0%, rgba(240, 147, 251, 0.15) 100%);
    transform: translateX(-8px);
    box-shadow: 5px 0 20px rgba(102, 126, 234, 0.3);
}

.competitor-link {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    padding: 1.25rem;
    margin: 0.75rem 0;
    transition: all 0.3s ease;
}

.competitor-link:hover {
    background: rgba(102, 126, 234, 0.1);
    border-color: rgba(102, 126, 234, 0.4);
    transform: translateX(-5px);
}

.competitor-link a {
    color: #a78bfa;
    text-decoration: none;
    font-weight: 700;
    font-size: 1.1rem;
    transition: color 0.3s ease;
}

.competitor-link a:hover {
    color: #f093fb;
}

.competitor-link p {
    color: rgba(255, 255, 255, 0.6);
    font-size: 0.95rem;
    margin: 0.75rem 0 0 0;
    line-height: 1.6;
}

.stTextInput > div > div > input,
.stTextInput input {
    background: rgba(255, 255, 255, 0.06) !important;
    border: 2px solid rgba(102, 126, 234, 0.3) !important;
    border-radius: 14px !important;
    color: white !important;
    padding: 1rem 1.25rem !important;
    font-size: 1.1rem !important;
    direction: rtl !important;
    text-align: right !important;
    transition: all 0.3s ease !important;
}

.stTextInput > div > div > input:focus,
.stTextInput input:focus {
    border-color: #667eea !important;
    box-shadow: 0 0 30px rgba(102, 126, 234, 0.3) !important;
    background: rgba(255, 255, 255, 0.08) !important;
}

.stTextArea > div > div > textarea,
.stTextArea textarea {
    background: rgba(255, 255, 255, 0.06) !important;
    border: 2px solid rgba(102, 126, 234, 0.3) !important;
    border-radius: 14px !important;
    color: white !important;
    padding: 1.25rem !important;
    font-size: 1.1rem !important;
    direction: rtl !important;
    text-align: right !important;
    line-height: 1.8 !important;
    transition: all 0.3s ease !important;
}

.stTextArea > div > div > textarea:focus,
.stTextArea textarea:focus {
    border-color: #667eea !important;
    box-shadow: 0 0 30px rgba(102, 126, 234, 0.3) !important;
    background: rgba(255, 255, 255, 0.08) !important;
}

.stTextArea > div > div > textarea::placeholder,
.stTextInput > div > div > input::placeholder {
    color: rgba(255,255,255,0.4) !important;
}

.stButton > button {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 14px !important;
    padding: 1rem 2.5rem !important;
    font-size: 1.2rem !important;
    font-weight: 800 !important;
    width: 100% !important;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
    box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4) !important;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.2) !important;
}

.stButton > button:hover {
    transform: translateY(-3px) scale(1.02) !important;
    box-shadow: 0 15px 40px rgba(102, 126, 234, 0.5) !important;
}

.stButton > button:active {
    transform: translateY(0) scale(0.98) !important;
}

.success-banner {
    background: linear-gradient(135deg, #10b981 0%, #34d399 50%, #6ee7b7 100%);
    color: white;
    padding: 1.25rem 2rem;
    border-radius: 16px;
    text-align: center;
    font-weight: 700;
    font-size: 1.15rem;
    margin: 1.5rem 0;
    box-shadow: 0 10px 30px rgba(16, 185, 129, 0.3);
}

.stSpinner > div {
    border-color: #667eea !important;
}

label, .stTextInput label, .stTextArea label {
    color: rgba(255, 255, 255, 0.95) !important;
    font-weight: 700 !important;
    font-size: 1.1rem !important;
    margin-bottom: 0.5rem !important;
    direction: rtl !important;
    text-align: right !important;
}

.stMarkdown, .stMarkdown p, .stMarkdown li, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
    color: rgba(255, 255, 255, 0.9) !important;
    direction: rtl !important;
    text-align: right !important;
}

h1, h2, h3, h4, h5, h6 {
    color: white !important;
    direction: rtl !important;
    text-align: right !important;
}

.element-container {
    color: rgba(255, 255, 255, 0.9);
    direction: rtl !important;
}

[data-testid="column"] {
    direction: rtl !important;
}

::-webkit-scrollbar {
    width: 10px;
    height: 10px;
}

::-webkit-scrollbar-track {
    background: rgba(255, 255, 255, 0.03);
    border-radius: 5px;
}

::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    border-radius: 5px;
}

::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(180deg, #764ba2 0%, #f093fb 100%);
}

.form-container {
    background: linear-gradient(145deg, rgba(255,255,255,0.06) 0%, rgba(255,255,255,0.02) 100%);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 20px;
    padding: 2rem;
    margin-bottom: 2rem;
}

.stats-badge {
    display: inline-block;
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.2) 0%, rgba(240, 147, 251, 0.1) 100%);
    padding: 0.5rem 1rem;
    border-radius: 20px;
    font-size: 0.9rem;
    color: #a78bfa;
    margin: 0.25rem;
    border: 1px solid rgba(102, 126, 234, 0.3);
}

[data-testid="stVerticalBlock"] {
    direction: rtl !important;
}

.row-widget {
    direction: rtl !important;
}

.score-container {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    gap: 1rem;
    margin: 1.5rem 0;
}

.score-item {
    background: linear-gradient(145deg, rgba(255,255,255,0.08) 0%, rgba(255,255,255,0.02) 100%);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 16px;
    padding: 1.25rem;
    text-align: center;
    min-width: 120px;
    flex: 1;
}

.score-value {
    font-size: 2.5rem;
    font-weight: 900;
    background: linear-gradient(90deg, #667eea 0%, #f093fb 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.score-label {
    color: rgba(255,255,255,0.7);
    font-size: 0.9rem;
    margin-top: 0.5rem;
}

.image-preview {
    border-radius: 16px;
    border: 2px solid rgba(102, 126, 234, 0.3);
    overflow: hidden;
    margin: 1rem 0;
}

.stFileUploader > div {
    background: rgba(255, 255, 255, 0.03) !important;
    border: 2px dashed rgba(102, 126, 234, 0.4) !important;
    border-radius: 16px !important;
    padding: 2rem !important;
}

.stFileUploader > div:hover {
    border-color: #667eea !important;
    background: rgba(102, 126, 234, 0.05) !important;
}

.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    background: transparent;
}

.stTabs [data-baseweb="tab"] {
    background: rgba(255,255,255,0.05);
    border-radius: 12px 12px 0 0;
    padding: 0.75rem 1.5rem;
    color: rgba(255,255,255,0.7);
    border: 1px solid rgba(255,255,255,0.1);
    border-bottom: none;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.2) 0%, rgba(240, 147, 251, 0.1) 100%) !important;
    color: white !important;
    border-color: rgba(102, 126, 234, 0.4) !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-header">
    <h1>🇪🇬 وكيل التسويق المصري</h1>
    <p>تحليل المنافسين • استراتيجية تسويق كاملة • شعارات جذابة • تحليل صور المنتجات</p>
</div>
""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["🚀 تحليل البيزنس", "📸 تحليل صورة المنتج"])

with tab1:
    with st.form("business_form"):
        st.markdown('<div class="form-container">', unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            name = st.text_input(
                "📛 اسم البيزنس",
                placeholder="مثال: كافيه الحارة - قهوة مصرية أصيلة"
            )
        
        with col2:
            industry = st.text_input(
                "🏭 المجال",
                placeholder="مثال: مطاعم وكافيهات"
            )
        
        details = st.text_area(
            "📝 وصف البيزنس بالتفصيل",
            placeholder="اكتب وصف كامل عن البيزنس بتاعك:\n• إيه الخدمة أو المنتج؟\n• مين العملاء المستهدفين؟\n• إيه الأسعار؟\n• إيه الأهداف؟",
            height=200
        )
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        submitted = st.form_submit_button("🚀 شغّل الوكيل التسويقي")

if submitted:
    if not name and not details:
        st.warning("⚠️ لازم تكتب اسم البيزنس أو وصف على الأقل")
    else:
        business_info = f"{name}"
        if industry:
            business_info += f" - {industry}"
        if details:
            business_info += f". {details}"
        
        with st.spinner("🔄 جاري التحليل... البحث عن المنافسين وإنشاء الاستراتيجية"):
            try:
                results = agent.run_full_pipeline(business_info)
            except ValueError as e:
                st.error(f"❌ خطأ في الإعدادات: {e}")
                st.info("💡 تأكد من إضافة GOOGLE_API_KEY في ملف .env")
                st.stop()
        
        st.markdown('<div class="success-banner">✅ تم التحليل بنجاح! شوف النتايج تحت 👇</div>', unsafe_allow_html=True)
        
        col_main, col_side = st.columns([5, 3])
        
        with col_main:
            st.markdown("""
            <div class="card">
                <div class="card-header">
                    <h2>📊 الاستراتيجية التسويقية</h2>
                </div>
                <div class="card-content">
            """, unsafe_allow_html=True)
            st.markdown(results["strategy"])
            st.markdown("</div></div>", unsafe_allow_html=True)
            
            st.markdown("""
            <div class="card">
                <div class="card-header">
                    <h2>🔍 تحليل المنافسين</h2>
                </div>
                <div class="card-content">
            """, unsafe_allow_html=True)
            st.markdown(results["competitor_summary"])
            st.markdown("</div></div>", unsafe_allow_html=True)
            
            st.markdown("""
            <div class="card">
                <div class="card-header">
                    <h2>🔗 روابط المنافسين</h2>
                </div>
            """, unsafe_allow_html=True)
            for c in results["competitors"]:
                st.markdown(f"""
                <div class="competitor-link">
                    <a href="{c.get('href')}" target="_blank">🔗 {c.get('title')}</a>
                    <p>{c.get('body')[:180]}...</p>
                </div>
                """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        
        with col_side:
            st.markdown("""
            <div class="card">
                <div class="card-header">
                    <h2>💬 الشعارات التسويقية</h2>
                </div>
            """, unsafe_allow_html=True)
            
            catchphrases = results.get("catchphrases", [])
            if catchphrases:
                for phrase in catchphrases:
                    st.markdown(f'<div class="catchphrase-item">{phrase}</div>', unsafe_allow_html=True)
            else:
                st.warning("مفيش شعارات اتولدت")
            
            st.markdown("</div>", unsafe_allow_html=True)
            
            st.markdown("""
            <div class="card">
                <div class="card-header">
                    <h2>📋 انسخ الشعارات</h2>
                </div>
            """, unsafe_allow_html=True)
            all_phrases = "\n".join(catchphrases) if catchphrases else "مفيش شعارات"
            st.text_area("", value=all_phrases, height=220, label_visibility="collapsed")
            st.markdown("</div>", unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="form-container">', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        img_name = st.text_input(
            "📛 اسم البيزنس",
            placeholder="مثال: مشاوي الحارة",
            key="img_name"
        )
    
    with col2:
        img_industry = st.text_input(
            "🏭 المجال",
            placeholder="مثال: مطاعم",
            key="img_industry"
        )
    
    img_desc = st.text_area(
        "📝 وصف مختصر للبيزنس",
        placeholder="وصف سريع عن البيزنس عشان نقدر نقيم الصورة صح",
        height=100,
        key="img_desc"
    )
    
    uploaded_file = st.file_uploader(
        "📸 ارفع صورة المنتج أو اللوجو",
        type=["jpg", "jpeg", "png", "webp"],
        help="ارفع صورة للمنتج أو اللوجو أو أي صورة تسويقية عايز تحللها"
    )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    if uploaded_file is not None:
        col_img, col_analysis = st.columns([1, 2])
        
        with col_img:
            st.markdown("""
            <div class="card">
                <div class="card-header">
                    <h2>🖼️ الصورة المرفوعة</h2>
                </div>
            """, unsafe_allow_html=True)
            st.image(uploaded_file, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)
        
        if st.button("🔍 حلل الصورة", use_container_width=True):
            if not img_name:
                st.warning("⚠️ لازم تكتب اسم البيزنس الأول")
            else:
                with st.spinner("🔄 جاري تحليل الصورة..."):
                    image_bytes = uploaded_file.getvalue()
                    business_desc = f"{img_name} - {img_industry}. {img_desc}" if img_industry else f"{img_name}. {img_desc}"
                    
                    try:
                        result = tools.analyze_product_image(image_bytes, img_name, business_desc)
                    except Exception as e:
                        st.error(f"❌ حصل خطأ: {e}")
                        st.stop()
                
                with col_analysis:
                    st.markdown("""
                    <div class="card">
                        <div class="card-header">
                            <h2>📊 التقييمات</h2>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    scores = result.get("scores", {})
                    st.markdown(f"""
                    <div class="score-container">
                        <div class="score-item">
                            <div class="score-value">{scores.get('image_quality', 0)}</div>
                            <div class="score-label">جودة الصورة</div>
                        </div>
                        <div class="score-item">
                            <div class="score-value">{scores.get('brand_fit', 0)}</div>
                            <div class="score-label">التوافق مع البراند</div>
                        </div>
                        <div class="score-item">
                            <div class="score-value">{scores.get('social_ready', 0)}</div>
                            <div class="score-label">جاهزية السوشيال</div>
                        </div>
                        <div class="score-item">
                            <div class="score-value">{scores.get('overall', 0)}</div>
                            <div class="score-label">التقييم العام</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    st.markdown("</div>", unsafe_allow_html=True)
                
                st.markdown("""
                <div class="card">
                    <div class="card-header">
                        <h2>📝 التحليل الكامل</h2>
                    </div>
                    <div class="card-content">
                """, unsafe_allow_html=True)
                st.markdown(result.get("analysis", "مفيش تحليل"))
                st.markdown("</div></div>", unsafe_allow_html=True)

