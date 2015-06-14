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
  //Esta funcion se encarga de controlar el funcionamiento del formulario para crear un ponente
  $('#iponente').validate({
    //Reglas de validacion
    rules: {
      nombreP: {
        required: true, //valor requerido
        maxlength: 30 //maximo 30 caracteres
      },
      apellidosP: {
        required: true,
        maxlength: 50
      },
      emailP: {
        mail: true
      },
      descripcionP: {
        maxlength: 240
      },
      telefonoP: {
        required: false
      },
      webP: {
        web: true
      },
      twitterP: {
        twitter: true
      }
    },

    //Esta funcion se encarga de cambiar el color de la frase en funcion del error
    //$(element[0]).data('error') - obtenemos el data-error del input
    //$('li[data-con="'+$(element[0]).data('error')+'"]') - buscamos el data-con correspondiente
    errorPlacement: function (error, element) {
      $('li[data-con="'+$(element[0]).data('error')+'"]').css('color', '#d43539');
    },

    //Esta funcion se encarga de cambiar el color de la frase cuando esta correcto
    success: function(label, element) {
      $('li[data-con="'+$(element).data('error')+'"]').css('color', '#7c7c7c');
    },

    //Si se valida el formulario lo enviamos
    submitHandler: function () {
      var email = $('#emailP').val();
      var nombre = $('#nombreP').val();
      var apellidos = $('#apellidosP').val();
      var twitter = $('#twitterP').val();
      var web = $('#webP').val();
      var tlf = $('#telefonoP').val();
      var descripcion = $('#descripcionP').val()

      var data = {
        'email': email,
        'nombre': nombre,
        'apellidos': apellidos,
        'twitter': twitter,
        'web': web,
        'tlf': tlf
      };

      $.ajax({
        type: 'POST',
        url: '/iPonente',
        data: data,
        success: function(resp) {
          if (resp.response === true) {
            window.location = "/misponentes";
          } else {
            alert('Ha habido un error');
          }
        }
      });
    }
  });

  //Esta funcion se encargan de deshabilitar el envio del formulario por defecto
  $('#iponente').on('submit', function(evt) {
    evt.preventDefault();
  });

});
