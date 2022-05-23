[![task-manager-CI](https://github.com/siderai/task-manager/actions/workflows/task-manager-CI.yml/badge.svg)](https://github.com/siderai/task-manager/actions/workflows/task-manager-CI.yml)
<a href="https://codeclimate.com/github/siderai/task-manager/test_coverage"><img src="https://api.codeclimate.com/v1/badges/777d2c6fdc6f40625215/test_coverage" /></a>

# Minimalistic task tracker

Deployed at Heroku: 

You must login to access most of features

## Functionality:

1. ***Tasks***: crud, filtration, cards with detailed info
2. Dynamic task management: 
      - organize your tasks into groups (***labels***) 
      - control task progress (***statuses***)
      - take responsibility or delegate (***executor***)
3. ***Users***: registration, authorization, personal page, editing rights, admin panel
4. Friendly redirect messages, reporting on completed and failed commands



## Stack:

Python3
• Django
• Pytest
• Poetry
• PostgreSQL
• Gunicorn
• Heroku
• Linux
• Git
• Github Actions (CI)
• Flake8
• CodeClimate


## Acquired skills: 
1. Fullstack development experience (Django + Bootstrap)
2. Integrating Django built-ins with custom features
3. Building hierarсhy of Django apps & templates
4. Django ORM practice and debug
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


