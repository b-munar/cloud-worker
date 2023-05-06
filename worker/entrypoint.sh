#!/bin/bash

mkdir -p /home/celery/var/run/

poetry run celery -A tasks worker -B -s /home/celery/var/run/celerybeat-schedule --concurrency=1
# poetry run celery -A tasks worker --concurrency=1

# poetry run celery -A tasks flower  --address=0.0.0.0 --port=5566