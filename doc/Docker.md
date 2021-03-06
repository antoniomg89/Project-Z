# Documentación de Docker

### Pasos para configurar Docker:

Instalar Docker en el sistema y crear una cuenta en [Docker Hub](https://hub.docker.com/).

Hecho esto se crea una "automated build" y se selecciona el repositorio del cual va a crear el contenedor.

![DOCKER_HUB1](./img/DockerHub-1.png)

![DOCKER_HUB2](./img/DockerHub-2.png)

En el repositorio de de github que se ha enlazado con Docker Hub hay que crear el correspondiente dockerfile, que contendrá las instrucciones necesarias para crear el contenedor.

~~~
# Imagen de python a usar
FROM python:3.6

# Directorio donde va a alojarse la aplicación
WORKDIR /app

# Copiar los contenidos del repositorio al directorio
COPY . /app

# Instalar librerías necesarias de requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Establecer 5000 como puerto por defecto. Este comando se ignora en el despliegue de Heroku)
EXPOSE 5000

# Cuando se lanza el contenedor se ejecuta QRS.py
ENTRYPOINT ["python3"]
CMD ["QRS.py"]

~~~

Con esto las próximas veces que se haga un push al repositorio de Github se actualizará el contenedor de Docker Hub forma automática.

### Pasos para configurar el despliegue del contenedor en Heroku:

El despliegue automático del contenedor se realizará con Travis.

Un resumen de los motivos por los cuales he decidido hacerlo así es que se tarda unos minutos (más de 3) en crear la imagen en Docker Hub, por tanto el despliegue automático del contenedor se ve afectado por esto. Si se realiza una copia del contenedor dentro de .travis.yml y se despliega a Heroku nada más pasar los tests se tarda menos de dos minutos. De esta forma tenemos la misma aplicación desplegada pero en mucho menos tiempo.

Como se va a ejecutar el comando docker es necesario indicar en el archivo que se va a hacer uso de **sudo**:

~~~
sudo: required
language: python
python:
  - "3.6"

services:
  - docker

install:
  - pip3 install -r requirements.txt

script:
  - pytest
  - docker build -t antoniomg89/project-z .
~~~

Se trata de realizar el despliegue del contenedor nada más pasar los tests.

El siguiente paso es realizar el despliegue del contenedor a Heroku. Para ello es necesario tener instalado Heroku CLI.

~~~
before_install:
  - wget -qO- https://toolbelt.heroku.com/install.sh | sh
  - echo "$HEROKU_PASSWORD" | docker login -u "$HEROKU_USERNAME" --password-stdin registry.heroku.com
~~~
Esta parte contiene la instalación de Heroku CLI y el inicio de sesión en Heroku.

Con esto es necesario agregar dos variables de entorno en Travis (HEROKU_PASSWORD y HEROKU_USERNAME).

La variable HEROKU_USERNAME ha de ser: **_**

Para HEROKU_PASSWORD ha de generarse un token con Heroku CLI de la siguiente forma:

~~~
$heroku authorizations:create
~~~

A continuación en Heroku, seleccionamos la aplicación creada previamente en el anterior hito, pero ya no la vinculamos con el repositorio de Github puesto que lo que queremos es que se realize el despliegue desde el contenedor y no desde el repositorio de Github.

El nombre de la aplicación en Heroku también lo añadimos a una nueva variable de entorno en Travis ($HEROKU_APP_NAME).

Una vez realizado esto hay que hacer un push de la imagen de Docker a Heroku.

~~~
script:
  - pytest
  - docker build -t antoniomg89/project-z .
  - docker tag antoniomg89/project-z registry.heroku.com/$HEROKU_APP_NAME/web

deploy:
  provider: script
  script:
    docker push registry.heroku.com/$HEROKU_APP_NAME/web;
~~~

Para terminar se hace uso del comando heroku release. Esto requiere de otra variable de entorno en Travis (HEROKU_API_KEY) ya que es necesario estar autentificado en Heroku CLI. El valor de esta variable lo obtenemos de la cuenta creada en Heroku:

![HEROKU_API_KEY](./img/Heroku_API_KEY.png)

Se añade el último comando para realizar el despliegue quedando el archivo .travis.yml así:

~~~
sudo: required
language: python
python:
  - "3.6"

services:
  - docker

before_install:
  - wget -qO- https://toolbelt.heroku.com/install.sh | sh
  - echo "$HEROKU_PASSWORD" | docker login -u "$HEROKU_USERNAME" --password-stdin registry.heroku.com

install:
  - pip3 install -r requirements.txt

script:
  - pytest
  - docker build -t antoniomg89/project-z .
  - docker tag antoniomg89/project-z registry.heroku.com/$HEROKU_APP_NAME/web

deploy:
  provider: script
  script:
    docker push registry.heroku.com/$HEROKU_APP_NAME/web;
    heroku container:release web --app $HEROKU_APP_NAME
~~~

Las variables de entorno creadas en Travis quedarían así:

![TRAVIS_ENV_VARS](./img/Travis_ENV_VARS.png)

Haciéndolo de esta forma  cada vez que se haga un push en el repositorio de Github se actualiza el contenedor en Docker Hub a la vez que se despliega en Heroku con la ventaja de que el contenedor quedaría creado y desplegado en menos tiempo de lo que tarda solo en construirse en Docker Hub.
