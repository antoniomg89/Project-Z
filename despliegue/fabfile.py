from fabric.api import *

def IniciarApp():
		# Iniciar aplicación.
        run ('echo inicia app')
        run('python3 /vagrant/prz/QRS.py &',pty=False)
