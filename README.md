# Project-Z

***

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

[![Build Status](https://travis-ci.com/antoniomg89/Project-Z.svg?branch=master)](https://travis-ci.com/antoniomg89/Project-Z)

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.png)](https://projectz-iv.herokuapp.com/genQR)

[AZ](https://projectz-iv.azurewebsites.net/) (En pruebas)

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

## Para realizar los tests

~~~
pytest

python3 test_qrclass.py
~~~

## Heroku

- [Despliegue](https://projectz-iv.herokuapp.com/)

- [Documentación](https://github.com/antoniomg89/Project-Z/blob/master/doc/Despliegue%20Heroku.md)
