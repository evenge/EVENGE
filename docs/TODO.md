##Tareas pendientes
=====
- [X] Creación y adaptación del repositorio de GitHub
- [ ] La explicación del proyecto:
    - [ ] Descripción del proyecto
    - [ ] Método de desarrollo y porque hemos usado esa PaaS
        - JJ:
            - Interaccion con Google Docs,
            - Interaccion con Google Calendar
            - Posible uso de emailing con Google
            - Inconvenientes para usar Django en los servidores(no instalado)
            - Inconvenientes para administrar el sistema
            - Inconvenietes de infraestructura
    - [ ] Herramientas para el desarrollo
        * Falta incluir hasta que no hayamos hecho #7 y #6 *

- [X] Creación de la documentación para el proyecto

###Síntesis propia (Hablado con JJ):

- Usuarios de la plataforma
    - [ ] Todos en principio administradores

- [ ] Gestión de evento:
  - [ ] Creacion, modificación y borrado de eventos
    - [ ] Lugar hora titulo descripcion ponentes
    - [ ] Registro de ponentes
  - [ ] Inscripcion opcional al evento:
    - [ ] Cuando te registras que mande un twitter viral
    - [ ] Nuestro propio formulario de inscripcion
    - [ ] Registro de asistencia
        - [ ] Nombre
        - [ ] Email
        - [ ] Twitter
        - [ ] Dni
    - [ ] Pasar lista de asistentes

- [ ] Publicación del evento:
    - [ ] Datos del evento:
        - [ ] Material del evento:
        - [ ] Fotos
        - [ ] Asistencia
    - [ ] Blog - podemos generar la historia para la hitoria
    - [ ] Email - podemos ver si podemos conectar con la red ugr  
    - [ ] Calendar (Google)
    - [ ] Twitter

- [ ] Generación a partir de evento:
  - [ ] Diplomas:
    - [ ] Asistente
    - [ ] Dni
    - [ ] Nombre
    - [ ] Nota
    - [ ] Duracion del evento
    - [ ] Descripcion breve

  - [ ] Informes:
    -    Numero de usuarios
    -    Numero de eventos
    -    Tipo del evento
    -    Situacion del evento

Notas sobre desarrollo:

- Desarrollo en Google App Engine
- Podemos usar Django y Python, pero no Mongo DB(App Engine tiene DataStore)
- Formularios con Google Docs

Fuentes de consulta aconsejadas:  
[GAE Python](https://cloud.google.com/appengine/docs/python/gettingstartedpython27/introduction)  
[DataStore API](https://developers.google.com/datastore/docs/apis/javadoc/com/google/api/services/datastore/DatastoreV1.PropertyFilter.Operator)  
