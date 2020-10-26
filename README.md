## HireUp - Backend API in Flask

### Set Up Flask App
- Install Python3 and Pip3 using `pyenv`, a version manager. These [instructions](https://opensource.com/article/19/5/python-3-default-mac#what-to-do) were helpful.
- Clone repo: `git clone git@github.com:HireUp-Turing/HireUp_backend.git`
- Virtual Environment Setup:
  - Build and activate a virtual environment to install your Python packages with `$ python3 -m venv ./venv`
  - _If you have Python3 set as your global version inside `pyenv` you probably can run `python` instead of `python3` at the beginning of that command.
  - Activate the virtual environment: `$ source venv/bin/activate`
  - Run `$ deactivate` to deactivate virtual environment.
- Install Python packages: `$ pip install -r requirements.txt`
- `$ python run.py` to run server on `localhost:5000`

**Database Setup**
- `$ createdb hireup_dev` & `$ createdb hireup_test`
- `$ export DATABASE_URL=postgresql://localhost:5432/hireup_dev`
- `$ python manage.py db migrate`
- `$ python manage.py db upgrade`
- `$ export DATABASE_URL=postgresql://localhost:5432/hireup_test`
- `$ python manage.py db migrate`
- `$ python manage.py db upgrade`

_If you get errors concerning the `FLASK_APP` environment not being set, try `$ export FLASK_APP=manage.py`_

_These instructions will be modified once an `.env` file is added to this repo._

### CLI commands
- `$ python manage.py routes` returns available routes
- _Coming soon... database migrate/seeding commands._

### Database Schema
![image](https://user-images.githubusercontent.com/62635544/96819356-a6626380-13e0-11eb-8398-eef92ca100f3.png)
