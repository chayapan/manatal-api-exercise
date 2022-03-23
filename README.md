
The objective of this exercise is to build APIs with Django.
While showing coding style and thought process when developing the solution.
Disclaimer: this is the first time I use DRF.

This README keeps track of incremental development of the project.

There are four steps:
Step 1.
Step 2.
Step 3.
Bonus.


Step 1. 10:40AM
- set up working environment for this project. Use Docker Compose so we have PostgreSQL and Python app server in one sandbox environment.
1. use docker-compose up to incrementally build the image.
2. get inside the container: ```docker run -it --rm manatal-api-exercise_web sh```
- pick baseline versions and setup environment per instruction.
  - Pipfile
  - .env
- add the model in school/models.py


- psql: SCRAM authentication requires libpq version 10 or above
- When bulding Docker image for use in Mac M1: export DOCKER_DEFAULT_PLATFORM=linux/amd64
see https://stackoverflow.com/questions/62807717/how-can-i-solve-postgresql-scram-authentifcation-problem and https://github.com/psycopg/psycopg2/issues/1360

- add .env for Docker Compose
```
    env_file:
      - ./.env.dev
```
https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/


Now it is 15:30PM. Done with Step 1 - 3. Except for last two requirements.
Also need to cleanup sensitive system information and put everything in .env file.

Last commit 16:30PM. Worked through step 1-3. Didn't have time to work on bonus part, but this repo comes with Docker Compose for preview.

### Remaining Points

- Didn't get Pipfile to work as the main package maangement as most work is done with Docker / requirements.txt
- The .env part was added last minute.
- No work done on Django Test, which should be a nice addition to this little program.

# References

Django in Docker Compose with PostgreSQL
  https://docs.docker.com/samples/django/

Workflow using Pipfile
  https://pypi.org/project/pipenv/
  https://pipenv.pypa.io/en/latest/#install-pipenv-today
  https://pipenv.pypa.io/en/latest/basics/#example-pipenv-workflow

# manatal-api-exercise

Usage:

```docker compose up``` will start development server.

Go to http://127.0.0.1:8000/

To set up admin user, to inside Docker Container and run:

```python3 manage.py createsuperuser --email=demo@mo.de --firstname=demo```
