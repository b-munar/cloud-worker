FROM python:3.11.2-bullseye
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_HOME="/usr/local"
ENV PORT $PORT
EXPOSE $PORT
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/usr/local python3 -
WORKDIR /usr/src/app
COPY . .
RUN poetry install --no-root
CMD exec poetry run gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app