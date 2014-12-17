FROM ubuntu:latest
MAINTAINER Evenge <desarrollo.evenge@gmail.com>

RUN apt-get update && apt-get install -y python
RUN apt-get install -y python-setuptools
RUN easy_install pip
RUN apt-get install -y python-dev build-essential
RUN pip install webapp2
RUN pip install jinja2

# Instalamos wget para poder descargar archivos
RUN apt-get install -y wget

# Descargamos el sdk de Google App Engine
RUN wget https://storage.googleapis.com/appengine-sdks/featured/google_appengine_1.9.17.zip --no-check-certificate

# Instalamos la herramienta zip
RUN apt-get install -y zip

# Descomprimimos el fichero descargado, con lo que ya tendremos disponibles las herramientas del sdk
RUN unzip google_appengine_1.9.17.zip

#Instalamos el google-cloud-sdk y configuramos el proyecto Evenge
# RUN curl -sSL https://sdk.cloud.google.com | bash
# RUN gcloud auth login
# RUN gcloud config set project <google-cloud-project-id>

# Una vez hecho esto ya tenemos instalado el entorno de desarrollo necesario para construir y ejecutar aplicaciones que luego funcionarán bajo Google App Engine

RUN apt-get install -y git
RUN git clone git@github.com:evenge/EVENGE.git
RUN cd gestor-de-eventos
RUN git branch -b $USER
