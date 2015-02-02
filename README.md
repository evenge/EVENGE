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

- [Dockerfile](https://github.com/evenge/EVENGE/blob/master/docs/dockerfile.md)
- [Integración continua](https://github.com/evenge/EVENGE/blob/master/docs/integracion-continua.md)
- [Despliegue de la aplicación](https://github.com/evenge/EVENGE/blob/master/docs/despliegue-aplicacion.md)
- [Testeo](https://github.com/evenge/EVENGE/blob/master/docs/Testeo.md)

#### Aportaciones de cada miembro:

## Carlos Campos:
* Scripts de provisionamiento
  * Commits: [fc552a28a210b849253e7b91e56feedb2f1d6308](https://github.com/evenge/EVENGE/commit/fc552a28a210b849253e7b91e56feedb2f1d6308)
  * Pull Request: [#154](https://github.com/evenge/EVENGE/pull/154)
  * Issues: [#143](https://github.com/evenge/EVENGE/issues/143)
* Tests:
  * Commits: [b9daa61139cedd10d16543a8f00aed66f3f3295c](https://github.com/evenge/EVENGE/commit/b9daa61139cedd10d16543a8f00aed66f3f3295c), [2e75aa52f71454582a1887cd42ab251de261c002](http://github.com/evenge/EVENGE/commit/2e75aa52f71454582a1887cd42ab251de261c002)
  * Pull Request: [#157]( https://github.com/evenge/EVENGE/pull/157)
  * Issues: [#145](https://github.com/evenge/EVENGE/issues/145), [#17](https://github.com/evenge/EVENGE/issues/17), [#165](https://github.com/evenge/EVENGE/issues/165), [#36](https://github.com/evenge/EVENGE/issues/36), [#51](https://github.com/evenge/EVENGE/issues/51), [#34](https://github.com/evenge/EVENGE/issues/34), [#61](https://github.com/evenge/EVENGE/issues/61), [#27](https://github.com/evenge/EVENGE/issues/27), [#85](https://github.com/evenge/EVENGE/issues/85), [#86](https://github.com/evenge/EVENGE/issues/86), [#83](https://github.com/evenge/EVENGE/issues/83), [#107](https://github.com/evenge/EVENGE/issues/107),
* Configuración de integración continua y PaaS:
  * Commits: [750380ea1f48d3a42fa522498fe5f6dc06aca049](https://github.com/evenge/EVENGE/commit/750380ea1f48d3a42fa522498fe5f6dc06aca049), [9f6ef41663034f0b80b62064971131a184666600](https://github.com/evenge/EVENGE/commit/9f6ef41663034f0b80b62064971131a184666600), [0153a045ad3c50515b61872ae8674a2ba7e36ccc](https://github.com/evenge/EVENGE/commit/0153a045ad3c50515b61872ae8674a2ba7e36ccc), [ef818b2e930cc9955ddfac9a239d1031394a5ccd](https://github.com/evenge/EVENGE/commit/ef818b2e930cc9955ddfac9a239d1031394a5ccd), [962510c7aa861655880c76b9cbf1ec410b204cdb](https://github.com/evenge/EVENGE/commit/962510c7aa861655880c76b9cbf1ec410b204cdb)
  * Pull Request:  [#138](https://github.com/evenge/EVENGE/pull/138), [#113](https://github.com/evenge/EVENGE/pull/113)
  * Issues: [#133](https://github.com/evenge/EVENGE/issues/133), [#107](https://github.com/evenge/EVENGE/issues/107)
* Configuración de despliegue automático:
  * Commits: [fc552a28a210b849253e7b91e56feedb2f1d6308](https://github.com/evenge/EVENGE/commit/fc552a28a210b849253e7b91e56feedb2f1d6308)
  * Pull Request: [#154](https://github.com/evenge/EVENGE/pull/154)
  * Issues: [#143](https://github.com/evenge/EVENGE/issues/143)

## Victor Coronas:
* Scripts de provisionamiento:
  * Commits: [wiki](https://github.com/evenge/EVENGE/wiki/Desplegar-el-entorno-de-desarrollo/a223122130b773bc628729e84c52f0595665d6a8), [Post](https://github.com/evenge/evenge.github.io/commit/303912c6d803540fb8b4f9017570d8a4e80f5f36#diff-1d0c6a774c173c2999a04ee7b5b6feeb)
  * Issues:[1](https://github.com/evenge/EVENGE/issues/148), [2](https://github.com/evenge/EVENGE/issues/144), [3](https://github.com/evenge/EVENGE/issues/139)


* Tests:
  * Commits: [Post](https://github.com/evenge/evenge.github.io/commit/a97be29b3a72cc0ef20d984218ca3440c25056fb#diff-3fffece9f737baf1e2b9d51d56a3ad0c),[Wiki](https://github.com/evenge/EVENGE/wiki/Ejecutar-test/d6069feeaf3f2d9f38c51d042babe9853d272519),
  * Issues:[1](https://github.com/evenge/EVENGE/issues/152), [2](https://github.com/evenge/EVENGE/issues/148),  [3](https://github.com/evenge/EVENGE/issues/139), [4](https://github.com/evenge/EVENGE/issues/147),
  [5](https://github.com/evenge/EVENGE/issues/7),
  [6](https://github.com/evenge/EVENGE/issues/150),
  [7](https://github.com/evenge/EVENGE/issues/6),
  [8](https://github.com/evenge/EVENGE/issues/18),
  [9](https://github.com/evenge/EVENGE/issues/32),
  [10](https://github.com/evenge/EVENGE/issues/40),
  [11](https://github.com/evenge/EVENGE/issues/43)


* Configuración de integración continua y PaaS:
  * Commits:[Post](https://github.com/evenge/evenge.github.io/commit/26791ced937512d3bb8d0b6d66732732f28a6e97#diff-4ceb80bbb705d7bbd146456089946507),[Wiki](https://github.com/evenge/EVENGE/wiki/Test-unitarios/1688149ce31c06103cef42c4a73a338d99f5e633)
  * Issues:[1](https://github.com/evenge/EVENGE/issues/151), [2](https://github.com/evenge/EVENGE/issues/148), [3](https://github.com/evenge/EVENGE/issues/139)


* Configuración de despliegue automático:
  * Commits: [Documentación](https://github.com/evenge/EVENGE/commit/401874a0e0e4244268e7a9a94ea94af93ef2651c#diff-5377c2487afc76788f872d39d21d3987),
[Post](https://github.com/evenge/evenge.github.io/commit/77e116bc946ff4ed27e7e35fd79a255ba06a3b2f#diff-feae184406671d7c9e74ea16ede72fce)
  * Issues:[Documentación](https://github.com/evenge/EVENGE/issues/153),
  [1](https://github.com/evenge/EVENGE/issues/148), [2](https://github.com/evenge/EVENGE/issues/139)

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
###Provisionamiento y PaaS
* Documentación de Dockerfile.
  * [#142](https://github.com/evenge/EVENGE/issues/142)
* Aportaciones funcionales a la aplicación
* Añadida platilla Asistente
  * [#54](https://github.com/evenge/EVENGE/issues/54)
* Añadido botón asistente para diploma
  * [#88](https://github.com/evenge/EVENGE/issues/88)
* Vista de Mi Cuenta
  * [#108](https://github.com/evenge/EVENGE/issues/108)
* Vista de Evento detallado
  * [#94](https://github.com/evenge/EVENGE/issues/94)
* Test de inserción de evento
  * [d8824c163e9e34ecf9ba3890d20661cf8931a5e5](https://github.com/evenge/EVENGE/commit/d8824c163e9e34ecf9ba3890d20661cf8931a5e5)

###Integración continua:
* Integración continua con Shippable
  * [#71](https://github.com/evenge/EVENGE/issues/71)

###Test
* Test e integración continua con Shippable
  * [#71](https://github.com/evenge/EVENGE/issues/71)
* Test de inserción de evento
  * [d8824c163e9e34ecf9ba3890d20661cf8931a5e5](https://github.com/evenge/EVENGE/commit/d8824c163e9e34ecf9ba3890d20661cf8931a5e5)

###Despliegue
* Despliegue automático con Shippable
  * [#71](https://github.com/evenge/EVENGE/issues/71)

###Otros
* Configuración de app.yaml para guardar en Datastore
  * [#21](https://github.com/evenge/EVENGE/issues/21)

### Ivan Ortega:
Link a todos los issues, en cada issue están todos los commits relacionados.
Hay más issues y commits, relacionados con gestión, organización y tareas externas de equipo que no están incluidos aqui.
Enlace a toda la historia de commits de Ivan Ortega: https://github.com/evenge/EVENGE/commits?author=ivanortegaalba
#### PROVISIONAMIENTO y PaaS:
  * Aportación al Dockerfile:
    * https://github.com/evenge/EVENGE/issues/70
    * https://github.com/evenge/EVENGE/issues/
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

#### Integración continua:
  * Configuración y explicación del papel de Shippable para la CI
    * https://github.com/evenge/EVENGE/issues/146

#### Test:
  * Test para la inserción de usuarios con NoseGAE
    * https://github.com/evenge/EVENGE/issues/161
  * Funcionamiento de NoseGAE junto a Shippable:
    * https://github.com/evenge/EVENGE/issues/163

#### Despliegue:
  * Configuración de Shippable para despliegue con push en rama master.
    * https://github.com/evenge/EVENGE/issues/146

# Documentación:

  - [Provisionamiento](https://github.com/evenge/EVENGE/blob/master/docs/dockerfile.md)
  - [Integración continua](https://github.com/evenge/EVENGE/blob/master/docs/integracion-continua.md)
  - [Testeo]()
  - [Despliegue de la aplicación](https://github.com/evenge/EVENGE/blob/master/docs/despliegue-aplicacion.md)
