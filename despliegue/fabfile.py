from fabric.api import *

def IniciarApp():
	# Iniciar aplicación con gunicorn.
    run ('echo inicia app')
    run('cd /vagrant/prz/ && sudo gunicorn QRS:app -b 0.0.0.0:80')
