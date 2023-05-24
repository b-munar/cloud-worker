Para levantar los servicios es necesario tener docker-compose descargado y ejecutar los siguientes comandos:

> docker build -t worker-image  .
> docker run --name worker-container -it -e PORT=5000 -p 5000:5000 worker-image