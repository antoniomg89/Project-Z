# Project-Z

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

***

Este proyecto será un servicio generador y validador de códigos QR.


Hará uso de una base de datos NoSQL como MongoDB.


Para su desarrollo se usará Flask como framework y python de lenguaje.

***

La clase [qrclass](https://github.com/antoniomg89/Project-Z/tree/master/doc/info.md) tiene dos propósitos:
- La creación de un código QR en base a un tamaño, borde e información que contendrá.

- La comprobación de un código QR en base a su información contenida.


## Instalar bibliotecas

~~~
pip3 install -r requirements.txt
~~~

## Para realizar los tests [![Build Status](https://travis-ci.com/antoniomg89/Project-Z.svg?branch=master)](https://travis-ci.com/antoniomg89/Project-Z)



~~~
pytest

python3 test_qrclass.py
~~~

## Despliegue Heroku

- ### Heroku [![Deploy to Heroku](https://www.herokucdn.com/deploy/button.png)](https://projectz-iv.herokuapp.com/genQR)
  - [Despliegue](https://projectz-iv.herokuapp.com/status)

  - [Documentación](https://github.com/antoniomg89/Project-Z/blob/master/doc/Despliegue%20Heroku.md)

- ### Azure
    - [Despliegue](https://projectz-iv.azurewebsites.net/genQR)(inactivo)

    - [Documentación](https://github.com/antoniomg89/Project-Z/blob/master/doc/Despliegue%20Azure.md)

## Docker

  - Contenedor: https://projectz-iv.herokuapp.com/status

  - [Documentación](https://github.com/antoniomg89/Project-Z/blob/master/doc/Docker.md)

  - [Docker Hub](https://hub.docker.com/r/antoniomg89/project-z/):

    Para ejecutar el contenedor en local:
    ~~~
    $docker run -p 5000:5000 antoniomg89/project-z:latest
    ~~~

## Provisionamiento y despliegue en Google Cloud Platform

  - Despliegue final: 35.246.76.197
  
  - [Documentación](https://github.com/antoniomg89/Project-Z/blob/master/doc/Despliegue%20final.md)
