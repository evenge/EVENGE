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

var marker;
var markers = [];

$(document).ready(function() {
  var coor = $('#map-canvas').data('coord').split(',');
  putMap(coor);

  $('.evenge-check').on('click', function() {
    if (!$(this).hasClass('selected')) {
      $('.evenge-check.selected').removeClass('selected');
      $(this).addClass('selected');
    }
  });

  $('.btn-form').on('click', function(evt) {
    evt.preventDefault();
    var isPrivado = true;
    var lat = false;
    var lon = false;
    if ( $(this).data('type') === 'public' ) { isPrivado = false; }
    if ( marker !== null ) {
      lat = marker.getPosition().lat();
      lon = marker.getPosition().lng();
    }

    var data = {
      'idE': $('#idEvento').val(),
      'nombre': $('#nombre').val(),
      'privado': isPrivado,
      'hora': $('#hora').val(),
      'fecha': $('#fecha').val(),
      'cantidadAsistentes': $('#cantidadAsistentes').val(),
      'descripcion': $('#descripcion').val(),
      'lugar': $('#lugar').val(),
      'asistencia': $('#asistencia').is(':checked'),
      'latitud': lat,
      'longitud': lon,
      'userT': $('.selected').data('us'),
      'idUser': $('.selected').data('key')
    };

    $.ajax({
      type: 'POST',
      url: '/mEvento',
      data: data,
      success: function(resp){
        if (resp.response === true) {
          window.location = "/eventos?id="+resp.idEvento;
        }
        else
          alert('Ha habido un error');
      }
    });
  });
});

function putMap(coor) {
  map = new google.maps.Map(document.getElementById('map-canvas'), {
    scrollwheel: false,
    mapTypeId: google.maps.MapTypeId.ROADMAP,
    center: new google.maps.LatLng(coor[0],coor[1]),
    zoom: 16
  });

  var myLatlng = new google.maps.LatLng(coor[0],coor[1]);
  var titulo = $('#nombre').val();
  var fecha = $('#fecha').val();
  var hora = $('#hora').val();
  var contentString = '<div class="info-marker"><h5>'+titulo+'</h5><h6>'+hora+'</h6><h6>'+fecha+'</h6></div>';
  var infowindow = new google.maps.InfoWindow({
    content: contentString
  });

  marker = new google.maps.Marker({
    position: myLatlng,
    map: map,
    title: titulo
  });

  infowindow.open(map,marker);

  google.maps.event.addListener(marker, 'click', function() {
    infowindow.open(map,marker);
  });

}
