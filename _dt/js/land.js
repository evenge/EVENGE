$(document).ready(function() {
  $('.map-canvas').each(function() {
    var coor = $(this).data('coord').split(',');
    putMap(coor, $(this)[0]);
  });

});

function putMap(coor, ele) {
  map = new google.maps.Map(ele , {
    scrollwheel: false,
    mapTypeId: google.maps.MapTypeId.ROADMAP,
    center: new google.maps.LatLng(coor[0],coor[1]),
    zoom: 16
  });

  var myLatlng = new google.maps.LatLng(coor[0],coor[1]);
  var titulo = $('.titular-h1').text();

  marker = new google.maps.Marker({
    position: myLatlng,
    map: map,
    title: titulo
  });

}
