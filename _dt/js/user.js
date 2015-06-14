var up = false; //variable utilizada para decidir si mostar exito al subir imagen o no

//Funcion llamada antes de enviar el avatar del usuario o la organizacion
//La funcion tiene dos parametros:
// img = input donde está la imagen
// com = contenedor donde mostrar los mensajes de error o exito
function beforeSubmit(img, com) {
  if (window.File && window.FileReader && window.FileList && window.Blob) {
    //comprobamos si hay una imagen. En caso negativo no seguimos con el proceso
    if( !$(img).val()) {
      $(com).html("Introduce alguna imagen");
      return false
    }
    //obtenemos el formato y el tamaño de la imagen
    var fsize = $(img)[0].files[0].size;
    var ftype = $(img)[0].files[0].type;

    //Comprobamos si tiene un formato adecuado. En caso negativo no seguimos con el proceso
    switch(ftype) {
      case 'image/png': case 'image/gif': case 'image/jpeg':
        break;
      default:
        $(com).html("Formato no permitido (jpg, png, gif)");
        return false
    }

    //Comprobamos si tiene un tamaño adecuado. En caso negativo no seguimos con el proceso
    if(fsize>548576) {
      $(com).html("El archivo pesa demasiado, solo están permitidas imagenes de menos de 500KB");
      return false
    }

    $(com).html("");
    up = true;

  } else {
    $(com).html("Por favor, actualiza tu navegador para soportar la subida de imágenes");
    return false;
  }
}

//Funcion llamada una vez hemos subido la imagen
// comment: contenedor donde mostramos el mensaje
// disa: desactivamos el boton de envio
function afterSuccess(comment, disa) {
  if (up) {
    $(comment).html('Imagen actualizada correctamente');
    $(disa).addClass('disabled');
    up = false;
  }
}

$(document).ready(function() {
  //Esta funcion se encarga de controlar el funcionamiento del formulario para crear una organizacion
  $('#iOrganizacion').on('submit', function (evt) {
    evt.preventDefault();
    var name = $('#org-name').val();
    var web = $('#org-web').val();
    var twitter = $('#org-twitter').val();
    var email = $('#org-mail').val();
    var tel = $('#org-tel').val();

    var data = {
      'nombre': name,
      'web': web,
      'twitter': twitter,
      'email': email,
      'telefono': tel
    };
    
    $.ajax({
      type: 'POST',
      url: '/iOrganizacion',
      data: data,
      success: function(resp) {
        if (resp.response === 'true') { window.location = "/micuenta"; }
        else alert('Ha habido un error');
      }
    });
  });

  //Esta funcion se encarga de controlar el funcionamiento del formulario para enviar una invitacion
  $('#einvitacion').on('submit', function(evt) {
    evt.preventDefault();
    var email = $('#emailI').val();
    //datos que vamos a enviar
    // email: email para la invitacion
    // idOrg: id de la organizacion
    var data = {
      'email': email,
      'idOrg': $('.invitacion').data('key')
    };

    $.ajax({
      type: 'POST',
      url: '/invitacion',
      data: data,
      success: function(resp) {
        if (resp.response === 'true') {
          var invi = '<tr><th>'+email+'</th><th>'+resp.fecha+'</th><th><a class="delete-invi" href="">' +
              '<i class="fa fa-times"></i></a></th></tr>';

          $('.invitaciones-pendientes tbody').append(invi)
        } else {
          alert('Ha habido un error');
        }
      }
    });
  });

  //Funcion que se encarga de controlar el funcionamiento del formulario para modificar el usuario
  $('#modificar-usuario').validate({
    //Reglas de validacion
    rules: {
      nombreU: {
        required: true, //valor requerido
        maxlength: 30 //maximo 30 caracteres
      },
      apellidosU: {
        required: true,
        maxlength: 50 //maximo 50 caracteres
      },
      ciudadU: {
        maxlength: 50
      },
      telefonoU: {
        required: true
      },
      webU: {
        web: true
      },
      twitterU: {
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
    submitHandler: function () {
      var nombre = $('#nombreU').val();
      var web = $('#webU').val();
      var twitter = $('#twitterU').val();
      var apellidos = $('#apellidosU').val();
      var ciudad = $('#ciudadU').val();
      var tel = $('#telefonoU').val();

      //Datos del usuario
      var data = {
        'nombre': nombre,
        'apellidos': apellidos,
        'ciudad': ciudad,
        'web': web,
        'twitter': twitter,
        'telefono': tel
      };

      $.ajax({
        type: 'POST',
        url: '/mUsuario',
        data: data,
        success: function(resp) {
          if (resp.response === 'true') { window.location = "/micuenta"; }
          else alert('Ha habido un error');
        }
      });
    }
  });

  $('#modificar-usuario').on('submit', function (evt) {
    evt.preventDefault();
  });

  //Esta funcion se encarga de actualizar la imagen del usuario
  $('#uImagenUsuarioF').submit( function() {
    var options = {
      target: '#update',
      beforeSubmit: beforeSubmit($('#imgU'), $('#output')),
      success: afterSuccess($('#output'), $('#uImagenUsuarioF .btn-form')),
      resetForm: true
    };

    $(this).ajaxSubmit(options);
      return false;
  });

  //Esta funcion se encarga de actualizar la imagen de la organizacion
  $('#uImagenOrganizacionF').submit( function() {
    var options = {
      target: '#update2',
      beforeSubmit: beforeSubmit($('#imgO'), $('#output2')),
      success: afterSuccess($('#output2'), $('#uImagenOrganizacionF .btn-form')),
      resetForm: true
    };

    $(this).ajaxSubmit(options);
      return false;
  });
});
