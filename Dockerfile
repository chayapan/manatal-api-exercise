# FROM python:3-slim-bullseye
FROM python:3-slim-buster
LABEL org.opencontainers.image.authors="chayapan@gmail.com"
ENV PYTHONUNBUFFERED 1

# Step below does not apply after first build.
RUN mkdir -p /app
COPY app/requirements.txt /app
WORKDIR /app
RUN python3 -m pip install -r requirements.txt

# Start a Django Project
# Can also add this to Compose file
#  command: python manage.py runserver 0.0.0.0:8000
# CMD django-admin startproject manatal

# Setup pipenv
RUN python3 -m pip install --user pipenv

# Setup PostgreSQL 14
RUN apt install --yes ca-certificates

# Tools for DBA
RUN apt-get update
RUN apt-get install --yes postgresql-client postgresql-common libpq-dev

# This is a dev/test server
EXPOSE 8000/tcp
CMD python3 manage.py runserver 0.0.0.0:8000
