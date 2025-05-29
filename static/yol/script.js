async function getWeather(city, elementId) {
    const apiKey = 'API_KEYİNİZİ_BURAYA_YAZIN'; // OpenWeatherMap API anahtarınız
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${city},TR&appid=${apiKey}&units=metric&lang=tr`;

    try {
        const response = await fetch(url);
        const data = await response.json();
        if (data.cod === 200) {
            document.getElementById(elementId).innerHTML = `
                <div class="alert alert-info mb-2">
                    <strong>${data.name}:</strong> ${data.weather[0].description}, ${Math.round(data.main.temp)}°C
                </div>
            `;
        } else {
            document.getElementById(elementId).innerHTML = `<div class="alert alert-warning">Hava durumu alınamadı.</div>`;
        }
    } catch (error) {
        document.getElementById(elementId).innerHTML = `<div class="alert alert-danger">Hata oluştu.</div>`;
    }
}

// Örnek: Formdan şehir seçildiğinde çağırabilirsiniz
getWeather('Ankara', 'weather1');
getWeather('İstanbul', 'weather2');