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
    var checkedCategories = {};

    // Get buildings from the API
    $.getJSON('/api/v1/buildings', function(data) {onGetJSON(data, bounds, map, categoryMap, checkedCategories)});
}

function onGetJSON(buildingList, bounds, map, categoryMap, checkedCategories) {
    //Place buildings on the map
    buildingList.forEach(function (building) {
        var latLong = new google.maps.LatLng(building.lat, building.lng);
        bounds.extend(latLong);
        var marker = new google.maps.Marker({
            position: latLong,
            map: map,
            title: building.title
        });
        marker.categories = [];

        // set marker color base on the complaints number
        var complaintNum = building.categories.length;
        if (complaintNum >= 4) {
            marker.setIcon('http://i.imgur.com/6s7buda.png');
        } else if (complaintNum >= 2) {
            marker.setIcon('http://i.imgur.com/PYNWdZn.png');
        } else {
            marker.setIcon('http://i.imgur.com/vErCcnm.png');
        }

        google.maps.event.addListener(marker, 'click', function () {
            window.location = "/building/" + building.id;
        });
        building.categories.forEach(function(category) {
            marker.categories.push(category);
            if(categoryMap[category]) {
                categoryMap[category].push(marker);
            } else {
                categoryMap[category] = [marker];
            }
            checkedCategories[category] = true;
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

        // Hide/show the appropriate markers
        checkbox.change(function() {
            var markers = categoryMap[category];
            if(checkbox.is(":checked")) {
                markers.forEach(function(marker) {
                    marker.setMap(map);
                });
                checkedCategories[category] = true;
            } else {
                checkedCategories[category] = false;
                markers.forEach(function(marker) {
                    var hide = true;
                    marker.categories.forEach(function(c) {
                        if(checkedCategories[c]) {
                            hide = false;
                        }
                    });
                    if(hide) {
                        marker.setMap(null);
                    }
                });
            }
        });

        label.append(checkbox, category);
        label.appendTo(categoryContainer);
    });

    map.fitBounds(bounds);
    map.panToBounds(bounds);
}
