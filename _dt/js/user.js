var up = false; //variable utilizada para decidir si mostar exito al subir imagen o no

function beforeSubmit(img, com) {
  if (window.File && window.FileReader && window.FileList && window.Blob) {
    if( !$(img).val()) {
      $(com).html("Introduce alguna imagen");
      return false
    }

    var fsize = $(img)[0].files[0].size;
    var ftype = $(img)[0].files[0].type;

    switch(ftype) {
      case 'image/png': case 'image/gif': case 'image/jpeg':
        break;
      default:
        $(com).html("Formato no permitido (jpg, png, gif)");
        return false
    }

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

function afterSuccess(comment, disa) {
  if (up) {
    $(comment).html('Imagen actualizada correctamente');
    $(disa).addClass('disabled');
    up = false;
  }
}

$(document).ready(function() {
  $('#iOrganizacion').on('submit', function (evt) {
    evt.preventDefault();
    var name = $('#org-name').val();
    var web = $('#org-web').val();
    var twitter = $('#org-twitter').val();
    var email = $('#org-mail').val();
    var tel = $('#org-tel').val();
    
    var send = validarValor(email, '', $(), 1);

    var data = {
      'nombre': name,
      'web': web,
      'twitter': twitter,
      'email': email,
      'telefono': tel
    };
    
    if (send) {
      $.ajax({
        type: 'POST',
        url: '/iOrganizacion',
        data: data,
        success: function(resp) {
          if (resp.response === 'true') { window.location = "/micuenta"; }
          else alert('Ha habido un error');
        }
      });
    }
  });

  $('#einvitacion').on('submit', function(evt) {
    evt.preventDefault();
    var email = $('#emailI').val();

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

  $('#modificar-usuario').validate({
    rules: {
      nombreU: {
        required: true,
        maxlength: 30
      },
      apellidosU: {
        required: true,
        maxlength: 50
      },
      ciudadU: {
        maxlength: 50
      },
      telefonoU: {
        required: true
      },
      webU: {
        required: true
      },
      twitterU: {
        twitter: true
      }
    },

    errorPlacement: function (error, element) {
      $('li[data-con="'+$(element[0]).data('error')+'"]').css('color', '#d43539');
    },
    success: function(label, element) {
      $('li[data-con="'+$(element).data('error')+'"]').css('color', '#7c7c7c');
    },
    submitHandler: function () {
      /*var nombre = $('#nombreU').val();
      var web = $('#webU').val();
      var twitter = $('#twitterU').val();
      var apellidos = $('#apellidosU').val();
      var ciudad = $('#ciudadU').val();
      var tel = $('#telefonoU').val();

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
      });*/
    }
  });

  $('#modificar-usuario').on('submit', function (evt) {
    evt.preventDefault();
  });

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
