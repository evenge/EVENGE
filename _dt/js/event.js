$(document).ready(function() {
  var coor = $('#map-canvas').data('coord').split(',');
  putMap(coor);
  
  $('#delete-href').on('click', function(evt) {
    evt.preventDefault();
    var data = {'id': $('.event-content').data('id')};
    $.ajax({
      type: 'POST',
      url: '/eliminarEvento',
      data: data,
      success: function(resp) {
        if (resp.response === true) { window.location = "/miseventos"; }
        else alert('Ha habido un error');
      }
    });
  });
});

function putMap(coor) {
  map = new google.maps.Map(document.getElementById('map-canvas'), {
    mapTypeId: google.maps.MapTypeId.ROADMAP,
    center: new google.maps.LatLng(coor[0],coor[1]),
    zoom: 16
  });
  
  var myLatlng = new google.maps.LatLng(coor[0],coor[1]);
  var titulo = $('.titular-h1').text();
  var fecha = $('.event-content').data('fecha');
  var hora = $('.event-content').data('hora');
  var contentString = '<div class="info-marker"><h5>'+titulo+'</h5><h6>'+hora+'</h6><h6>'+fecha+'</h6></div>';
  var infowindow = new google.maps.InfoWindow({
    content: contentString
  });

  marker = new google.maps.Marker({
    position: myLatlng,
    map: map,
    title: titulo
  });

  google.maps.event.addListener(marker, 'click', function() {
    infowindow.open(map,marker);
  });
  
}