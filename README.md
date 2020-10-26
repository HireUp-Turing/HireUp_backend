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
​    "updated_at": "Oct_20_etc_etc",
​    "skills": ["javascript", "react"],
​    "values": ["writing", "teamwork"]
  }, {
​    "id": "2",
​    "username": "BeBe",
    "bio": "I'm the best one you could possibly hire",
​    "updated_at": "Oct_20_etc_etc",
​    "skills": ["javascript", "react"],
​    "values": ["paired programming", "magic"]
  }, {
​    "id": "3",
​    "username": "Wingnut",
    "bio": "I'm the best one you could possibly hire",
​    "updated_at": "Oct_20_etc_etc",
​    "skills": ["react"],
​    "values": ["paired programming", "teamwork"]
  }]
}
```
#### GET `/api/v1/applicants/search-options` or `/api/v1/applicants/attributes`
##### Response
(returns skills and values that are present in applicant profiles)
```
{
  data: {
    skills: ["javascript", "react"],
    values: ["paired programming", "teamwork", "magic", "writing"]
  }
}
```
#### GET `/api/v1/applicants/search`
##### Request Body
(one of these arrays can be empty, but not both)
```
{
  skills: ["javascript"]
  values: ["magic"]
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
​    "updated_at": "Oct_20_etc_etc",
​    "skills": ["javascript", "react"],
​    "values": ["writing", "teamwork"]
  }, {
​    "id": "2",
​    "username": "Oct_20_etc_etc",
    "bio": "I'm the best one you could possibly hire",
​    "updated_at": "timestamp",
​    "skills": ["javascript", "react"],
​    "values": ["paired programming", "magic"]
  }]
}
```
#### GET `/api/v1/applicants/:id`
(eventually this endpoint should require some sort of authentication and that the user is logged in)
##### Response
```
  data: {
    "id": $id,
    "first_name": "Greyson",
    "last_name": "Johns",
    "bio": "I'm the best one you could possibly hire",
    "email": "google@google.com",
    "username": "Chipmunk",
​    "updated_at": "Oct_20_etc_etc",
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
​    "updated_at": "Oct_20_etc_etc",
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
### PATCH  `/api/v1/applicants/:id
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
#### GET `/api/v1/messages/:user_id/
(eventually this endpoint should require some sort of authentication and that the user is logged in)
##### Response
(returns messages associated with the provided user id)
```
data: {
  [{
    "applicant_id": "1",
    "message_id": "1",
​    "employer_name": "google",
​    "employer_email": "google@email.com",
​    "body": "message goes here",
​    "read_status": false
​  }, {
​    "applicant_id": "1",
    "message_id": "2",
​    "employer_name": "Aerion Inc",
​    "employer_email": "aerioninc@email.com",
​    "body": "message goes here",
​    "read_status": true
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

