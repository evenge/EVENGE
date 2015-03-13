/*jslint browser: true*/
/*global $, jQuery, alert*/
function sticky_relocate() {
  'use strict';
  var window_top = $(window).scrollTop(),
    div_top = 40;
  if (window_top > div_top) {
    $('.individual-menu').addClass('transp');
  } else {
    $('.individual-menu').removeClass('transp');
  }
}

$(document).ready(function () {
  'use strict';
  $('#menu-bottom').on('click', function (evt) {
    if ($(this).hasClass('active')) {
      $(this).removeClass('active');
      $('#menu-div').slideUp();
    } else {
      $(this).addClass('active');
      $('#menu-div').slideDown();
    }
    evt.preventDefault();
    evt.stopPropagation();
  });

  $('html').click(function (evt) {
    if ($('#menu-bottom').hasClass('active')) {
      $('#menu-bottom').removeClass('active');
      $('#menu-div').slideUp();
    }
  });

  $('#menu-div').click(function (evt) {
    evt.stopPropagation();
  });

  $(function () {
    $(window).scroll(sticky_relocate);
    sticky_relocate();
  });
});
