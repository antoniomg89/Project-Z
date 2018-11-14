# Use an official Python runtime as a parent image
FROM python:3.6

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Set proxy server, replace host:port with values for your servers
ENV http_proxy host:port
ENV https_proxy host:port

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
ENTRYPOINT ["python3"]
CMD ["QRS.py"]
