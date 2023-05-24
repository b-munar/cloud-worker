Para levantar los servicios es necesario tener docker-compose descargado y ejecutar los siguientes comandos:

> docker build -t worker-image  .
> docker run --name worker-container -it -e PORT=8080 -p 8080:8080 worker-image