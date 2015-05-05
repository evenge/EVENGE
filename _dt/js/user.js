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
});