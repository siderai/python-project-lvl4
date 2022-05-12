[![task-manager-CI](https://github.com/siderai/task-manager/actions/workflows/task-manager-CI.yml/badge.svg)](https://github.com/siderai/task-manager/actions/workflows/task-manager-CI.yml)
<a href="https://codeclimate.com/github/siderai/task-manager/test_coverage"><img src="https://api.codeclimate.com/v1/badges/777d2c6fdc6f40625215/test_coverage" /></a>

# Minimalistic task tracker

Deployed at Heroku: 

You must login to access most of features

## Functionality:

1. ***Tasks***: crud, filtration, cards with details
2. Dynamic task management: 
      - organize your tasks into groups (***labels***) 
      - control task progress (***statuses***)
      - take responsibility or delegate (***executor***)
3. ***Users*** registration, authorization, personal page, editing rights, admin panel
      - Anonimous users are read-only
      - Authorized users are able to create, update and delete basic entities. Deletion is safe: linked entities are not removable
      - Admins can edit all entities
4. Friendly redirect messages to provide smooth UX. They report on your successful and failed actions



## Stack:

Python3
• Django
• Pytest
• Poetry
• Linux
• Git
• Github Actions (CI)
• Heroku
• Flake8
• CodeClimate
• Make

## Acquired skills: 
1. Fullstack development experience (Django + Bootstrap)
2. Integrating Django built-ins with custom features
3. Building hierarсhy of Django apps & templates
4. Django ORM usage and debug
5. TDD experience


## Local quickstart:

``` 
git clone https://github.com/siderai/task-manager
cd task-manager/
python3 -m venv venv
source venv/bin/activate
make install
make test
python3 manage.py runserver
```

Training project at hexlet.io.


