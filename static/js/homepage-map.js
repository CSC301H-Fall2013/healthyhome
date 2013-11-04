google.maps.event.addDomListener(window, 'load', initialize);

function initialize() {

    var bounds = new google.maps.LatLngBounds();
    var mapOptions = {
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        disableDefaultUI: true,
        panControl: true,
        zoomControl: true
    }
    var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
    var categoryMap = {};

    //TODO: replace mock data with API call
    var buildingList = [
        {
            "lat": 43.667576,
            "lng": -79.391868,
            "id": "1",
            "title": "building1",
            "categories": ["Bedbugs", "Mice"]
        },
        {
            "lat": 43.663991,
            "lng": -79.398580,
            "id": "2",
            "title": "building2",
            "categories": ["Leakage"]
        },
        {
            "lat": 43.651230,
            "lng": -79.409866,
            "id": "3",
            "title": "building3",
            "categories": ["Leakage"]

        },
        {
            "lat": 43.665326,
            "lng": -79.411154,
            "id": "4",
            "title": "building4",
            "categories": ["Mice"]
        },
        {
            "lat": 43.775326,
            "lng": -79.411154,
            "id": "5",
            "title": "building5",
            "categories" : ["Bedbugs"]
        }
    ];

    //Place buildings on the map
    buildingList.forEach(function (building) {
        var latLong = new google.maps.LatLng(building.lat, building.lng);
        bounds.extend(latLong);
        var marker = new google.maps.Marker({
            position: latLong,
            map: map,
            title: building.title
        });
        google.maps.event.addListener(marker, 'click', function () {
            window.location = "/building/" + building.id;
        });
        building.categories.forEach(function(category) {
            if(categoryMap[category]) {
                categoryMap[category].push(marker);
            } else {
                categoryMap[category] = [marker];
            }
        });
    });
    
    // Create the container for checkboxes
    var categoryContainer = $('<div/>', {
            id: 'categoryContainer',
            label: "Selectors",
            'class': 'item gradient rounded shadow'
        }).appendTo('#map-canvas');

    //Create category filter for each category
    Object.keys(categoryMap).forEach(function(category) {
        var label = $('<label/>', {
            'class' : "category"
        });

        var checkbox = $('<input/>', {
            'class': "categoryCheckbox",
            type: "checkbox",
            value: category,
            checked: true
        });

        label.append(checkbox, category);
        label.appendTo(categoryContainer);
    });

    map.fitBounds(bounds);
    map.panToBounds(bounds);
}
