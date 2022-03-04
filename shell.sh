#!/bin/bash
HOME="$(pwd)"

# This basic shell doesn't connect to database

docker run -it -v "$HOME/app":/app --rm manatal-api-exercise_web bash


# To get to running docker compose
# docker compose up
# docker ps
# docker exec -it manatal-api-exercise_web_1 bash
