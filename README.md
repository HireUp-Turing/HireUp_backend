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

### Running tests
_more details to come_
- `python -m pytest -v`

### Database Schema
![image](https://user-images.githubusercontent.com/62635544/96819356-a6626380-13e0-11eb-8398-eef92ca100f3.png)

### Endpoint Map

### Applicants
#### GET `/api/v1/applicants`
##### Response
(all applicants)
```
{
  data: [{
​    "id": "1",
​    "username": "Chipmunk",
    "bio": "I'm the best one you could possibly hire",
​    "skills": ["javascript", "react"],
​    "values": ["writing", "teamwork"]
  }, {
​    "id": "2",
​    "username": "BeBe",
    "bio": "I'm the best one you could possibly hire",
​    "skills": ["javascript", "react"],
​    "values": ["paired programming", "magic"]
  }, {
​    "id": "3",
​    "username": "Wingnut",
    "bio": "I'm the best one you could possibly hire",
​    "skills": ["react"],
​    "values": ["paired programming", "teamwork"]
  }]
}
```
#### GET `/api/v1/applicants/search-options` or `/api/v1/applicants/attributes`
##### Response
(returns alphabetically ordered skills and values that are present in applicant profiles)
```
{
    "success": true,
    "data": [
        {
            "skills": [
                {
                    "id": 2,
                    "attribute": "flask"
                },
                {
                    "id": 1,
                    "attribute": "rails"
                },
                {
                    "id": 3,
                    "attribute": "ruby"
                }
            ],
            "values": [
                {
                    "id": 1,
                    "attribute": "creativity"
                },
                {
                    "id": 2,
                    "attribute": "mentorship"
                }
            ]
        }
    ]
}
```
#### GET `/api/v1/applicants/search`
##### Request Body
(one of these arrays can be empty, but not both)
```
{
  "skill_ids": [2, 4]
  "value_ids": [3]
}
```
##### Response
(returns any user that contains any property)
```
{
  data: [{
​    "id": "1",
​    "username": "Chipmunk",
    "bio": "I'm the best one you could possibly hire",
​    "skills": ["javascript", "react"],
​    "values": ["writing", "teamwork"]
  }, {
​    "id": "2",
​    "username": "time-traveler",
    "bio": "I'm the best one you could possibly hire",
​    "skills": ["javascript", "react"],
​    "values": ["paired programming", "magic"]
  }]
}
```
#### GET `/api/v1/applicants/:applicant_id`
(eventually this endpoint should require some sort of authentication and that the user is logged in)
##### Response
```
  data: {
    "id": $id,
    "email": "google@google.com",
    "username": "Chipmunk",
    "first_name": "Greyson",
    "last_name": "Johns",
    "bio": "I'm the best one you could possibly hire",
​    "skills": ["javascript", "react"],
​    "values": ["writing", "teamwork"]
  }
```
### POST `/api/v1/applicants/
#### Request
```
data: {
    "first_name": "Greyson",
    "last_name": "Johns",
    "bio": "I'm the best one you could possibly hire",
    "email": "google@google.com",
    "username": "Chipmunk",
​    "skills": ["javascript", "react"],
​    "values": ["writing", "teamwork"]
  }

```
#### Response
(returns the new users id)
```
data: {
  id: $id
}
```
### PATCH  `/api/v1/applicants/:applicant_id
(eventually this endpoint should require some sort of authentication and that the user is logged in)
#### Request
(contains at least one, if not all of the following properties)
```
{
  "first_name": "Now I'm John",
  "last_name": "Smith",
  "bio": "Call me that from now on",
  "email": "jjj@comcast.com"
  "username": "Tameen"
  "skills": ["bird-watching", "singing operatic sonatas poorly"],
  "values": ["silliness", "charisma"]
}
```
#### Response
### Messages
#### GET `/api/v1/messages?applicant_id=<applicant_id>
* use query params to send applicant_id! *
(eventually this endpoint should require some sort of authentication and that the user is logged in)
##### Response
(returns messages associated with the provided user id)
```
data: {
  [{
    "id": "1",
    "applicant_id": "1",
​    "employer_name": "google",
​    "employer_email": "google@email.com",
​    "body": "message goes here",
​    "read_status": false,
      "created_at": "Oct_21_etc_ect"
​  }, {
​    "id": "2",
    "applicant_id": "1",
​    "employer_name": "Aerion Inc",
​    "employer_email": "aerioninc@email.com",
​    "body": "message goes here",
​    "read_status": true,
    "created_at": "Oct_21_etc_ect"
​  }]
}
```
#### POST `/api/v1/messages
##### Request
(body includes the id of the recipient)
```
  {
    id: id
  }
```
