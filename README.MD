# Türkiye Yol Ücretleri ve Rota Planlama Projesi

## Proje Tanımı

Bu proje, Türkiye'deki şehirler arası yolculuklar için güzergah planlaması ve yol ücretlerinin hesaplanmasını sağlayan bir web uygulamasıdır. Kullanıcılar, başlangıç ve varış noktalarını, araç sınıfını ve yol tercihlerini seçerek, en uygun rotayı ve geçiş ücretlerini öğrenebilirler. Ayrıca, yolculuk noktalarındaki güncel hava durumu bilgileri de sunulmaktadır.

## Özellikler

- Şehirler arası güzergah ve yol ücreti hesaplama
- Araç sınıfına göre ücretlendirme
- Kullanıcı tercihlerine göre rota özelleştirme (ücretli yol kullanmama, hızlı yol, yakıt ekonomisi)
- Başlangıç ve varış noktası için anlık hava durumu gösterimi (OpenWeatherMap API)
- Google Gemini API ile doğal dilde rota ve ücret açıklaması
- Modern ve kullanıcı dostu arayüz (Bootstrap ile responsive tasarım)

## Kullanılan Teknolojiler

- **Backend:** Django 5.1.4 (Python)
- **Frontend:** HTML, CSS (Bootstrap), JavaScript
- **API Entegrasyonları:** Google Gemini (LLM), OpenWeatherMap
- **Veritabanı:** SQLite3

## Literatür Özeti

Yol ücretleri ve rota planlama sistemleri, ulaşım mühendisliği ve akıllı şehir uygulamalarında önemli bir yer tutar. Literatürde, güzergah optimizasyonu için çeşitli algoritmalar (Dijkstra, A*, Yeniden Ağırlıklandırılmış Kısa Yol vb.) kullanılırken, son yıllarda yapay zeka tabanlı yaklaşımlar da öne çıkmaktadır. Özellikle, kullanıcı tercihlerinin doğal dilde alınması ve işlenmesi için büyük dil modelleri (LLM) kullanılmaya başlanmıştır. Bu proje, Google Gemini gibi bir LLM ile kullanıcıdan alınan doğal dil girdilerini işleyerek, kişiselleştirilmiş ve anlaşılır rota/ücret çıktıları üretmektedir.

Ayrıca, yolculuk planlamasında hava durumu bilgisinin entegrasyonu, sürüş güvenliği ve konforu açısından önemlidir. OpenWeatherMap gibi servisler, gerçek zamanlı hava durumu verisi sağlayarak, güzergah planlamasını daha bilinçli hale getirir.

## Kurulum ve Çalıştırma

1. Gerekli bağımlılıkları yükleyin:
    ```sh
    pip install -r requirements.txt
    ```
2. Veritabanı migrasyonlarını uygulayın:
    ```sh
    python manage.py migrate
    ```
3. Sunucuyu başlatın:
    ```sh
    python manage.py runserver
    ```
4. Tarayıcıdan `http://127.0.0.1:8000/` adresine gidin.

## Dosya Yapısı

- `bbc_llm_proje/` : Django ana projesi
- `yol/` : Uygulama dosyaları (views, urls, templates)
- `static/` : Statik dosyalar (CSS, JS)
- `db.sqlite3` : Veritabanı dosyası

