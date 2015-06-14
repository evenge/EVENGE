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

  $('#uImagenUsuarioF').submit(function() {
    var options = {
      target: '#imgU',
      beforeSubmit:  beforeSubmit,
      resetForm: true
    };

    $(this).ajaxSubmit(options);
      return false;
  });
});


function beforeSubmit(){
  if (window.File && window.FileReader && window.FileList && window.Blob) {
    if( !$('#imgU').val()) {
      $("#output").html("Introduce alguna imagen");
      return false
    }

    var fsize = $('#imgU')[0].files[0].size;
    var ftype = $('#imgU')[0].files[0].type;

    switch(ftype) {
      case 'image/png': case 'image/gif': case 'image/jpeg': case 'image/pjpeg':
        break;
      default:
        $("#output").html("<b>"+ftype+"</b> Formato no permitido!");
        return false
    }

    if(fsize>1048576) {
      $("#output").html("<b>"+fsize +"</b> El archivo pesa demasiado, solo están permitidas imagenes de menos de 1MB");
      return false
    }

    $("#output").html("");

  } else {
    $("#output").html("Por favor, actualiza tu navegador para soportar la subida de imágenes");
    return false;
  }
}
