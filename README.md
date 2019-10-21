# GigAdvisor

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/fabiog97/GigAdvisor/
$ cd Gig



Create a virtual environment to install dependencies in and activate it:


$ virtualenv --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd Gig
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/GigAdvisor/`.

## Database
The database is on `https://remotemysql.com/`




