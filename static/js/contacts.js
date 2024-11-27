function initMap() {
    var location = { lat: 55.7558, lng: 37.6173 }; // Координаты Москвы

    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 12,
        center: location
    });

    var marker = new google.maps.Marker({
        position: location,
        map: map,
        title: 'Мы здесь!'
    });
}