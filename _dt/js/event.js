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

$(document).ready(function() {
  var coor = $('#map-canvas').data('coord').split(',');
  putMap(coor);

  $('.select-asistentes').select2();

  $('.delete-eve').on('click', function(evt) {
    evt.preventDefault();
    var data = {
      'id': $('.event-content').data('id')
    };

    $.ajax({
      type: 'POST',
      url: '/eliminarEvento',
      data: data,
      type: 'json',
      success: function(resp) {
        if (resp.response === true) {
          window.location = "/miseventos";
        } else {
          alert('Ha habido un error');
        }
      }
    });
  });

  $('#form-ins').on('submit', function(evt) {
    evt.preventDefault();
    var data = {
      'id': $('.event-content').data('id'),
      'nombre': $('#ins-nombre').val(),
      'apellidos': $('#ins-apellidos').val(),
      'dni': $('#ins-dni').val(),
      'email': $('#ins-email').val(),
      'telefono': $('#ins-telefono').val(),
      'twitter': $('#ins-twitter').val(),
      'web': $('#ins-web').val()
    };

    $.ajax({
      type: 'POST',
      url: '/iAsistente',
      data: data,
      dataType: 'json',
      success: function(resp) {
        var as = '<tr><th>'+data.nombre+'</th><th>'+data.apellidos+'</th><th>'+data.dni+'</th><th>No ha asistido</th><th><button data-id="'+data.dni+'" class="btn btn-default asitencia-button"><i class="fa fa-check fa-fw"></i></button></th><th><button data-id="'+data.dni+'" class="btn btn-default delete-button"><i class="fa fa-times"></i></button></th><th><button data-id="'+data.dni+'" class="btn btn-default pdf-button"><i class="fa fa-file-pdf-o"></i></button></th></tr>';

        $('#modalAsistente').modal('hide');
        $('.tasistentes').append(as);
      }
    });
  });

  $('.asitencia-button').on('click', function(evt) {
    evt.preventDefault();
    var bt = $(this);
    var data = {
      'idE': $('.event-content').data('id'),
      'dni': $(this).data('id')
    };

    $.ajax({
      type: 'POST',
      url: '/cAsistente',
      data: data,
      dataType: 'json',
      success: function(resp) {
        if (resp.response === 'true') {
          $(bt).hide();
        } else {
          alert ('Ha habido un error');
        }
      }
    });
  });

  $('#iponente').on('submit', function(evt) {
    evt.preventDefault();
    var email = $('#email-p').val();
    var nombre = $('#nombre-p').val();
    var apellidos = $('#apellidos-p').val();
    var twitter = $('#twitter-p').val();
    var web = $('#web-p').val();
    var tlf = $('#telefono-p').val();
    var idEvento = $('.event-content').data('id')
    var descripcion = $('#descripcion-p').val()

    var data = {
      'email': email,
      'nombre': nombre,
      'apellidos': apellidos,
      'twitter': twitter,
      'web': web,
      'tlf': tlf,
      'guardar': '1',
      'idEvento': idEvento,
      'descripcion': descripcion
    };

    $.ajax({
      type: 'POST',
      url: '/iPonente',
      data: data,
      dataType: 'json',
      success: function(resp) {
        if (resp.response === true) {
          $('#modalPonente').modal('hide');
          var p = resp.p;
          var pon = '<div class="col-sm-3"><div class="col-sm-12 ponente"><div class="imagen"><img alt="avatar" src="/_dt/img/default_avatar.png"></div><div class="detalles detalles1 col-md-12"><h2>'+data.nombre+' '+data.apellidos+'</h2></div><div class="detalles detalle-d col-md-12"><h4>'+data.descripcion+'</h4></div><div class="detalles detalle-w col-md-12"><h3><a href="'+data.web+'"><i class="fa fa-link fa-fw"></i> '+data.web+'</a></h3></div><div class="detalles detalle-t col-md-12"><h3><a href="http://twitter.com/'+data.twitter+'"><i class="fa fa-twitter fa-fw"></i> '+data.twitter+'</a></h3></div><div class="detalles col-md-12"><h3><i class="fa fa-phone fa-fw"></i> '+data.telefono+'</h3></div></div>';
          $('.ponentes-cont').append(pon);
        } else {
          alert('Ha habido un error');
        }
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

  infowindow.open(map,marker);

  google.maps.event.addListener(marker, 'click', function() {
    infowindow.open(map,marker);
  });

}
