$(document).ready(function() {
  $('#menu-bottom').on('click', function(evt) {
    if ( $(this).hasClass('active') ) {
      $(this).removeClass('active');
      $('#menu-div').hide();
    }
    else {
      $(this).addClass('active');
      $('#menu-div').show();
    }
    evt.preventDefault();
    evt.stopPropagation();
  });

  $('html').click(function(evt) {
    if ( $('#menu-bottom').hasClass('active') ) {
      $('#menu-bottom').removeClass('active');
      $('#menu-div').hide();
    }
  });

  $('#menu-div').click(function(evt){
    evt.stopPropagation();
  });
});
