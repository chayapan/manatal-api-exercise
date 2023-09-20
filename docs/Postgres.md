__PostgreSQL__ database 


Test with this command-line:
```
psql -h 10.33.123.321 -U dbdev dev_api
```

## Migration

Set up tables

```
pipenv run python app/manage.py makemigrations

pipenv run python app/manage.py migrate
```


### Create Super User


```
pipenv run python app/manage.py createsuperuser
```

admin, admin@example.com, q___4
