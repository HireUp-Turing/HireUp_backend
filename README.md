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
#### Response
Returns all applicants
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
#### GET `/api/v1/applicants/search-options`
#### Response
Returns alphabetically ordered skills and values that are present in applicant profiles
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
#### Request Body
One of these arrays can be empty, but not both
```
{
  "skills": [2, 4]
  "values": [3]
}
```
#### Response
Returns any user that contains any of the attributes selected in the search
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
#### Response
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

#### POST `/api/v1/applicants/`
#### Request
Email, skills, and values are **required fields**

```
{
    "first_name": "Greyson",
    "last_name": "Johns",
    "bio": "I'm the best one you could possibly hire",
    "email": "google@google.com",
    "username": "Chipmunk",
​    "skills": [1, 2],
​    "values": [2]
  }

```
_New applicant cannot come in with empty arrays for either skills or values when being created, else response is 400 error message:_
```
{
    "success": false,
    "error": 400,
    "errors": [
        "required 'values' parameter is blank"
    ]
}
```
#### Response
Returns the new users id
```
data: {
  id: $id
}
```
#### PATCH  `/api/v1/applicants/:applicant_id`
#### Request
_This needs to be updated, as skills/values will probably need to come in as an array of id's, same as with the search function_

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
No specific response beyond `success`

### Messages
#### GET `/api/v1/messages?applicant_id=<applicant_id>`
Use query params to send applicant_id!

#### Response
Returns messages associated with the provided user id
```
data: [
  {
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
​  }
]
```
#### POST `/api/v1/messages`
##### Request
Body includes the id of the applicant (recipient), and the default `read_status` will be false so no need to send that in.
```
  {
    "applicant_id": $id,
    "employer_name": "Turing",
    "employer_email" : "info@turing.com",
    "body" : "message body here"
  }
```
##### Response
Returns the message in [data] with primary_key id, read_status, and created_at timestamp in addition to the details that were sent in to save.
```
  {
    "id": 1,
    "applicant_id": 2,
    "employer_name": "Turing",
    "employer_email" : "info@turing.com",
    "body" : "message body here",
    "read_status": "False",
    "created_at": "<date_string"
  }
```
### Skills
#### GET `/api/v1/skills`
#### Response
```
data: [
  {
    "id": $id,
    "name": "creativity"
  },
  {
    "id": $id,
    "name": "javascript"
  },
  ...
]
```

### Values
#### GET `/api/v1/values`
#### Response
```
data: [
  {
    "id": $id,
    "name": "work/life balance"
  },
  {
    "id": $id,
    "name": "other random value"
  },
  ...
]
```
