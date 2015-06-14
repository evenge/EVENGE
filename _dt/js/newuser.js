
$(document).ready(function() {

    $('#iUsuario').on('submit', function (evt) {
      evt.preventDefault();
    });

    /*Validacion del registro de usuario*/
    $('#iUsuario').validate({
      rules: {
        nombreR: {
          required: true,
          maxlength: 30
        },
        apellidosR: {
          required: true,
          maxlength: 50
        },
        contrasenaR: {
          required: true,
          minlength: 8,
          maxlength: 50
        },
        repetirContrasenaR: {
            required: true,
            equalTo: "#contrasenaR"
        },
        emailR: {
            required: true,
            email:true,
        },
        ciudadR: {
          maxlength: 50
        },
        telefonoR: {
          telefono: true
        },
        webR: {
          web: true
        },
        twitterR: {
          twitter: true
        }
      },
      /*Marca la opción que no se cumple del formulario*/
      errorPlacement: function (error, element) {
        $('li[data-con="'+$(element[0]).data('error')+'"]').css('color', '#d43539');
      },
      /*Marca la opción cuando se cumple del formulario*/
      success: function(label, element) {
        $('li[data-con="'+$(element).data('error')+'"]').css('color', '#7c7c7c');
    },
    submitHandler: function () {
      var nombre = $('#nombreR').val();
      var apellidos = $('#apellidosR').val();
      var email = $('#emailR').val();
      var contrasena = $('#contrasenaR').val();
      var tel = $('#telefonoR').val();
      var ciudad = $('#ciudadR').val();
      var web = $('#webR').val();
      var twitter = $('#twitterR').val();


      //Datos del usuario
      var data = {
        'nombre': nombre,
        'apellidos': apellidos,
        'email': email,
        'contrasena': contrasena,
        'ciudad': ciudad,
        'web': web,
        'twitter': twitter,
        'telefono': tel
      };

      $.ajax({
        type: 'POST',
        url: '/registrate',
        data: data,
        success: function(resp) {
            console.log(resp.response);
          if (resp.response == true) { window.location = "/login"; }
          else alert('Ha habido un error');
        }
      });
    }
    });
});
