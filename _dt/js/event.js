$(document).ready(function() {
  var coor = $('#map-canvas').data('coord').split(',');
  putMap(coor);

  $('.select-asistentes').select2();

  $('#delete-href').on('click', function(evt) {
    evt.preventDefault();
    var data = {
      'id': $('.event-content').data('id')
    };

    $.ajax({
      type: 'POST',
      url: '/eliminarEvento',
      data: data,
      success: function(resp) {
        if (resp.response === true) {
          window.location = "/miseventos";
        } else {
          alert('Ha habido un error');
        }
      }
    });
  });

  $("#inscribete-btn").click(function() {
    $("#form-inscribete").slideToggle("7000");
  });

  $('#form-ins').on('submit', function(evt) {
    evt.preventDefault();
    var data = {
      'id': $('.event-content').data('id'),
      'nombre': $('#ins-nombre').val(),
      'apellidos': $('#ins-apellidos').val(),
      'dni': $('#ins-dni').val(),
      'email': $('#ins-email').val(),
      'telefono': $('#ins-telefono').val(),
      'twitter': $('#ins-twitter').val(),
      'web': $('#ins-web').val()
    };

    $.ajax({
      type: 'POST',
      url: '/iAsistente',
      data: data,
      success: function(resp) {
        $('#modalAsistente').modal('hide');
      }
    });
  });

  $('#iponente').on('submit', function(evt) {
    evt.preventDefault();
    var email = $('#email-p').val();
    var nombre = $('#nombre-p').val();
    var apellidos = $('#apellidos-p').val();
    var twitter = $('#twitter-p').val();
    var web = $('#web-p').val();
    var tlf = $('#telefono-p').val();
    var idEvento = $('.event-content').data('id')
    var descripcion = $('#descripcion-p').val()

    var data = {
      'email': email,
      'nombre': nombre,
      'apellidos': apellidos,
      'twitter': twitter,
      'web': web,
      'tlf': tlf,
      'guardar': '1',
      'idEvento': idEvento,
      'descripcion': descripcion
    };

    $.ajax({
      type: 'POST',
      url: '/iPonente',
      data: data,
      success: function(resp) {
        if (resp.response === true) {
          $('#modalPonente').modal('hide');
        } else {
          alert('Ha habido un error');
        }
      }
    });
  });

});

function putMap(coor) {
  map = new google.maps.Map(document.getElementById('map-canvas'), {
    scrollwheel: false,
    mapTypeId: google.maps.MapTypeId.ROADMAP,
    center: new google.maps.LatLng(coor[0],coor[1]),
    zoom: 16
  });

  var myLatlng = new google.maps.LatLng(coor[0],coor[1]);
  var titulo = $('.titular-h1').text();
  var fecha = $('.event-content').data('fecha');
  var hora = $('.event-content').data('hora');
  var contentString = '<div class="info-marker"><h5>'+titulo+'</h5><h6>'+hora+'</h6><h6>'+fecha+'</h6></div>';
  var infowindow = new google.maps.InfoWindow({
    content: contentString
  });

  marker = new google.maps.Marker({
    position: myLatlng,
    map: map,
    title: titulo
  });

  infowindow.open(map,marker);

  google.maps.event.addListener(marker, 'click', function() {
    infowindow.open(map,marker);
  });

}
