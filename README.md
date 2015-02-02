<!--
Evenge - gestor de eventos (events management)
Copyright (C) 2014 - desarrollo.evenge@gmail.com
Carlos Campos Fuentes | Francisco Javier Expósito Cruz | Iván Ortega Alba | Victor Coronas Lara

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
-->

# EVENGE
###### Gestor de eventos

**Evenge** es un sistema de **gestión automática de eventos** con inclusión en diferentes blog (Wordpress, Blogspot), correo electrónico y redes sociales.  

Evenge dispone de las siguientes funcionalidades:  
* Calendario
* Creación de eventos
* Registro de ponentes
* Control de asistencia
* Generación de diplomas
* Registro del número de personas que han asistido
* Generación de informes sobre los eventos: lugar, asistencia.

#### Desarrolladores:

* [Carlos Campos Fuentes](http://github.com/ccamposfuentes)
* [Iván Ortega Alba](http://github.com/ivanortegaalba)
* [Francisco Javier Expósito Cruz](http://github.com/franexposito)
* [Victor Coronas Lara](http://github.com/VictorCoronas)

-------------------------
**Aplicación**: [evenge-2014.appspot.com](https://evenge-2014.appspot.com)  
**Email**: [desarrollo.evenge@gmail.com](mailto://desarrolo.evenge@gmail.com)  
**Blog**: [evenge.github.io](http://evenge.github.io)  
**Twitter**: [@grupoEvenge](https://twitter.com/grupoEvenge)  
**Entorno de desarrollo**: [Docker](https://registry.hub.docker.com/u/ivanortegaalba/evenge/)

-------------------------

## Aportaciones de cada miembro:

### Carlos Campos:
* Scripts de provisionamiento
  * Commits:
  * Pull Request:
  * Issues:
* Tests:
  * Commits:
  * Pull Request:
  * Issues:
* Configuración de integración continua y PaaS:
  * Commits:
  * Pull Request:
  * Issues:
* Configuración de despliegue automático:
  * Commits:
  * Pull Request:
  * Issues:

### Victor Coronas:
* Scripts de provisionamiento
  * Commits:
  * Pull Request:
  * Issues:
* Tests:
  * Commits:
  * Pull Request:
  * Issues:
* Configuración de integración continua y PaaS:
  * Commits:
  * Pull Request:
  * Issues:
* Configuración de despliegue automático:
  * Commits:
  * Pull Request:
  * Issues:

### Fran Expósito:
* Scripts de provisionamiento
  * Commits:
  * Pull Request:
  * Issues:
* Tests:
  * Commits:
  * Pull Request:
  * Issues:
* Configuración de integración continua y PaaS:
  * Commits:
  * Pull Request:
  * Issues:
* Configuración de despliegue automático:
  * Commits:
  * Pull Request:
  * Issues:

### Ivan Ortega:
* PROVISIONAMIENTO y PaaS:

  * Aportación al Dockerfile:
    * https://github.com/evenge/EVENGE/issues/70

  * Aportación al Script de instalación de Dockerfile y todo lo necesario para descargar la imagen de DockerHub:
    * https://github.com/evenge/EVENGE/issues/70

  * Aportaciones Funcionales a la Aplicación:

    * Añadido estilo al formulario Usuario y añadida la barra de menu
      * https://github.com/evenge/EVENGE/commit/91fcd617f4dd2a8f27792fed6a4e4f127486558a

    * Plantillas con Jinja y herencia entre ellas generica, asistente y corrige bug:
      * https://github.com/evenge/EVENGE/issues/35
      * https://github.com/evenge/EVENGE/issues/36
      * https://github.com/evenge/EVENGE/issues/37

    * Listar todos los eventos:
      * https://github.com/evenge/EVENGE/issues/38
    * Añadir la biblioteca Fontawesome de iconos
      * https://github.com/evenge/EVENGE/issues/95
    * Arreglo de bug en vista:
      * https://github.com/evenge/EVENGE/issues/93
    * Añadido el footer a la plantilla esqueleto (Con gif de celebración incuido):
      * https://github.com/evenge/EVENGE/issues/87
    * Añadido navegador:
      * https://github.com/evenge/EVENGE/issues/92
    * Añadida plantilla para usuario:
      * https://github.com/evenge/EVENGE/issues/89
      * https://github.com/evenge/EVENGE/issues/106

* Integración continua:
  * Configuración y explicación del papel de Shippable para la CI
    * https://github.com/evenge/EVENGE/issues/146

* Test:
  * Test para la inserción de usuarios con NoseGAE
    * https://github.com/evenge/EVENGE/issues/161
  * Funcionamiento de NoseGAE junto a Shippable:
    * https://github.com/evenge/EVENGE/issues/163
* Despliegue:
  * Configuración de Shippable para despliegue con push en rama master.
    * https://github.com/evenge/EVENGE/issues/146

# Documentación:

  - [Provisionamiento](https://github.com/evenge/EVENGE/blob/master/docs/dockerfile.md)
  - [Integración continua](https://github.com/evenge/EVENGE/blob/master/docs/integracion-continua.md)
  - [Testeo]()
  - [Despliegue de la aplicación](https://github.com/evenge/EVENGE/blob/master/docs/despliegue-aplicacion.md)
