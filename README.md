## HireUp - Backend API in Flask

### Set Up Flask App
- Use _Homebrew_ to set up a Python virtual environment (we used `pyenv`) to avoid using the default Python distribution on your machine, install `Python 3` as well as `pip`, a package manager, and set the latest version of both as the global default inside `pyenv`. These [instructions](https://opensource.com/article/19/5/python-3-default-mac#what-to-do) were helpful.
- Clone repo: `git clone git@github.com:HireUp-Turing/HireUp_backend.git`
- Set up virtual environment
  - build a virtual environment to install your Python packages: `$ python3 -m venv ./venv`
  - activate the virtual environment: `$ source venv/bin/activate`
- install Python packages: `$ pip install -r requirements.txt`
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

### CLI commands
- `$ python manage.py routes` returns available routes
- _Coming soon... database migrate/seeding commands._

### Database Schema
![image](https://user-images.githubusercontent.com/62635544/96819356-a6626380-13e0-11eb-8398-eef92ca100f3.png)
