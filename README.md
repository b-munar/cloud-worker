Para levantar los servicios es necesario tener docker-compose descargado y ejecutar los siguientes comandos:

> docker compose build

> docker compose up -d
 
 o

> docker-compose build

> docker-compose up -d

Para utilizar flower, ir al bash del server,

> docker exec -it "id desarrollo-software-nube-api-1" bash

y escribir en ese bash,

> poetry run celery -A tasks flower  --address=0.0.0.0 --port=5566

poetry run python
from tasks import queueing
queueing.delay()

Para utilizar prometheus, en una terminal a nivel de sistema

> docker run --name Prometheus -v $(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml -p 9090:9090 --network host prom/prometheus
