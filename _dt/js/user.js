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
});
