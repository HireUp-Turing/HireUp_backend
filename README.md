## HireUp - Backend API in Flask

### Set Up Flask App
- Use _Homebrew_ to set up a Python virtual environment (we used `pyenv`) to avoid using the default Python distribution on your machine, install `Python 3` as well as `pip`, a package manager, and set the latest version of both as the global default inside `pyenv`. These [instructions](https://opensource.com/article/19/5/python-3-default-mac#what-to-do) were helpful.
- Clone down repo
- `$ pip install -r requirements.txt`
- `$ python run.py` to run server on `localhost:5000`

**Database Setup**
- `$ createdb hireup_dev` & `$ createdb hireup_test`
- `$ export DATABASE_URL=postgresql://localhost:5432/hireup_dev`
- `$ export DATABASE_URL=postgresql://localhost:5432/hireup_test`
- _Include steps for 'migrating' db here._

### CLI commands
- `$ python manage.py routes` returns available routes
- _Coming soon... database migrate/seeding commands._
