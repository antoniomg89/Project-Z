# Documentación de Docker

### Pasos para configurar Docker:

Instalar Docker en el sistema y crear una cuenta en [Docker Hub](https://hub.docker.com/).

Hecho esto se crea una "automated build" y se selecciona el repositorio del cual va a crear el contenedor.

![DOCKER_HUB1](./img/DockerHub-1.png)

En el repositorio de de github que se ha enlazado con Docker Hub hay que crear el correspondiente dockerfile, que contendrá las instrucciones necesarias para crear el contenedor.

~~~
# Use an official Python runtime as a parent image
FROM python:3.6

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
ENTRYPOINT ["python3"]
CMD ["QRS.py"]

~~~

Con esto las próximas veces que se haga un push al repositorio de Github se actualizará el contenedor de forma automática.

### Pasos para configurar el despliegue del contenedor en Heroku:

El despliegue automático del contenedor se realizará con Travis.

Como se va a ejecutar el comando docker es necesario indicar en el archivo que se va a hacer uso de **sudo**:

~~~
sudo: required

services:
  - docker
~~~

El siguiente paso es iniciar sesión en Docker Hub:

~~~
sudo: required
language: python
python:
  - "3.6"

services:
  - docker

before_install:
  - echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
~~~

Para iniciar la sesión se crean dos variables de entorno (DOCKER_PASSWORD y DOCKER_USERNAME) en Travis. Estas variables creadas contendrán el usuario y contraseña de Docker Hub.


Ahora que ya se ha iniciado sesión ya se puede construir la imagen y hacer un push a Docker Hub.

~~~
sudo: required
language: python
python:
  - "3.6"

services:
  - docker

before_install:
  - echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin

install:
  - pip3 install -r requirements.txt

script:
  - pytest
  - docker build -t antoniomg89/project-z-iv .

deploy:
  provider: script
  script:
    docker push antoniomg89/project-z-iv;
branch: master
~~~

En el push indicamos nombrecuenta/repositorio donde se va a subir la imagen.

Con lo realizado hasta ahora el despliegue siempre será posterior a la ejecución de los tests, de esta forma si fallasen no se ejecutan las instrucciones de *deploy*.

Con *branch: master* se indica el cambio a dicha rama en el despliegue para asegurarnos en caso de tener alguna otra más.

Hasta ahora tendríamos la parte de tests y docker realizada.

#### 3. Configuracion travis.yml y Heroku

El siguiente paso es realizar el despliegue del contenedor en Docker Hub a Heroku. Para ello es necesario tener instalado Heroku CLI.

~~~
before_install:
  - wget -qO- https://toolbelt.heroku.com/install.sh | sh
  - echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
- echo "$HEROKU_PASSWORD" | docker login -u "$HEROKU_USERNAME" --password-stdin registry.heroku.com
~~~
Esta parte contiene la instalación de Heroku CLI y el inicio de sesión en Heroku.

Con esto es necesario agregar dos variables de entorno más en Travis (HEROKU_PASSWORD y HEROKU_USERNAME).

La variable HEROKU_USERNAME ha de ser: **_**

Para HEROKU_PASSWORD ha de generarse un token con Heroku CLI de la siguiente forma:

~~~
$heroku authorizations:create
~~~

A continuación en Heroku, seleccionamos la aplicación creada previamente en el anterior hito, pero ya no la vinculamos con el repositorio de Github puesto que lo que queremos es que se realize el despliegue desde el contenedor y no desde el repositorio de Github.d

El nombre de la aplicación en Heroku también lo añadimos a una nueva variable de entorno en Travis ($HEROKU_APP_NAME).

Una vez realizado esto hay que hacer un push de la imagen de Docker en Heroku en travis.yml:

~~~
script:
  - pytest
  - docker build -t antoniomg89/project-z-iv .
  - docker tag antoniomg89/project-z-iv registry.heroku.com/$HEROKU_APP_NAME/web

deploy:
  provider: script
  script:
    docker push antoniomg89/project-z-iv;
    docker push registry.heroku.com/$HEROKU_APP_NAME/web;

branch: master
~~~

Para terminar se hace uso del comando heroku release. Esto requiere de otra variable de entorno en Travis (HEROKU_API_KEY) ya que es necesario estar autentificado en Heroku CLI. El valor de esta variable lo obtenemos de la cuenta creada en Heroku:

![HEROKU_API_KEY](./img/Heroku_API_KEY.png)

Para terminar se añade el último comando para realizar el despliegue quedando el archivo travis.yml así:

~~~
sudo: required
language: python
python:
  - "3.6"

services:
  - docker

before_install:
  - wget -qO- https://toolbelt.heroku.com/install.sh | sh
  - echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
  - echo "$HEROKU_PASSWORD" | docker login -u "$HEROKU_USERNAME" --password-stdin registry.heroku.com

install:
  - pip3 install -r requirements.txt

script:
  - pytest
  - docker build -t antoniomg89/project-z-iv .
  - docker tag antoniomg89/project-z-iv registry.heroku.com/$HEROKU_APP_NAME/web

deploy:
  provider: script
  script:
    docker push antoniomg89/project-z-iv;
    docker push registry.heroku.com/$HEROKU_APP_NAME/web;
    heroku container:release web --app $HEROKU_APP_NAME
branch: master
~~~

Las variables de entorno creadas en Travis quedarían así:

![TRAVIS_ENV_VARS](./img/Travis_ENV_VARS.png)

De esta forma cada vez que se haga un push en el repositorio de Github se realiza todo de forma automática(Tests, Docker y Heroku).
