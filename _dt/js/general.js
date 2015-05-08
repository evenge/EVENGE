/*jslint browser: true*/
/*global $, jQuery, alert*/

$(document).ready(function () {
  'use strict';
  $('#menu-bottom').on('click', function (evt) {
    if ($(this).hasClass('active')) {
      $(this).removeClass('active');
      $(function () {
        $(".menu-content").animate({width: '0'}, { duration: 200, queue: false });
        $(".pad120").animate({padding: '0'}, { duration: 200, queue: false });
      });
    } else {
      $(this).addClass('active');
      $(function () {
        $(".menu-content").animate({width: '220px'}, { duration: 200, queue: false });
        $(".pad120").animate({padding: '0 0 0 220px'}, { duration: 200, queue: false });
      });
    }
    evt.preventDefault();
    evt.stopPropagation();
  });

  /*$('html').click(function (evt) {
    if ($('#menu-bottom').hasClass('active')) {
      $('#menu-bottom').removeClass('active');
      $('#menu-div').hide("slide", { direction: "left" }, 800);
      $('.main-body').removeClass('pad120');
    }
  });

  $('#menu-div').click(function (evt) {
    evt.stopPropagation();
  });*/

});
