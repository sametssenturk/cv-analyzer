"""
Gemini LLM entegrasyon modülü
Google Gemini 2.5 Flash API ile iletişim kurar
"""

import os
import google.generativeai as genai
from typing import Optional
from dotenv import load_dotenv

# .env dosyasından API anahtarını yükle
load_dotenv()

# Streamlit secrets desteği
try:
    import streamlit as st
    STREAMLIT_AVAILABLE = True
except ImportError:
    STREAMLIT_AVAILABLE = False


def gemini_client() -> Optional[genai.GenerativeModel]:
    """
    Gemini API istemcisini yapılandırır ve döndürür
    Önce Streamlit secrets'ı kontrol eder, sonra .env dosyasına bakar
    
    Returns:
        GenerativeModel: Yapılandırılmış Gemini model objesi
    """
    try:
        # Önce Streamlit secrets'ı dene (Cloud deployment için)
        if STREAMLIT_AVAILABLE and hasattr(st, 'secrets'):
            try:
                api_key = st.secrets.get("GEMINI_API_KEY")
            except:
                api_key = None
        else:
            api_key = None
        
        # Streamlit'te yoksa, environment variable'ı kullan
        if not api_key:
            api_key = os.getenv("GEMINI_API_KEY")
        
        if not api_key:
            raise ValueError("GEMINI_API_KEY bulunamadı. Lütfen .env dosyasını veya Streamlit secrets'ı kontrol edin.")
        
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        return model
    
    except Exception as e:
        print(f"Gemini client hatası: {e}")
        return None


def llm_analyze(text: str) -> Optional[str]:
    """
    CV metnini analiz eder ve güçlü/zayıf yönleri belirler
    
    Args:
        text: Analiz edilecek CV metni
        
    Returns:
        str: Analiz sonuçları (JSON formatında)
    """
    try:
        model = gemini_client()
        if not model:
            return None
        
        prompt = f"""
        Aşağıdaki CV'yi detaylı analiz et ve şu formatta JSON yanıtı ver:
        
        {{
            "güçlü_yönler": ["yön1", "yön2", ...],
            "zayıf_yönler": ["yön1", "yön2", ...],
            "teknik_beceriler": ["beceri1", "beceri2", ...],
            "genel_değerlendirme": "kısa değerlendirme metni",
            "öneriler": ["öneri1", "öneri2", ...]
        }}
        
        CV Metni:
        {text}
        
        NOT: Sadece JSON formatında yanıt ver, başka açıklama ekleme.
        """
        
        response = model.generate_content(prompt)
        return response.text
    
    except Exception as e:
        print(f"LLM analiz hatası: {e}")
        return None


def llm_cover_letter(text: str, job_desc: str) -> Optional[str]:
    """
    CV ve iş ilanına göre cover letter oluşturur
    
    Args:
        text: CV metni
        job_desc: İş ilanı açıklaması
        
    Returns:
        str: Oluşturulan cover letter metni
    """
    try:
        model = gemini_client()
        if not model:
            return None
        
        prompt = f"""
        Aşağıdaki CV ve iş ilanına göre profesyonel bir cover letter (motivasyon mektubu) yaz.
        
        Cover letter Türkçe olmalı, profesyonel bir dil kullanmalı ve 300-400 kelime arasında olmalı.
        
        Adayın CV'sindeki güçlü yönleri ve iş ilanındaki gereksinimler arasında bağlantı kur.
        
        CV:
        {text}
        
        İş İlanı:
        {job_desc}
        
        NOT: Sadece cover letter metnini ver, başlık veya ek açıklama ekleme.
        """
        
        response = model.generate_content(prompt)
        return response.text
    
    except Exception as e:
        print(f"Cover letter oluşturma hatası: {e}")
        return None


def llm_interview_questions(text: str) -> Optional[str]:
    """
    CV'ye göre mülakat soruları oluşturur
    
    Args:
        text: CV metni
        
    Returns:
        str: Mülakat soruları (JSON formatında)
    """
    try:
        model = gemini_client()
        if not model:
            return None
        
        prompt = f"""
        Aşağıdaki CV'ye göre mülakat soruları oluştur. Sorular adayın deneyimi ve becerilerine uygun olmalı.
        
        Şu formatta JSON yanıtı ver:
        
        {{
            "teknik_sorular": [
                {{"soru": "soru metni", "amaç": "sorunun amacı"}},
                ...
            ],
            "davranışsal_sorular": [
                {{"soru": "soru metni", "amaç": "sorunun amacı"}},
                ...
            ],
            "genel_sorular": [
                {{"soru": "soru metni", "amaç": "sorunun amacı"}},
                ...
            ]
        }}
        
        CV Metni:
        {text}
        
        NOT: Her kategoride en az 5 soru üret. Sadece JSON formatında yanıt ver.
        """
        
        response = model.generate_content(prompt)
        return response.text
    
    except Exception as e:
        print(f"Mülakat soruları oluşturma hatası: {e}")
        return None
