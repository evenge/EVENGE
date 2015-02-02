#DESPLIEGUE DE LA APLICACIÓN#


Antes de comenzar tenemos que saber que GAE tiene una serie de limitaciones si se usa de forma gratuita a la hora de desplegar nuestras aplicaciones, que son las siguientes:

- Tiene un espacio máximo de 10 aplicaciones de forma gratuita.

- Tiene cierta limitación en la cuota de visita(5 millones de visitas mensuales), ejemplo:

  Si 50 visitantes acceden a mi página, es probable que dicha cuota se encuentre en, aproximadamente, un 10%. Esto indicaría que si accedieran otros 450 visitantes se completaría la cuota, llegando al 100%, y mi aplicación quedaría pausada hasta el reinicio de todas las cuotas (cada 24hs).

- Tiene cierta limitación en el almacenamiento de datos(500MB de espacio), ejemplo:

  Si la cuota estándar (gratis) se limita a los 1000 MB de datos almacenados y nuestra aplicación alcanza dicha cantidad, podrá seguir recibiendo peticiones (si es que no se ha alcanzado el máximo de ésta cuota), pero no podrá continuar almacenando en la base de datos.


Para ello se puede contratar más de cantidad de visitas como de almacenamiento.

#Registro#
Antes de despleglar nuestra aplicación debemos de registrar nuestra aplicacion en [appengine.google.com](https://accounts.google.com/ServiceLogin?service=ah&passive=true&continue=https%3A%2F%2Fappengine.google.com%2F_ah%2Fconflogin%3Fcontinue%3Dhttps%3A%2F%2Fappengine.google.com%2F&ltmpl=ae)
Una vez ingresado, presiona en el botón “Create Application”.

[![GAE](http://recursospython.com/wp-content/uploads/2013/10/4.png)]()

Ahora procedemos a rellenar los campos teniendo en cuenta lo siguiente:

- Application Identifier: dominio por el cual tendremos acceso a nuestra aplicación. Utiliza el botón “Check Availability” para verificar que esté disponible.
- Application Title: título para la aplicación. No es muy relevante pero no puede ser cambiado. Te recomiendo un nombre en minúsculas y sin espacios.
En los demás campos deja los valores por defecto.
Por último presiona "Create Application". Una vez creada, dirígete nuevamente a appengine.google.com y verás tu aplicación en la lista.


#Ejecutar nuestra apliación en local#

Un paso muy importante antes de desplegar nuestra aplicación en el servidor de GAE, es desplegarla "Localmente", para realizar las pertinentes pruebas y test de funcionamiento.

[Linux]()

Si usamos  linux se realizaria de la siguiente manera en la terminal introduciendo estos comandos:

Iniciar el servidor de desarrollo local indica lo siguiente en la terminal:

      dev_appserver.py ubicacionapp

Por defecto el puerto 8080 será utilizado. Para cambiarlo, indica:

      dev_appserver.py --port=8081 ubicacionapp/

[Mac y Windows]()

Mac y Windows cuentan con un "Laucher" para esta tarea, ambos "Laucher" son iguales así que realizaré la explicación en Mac.

Lo primero que debemos de hacer es instalar el [SDK](https://cloud.google.com/appengine/downloads), en caso de no tenerlo instalado.

Una vez que lo tenemos instalado, vamos a crear el proyecto en con el "Laucher" que se nos ha instalado.

En mi caso yo uso Mac, así que simplemente tenemos que ejecutar el Launcher de GAE que hemos instalado.

Cuando se haya ejecutado le tenemos que dar al botón "+" que se encuentra en la parte inferior izquierda.

Cuando hayamos hecho eso, se nos abrirá una ventanita donde debemos de buscar la carpeta que contiene nuestro proyecto, y también debemos de especificar el nombre que le queremos poner al proyecto para hacer las pruebas en local.

Los siguientes puertos vienen por defecto:
+ Admin port
+ Port

pero nosotros podemos especificar los que queramos.

Cuando ya tengamos todo listo, le damos al botón "Create", de esta manera el proyecto se nos creará y se añadira a la lista de proyectos.

Una vez realizados todos estos pasos, solo debemos de darle a botón "Run" y nuestro proyecto se ejecutará en local.

Ahora solo debemos de irnos a nuestro navegador y escribir:

localhost:8080


[![GAE](http://i.imgur.com/bX9LexV.png)]()

De esta manera se usaría en local nuestra aplicación y podreamos probar todo lo que queramos.

#Desplegar la aplicación definitivamente#

Una vez desarrollado la aplicación y testeado su funcionalidad en el servidor de desarrollo local, procederemos a desplegar
la aplicación en Google. Para usuarios de Linux el procedimiento será vía consola. Para Windows y Mac OS X utilizaremos el "Launcher".

[Linux]()

Abre la terminal y ejecuta:

      appcfg.py --email=yo@gmail.com update ubicacionapp/

- La opción --email indica la cuenta de Google en la cual se encuentra registrada la aplicación. Si tu dirección es @gmail.com, éste puede omitirse (--email=yo).
- Luego, será solicitada la contraseña.
- ubicacionapp/ indica la carpeta o ruta en donde se encuentra el archivo app.yaml junto con los demás, pero este primero determinará la existencia de una aplicación en dicha ruta para appcfg.py.
- En caso de haber especificado erróneamente la ubicación, se quejará diciendo:

      appcfg.py: error: Directory does not contain an Documents.yaml configuration file.


[Mac y Windows]()

Para este caso ejecutamos el "Laucher" y selecciona tu aplicación en la lista de aplicaciones. Luego, presiona el botón “Deploy” en la barra superior. La dirección de correo y contraseña serán solicitados. Al finalizar el proceso, la ventana “Delpoyment to Google” indicará que la misma puede ser cerrada.

[![GAE](http://i.imgur.com/LlyJ4F2.png)]()


De esta manera, ya se encuentra nuestra aplicación en funcionamiento.
[evenge-2014.appspot.com](evenge-2014.appspot.com)
