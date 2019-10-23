# Despliegue final

Se ha hecho uso de vagrant para lanzar la vm y ansible como provisionamiento.

A continuación se muestra el fichero de provisionamiento de ansible:

~~~
# Hosts a los que conectarse para realizar el provisionamiento.
- hosts: all

  #Se va a hacer uso del superusuario para ejecutar gunicorn.
  #sudo: yes

  # Usuario a utilizar.
  remote_user: amgarcia

#  vars:
#    service_account_file: /home/amgarcia/II/Pruebas/projectz-1cb22d1d7fc5.json
#    project: projectz
#    auth_kind: serviceaccount

  # Tareas a realizar.
  tasks:

    # Agregar repositorio python 3.6
    - name: Agregar repositorio
      become: true
      apt_repository: repo=ppa:deadsnakes/ppa state=present

    # Actualizar apt.
    - name: Actualizar apt
      become: true
      apt:
        upgrade: yes
        update_cache: yes

    # Instalar Python 3.6.
    - name: Instalar Python 3.6
      become: true
      apt: pkg=python3.6 state=present

    # Instalar pip
    - name: Instalar pip
      become: true
      apt: pkg=python-pip state=latest

    # Instalo pip3.
    - name: Instalar pip3
      become: true
      apt: pkg=python3-pip state=latest

    # Instalar setuptools.
    - name: Instalar setuptools
      become: true
      pip: name=setuptools state=latest

    # Instalar git
    - name: Instalar git
      become: true
      apt: pkg=git state=latest

    # Clonar el repositorio de github
    - git:
        repo: https://github.com/antoniomg89/Project-Z.git
        dest: /vagrant/prz

    # Instalar Flask.
    - pip:
        name: Flask
        executable: pip3

    # Instalar Jinja2.
    - pip:
        name: Jinja2
        executable: pip3

    # Instalar Pillow.
    - pip:
        name: Pillow
        executable: pip3

    # Instalar qrcode.
    - pip:
        name: qrcode
        executable: pip3

    # Instalar gunicorn.
    - pip:
        name: gunicorn
        executable: pip3
~~~

Una vez se tiene el playbook.yml de ansible se configura el archivo Vagrantfile con la información necesaria para la creación de la vm:

~~~
Vagrant.configure("2") do |config|
    # VM.
    config.vm.box = "google/gce"

    config.vm.provider :google do |google, override|
        # ID del proyecto en google cloud platform.
        #google.google_project_id = ENV['ID_GCP']
        google.google_project_id ="projectz"

        # Email.
        #google.google_client_email = ENV['CEM']
        google.google_client_email = "iv-524@projectz.iam.gserviceaccount.com"

        # clave cuenta de servicio.
        #google.google_json_key_location = ENV['JLOC']
        google.google_json_key_location = "/home/amgarcia/II/proz.json"

        google.image_family = 'ubuntu-1604-lts'
        google.zone = 'europe-west2-a'
        google.name = 'projectz'
        google.machine_type = 'g1-small'

        # Configuración de usuario y clave privada para la conexión por SSH.
        override.ssh.username = 'amgarcia'
        override.ssh.private_key_path = '~/.ssh/google_compute_engine'
    end

    # Provisionamiento Ansible.
    config.vm.provision "ansible" do |ansible|
      ansible.playbook = "provision/playbook.yml"
    end
end
~~~

Para que se cree la vm de google es necesario instalar el plugin de google para vagrant.

También es necesario generar uns pareja de claves privada/pública para la conexión por ssh. Con la pareja creada (google_compute_engine, google_compute_engine.pub) se introduce el valor de la clave pública en los metadatos del proyecto quedando de la siguiente manera:

![DFinal0](./img/DFinal0.png)

También es necesario crear una clave JSON de cuenta de servicio del proyecto:

![DFinal1](./img/DFinal1.png)

Para crear la máquina por primera vez:

~~~
$vagrant up --provider=google
~~~

Ahora en la consola de google tenemos que habilitar a nuestra vm para recibir peticiones http/https que por defecto están deshabilitadas:

![DFinal2](./img/DFinal2.png)

Cuando ya está creada la vm se realiza:

~~~
$vagrant up
$vagrant provision
~~~

![DFinal3](./img/DFinal3.png)

Para terminar, con la vm creada y provisionada, se procede al despliegue del servicio con fabric:

Versión actual de fabfile.py:

~~~
#-*- coding: utf-8 -*-
from fabric.api import *


# Información del host
def prod():
    env.user = 'amgarcia'
    env.hosts = ['35.246.76.197']

# Iniciar aplicación con gunicorn
def arranca():
    run('cd /vagrant/prz/ && sudo gunicorn QRS:app -b 0.0.0.0:80')

# Detener proceso gunicorn
def para():
    sudo('pkill gunicorn')
~~~

Este archivo se ejecuta de las siguientes formas:

~~~
$fab prod arranca
$fab prod para
~~~

Se ha creado una vm de prueba (copia de la original del proyecto) para realizar las últimas pruebas con fabric, por lo que en la captura de pantalla varía la dirección ip.

Comprobamos que fabric se ejecuta correctamente y se puede acceder a nuestra dirección:

![DespliegueFabric](./img/DFabric.png)

## Bibliografía

Referente al Vagrantfile, claves ssh y fabfile.

https://blog.eduonix.com/system-programming/learn-use-vagrant-cloud/
https://cloud.google.com/compute/docs/instances/adding-removing-ssh-keys
https://stackoverflow.com/questions/2326797/how-to-set-target-hosts-in-fabric-file
