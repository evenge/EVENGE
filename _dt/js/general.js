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

//variable para obtener el prefijo del navegador
var prefix = (function prefix() {
  var regex = /^(Webkit|Khtml|Moz|ms|O)(?=[A-Z])/;
  var styleDeclaration = document.getElementsByTagName('script')[0].style;
  for (var prop in styleDeclaration) {
    if (regex.test(prop)) {
      return '-' + prop.match(regex)[0].toLowerCase() + '-';
    }
  }
  // Nothing found so far? Webkit does not enumerate over the CSS properties of the style object.
  // However (prop in style) returns the correct value, so we'll have to test for
  // the precence of a specific property
  if ('WebkitOpacity' in styleDeclaration) { return '-webkit-'; }
  if ('KhtmlOpacity' in styleDeclaration) { return '-khtml-'; }
  return '';
}());

//inicializamos las opciones del menu
var _menu = document.getElementById('menuM'),
    _panel = document.getElementById('panel'),
    _opened = false,
    _duration = 300;

//inicializamos variables opciones avanzadas
var _openedA = false;

jQuery.validator.addMethod("twitter", function (value, element) {
  return this.optional(element) || /@([A-Za-z0-9_])+/.test(value);
}, "No es una cuenta de twitter correcta");

jQuery.validator.addMethod("web", function (value, element) {
  return this.optional(element) || /^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \?=.-]*)*\/?$/.test(value);
}, "No es una web correcta");

jQuery.validator.addMethod("telefono", function (value, element) {
  return this.optional(element) ||  /^((\+?34([ \t|\-])?)?[9|6|7]((\d{1}([ \t|\-])?[0-9]{3})|(\d{2}([ \t|\-])?[0-9]{2}))([ \t|\-])?[0-9]{2}([ \t|\-])?[0-9]{2})$/.test(value);
}, "No es un telefono correcto");

jQuery.validator.addMethod("mail", function (value, element) {
  return this.optional(element) || /^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3})$/.test(value);
}, "No es un email correcto");

function setTransform(offset) {
  _panel.style[prefix + 'transform'] = _panel.style.transform = 'translate3d('+offset+'px, 0, 0)';
}

function setTransition() {
  _panel.style[prefix + 'transform'] = _panel.style.transition = prefix + 'transform ' +_duration+'ms ease';
}

function open() {
  $('html').addClass( "menu-open");
  setTransition();
  _opened = true;
  setTimeout( function () {
    setTransform(256);
  }, _duration + 50);
}

function close() {
  setTransition()
  _opened = false;
  setTransform(0);
  setTimeout( function () {
    $('html').removeClass('menu-open');
  }, _duration + 50);
}

$(document).ready(function () {
  'use strict';

  $('#menu-bottom').on('click', function (evt) {
    if ( _opened ) {
      close();
    } else {
      open();
    }
    evt.preventDefault();
  });

  $('.menu-content .dropdown').on('show.bs.dropdown', function(e) {
    $(this).find('.dropdown-menu').first().stop(true, true).slideDown();
  });

  // ADD SLIDEUP ANIMATION TO DROPDOWN //
  $('.menu-content .dropdown').on('hide.bs.dropdown', function(e) {
    $(this).find('.dropdown-menu').first().stop(true, true).slideUp();
  });

  $('.navbar-nav .dropdown').on('show.bs.dropdown', function(e) {
    $(this).find('.dropdown-menu').first().stop(true, true).show('slide', {direction: 'right'}, 300);
  });

  // ADD SLIDEUP ANIMATION TO DROPDOWN //
  $('.navbar-nav .dropdown').on('hide.bs.dropdown', function(e) {
    $(this).find('.dropdown-menu').first().stop(true, true).hide('slide', {direction: 'right'}, 300);
  });

  $('.advanced-options-bottom').on('click', function () {
    if (_openedA) {
      $('.advanced-options').slideUp();
      _openedA = false;
    } else {
      $('.advanced-options').slideDown();
      _openedA = true;
    }
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
