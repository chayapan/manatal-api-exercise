__Pipenv__ is better package management for Python development. The mechanism is similar to __npm__ in Node.JS, __composer__ for PHP, which use package.json and etc.. There will be Pipfile and Pipfile.lock.

The manifest file contains dependencies list.


```
pip install --user pipenv
```

To install Pipenv without Pip:
```
curl https://raw.githubusercontent.com/pypa/pipenv/master/get-pipenv.py | python
```

Install package:
```
pipenv install requests
```

Run Python inside virtual environment.
```
pipenv run python main.py
```


From the fresh Repo, run

```
pipenv install
```

will install dependencies from Pipfile.