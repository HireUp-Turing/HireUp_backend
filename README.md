# HireUp - Backend API in Flask

[![Build Status](https://travis-ci.org/HireUp-Turing/HireUp_backend.svg?branch=main)](https://travis-ci.org/HireUp-Turing/HireUp_backend)

![HireUp gif](https://github.com/HireUp-Turing/HireUp_frontend/blob/master/public/images/new-applicant.gif?raw=true)

### Jump To
- [About](#about)
- [Contributors](#contributors)
- [Setup](#setup)
- [CLI Commands](#cli-commands)
- [Testing](#testing)
- [Database Schema](#database-schema)
- [Endpoint Documentation](#endpoint-documentation)
  - [Applicants](#applicants)
  - [Searching](#searching)
  - [Messages](#messages)
  - [Skills](#skills)
  - [Values](#values)
- [Technologies](#technologies)
- [Roadmap](#roadmap)

## About
HireUp aims to minimize bias in the hiring process, and reduce efforts required of job applicants to produce application materials and of employers to read through piles of those materials. Job seekers can create anonymous applicant profiles that highlight their skills and values, and employers can browse through those anonymous profiles and message applicants they believe would be a good fit for their open roles.

This repo is the back-end service for HireUp and is consumed by our front-end application. The front-end GitHub repo can be found [here](https://github.com/HireUp-Turing/HireUp_frontend) and the deployed site [here](https://hire-up-turing.herokuapp.com/).

## Contributors
- Back-End Team:
  - Ruthie Rabinovitch | [GitHub](https://github.com/rrabinovitch) | [LinkedIn](https://www.linkedin.com/in/ruthie-r/) | rrabinovitch1@gmail.com
  - Gaby Méndez | [GitHub](https://github.com/gabichuelas) | [LinkedIn](https://www.linkedin.com/in/gabymendez/) | gmendez90@gmail.com
- Front-End Team:
  - Erin Untermeyer | [GitHub](https://github.com/ErinUntermeyer) | [LinkedIn](https://www.linkedin.com/in/erin-untermeyer/) | aerinuntermeyer@gmail.com
  - Amy Karnaze | [GitHub](https://github.com/amykarnaze) | [LinkedIn](https://www.linkedin.com/in/amy-karnaze-ba94b917/) | Akarnaze@gmail.com
  - Greyson Elkins | [GitHub](https://github.com/GreysonElkins) | [LinkedIn](https://github.com/GreysonElkins) | greysonelkins@gmail.com

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
  $ python manage.py db migrate # generates new migration files from any changes made to models.py
  $ python manage.py db upgrade # runs migrations on your dev database
  $ python manage.py db_seed # seed data in dev database
  $ export DATABASE_URL=postgresql://localhost:5432/hireup_test # connects you to your test database in order to run the following commands
  $ python manage.py db upgrade # runs migrations on your test database
  ```
- Run `$ export DATABASE_URL=postgresql://localhost:5432/hireup_dev` again to reset DATABASE_URL to the development database for any future work.
- In order to avoid needing to restart the server manually after each change to your code, run the following commands, which enable all development features, including [debug mode](https://flask.palletsprojects.com/en/1.1.x/quickstart/#debug-mode):
	```
	$ export FLASK_ENV=development
	$ flask run
	```
- `$ python run.py` to run server on `localhost:5000` (_If you get errors concerning the `FLASK_APP` environment not being set, try `$ export FLASK_APP=manage.py`_)

## CLI commands
- `$ python manage.py routes` returns available routes
- `$ python manage.py db_seed` drops all tables, creates all tables, and seeds whichever database is currently set to `DATABASE_URL` environment variable.

## Testing
- Run tests without coverage: `$ pytest -v`
- Run tests with coverage report: `$ pytest --cov`
  - See browser-based coverage report
    ```
    $ coverage html
    $ open coverage_html_report/index.html
    ```

## Database Schema
![image](https://user-images.githubusercontent.com/62635544/97842714-49e72a00-1ca5-11eb-8787-f188eb7d8ed3.png)

## Endpoint Documentation
[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/e5f0567156412937dafe)  
###### Base URL: Use `localhost:5000` to explore endpoints with local server and `hireup-be.herokuapp.com` to explore the endpoints via the live Heroku app

### Applicants
#### GET `/api/v1/applicants`
###### Response: Returns all applicants
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
					{
						"attribute": "flask"
					},
					{
						"attribute": "rails"
					},
				],
				"values": [
					{
						"attribute": "creativity"
					},
					{
						"attribute": "mentorship"
					}
				]
			},
			{
				"id": 2,
				"username": "Famous Hippo",
				"email": "ruthie@hireup.com",
				"bio": "Noodle's mom's accountabilabuddy!",
				"skills": [
					{
						"attribute": "flask"
					},
					{
						"attribute": "rails"
					},
				],
				"values": [
					{
						"attribute": "creativity"
					},
					{
						"attribute": "mentorship"
					}
				]
			}
		]
  }
  ```

#### GET `/api/v1/applicants/:applicant_id`
###### Response: Does not include any identifying information about the applicant
  ```JSON
  {
		"success": true,
		"data": {
			"id": 1,
			"username": "Fancy Chipmunk",
			"email": "greyson@hireup.com",
			"bio": "I'm the best one you could possibly hire",
			"skills": [
				{
					"attribute": "flask"
				},
				{
					"attribute": "rails"
				},
			],
			"values": [
				{
					"attribute": "creativity"
				},
				{
					"attribute": "mentorship"
				}
			]
		}
  }
  ```

#### POST `/api/v1/applicants/`
###### Request: Email, skills, and values are required fields
  ```JSON
  {
		"first_name": "Greyson",
		"last_name": "Johns",
		"bio": "I'm the best one you could possibly hire",
		"username": "Chipmunk",
		"skills": [2, 3],
		"values": [2]
  }
  ```

###### Response: Creates new applicant and returns attributes including the new user's id
  ```JSON
  {
		"success": true,
		"data": {
			"id": 6,
			"username": "Chipmunk",
			"email": "greyson@google.com",
			"bio": "I'm the best one you could possibly hire",
			"skills": [
				{
					"attribute": "flask"
				},
				{
					"attribute": "rails"
				},
			],
			"values": [
				{
					"attribute": "creativity"
				},
				{
					"attribute": "mentorship"
				}
			],
		}
  }
  ```

###### Error handling: Request body with empty arrays for either skills or values when being created will produce a 400 error message  
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

<!-- COMMENTED OUT BC THIS ENDPOINT IS NOT YET EXPOSED / IT'S AN EXTENSION -->
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

### Searching
#### GET `/api/v1/applicants/search-options`
###### Response: Returns alphabetically ordered skills and values that are actively associated with applicant records. This endpoint is used on the front-end in in order to populate search filter options for employers to browse applicant profiles.
```JSON
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

#### POST `/api/v1/applicants/search`
###### Request Body: Attribute arrays contain ids associated with the selected skills and values attributes on the front-end search page. One of the arrays can be empty, but not both.
```JSON
{
  "skills": [2, 4],
  "values": [3]
}
```
###### Response: Returns all applicants that partially match the attributes specified by the request
```JSON
{
	"success": true,
	"data": [
		{
			"id": 1,
			"username": "Chipmunk",
			"email": "gaby@hireup.com",
			"bio": "Noodle's mom!",
			"skills": [
				{
					"attribute": "rails"
				},
				{
					"attribute": "ruby"
				}
			],
			"values": [
				{
					"attribute": "creativity"
				}
			]
		},
		{
			"id": 2,
			"username": "Anonymous Giraffe",
			"email": "ruthie@hireup.com",
			"bio": "Noodle's mom's accountabilabuddy!",
			"skills": [
				{
					"attribute": "rails"
				},
				{
					"attribute": "flask"
				}
			],
			"values": [
				{
					"attribute": "creativity"
				},
				{
					"attribute": "mentorship"
				}
			]
		}
	]
}
```
###### Error handling: A request body that does not specify any skills or values will produce a 400 error message  
Example erroneous request:
```JSON
{
	"skills": [],
	"values": []
}
# missing skills and values ids
```
Error message response:
```JSON
{
	"success": false,
	"error": 400,
	"errors": "At least one skill or value id must be specified in order to filter applicant search results."
}
```

### Messages
#### GET `/api/v1/messages?applicant_id=<applicant_id>`
###### Request: Use query params to specify the id of the applicant whose messages need to be retrieved

###### Response: Returns messages associated with the specified user id
```JSON
{
	"success": true,
	"data": [
		{
			"id": 1,
			"applicant_id": 2,
			"employer_name": "Google",
			"employer_email": "info@turing.com",
			"body": "We know you'll rock our world as CEO of Google - please interview with us.",
			"read_status": false,
			"created_at": "2020-11-01 14:11:53.212912-07:00"
		},
		{
			"id": 2,
			"applicant_id": 2,
			"employer_name": "Aerion Inc",
			"employer_email": "aerioninc@email.com",
			"body": "Come work for us. Pretty please.",
			"read_status": true,
			"created_at": "2020-11-01 14:11:53.212912-07:00"
		}
	]
}
```
#### POST `/api/v1/messages`
###### Request: Body should specify `applicant_id` (referencing the message recipient), `employer_name`, `employer_email`, and a message `body`. `read_status` defaults to `false` and should not be included in the request body.

```JSON
{
	"applicant_id": 1,
	"employer_name": "Turing",
	"employer_email" : "info@turing.com",
	"body" : "We're interested in interviewing you for our Back-End Instructor role. You'll rock our students' worlds!"
}
```
###### Response: Returns the new message attributes and its id
```JSON
{
	"success": true,
	"data": {
		"id": 3,
		"applicant_id": 1,
		"employer_name": "Blop",
		"employer_email": "careers@blop.com",
		"body": "We're desperate to hire you at Blop Corp. Will you interview with us this Friday?",
		"read_status": false,
		"created_at": "2020-11-02 02:10:15.909406-07:00",
		"success": true
	}
}
```
<!-- add documentation re: error handling here -->

### Skills
#### GET `/api/v1/skills`
###### Response: Returns all skills. Used on the front-end to populate the list of skills an applicant may select when creating their profile.
```JSON
{
	"success": true,
	"data": [
		{
			"id": 1,
			"attribute": "rails"
		},
		{
			"id": 2,
			"attribute": "flask"
		},
		{
			"id": 3,
			"attribute": "ruby"
		},
		{
			"id": 4,
			"attribute": "java"
		},
		...
	]
}
```

### Values
#### GET `/api/v1/values`
###### Response: Returns all values. Used on the front-end to populate the list of values an applicant may select when creating their profile.
```JSON
{
	"success": true,
	"data": [
		{
			"id": 1,
			"attribute": "creativity"
		},
		{
			"id": 2,
			"attribute": "mentorship"
		},
		{
			"id": 3,
			"attribute": "engages with community"
		},
		...
  ]
}
```

## Technologies
<!-- fill in versions and additional notes later -->
- Python
- Flask
- SQLAlchemy
- Pytest
- TravisCI

## Roadmap
Feel free to explore our list of [open issues](https://github.com/HireUp-Turing/HireUp_backend/issues) and our [project board](https://github.com/orgs/HireUp-Turing/projects/2) to learn about what our team has in mind for future iterations of HireUp
