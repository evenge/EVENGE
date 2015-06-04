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

});

!function (d, s, id) {
  var js,
    fjs = d.getElementsByTagName(s)[0],
    p = /^http:/.test(d.location) ? 'http' : 'https';

  if (!d.getElementById(id)) {
    js = d.createElement(s);
    js.id = id;
    js.src = p + '://platform.twitter.com/widgets.js';
    fjs.parentNode.insertBefore(js, fjs);
  }

}(document, 'script', 'twitter-wjs');
