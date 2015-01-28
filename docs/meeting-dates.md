Meeting dates
=====================
# 10 de Diciembre de 2014
###Place: CETIC office

Puntos a tratar en la reunión:
- Testeo de la aplicación con GAE.
- Corrección de un merge conflictivo (revisamos cada archivo del repositorio).
- Se revisa tema de permisos en una rama, para dejar solo a Carlos con permiso de escritura en **master**.

# 26 de Noviembre de 2014
###Place: CETIC office

Puntos a tratar en la reunión:
- Planteamiento, elección y aprendizaje sobre el uso de test en GAE.Posibles herramientas:[Local Unit Testing for Python](https://cloud.google.com/appengine/docs/python/tools/localunittesting)
Se resolverá en la OSL el miercoles que viene.

- Debate en como hacer la contribución al master del repositorio del proyecto: trabajando en fork, mergeando cuando estemos reunidos, nombramiento de administrador de pull request, etc.
Se le asigna el trabajo a Carlos Campos.

- Posible implementación de alguna funcionalidad con interacción entre vistas.

  - Se le dá prioridad a la obtención de datos del Datastore.

  - Además hacemos y estilamos las plantillas de los formularios.

IMPORTANTE: Tenemos que comentar el código.

# 19 de Noviembre de 2014
###Place: CETIC office

- Al final hemos decidido usar webapp2

- Vemos como hacer formularios con webapp2

- Creamos ramas independientes para no tocar la master hasta que todo este bien.

- Para aprender la interacción con BD usando el ORM de GAE, cada uno nos asignamos una de las interfaces con formularios que habrá en la app y la implementamos.

- Hacemos las tareas mediante el Board de ZenHub

- Todos nos pasmaos a usar Atom


# 12 de Noviembre de 2014
###Place: CETIC office

- Reordenamos la estructura del repositorio donde creamos la carpeta docs con la documentación del proyecto.

- Hablamos sobre la página web de información del producto.

- Discutimos el uso de "DJANGO" o "webapp2", mandamos correo a Sergio para ver si puede usar un entorno u otro.

- Hablamos sobre el modelo que vamos a seguir en el diseño de las clases, entidades, tablas.

# 6 de Noviembre de 2014
###Place: ETSIIT -1.1

####Explicación por Fran de la interacción con GAE.

GAE, en principio vemos la diferencia del uso de BD. Nosotros tendremos nuestro proyecto con su estructura de directorios, y dispondremos de una API para comunicarnos con el Data Store.

El Data Store se basa en Tipos y Entidades.
Tendremos Entidades de un tipo, pueden tener distintos atributos, y dispondremos de Clases de las que extender nuestras entidades.
Otra cosa a tener en cuenta son los indices del Data Store.

Para comprobar algun tipo de consulta, accederemos en GAE a Query. En query podremos crear consultas en GQL, comprobar que funcionan, y si no fuera así tendriamos que agregar, el condigo que nos indique, al archivo index.yaml.

Acordamos usar Bootstrap.

Planificación de la estructura de directorios y ficheros, en función a las necesidades de nuestro programa.

# 21 de Octubre de 2014
###Place: ETSIIT -1.1
Hemos hablado con JJ y nos ha planteado las necesidades del proyecto.
Nos ha comentado la necesidad de hacerlo en nube, ya que los servidores que tienen no están acondicionados y necesitaría muchas modificaciones y instalaciones para ponerlo en funcionamiento.
Además hemos de tener en cuenta que no tienen administradores de sistemas, y que sería dificil por su parte mantener la infraestructura.
Por todos estos motivos, hemos decidido hacerlo en Google App Engine.
Hemos creado una descripción o esquema del desarrollo y requisitos.
Decidimos hacerlo con ingeniería del software simple: RF, Diag, de clases y lo que venga.

# 15 de Ocubre 2014

###Place: CETIC office
Comprendemos lo que nos pide la descripción del proyecto por parte del interesado.
Proponemos herramientas para el desarrollo, planificación, despliegue y testeo.
Establecer objetivos o linea de vida del proyecto.

Tormenta de ideas:
uso de google maps
uso de mvc
fuera de paas
