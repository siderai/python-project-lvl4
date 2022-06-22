[![task-manager-CI](https://github.com/siderai/task-manager/actions/workflows/task-manager-CI.yml/badge.svg)](https://github.com/siderai/task-manager/actions/workflows/task-manager-CI.yml)
<a href="https://codeclimate.com/github/siderai/task-manager/test_coverage"><img src="https://api.codeclimate.com/v1/badges/777d2c6fdc6f40625215/test_coverage" /></a>

# Minimalistic task tracker

Useful tool for both personal and team projects. Implemented with Django + Bootstrap, but also provides Django REST API for frontend. 

Take a look: 

1. Fullstack app is deployed on [Heroku](https://siderai-tm.herokuapp.com/); 
2. For using as API check out [documentation](https://siderai-tm.herokuapp.com/swagger/).

To access platform, you must create a user or authorize as one of registered users.

## Quickstart credentials:

login: 
``
АндрейБ.
``
password (same for all users): 
``
WarAndPeace
``



## Functionality:

1. Dynamic **task** management:
      - add, update and delete tasks
      - organize your tasks into groups (**labels**) 
      - control task progress (**statuses**)
      - take responsibility or delegate (**executor**)
      - search for related tasks (filtration)
2. **Users**: registration, authorization, personal page, editing rights.
3. Friendly redirect messages, reporting on completed and failed user commands.



## Stack:

Python3
• Django
• DRF
• Pytest
• PostgreSQL
• Gunicorn
• Heroku
• Bootstrap
• HTML
• Linux
• Git
• Github Actions (CI)
• Flake8
• CodeClimate


## Acquired skills: 
1. Fullstack development (Django + Bootstrap)
2. Building API with Django REST Framework
3. Django ORM practice and debug
4. Integrating Django built-ins with custom features
5. CI/CD (GitHub Actions + Heroku)


## Local quickstart:

``` 
git clone https://github.com/siderai/task-manager
cd task-manager/
python3 -m venv venv
source venv/bin/activate
make install
python3 manage.py migrate
make test
python3 manage.py runserver
```

Training project at hexlet.io.


