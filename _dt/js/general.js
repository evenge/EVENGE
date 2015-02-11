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

  $(function () {
    $(window).scroll(sticky_relocate);
    sticky_relocate();
  });
});

function sticky_relocate() {
  var window_top = $(window).scrollTop();
  var div_top = 40;
  if (window_top > div_top) {
    $('.individual-menu').addClass('transp');
  }
  else {
    $('.individual-menu').removeClass('transp');
  }
}
