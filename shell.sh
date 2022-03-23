#!/bin/bash
HOME="$(pwd)"

# This basic shell doesn't connect to database

docker run -it -v "$HOME/app":/app -v "$HOME":/opt -p 8000:8000 --rm manatal-api-exercise_school_api bash


# To get to running docker compose
# docker compose up
# docker ps
# docker exec -it manatal-api-exercise_school_api_1 bash
