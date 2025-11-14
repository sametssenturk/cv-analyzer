# 📄 CV Analyzer v1.0

CV'lerinizi yapay zeka ile analiz eden, güçlü/zayıf yönleri belirleyen, profesyonel cover letter oluşturan ve mülakat soruları üreten bir Streamlit uygulaması.

## 🖥️ Web Arayüzü
- Deploy Link: https://cv-analyzer-v1.streamlit.app/

## 🚀 Özellikler

### 🔍 CV Analizi
- **Güçlü Yönler**: CV'nizdeki öne çıkan özellikler
- **Zayıf Yönler**: Geliştirilebilecek alanlar
- **Teknik Beceriler**: Tespit edilen tüm teknik yetenekler
- **Genel Değerlendirme**: Kapsamlı bir özet
- **Öneriler**: CV'nizi geliştirmek için tavsiyeler
- **JSON Export**: Analiz sonuçlarını indirme

### ✉️ Cover Letter Üretimi
- İş ilanına özel motivasyon mektubu
- Profesyonel Türkçe dil
- UI'da direk görüntüleme
- 300-400 kelime arası optimal uzunluk

### 💼 Mülakat Soruları
- **Teknik Sorular**: CV'nizdeki teknolojilere özel
- **Davranışsal Sorular**: Deneyimlerinizi değerlendiren
- **Genel Sorular**: Pozisyona uygunluk soruları
- Her soru için amaç açıklaması
- JSON formatında indirme

## 🛠️ Teknolojiler

- **Python 3.8+**
- **Streamlit**: Web arayüzü
- **Google Gemini 2.5 Flash**: LLM API
- **PyPDF2**: PDF okuma
- **python-dotenv**: Ortam değişkenleri

## 📦 Kurulum

### 1. Repoyu Klonlayın veya İndirin

```bash
git clone <repo-url>
cd cv-analyzer
```

### 2. Sanal Ortam Oluşturun (Önerilen)

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Gerekli Paketleri Yükleyin

```powershell
pip install -r requirements.txt
```

### 4. API Anahtarını Yapılandırın

`.env.example` dosyasını `.env` olarak kopyalayın:

```powershell
Copy-Item .env.example .env
```

`.env` dosyasını düzenleyin ve Gemini API anahtarınızı ekleyin:

```env
GEMINI_API_KEY=your_actual_api_key_here
```

**Gemini API Anahtarı Nasıl Alınır?**
1. [Google AI Studio](https://makersuite.google.com/app/apikey) adresine gidin
2. Google hesabınızla giriş yapın
3. "Get API Key" butonuna tıklayın
4. Oluşturulan anahtarı kopyalayın

## 🎯 Kullanım

### Uygulamayı Başlatın

```powershell
streamlit run app.py
```

Tarayıcınızda otomatik olarak `http://localhost:8501` adresi açılacaktır.

### Adım Adım Kullanım

1. **CV Yükleme**
   - Sol taraftaki sidebar'dan "Browse files" butonuna tıklayın
   - PDF veya TXT formatında CV'nizi seçin
   - Dosya otomatik olarak yüklenecektir

2. **CV Analizi**
   - "🔍 CV Analizi" sekmesine gidin
   - "🚀 Analiz Başlat" butonuna tıklayın
   - Sonuçları görüntüleyin ve JSON olarak indirin

3. **Cover Letter Oluşturma**
   - "✉️ Cover Letter" sekmesine gidin
   - İş ilanı açıklamasını metin kutusuna yapıştırın
   - "📝 Cover Letter Oluştur" butonuna tıklayın
   - Oluşturulan mektubu UI'da görüntüleyin

4. **Mülakat Soruları**
   - "💼 Mülakat Soruları" sekmesine gidin
   - "❓ Soru Üret" butonuna tıklayın
   - Soruları kategorilere göre inceleyin
   - JSON olarak indirin

## 📁 Proje Yapısı

```
cv-analyzer/
├── app.py                 # Ana Streamlit uygulaması
├── requirements.txt       # Python bağımlılıkları
├── .env.example          # Ortam değişkenleri şablonu
├── README.md             # Bu dosya
│
└── utils/                # Yardımcı modüller
    ├── __init__.py
    ├── extract.py        # PDF/TXT okuma fonksiyonları
    ├── llm.py           # Gemini API entegrasyonu
    └── analysis.py      # Analiz ve üretim fonksiyonları
```

## 🔧 Yapılandırma

### Gemini Model Değiştirme

`utils/llm.py` dosyasında model adını değiştirebilirsiniz:

```python
model = genai.GenerativeModel('gemini-2.0-flash-exp')
# veya
model = genai.GenerativeModel('gemini-pro')
```

### Cover Letter Uzunluğu

`utils/llm.py` dosyasındaki `llm_cover_letter` fonksiyonunda prompt'u düzenleyebilirsiniz:

```python
Cover letter Türkçe olmalı, profesyonel bir dil kullanmalı ve 300-400 kelime arasında olmalı.
```

## ⚠️ Notlar

- API çağırıları internet bağlantısı gerektirir
- Gemini API ücretsiz kotası sınırlıdır
- Büyük PDF dosyaları işlem süresini artırabilir
- **Streamlit Cloud'a deploy edilebilir** - Dosya sistemi kullanmıyor, tamamen bellekten çalışıyor

## 🐛 Sorun Giderme

### "GEMINI_API_KEY bulunamadı" Hatası
- `.env` dosyasının proje kök dizininde olduğundan emin olun
- API anahtarının doğru girildiğini kontrol edin
- Uygulamayı yeniden başlatın

### PDF Okuma Hatası
- PDF'in şifreli olmadığından emin olun
- Dosya boyutunun 10MB'dan küçük olduğunu kontrol edin
- TXT formatını deneyin

### Streamlit Başlamıyor
- Port 8501'in kullanımda olmadığını kontrol edin
- Farklı bir port kullanın: `streamlit run app.py --server.port 8502`

## 📝 Lisans

Bu proje eğitim amaçlıdır ve özgürce kullanılabilir.

## 👤 Geliştirici

CV Analyzer v1.0 - 2025

---

**Not**: Bu uygulama Google Gemini API kullanmaktadır. API kullanım koşullarına uygun şekilde kullanınız.
