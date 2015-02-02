# Integración continua.

Para provisionar nuestro proyecto con integración continua barajamos varias posibilidades.
 1. La sincronización directa con GitHub que nos provee GAE.
  Simplemente con añadir el repo donde tenemos el código, GAE sincroniza la app con el, y cuando se realice un push, se hará el despliegue automático.
  Esto es factible, si y solo si tenemos unicamente el código de la aplicación el el repo.
  Pero nosotros tenemos documentación, lista de tareas, etc. Por lo que no nos valía.

2. La segunda opción, y por la que nos decantamos finalmente, fue el despliegue por Shippable.
Este sistema de CI permite crear, provisionar, testear y desplegar nuestra app en una máquina virtual, en el servidor que queramos.
Además trabaja con IaaS y PaaS como Heroku, Amazon Elastic Beanstalk, OpsWorks AWS, Google App Engine, Red Hat OpenShift o cualquier proveedor de infraestructura después de una compilación exitosa.

## Shippable
### Introduccion

Shippable usa Docker para el despliegue de las apps.
Sus casos de uso más comunes, y concretamente los que vamos a darle en el proyecto son:
- Automatización del empaquetado y despliegue de web apps.
- Testeo automatizado y despliegue en caso de éxito.




Nosotros, por comodidad y compatibilidad, ya que GAE es muy especifico para muchos servicios de Google vamos a usar el SDK durante el desarrollo y los test de la app.
