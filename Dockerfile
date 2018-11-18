# Imagen de python a usar
FROM python:3.6

# Directorio donde va a alojarse la aplicación
WORKDIR /app

# Copiar los contenidos del repositorio al directorio
COPY . /app

# Instalar librerías necesarias de requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Establecer 5000 como puerto por defecto. Este comando se ignora en el despliegue de Heroku
EXPOSE 5000

# Cuando se lanza el contenedor se ejecuta QRS.py
ENTRYPOINT ["python3"]
CMD ["QRS.py"]
