from django.shortcuts import render
import google.generativeai as genai
from django.http import JsonResponse
from google import genai


client = genai.Client(api_key="API_KEY_HERE")  # Replace with your actual API key

def index(request):
    return render(request, 'yol/index.html')

def send_gemini_message(history_data, user_message):
    contents = [
        {"role": "user", "parts": [{"text": history_data}]},
        {"role": "user", "parts": [{"text": user_message}]}
    ]

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=contents,
    )

    return response.text


def sorgula(request):
    if request.method == 'POST':
        departure = request.POST.get('departure')
        arrival = request.POST.get('arrival')
        vehicle_class = request.POST.get('vehicle_class')
        fuel_economy = request.POST.get('fuel_economy', '')
        paid_roads = request.POST.get('paid_roads', 'false') == 'true'
        fast_routes = request.POST.get('fast_routes', 'false') == 'true'
        fuel_efficient = request.POST.get('fuel_efficient', 'false') == 'true'
        question = request.POST.get('question', '')
        
        # Tercihleri açıklamaya dönüştür
        preferences = []
        if not paid_roads:
            preferences.append("ücretli yolları tercih et")
        if fast_routes:
            preferences.append("en hızlı yolu tercih et")
        if fuel_efficient:
            preferences.append("yakıt tasarrufu sağlayan rotayı tercih et")
        if fuel_economy:
            preferences.append(f"yakıt tüketimi {fuel_economy} L/100km olarak hesapla")
            
        preferences_text = ", ".join(preferences) if preferences else "standart tercihler"
        
        full_question = (
            f"{departure} şehrinden {arrival} şehrine gideceğim. "
            f"Araç sınıfım: {vehicle_class}. "
            f"Tercihlerim: {preferences_text}. "
            f"{'Ek notlarım: ' + question if question else ''} "
            "Bu bilgilere göre [Geçilecek Yollar: Geçiş Ücretleri] şeklinde çıktı ver."
        )
        
        csv_data = """
                Geçiş Noktası,1. Sınıf (TL),2. Sınıf (TL),3. Sınıf (TL),4. Sınıf (TL),5. Sınıf (TL),6. Sınıf (TL)
    1915 Çanakkale Köprüsü,795,990,1780,1975,3755,200
    Osmangazi Köprüsü,795,1270,1510,2005,2530,555
    Yavuz Sultan Selim Köprüsü,80,110,200,510,630,55
    Fatih Sultan Mehmet Köprüsü,47,60,134,265,351,20
    15 Temmuz Şehitler Köprüsü,47,60,134,265,351,20
    KMO Avrupa - Kınalı,175,280,325,425,535,130
    KMO Avrupa - Silivri,150,235,280,360,455,110
    KMO Avrupa - Çatalca,110,150,175,235,290,70
    KMO Avrupa - Yassıören,150,210,250,330,455,110
    KMO Avrupa - Tayakadın,175,250,325,405,505,130
    KMO Avrupa - Mahmutbey,100,135,175,230,300,60
    KMO Avrupa - Riva,130,180,240,315,400,85
    KMO Anadolu - Kurnaköy,405,486,650,842,1010,162
    KMO Anadolu - İstanbul Park,45,54,72,93,112,18
    KMO Anadolu - İzmit Kuzey,210,252,336,433,520,84
    KMO Anadolu - Adapazarı-1,325,390,520,671,804,130
    KMO Anadolu - Sevindikli,150,180,240,309,371,60
    KMO Anadolu - Akmeşe,280,336,448,578,693,112
    KMO Anadolu - Karasu,330,396,528,682,817,132
    KMO Anadolu - TEM Akyazı,405,486,650,842,1010,162
    KMO Anadolu - Paşaköy,160,210,270,340,430,95
    KMO Anadolu - Kartepe (İzmit Doğu),210,252,336,433,520,84
    Anadolu Otoyolu - İstanbul (Çamlıca),22,25,31,40,64,8
    Anadolu Otoyolu - Şekerpınar,27,31,36,64,82,11
    Anadolu Otoyolu - Gebze,27,31,36,64,82,11
    Anadolu Otoyolu - İzmit Doğu,40,45,82,107,142,18
    Anadolu Otoyolu - Adapazarı,49,67,93,142,149,20
    Anadolu Otoyolu - Düzce,74,86,142,176,209,29
    Anadolu Otoyolu - Bolu,160,191,254,325,412,64
    Anadolu Otoyolu - Gerede,180,205,287,347,416,74
    Anadolu Otoyolu - Ankara (Şaşmaz),187,216,289,374,449,75
    Gebze-İzmir Otoyolu (Orhangazi),135,200,260,345,440,100
    Gebze-İzmir Otoyolu (Gemlik),180,250,310,410,510,120
    Gebze-İzmir Otoyolu (Bursa Doğu),210,300,380,510,640,140
    Gebze-İzmir Otoyolu (Balıkesir),350,470,620,800,1000,220
    Gebze-İzmir Otoyolu (Manisa),450,600,780,1000,1250,280
    Gebze-İzmir Otoyolu (İzmir),500,700,910,1170,1460,300
    Ankara-Niğde Otoyolu (Gölbaşı),135,190,245,310,400,90
    Ankara-Niğde Otoyolu (Şereflikoçhisar),200,280,370,470,600,135
    Ankara-Niğde Otoyolu (Aksaray),280,400,530,680,860,190
    Ankara-Niğde Otoyolu (Niğde),350,500,660,850,1070,230
    Malkara – Çanakkale Otoyolu (Malkara),120,170,230,310,395,90
    Malkara – Çanakkale Otoyolu (Gelibolu),150,210,280,370,460,110
    Malkara – Çanakkale Otoyolu (Lapseki),175,240,320,420,520,125
    Menemen-Aliağa-Çandarlı Otoyolu,150,220,310,400,500,120
    Avrasya Tüneli,225,337,Yok,Yok,Yok,175
    Zigana Tüneli,90,150,220,400,Yok,60
    Ovit Tüneli,0,0,0,0,0,0
    Bolu Dağı Tüneli (0),0,0,0,0,0,0
    E-5 Karayolu,0,0,0,0,0,0
    D-100 Karayolu,0,0,0,0,0,0
    D-650 Karayolu,0,0,0,0,0,0

        """
        
        response = send_gemini_message(csv_data, full_question)
        return JsonResponse({'response': response})
    
    return JsonResponse({'error': 'Geçersiz istek'}, status=400)