#!/bin/bash

mkdir -p /home/celery/var/run/

# poetry run celery -A tasks worker -B -s /home/celery/var/run/celerybeat-schedule
poetry run celery -A tasks worker