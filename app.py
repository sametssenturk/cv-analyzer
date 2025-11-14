"""
CV Analyzer v1.0
PDF/TXT CV dosyalarını analiz eden, cover letter üreten ve mülakat soruları hazırlayan Streamlit uygulaması
"""

import streamlit as st
import json
from utils.extract import extract_text_from_file
from utils.analysis import (
    analyze_cv, 
    generate_cover_letter, 
    generate_interview_questions
)


# Sayfa yapılandırması
st.set_page_config(
    page_title="CV Analyzer v1",
    page_icon="📄",
    layout="wide"
)


def main():
    """Ana uygulama fonksiyonu"""
    
    # Başlık
    st.title("📄 CV Analyzer v1.0")
    st.markdown("---")
    st.markdown("**CV'nizi yükleyin ve yapay zeka ile analiz edin!**")
    st.markdown("")
    
    # Sidebar - Dosya yükleme
    with st.sidebar:
        st.header("📂 CV Yükle")
        
        uploaded_file = st.file_uploader(
            "PDF veya TXT formatında CV yükleyin",
            type=['pdf', 'txt'],
            help="Maksimum 10MB"
        )
        
        st.markdown("---")
        st.markdown("### ℹ️ Hakkında")
        st.info(
            "Bu uygulama Gemini 2.5 Flash API kullanarak CV'nizi analiz eder, "
            "güçlü ve zayıf yönlerinizi belirler, cover letter oluşturur ve "
            "mülakat soruları üretir."
        )
    
    # Ana içerik
    if uploaded_file is not None:
        # Dosyadan metin çıkar
        with st.spinner("📖 CV okunuyor..."):
            cv_text = extract_text_from_file(uploaded_file)
        
        if cv_text:
            st.success(f"✅ CV başarıyla yüklendi! ({len(cv_text)} karakter)")
            
            # CV önizleme (isteğe bağlı)
            with st.expander("📋 CV Önizleme"):
                st.text_area("CV İçeriği", cv_text, height=200, disabled=True)
            
            st.markdown("---")
            
            # Sekmeler
            tab1, tab2, tab3 = st.tabs([
                "🔍 CV Analizi", 
                "✉️ Cover Letter", 
                "💼 Mülakat Soruları"
            ])
            
            # TAB 1: CV ANALİZİ
            with tab1:
                st.header("🔍 CV Analizi")
                
                if st.button("🚀 Analiz Başlat", key="analyze_btn", type="primary"):
                    with st.spinner("🤖 CV analiz ediliyor..."):
                        analysis = analyze_cv(cv_text)
                    
                    if analysis:
                        st.success("✅ Analiz tamamlandı!")
                        
                        # Sonuçları göster
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            st.subheader("💪 Güçlü Yönler")
                            for item in analysis.get("güçlü_yönler", []):
                                st.markdown(f"- ✅ {item}")
                        
                        with col2:
                            st.subheader("⚠️ Zayıf Yönler")
                            for item in analysis.get("zayıf_yönler", []):
                                st.markdown(f"- ⚠️ {item}")
                        
                        st.markdown("---")
                        
                        st.subheader("🛠️ Teknik Beceriler")
                        skills = analysis.get("teknik_beceriler", [])
                        st.write(", ".join(skills))
                        
                        st.markdown("---")
                        
                        st.subheader("📝 Genel Değerlendirme")
                        st.info(analysis.get("genel_değerlendirme", ""))
                        
                        st.markdown("---")
                        
                        st.subheader("💡 Öneriler")
                        for item in analysis.get("öneriler", []):
                            st.markdown(f"- 💡 {item}")
                        
                        # JSON indirme butonu
                        st.markdown("---")
                        json_data = json.dumps(analysis, ensure_ascii=False, indent=2)
                        st.download_button(
                            label="📥 Analizi JSON olarak indir",
                            data=json_data,
                            file_name="cv_analysis.json",
                            mime="application/json"
                        )
                    else:
                        st.error("❌ Analiz sırasında bir hata oluştu. Lütfen tekrar deneyin.")
            
            # TAB 2: COVER LETTER
            with tab2:
                st.header("✉️ Cover Letter Oluştur")
                
                job_description = st.text_area(
                    "İş İlanı Açıklaması",
                    height=200,
                    placeholder="İş ilanının açıklamasını buraya yapıştırın...",
                    help="Cover letter'ın iş ilanına özel oluşturulması için gereklidir"
                )
                
                if st.button("📝 Cover Letter Oluştur", key="cover_btn", type="primary"):
                    if not job_description.strip():
                        st.warning("⚠️ Lütfen iş ilanı açıklamasını girin!")
                    else:
                        with st.spinner("✍️ Cover letter oluşturuluyor..."):
                            cover_letter = generate_cover_letter(cv_text, job_description)
                        
                        if cover_letter:
                            st.success("✅ Cover letter oluşturuldu!")
                            
                            # Cover letter'ı göster
                            st.markdown("### 📄 Oluşturulan Cover Letter")
                            st.markdown("---")
                            st.write(cover_letter)
                        else:
                            st.error("❌ Cover letter oluşturulurken bir hata oluştu.")
            
            # TAB 3: MÜLAKAT SORULARI
            with tab3:
                st.header("💼 Mülakat Soruları")
                
                if st.button("❓ Soru Üret", key="questions_btn", type="primary"):
                    with st.spinner("🤔 Mülakat soruları hazırlanıyor..."):
                        questions = generate_interview_questions(cv_text)
                    
                    if questions:
                        st.success("✅ Sorular oluşturuldu!")
                        
                        # Teknik sorular
                        st.subheader("💻 Teknik Sorular")
                        for i, q in enumerate(questions.get("teknik_sorular", []), 1):
                            with st.expander(f"Soru {i}: {q.get('soru', '')}"):
                                st.markdown(f"**Amaç:** {q.get('amaç', '')}")
                        
                        st.markdown("---")
                        
                        # Davranışsal sorular
                        st.subheader("🧠 Davranışsal Sorular")
                        for i, q in enumerate(questions.get("davranışsal_sorular", []), 1):
                            with st.expander(f"Soru {i}: {q.get('soru', '')}"):
                                st.markdown(f"**Amaç:** {q.get('amaç', '')}")
                        
                        st.markdown("---")
                        
                        # Genel sorular
                        st.subheader("📋 Genel Sorular")
                        for i, q in enumerate(questions.get("genel_sorular", []), 1):
                            with st.expander(f"Soru {i}: {q.get('soru', '')}"):
                                st.markdown(f"**Amaç:** {q.get('amaç', '')}")
                        
                        # JSON indirme butonu
                        st.markdown("---")
                        json_data = json.dumps(questions, ensure_ascii=False, indent=2)
                        st.download_button(
                            label="📥 Soruları JSON olarak indir",
                            data=json_data,
                            file_name="interview_questions.json",
                            mime="application/json"
                        )
                    else:
                        st.error("❌ Sorular oluşturulurken bir hata oluştu.")
        
        else:
            st.error("❌ CV okunamadı. Lütfen geçerli bir PDF veya TXT dosyası yükleyin.")
    
    else:
        # Karşılama ekranı
        st.info("👈 Başlamak için sol taraftan bir CV dosyası yükleyin.")
        
        st.markdown("### 🚀 Özellikler")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            #### 🔍 CV Analizi
            - Güçlü yönler
            - Zayıf yönler
            - Teknik beceriler
            - Öneriler
            """)
        
        with col2:
            st.markdown("""
            #### ✉️ Cover Letter
            - İş ilanına özel
            - Profesyonel dil
            - PDF/TXT indirme
            """)
        
        with col3:
            st.markdown("""
            #### 💼 Mülakat Soruları
            - Teknik sorular
            - Davranışsal sorular
            - Genel sorular
            """)


if __name__ == "__main__":
    main()
