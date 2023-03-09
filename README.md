# FastAPI - SQLAlchemy - Alembic Starter

Getting started with these tools can be overwhelming, so here is some code to give you a smoother begin.

## How to use this template?

1. Click on the `use template` button. This will create a copy of this repo ono your github. Choose a name and create it.

2. With the repo already on your GitHub, clone it. The command will start with `git clone ...`

## Setting up locally

With the repo already cloned, it's time to run it, you'll need to make a few modifications before it's ready:

1. Replace the URL in `database.py` and `alembic.ini`. You can use [Elephant SQL](https://www.elephantsql.com/) to create a PostgreSQL instance.

```py
# database.py

SQLALCHEMY_DATABASE_URL = "ADD_DATABASE_URL_HERE" # line 7
```

```py
# alembic.init

sqlalchemy.url = ADD_DATABASE_URL_HERE # line 58
```

2. Run `pipenv install` to install all dependencies

3. Inside `sql_app`, run `pipenv run alembic revision --autogenerate -m "First revision"`

![Expected output](https://kyn.ac/SCR-20230303-tfa.png)

4. Run `pipenv run alembic upgrade head` and you should see your tables oon your Database client

5. Create and/or delete models, you can start your own project from here
