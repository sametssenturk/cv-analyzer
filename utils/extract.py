"""
CV dosyalarından metin çıkarma modülü
PDF ve TXT formatlarını destekler
"""

import PyPDF2
from typing import Optional


def read_pdf(file) -> Optional[str]:
    """
    PDF dosyasından metin çıkarır
    
    Args:
        file: Streamlit tarafından yüklenen dosya objesi
        
    Returns:
        str: Çıkarılan metin içeriği veya None
    """
    try:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        
        # Tüm sayfaları oku
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        
        return text.strip()
    
    except Exception as e:
        print(f"PDF okuma hatası: {e}")
        return None


def read_txt(file) -> Optional[str]:
    """
    TXT dosyasından metin çıkarır
    
    Args:
        file: Streamlit tarafından yüklenen dosya objesi
        
    Returns:
        str: Dosya içeriği veya None
    """
    try:
        # Dosyayı string olarak oku
        text = file.read().decode("utf-8")
        return text.strip()
    
    except Exception as e:
        print(f"TXT okuma hatası: {e}")
        return None


def extract_text_from_file(file) -> Optional[str]:
    """
    Dosya tipine göre uygun okuma fonksiyonunu çağırır
    
    Args:
        file: Streamlit tarafından yüklenen dosya objesi
        
    Returns:
        str: Çıkarılan metin içeriği veya None
    """
    if file.name.endswith('.pdf'):
        return read_pdf(file)
    elif file.name.endswith('.txt'):
        return read_txt(file)
    else:
        print("Desteklenmeyen dosya formatı")
        return None
