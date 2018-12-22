from fabric.api import *

def IniciarApp():
		# Iniciar aplicación.
        run ('echo inicia app')
        run('cd /vagrant/prz/QRS.py && sudo gunicorn QRS:app -b 0.0.0.0:80')
