# Lab - Class 32
## Project: drf-api-perissions-postgres

Author: Sarah Glass for Python 401

## Overview

- Let’s move our site closer to production grade by adding Permissions and Postgresql Database.

**Feature Tasks and Requirements - General**

- You have been supplied with two demos, each presenting a key new feature.
- One demonstrates how to restrict access to portions of your APIs data.
- The other demonstrates switching over to using postgres vs sqlite
- Your job is to merge the functionality of both demos.
- Customize your project to use different application features/models than what was used in demos.


**Features - Django REST Framework**

- Make your site a DRF powered API as you did in previous lab.
- Adjust project’s permissions so that only authenticated user’s have access to API.
- Add a custom permission so that only appropriate users can update or delete it.
- Exactly what this means will depend on your application, so if you have any questions about “appropriate users” means reach out to TA/Instructor.
- Add ability to switch user’s directly from browsable API.

**Features - Docker**

- NOTE Refer to demo for built out Dockerfile and docker-compose.yml examples.
- create Dockerfile based off python:3.10-slim
- create docker-compose.yml to run Django app as a web service.
- enter docker compose up --build to start your site.
- add postgres as a service. Note: It is not required to include a volume so that data can persist when container is shut down.
- Go to browsable api and confirm site properly restricts users based on their permissions.

## Links and Resources

* TA help.
* chatGPT helped with tests.

## Setup

- No env variables -> used Docker

## How to initialize/run your application

- python manage.py runserver
- docker compose up --build
- runs at `http://127.0.0.1:8000/api/v1/states/3`

## Libraries / Requirements

asgiref==3.7.2
Django==4.2.3
djangorestframework==3.14.0
psycopg2-binary==2.9.6
pytz==2023.3
sqlparse==0.4.4

## Tests

Built-in Django testing

- python manage.py test
