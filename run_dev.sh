#!/bin/bash

# Run this app using Pipenv virtual environment.

cd ./app
echo $(pwd)
pipenv run python3 ./app/manage.py runserver