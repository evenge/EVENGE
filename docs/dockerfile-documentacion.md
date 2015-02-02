#Docker
[Docker](https://www.docker.com/) es un una plataforma para desarrolladores y administradores de sistema que te permite desarrollar, desplegar y ejecutar aplicaciones. Docker permite testear el codigo y desplegarlo en producción rápidamente.  

##Introducción
En Evenge hemos decidido automatizar el proceso de instalación del docker mediante [este](https://github.com/evenge/EVENGE/blob/master/despliegue/Dockerfile) script.

##Docker
####Explicando el script
En primer lugar tendremos que instalar las depencencias de python que necesitamos:

* Python
* Python setuptools
* [Pip](https://pypi.python.org/pypi/pip/)
* Python build-essential
* wget
* zip

```
RUN apt-get update && apt-get install -y python
RUN apt-get install -y python-setuptools
RUN easy_install pip
RUN apt-get install -y python-dev build-essential
RUN apt-get install -y wget
RUN apt-get install -y zip
```

Después tendremos que instalar los distintos frameworks que vamos a usar en el desarrollo de nuestra aplicación. En nuestro caso son dos:

* webapp2
* jinja

Los motivos de porque hemos usado estos frameworks están mejor detallados [aqui](http://evenge.github.io/general/2014/12/16/uso-de-webapp2-y-jinja2/).

```
RUN pip install webapp2
RUN pip install jinja2
```

El siguiente paso es descargar el SDK de GAE y descomprimirlo:

```
RUN wget https://storage.googleapis.com/appengine-sdks/featured/google_appengine_1.9.17.zip --no-check-certificate
RUN unzip google_appengine_1.9.17.zip
```

Tras descargar y descomprimir el SDK de GAE nos toca instalar el google-cloud-sdk y configurar el proyecto Evenge:

```
RUN curl -sSL https://sdk.cloud.google.com | bash
RUN gcloud auth login
RUN gcloud config set project <google-cloud-project-id>
```

El último paso es instalar git y clonar nuestro repostorio:

```
RUN apt-get install -y git
RUN git clone https://github.com/evenge/EVENGE.git
RUN cd EVENGE && git branch -b $USER
```

Una vez realizados todos los pasos tendremos desplegado nuestro entorno de desarrollo.


##Script de automatización de Docker
####Introducción
También hemos hecho un Script que automatiza el proceso de instalación de Docker. A continuación la explicación paso a paso.

####Explicación del script
En primer lugar, se instala Docker y las dependencias necesarias:

´´´
su -c 'apt-get update
apt-get install -y docker.io
source /etc/bash_completion.d/docker.io
[ -e /usr/lib/apt/methods/https ] || {
  apt-get update
  apt-get install -y apt-transport-https
}
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 36A1D7869245C8950F966E92D8576A8BA88D21E9
sh -c "echo deb https://get.docker.com/ubuntu docker main\
> /etc/apt/sources.list.d/docker.list"
apt-get update
apt-get install -y lxc-docker
´´´

Tras esto nos descargamos la imagen producida con el Dockerfile y la ejecutamos:

```
docker pull ivanortegaalba/evenge
docker run -t -i ivanortegaalba/evenge /bin/bash'
```
