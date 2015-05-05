var map;
var marker;
var markers = [];
var tipo = 'personal';

$(document).ready(function() {
  putMap();
  
  $('.evenge-check').on('click', function() {
    if (!$(this).hasClass('selected')) {
      $('.evenge-check.selected').removeClass('selected');
      $(this).addClass('selected');
      tipo = $(this).data('type');
      console.log(tipo);
    }
  });
  
  $('.btn-form').on('click', function(evt) {
    evt.preventDefault();
    var isPrivado = true;
    var lat = false;
    var lon = false;
    if ( $(this).data('type') === 'public' ) { isPrivado = false; }
    if ( marker != null ) {
      lat = marker.getPosition().lat();
      lon = marker.getPosition().lng();
    }
    
    var data = {
      'nombre': $('#nombre').val(),
      'hora': $('#hora').val(),
      'fecha': $('#fecha').val(),
      'cantidadAsistentes': $('#cantidadAsistentes').val(),
      'descripcion': $('#descripcion').val(),
      'lugar': $('#lugar').val(),
      'asistencia': $('#asistencia').is(':checked'),
      'latitud': lat,
      'longitud': lon,
      'privado': isPrivado,
      'idUser': $('#newevent-cont').data('key')
    };
    
    
    $.ajax({
      type: 'POST',
      url: '/iEvento',
      data: data,
      success: function(resp){
        if (resp.response === true) { window.location = "/eventos?id="+resp.idEvento; }
        else alert('Ha habido un error');
      }
    });
  });
});

function putMap() {
  map = new google.maps.Map(document.getElementById('map-canvas'), {
    mapTypeId: google.maps.MapTypeId.ROADMAP,
    center: new google.maps.LatLng(40.4378271,-3.6795367),
    zoom: 6
  });

  map.setOptions({draggableCursor:'pointer'});

  var input = (document.getElementById('pac-input'));
  map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);

  var searchBox = new google.maps.places.SearchBox((input));

  google.maps.event.addListener(searchBox, 'places_changed', function() {
    var places = searchBox.getPlaces();

    if (places.length == 0) {
      return;
    }
    for (var i = 0, marker; marker = markers[i]; i++) {
      marker.setMap(null);
    }

    markers = [];
    var bounds = new google.maps.LatLngBounds();
    for (var i = 0, place; place = places[i]; i++) {
      var image = {
        url: place.icon,
        size: new google.maps.Size(71, 71),
        origin: new google.maps.Point(0, 0),
        anchor: new google.maps.Point(17, 34),
        scaledSize: new google.maps.Size(25, 25)
      };

     var marker = new google.maps.Marker({
        map: map,
        icon: image,
        title: place.name,
        position: place.geometry.location
      });

      markers.push(marker);

      bounds.extend(place.geometry.location);
    }

    map.fitBounds(bounds);
  });

  google.maps.event.addListener(map, 'bounds_changed', function() {
    var bounds = map.getBounds();
    searchBox.setBounds(bounds);
  });
  
  google.maps.event.addListener(map, 'click', function(event) {
    placeMarker(event.latLng);
  });
  
}

function placeMarker(location) {
  setAllMap(null);
  markers = [];
  marker = new google.maps.Marker({
    position: location, 
    map: map,
    title: 'Click para aplicar zoom'
  });
  markers.push(marker);
  map.setCenter(marker.getPosition());
}

function setAllMap(m) {
  for (var i = 0; i < markers.length; i++) {
    markers[i].setMap(m);
  }
}