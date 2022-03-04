FROM python:3-slim-buster
MAINTAINER Chayapan Khannbha <chayapan@gmail.com>
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY app/requirements.txt /app
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
RUN apt-get install --yes postgresql-client

# This is a dev/test server
CMD python3 manage.py runserver 0.0.0.0:8000
