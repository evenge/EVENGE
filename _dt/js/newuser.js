$(document).ready(function() {
    $('#iUsuario').on('submit', function (evt) {
      evt.preventDefault();
    });

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

      errorPlacement: function (error, element) {
        $('li[data-con="'+$(element[0]).data('error')+'"]').css('color', '#d43539');
      },
      success: function(label, element) {
        $('li[data-con="'+$(element).data('error')+'"]').css('color', '#7c7c7c');
      }
    });


});
