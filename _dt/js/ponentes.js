$(document).ready(function() {
  $('.delete-p').on('click', function (evt) {
    evt.preventDefault();
    var ponente = $(this).parent().parent().parent();

    var data = {
      'idP': $(this).data('id')
    };

    $.ajax({
      type: 'POST',
      url: '/bPonente',
      data: data,
      dataType: 'json',
      success: function(resp) {
        if (resp.response === 'true') {
          $(ponente).hide();
        } else {
          alert('Ha habido un error');
        }
      }
    });
  });
});
