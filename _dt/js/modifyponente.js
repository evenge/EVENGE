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
  $('#mponente').on('submit', function(evt) {
    evt.preventDefault();
    var email = $('#email-p').val();
    var nombre = $('#nombre-p').val();
    var apellidos = $('#apellidos-p').val();
    var twitter = $('#twitter-p').val();
    var web = $('#web-p').val();
    var tlf = $('#telefono-p').val();
    var descripcion = $('#descripcion-p').val()

    var data = {
      'email': email,
      'nombre': nombre,
      'apellidos': apellidos,
      'twitter': twitter,
      'web': web,
      'tlf': tlf,
      'idPonente': $('.evenge-form').data('id')
    };

    $.ajax({
      type: 'POST',
      url: '/mPonente',
      data: data,
      success: function(resp) {
        if (resp.response === true) {
          window.location = "/misponentes";
        } else {
          alert('Ha habido un error');
        }
      }
    });
  });
});
