# ProjectHub
### Nicholas Bradford, Ben Bianchi, and co.
A Django web app for WPI students and faculty to meet and collaborate on side projects, MQPs, research, startups, and anything else.

## Installation

Create a new Python 2 virtualenv, activate it, and install dependencies:

    $ virtualenv env
    $ source env/bin/activate
    $ pip install -r requirements.txt

Install dependencies in `./static/bower.json`:

    $ cd ./static
    $ bower install
    $ cd ..

Create a superuser account for yourself:

    $ python manage.py createsuperuser

Run the server at **http://localhost:8000/** to view a development version of the site:

    $ python manage.py runserver

## Repository structure

    /membership
        /migrations             Database migrations for Django
        /profile                Everything about User profiles
            forms.py            ? Form for creating user profile
            models.py           ? User profile model
            views.py            ? ProfileRead and ProfileUpdate
        /project                Everything about Projects
            forms.py            ? ProjectForm
            models.py           Models for Major, Skill, Projecct
            views.py            Views for ManageProject, ProjectList, and CRUD
        admin.py                Register Project, Skill, Major models for Admin interface
        apps.py                 ? MembershipConfig
        forms.py                ? LoginForm
        models.py               ? empty
        tests.py                ? empty
        urls.py                 URLs for everything else
        views.py                Views for home, discover, and profile
    /projectHub                 Inner project with settings, urls, wsgi
        settings.py             Settings
        urls.py                 ? URLs for admin, login, logout, accounts
        wsgi.py                 ? Interface
    /static                     Static things, of course
        /bower_components       Stuff for bower
        /img                    Static images
        bower.json              Front-end dependencies
        style.css               Styling
    /templates                  HTML django templates
        base.html               The base for all the other pages.
    manage.py                   Django file for running project management commands
    package.json                Metadata for $ npm install
    Procfile                    Commands on Heroku
    requirements.txt            Python dependencies


## About

### Why this exists

As a freshman attempting to get involved with research, or a junior trying to find an MQP, students are limited to sending emails to professors in search of potential opportunities. Likewise, when faculty want to enlist students, they are limited to blasting out emails to the major aliases We have several existing systems for project posting, but they are fragmented, under-publicized, and under-utilized. This is bad, because starting early with research and side projects gives you the experience/skills needed for the best internships/jobs/MQP success.

### Our solution

Students/faculty can create account (authenticated by wpi.edu email), and can create projects with Title, Dates, Description, Skills Required, etc. Anyone can visit main page of the website to view complete list of projects, which is filterable (by skills) and searchable (by keywords).

### Our goals

* Simple: easy to maintain and easy to use, focus on just linking the right people together (offload other responsibilities to Email, Slack, Facebook…).
* Generic: We want something generic: works with formal research initiatives, MQPs, startups, and student-led collaborative projects.
* Extendable: can later expand to include cross-institution collaboration with other Worcester or Massachusetts universities, and then to everywhere else.

### Get in touch

[Nicholas Bradford](www.NicholasSBradford.com), [Ben Bianchi](https://github.com/benbianchi)