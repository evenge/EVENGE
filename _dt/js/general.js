/*# Evenge - gestor de eventos (events management)
# Copyright (C) 2014 - desarrollo.evenge@gmail.com
# Carlos Campos Fuentes | Francisco Javier Exposito Cruz | Ivan Ortega Alba | Victor Coronas Lara
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.*/

/*jslint browser: true*/
/*global $, jQuery, alert*/

jQuery.validator.addMethod("twitter", function(value, element) {
  return this.optional(element) || /@([A-Za-z0-9_])+/.test(value);
}, "No es una cuenta de twitter correcta");

jQuery.validator.addMethod("web", function(value, element) {
  return this.optional(element) || /^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \?=.-]*)*\/?$/.test(value);
}, "No es una web correcta");

jQuery.validator.addMethod("telefono", function(value, element) {
  return this.optional(element) ||  /^((\+?34([ \t|\-])?)?[9|6|7]((\d{1}([ \t|\-])?[0-9]{3})|(\d{2}([ \t|\-])?[0-9]{2}))([ \t|\-])?[0-9]{2}([ \t|\-])?[0-9]{2})$/.test(value);
}, "No es un telefono correcto");

jQuery.validator.addMethod("mail", function(value, element) {
  return this.optional(element) || /^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3})$/.test(value);
}, "No es un email correcto");

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

  $('#noti-bottom').on('click', function (evt) {
    if ($(this).hasClass('active')) {
      $(this).removeClass('active');
      $(function () {
        $(".notifications-content").animate({width: '0'}, { duration: 200, queue: false });
        $(".pad120").animate({padding: '0'}, { duration: 200, queue: false });
      });
    } else {
      $(this).addClass('active');
      $(function () {
        $(".notifications-content").animate({width: '240px'}, { duration: 200, queue: false });
        $(".pad120").animate({padding: '0 240px 0 0'}, { duration: 200, queue: false });
      });
    }
    evt.preventDefault();
    evt.stopPropagation();
  });

  $('.menu-content .dropdown').on('show.bs.dropdown', function(e) {
    $(this).find('.dropdown-menu').first().stop(true, true).slideDown();
  });

  // ADD SLIDEUP ANIMATION TO DROPDOWN //
  $('.menu-content .dropdown').on('hide.bs.dropdown', function(e) {
    $(this).find('.dropdown-menu').first().stop(true, true).slideUp();
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
