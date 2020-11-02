# HireUp - Backend API in Flask
[![Build Status](https://travis-ci.org/HireUp-Turing/HireUp_backend.svg?branch=main)](https://travis-ci.org/HireUp-Turing/HireUp_backend)

![HireUp gif](https://camo.githubusercontent.com/cf285267b017ce5b84275172ecafc2e72f812035/687474703a2f2f672e7265636f726469742e636f2f6259456f4b43534767652e676966)

## HireUp Back-End Service

### Jump To
- [About](#about)
- [Setup](#setup)
- [CLI Commands](#cli-commands)
- [Testing](#testing)
- [Database Schema](#database-schema)
- [Endpoint Documentation](#endpoint-documentation)

## About
HireUp aims to minimize bias in the hiring process, and reduce efforts required of job applicants to produce application materials and of employers to read through piles of those materials. This API is consumed by the the [HireUp front-end application](https://github.com/HireUp-Turing/HireUp_frontend).

## Setup
- If you do not yet have `pyenv`, Python3, or Pip3 installed, follow [these](https://opensource.com/article/19/5/python-3-default-mac#what-to-do) instructions.
- Clone repo: `git clone git@github.com:HireUp-Turing/HireUp_backend.git`
- Virtual Environment Setup:
  - Build and activate a virtual environment to install your Python packages with `$ python3 -m venv ./venv`
    - If you have Python3 set as your global version inside `pyenv` you probably can run `python` instead of `python3` at the beginning of that command.
  - Activate the virtual environment: `$ source venv/bin/activate` (Run `$ deactivate` to deactivate the virtual environment when done working with the app)
- Install Python packages: `$ pip install -r requirements.txt`
- Set up local databases
  ```shell
  $ createdb hireup_dev # creates your dev database
  $ createdb hireup_test # creates your test database
  $ export DATABASE_URL=postgresql://localhost:5432/hireup_dev # connects you to your dev database in order to run the following commands
  $ python manage.py db migrate # add explanation here
  $ python manage.py db upgrade # runs migrations on your dev database
  $ python manage.py db_seed # seed data in dev database
  $ export DATABASE_URL=postgresql://localhost:5432/hireup_test # connects you to your test database in order to run the following commands
  $ python manage.py db migrate # add explanation here
  $ python manage.py db upgrade # runs migrations on your dev database
  ```
  <!-- do the commands for creating the local db's work without entering the psql console? -->
- `$ python run.py` to run server on `localhost:5000` (_If you get errors concerning the `FLASK_APP` environment not being set, try `$ export FLASK_APP=manage.py`_)

<!-- do we still need this part? -->
<!-- _These instructions will be modified once an `.env` file is added to this repo._ -->

## CLI commands
- `$ python manage.py routes` returns available routes
- _Coming soon... database migrate/seeding commands._

## Testing
_more details to come_
_add info about coverage_
- Run tests: `python -m pytest -v`

## Database Schema
![image](https://user-images.githubusercontent.com/62635544/97842714-49e72a00-1ca5-11eb-8787-f188eb7d8ed3.png)

## Endpoint Documentation

### Applicants
#### GET `/api/v1/applicants`
**Response**: Returns all applicants
  ```JSON
  {
      "success": true,
      "data": [
          {
              "id": 1,
              "username": "Anonymous Giraffe",
              "email": "gaby@hireup.com",
              "bio": "Noodle's mom!",
              "skills": [
                  "rails",
                  "ruby"
              ],
              "values": [
                  "creativity"
              ]
          },
          {
              "id": 2,
              "username": "Famous Hippo",
              "email": "ruthie@hireup.com",
              "bio": "Noodle's mom's accountabilabuddy!",
              "skills": [
                  "rails",
                  "flask"
              ],
              "values": [
                  "creativity",
                  "mentorship"
              ]
          }
      ]
  }
  ```

#### GET `/api/v1/applicants/:applicant_id`
**Response**:
  ```JSON
  {
      "success": true,
      "data": {
          "id": 1,
          "username": "Fancy Chipmunk",
          "email": "greyson@hireup.com",
          "bio": "I'm the best one you could possibly hire",
          "skills": [
              "rails",
              "ruby"
          ],
          "values": [
              "creativity"
          ]
      }
  }
  ```

#### POST `/api/v1/applicants/`
**Request**: Email, skills, and values are required fields
  ```JSON
  {
      "first_name": "Greyson",
      "last_name": "Johns",
      "bio": "I'm the best one you could possibly hire",
      "email": "greyson@google.com",
      "username": "Chipmunk",
      "skills": [2, 3],
      "values": [2]
  }
  ```

**Response**:
Creates new applicant and returns attributes including the new user's id
  ```JSON
  {
      "success": true,
      "data": {
          "id": 6,
          "username": "Chipmunk",
          "email": "greyson@google.com",
          "bio": "I'm the best one you could possibly hire",
          "skills": [
              "flask",
              "ruby"
          ],
          "values": [
              "mentorship"
          ],
          "success": true
      }
  }
  ```
**Error handling**: New applicant cannot come in with empty arrays for either skills or values when being created, else response is 400 error message  
Example erroneous request:
  ```JSON
  {
      "first_name": "Greyson",
      "last_name": "Johns",
      "bio": "I'm the best one you could possibly hire",
      "email": "greyson@google.com",
      "username": "Chipmunk",
      "skills": [2, 3]
  }
  # missing "values" array
  ```
Error message response:
  ```JSON
  {
      "success": false,
      "error": 400,
      "errors": [
          "required 'values' parameter is missing"
      ]
  }
  ```

<!-- commenting this out until we have this request body figured out -->
<!-- #### PATCH  `/api/v1/applicants/:applicant_id`
**Request**:
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
No specific response beyond `success` -->

#### GET `/api/v1/applicants/search-options`
###### Response:
Returns alphabetically ordered skills and values that are actively associated with applicant records. Used to populate search filter options for employers to browse applicant profiles.
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
