var up = false; //variable utilizada para decidir si mostar exito al subir imagen o no

$(document).ready(function() {
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

  $('#modificar-usuario').on('submit', function(evt) {
    evt.preventDefault();

    var img = $('#imgU').val();
    console.log(img);
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

function afterSuccess (comment, disa) {
  if (up) {
    $(comment).html('Imagen actualizada correctamente');
    $(disa).addClass('disabled');
    up = false;
  }
}
