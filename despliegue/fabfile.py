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
