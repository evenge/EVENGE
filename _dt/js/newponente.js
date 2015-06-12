$(document).ready(function() {
  $('#iponente').on('submit', function(evt) {
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
  });
});
