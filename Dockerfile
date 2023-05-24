FROM python:3.11.2-bullseye
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_HOME="/usr/local"
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/usr/local python3 -
WORKDIR /usr/src/app
COPY . .
RUN poetry install --no-root
ENTRYPOINT ["bash", "./entrypoint.sh" ]