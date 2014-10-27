#Gevent

### Descripción breve del proyecto

Gevent será una aplicación de gestión de eventos o saraos, la cual nos permitirá crear, notificar y crear informes en base a los asistentes.

Todo esto por supuesto en un entorno Cloud, es decir, en una aplicación integramente en la nube, con todas las ventajas que esto conlleva.

Pordrá hacerse uso de listas de asistencias, generación de informes y diplomas, publicación mediante Twitter, correo y blog. 

###Características principales

- **Gestión de usuarios** de la plataforma.
    
- Gestión de **información acerca del evento** (ponentes, lugar, temática, asistentes, etc)
    
- **Inscripción** por parte del asistente al evento y **publicación automática** en las redes sociales.

- **Control de asistencia** mediante lista.
	
- **Publicación del material** relacionado con el evento (Fotos, documentos, asistencia, etc)
	
- Gestión de **calendario** con los eventos próximos
	
- Generación a partir de evento de **diplomas** para los asistentes e **informes** para los organizadores incluyendo información acerca del evento (asistentes, ponentes, resumen del evento, etc).

###Razones por las que elegir Cloud y una PaaS como Google App Engine

El primer inconveniente surge de **la necesidad de montar, configurar y mantener un servidor** donde alojar la aplicación, que conlleva el tener un servidor físico, del cual no disponemos y un administrador de sistemas que mantenga ese servidor disponible, el que tampoco tenemos.

La principal ventaja que nos ofrece un PaaS como GAE es el poder trabajar sobre una plataforma que te ofrece todas las utilidades necesarias para esta aplicación: como la base de datos(**Data Store**), leguajes de programación web que cubren nuestras necesidades (**Python**) y utilidades de testeo, además de contar con *frameworks* que facilitan estas tareas.

Además GAE cuenta con una fácil interacción con herramientas como **Google Docs**(para la creación de formularios), **Google Calendar** (para llevar el calendario de eventos) y **Gmail** (para publicitar los eventos por email).

Otra ventaja más, es el evitarnos pruebas de testeo por parte de aplicaciones que tendríamos que lanzar manualmente sobre nuestra aplicación en el servidor. Para ello **GAE nos proporciona una serie de herramientas de testeo**. En particular nos ofrece dos herramientas diferente:
 - [Local Unit Testing for Python](https://cloud.google.com/appengine/docs/python/tools/localunittesting), que nos permite realizar un testeo de nuestra aplicacion web durante el desarrollo, que nos ayuda a testear el código, nos ayuda en el diseño del proyecto, así como la reutilización y mantenimiento del código. Todo ello a nivel loca, sin la necesidad de desplegarla en App Engine.
 - [Handler Testing For Python](https://cloud.google.com/appengine/docs/python/tools/handlertesting), que nos permite testear la aplicacion por completo o por módulos de código, para ello hacemos uso de WebTest, que nos permite interactuar sin estar en un entorno de desarrollo de App Engine, todo esto de forma local, esta aplicacion nos falicitará mucho las cosas.

Otra de las ventajas que ofrece GAE es que el mantenimiento de la base de datos, la organización y la actualización corre a cuenta de Google de manera que siempre disponemos de una base de datos correctamente mantenida.  

Y por ultimo, por parte del despliegue, GAE nos evita el tener que configurar script para desplegar la app en un servidor físico. **GAE es facilmente desplegable** y mediante algunas utilidades nos **permitirá hacer exportaciones** si se quisiera migrar la aplicación.

En concreto, **el cliente primero de esta aplicación tiene el Django sin instalar en ningún servidor, no tiene administrador de sistemas disponible y problemas de infraestructura en sus servidores**, los cuales no pueden dar capacidad a este.

