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

var map;
var marker;
var markers = [];
var p = false;

$(document).ready(function() {
  var editor = new wysihtml5.Editor("descripcion", { // id of textarea element
    toolbar:      "toolbar-descripcion", // id of toolbar element
    stylesheets: "_dt/css/toolbar.css",
    parserRules:  wysihtml5ParserRules // defined in parser rules set
  });

  putMap();
  
  $('.evenge-check').on('click', function() {
    if (!$(this).hasClass('selected')) {
      $('.evenge-check.selected').removeClass('selected');
      $(this).addClass('selected');
    }
  });
  
  $('#create').on('click', function(evt) {
    evt.preventDefault();
    var isPrivado = p;
    var lat = false;
    var lon = false;
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
      'userT': $('.selected').data('us'),
      'idUser': $('.selected').data('key')
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

  $('.btn-form').on('click', function (evt) {
    evt.preventDefault();
    if ( $(this).data('type') === 'public' ) {
      p = false;
    } else {
      p = true;
    }
  });
});

function putMap() {
  map = new google.maps.Map(document.getElementById('map-canvas'), {
    scrollwheel: false,
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
