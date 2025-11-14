"""
CV analiz ve içerik üretme fonksiyonları
LLM modülünü kullanarak yüksek seviye analiz işlemleri yapar
"""

import json
from typing import Dict, Optional
from utils.llm import llm_analyze, llm_cover_letter, llm_interview_questions


def analyze_cv(text: str) -> Optional[Dict]:
    """
    CV metnini analiz eder ve yapılandırılmış sonuç döndürür
    
    Args:
        text: CV metni
        
    Returns:
        dict: Analiz sonuçları (güçlü/zayıf yönler, beceriler vb.)
    """
    try:
        # LLM'den analiz al
        result = llm_analyze(text)
        
        if not result:
            return None
        
        # JSON'u parse et
        # Bazen LLM markdown code block ile sarabilir, temizle
        if "```json" in result:
            result = result.split("```json")[1].split("```")[0]
        elif "```" in result:
            result = result.split("```")[1].split("```")[0]
        
        analysis = json.loads(result.strip())
        return analysis
    
    except json.JSONDecodeError as e:
        print(f"JSON parse hatası: {e}")
        print(f"Ham yanıt: {result}")
        return None
    
    except Exception as e:
        print(f"CV analiz hatası: {e}")
        return None


def generate_cover_letter(text: str, job_desc: str) -> Optional[str]:
    """
    Cover letter (motivasyon mektubu) oluşturur
    
    Args:
        text: CV metni
        job_desc: İş ilanı açıklaması
        
    Returns:
        str: Cover letter metni
    """
    try:
        cover_letter = llm_cover_letter(text, job_desc)
        
        if not cover_letter:
            return None
        
        # Markdown formatını temizle
        cover_letter = cover_letter.replace("```", "").strip()
        
        return cover_letter
    
    except Exception as e:
        print(f"Cover letter üretme hatası: {e}")
        return None


def generate_interview_questions(text: str) -> Optional[Dict]:
    """
    Mülakat soruları oluşturur
    
    Args:
        text: CV metni
        
    Returns:
        dict: Mülakat soruları (teknik, davranışsal, genel)
    """
    try:
        # LLM'den sorular al
        result = llm_interview_questions(text)
        
        if not result:
            return None
        
        # JSON'u parse et
        if "```json" in result:
            result = result.split("```json")[1].split("```")[0]
        elif "```" in result:
            result = result.split("```")[1].split("```")[0]
        
        questions = json.loads(result.strip())
        return questions
    
    except json.JSONDecodeError as e:
        print(f"JSON parse hatası: {e}")
        print(f"Ham yanıt: {result}")
        return None
    
    except Exception as e:
        print(f"Mülakat soruları üretme hatası: {e}")
        return None
