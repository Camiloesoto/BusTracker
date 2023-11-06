let map;
function initpam(){
    const colCoords = {lat: 4.57, lng:-74.29};
    const map = new google.maps.Map(mapDiv, {
        center: colCoords,
        zoom: 6,
    });
    const marker = new google.maps.Marker({
        position: colCoords,
        map,
    });

    button2.addEventListener('click', ()=>{
        const coords2 = {
            lat: 6.200271, 
            lng: -75.577620
        };
        map.setCenter(coords2);
        map.setZoom(17);
        marker.setPosition(coords2);
    })

    button3.addEventListener('click', ()=>{
        const coords3 = {
            lat: 6.214070, 
            lng: -75.576224
        };
        const marker = new google.maps.Marker({
            position: coords3,
            map,
            icon:"./icons/icon_bus.png"
        })
        google.maps.event.addEventListener(marker,"click",()=>{
            map.setCenter(coords3);
            map.setZoom(17);
        });
    })

    button.addEventListener('click', ()=>{
        if(navigator.geolocation){
            navigator.geolocation.getCurrentPosition(
                (position)=>{
                    const coords = {
                        lat: position.coords.latitude,
                        lng: position.coords.longitude
                    };
                    console.log(coords);
                    map.setCenter(coords);
                    map.setZoom(17);
                    marker.setPosition(coords);  
                    var origin1 = new google.maps.LatLng(coords[0], coords[1]);
                    var destination1 = new google.maps.LatLng(6.200271, -75.577620);  
                    var service = new google.maps.DistanceMatrixService();
                    service.getDistanceMatrix(
                    {
                        origins: [origin1],
                        destinations: [destination1],
                        travelMode: 'WALKING',
                    }, callback);
                    console.log(callback);
                }, 
                ()=>{
                    alert('Tu navegador esta bien, pero ocurrio algun problema')
                }
            );
        }else{
            alert(
                "Tu navegador no dispone de la geolocalizacion, actualizalo para continuar"
            );
        }
    })

}