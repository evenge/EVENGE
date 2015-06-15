/*# Evenge - gestor de eventos (events management)
# Copyright (C) 2014 - desarrollo.evenge@gmail.com
# Carlos Campos Fuentes | Francisco Javier Exposito Cruz | Ivan Ortega Alba | Victor Coronas Lara
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.*/

function putMap(coor, ele) {
  map = new google.maps.Map(ele, {
    scrollwheel: false,
    mapTypeId: google.maps.MapTypeId.ROADMAP,
    center: new google.maps.LatLng(coor[0], coor[1]),
    zoom: 16
  });

  var myLatlng = new google.maps.LatLng(coor[0], coor[1]),
    titulo = $('.titular-h1').text();

  marker = new google.maps.Marker({
    position: myLatlng,
    map: map,
    title: titulo
  });

}

$(document).ready(function () {
  $('.map-canvas').each(function () {
    var coor = $(this).data('coord').split(',');
    putMap(coor, $(this)[0]);
  });

});
