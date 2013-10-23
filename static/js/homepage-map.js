  
google.maps.event.addDomListener(window, 'load', initialize);

function initialize() {

	var myLatlng = new google.maps.LatLng(43.663277,-79.396992);
	var bounds = new google.maps.LatLngBounds();
	var mapOptions = {
		zoom: 13,
		center: myLatlng,
		mapTypeId: google.maps.MapTypeId.ROADMAP
	}

	var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

	//TODO: replace mock data with API call  
	var buildingList = [
	{
		"lat" 	: 43.667576,
		"lng" 	: -79.391868,
		"id"  	: "1",
		"title" : "building1"
	},
	{
		"lat" 	: 43.663991,
		"lng"	: -79.398580,
		"id"  	: "2",
		"title" : "building2"
	},
	{
		"lat"	: 43.651230,
		"lng" 	: -79.409866,
		"id"  	: "3",
		"title" : "building3"
	},
	{
		"lat" 	: 43.665326,
		"lng" 	: -79.411154,
		"id"  	: "4",
		"title" : "building4"
	},
	{
		"lat"	: 43.775326,
		"lng" 	: -79.411154,
		"id"  	: "5",
		"title" : "building5"
	}	
	];

	$.each(buildingList, function(index, value) {
		var latLong = new google.maps.LatLng(value.lat, value.lng);
		bounds.extend(latLong);
		new google.maps.Marker({
			position: latLong,
			map: map,
			title: value.title
		});
	});
	map.fitBounds(bounds);
	map.panToBounds(bounds);
}
