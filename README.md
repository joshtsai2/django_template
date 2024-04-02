## This will be a helpful template for anyone who wants a kickstart to creating their own Django backend.
This Django guide is largely helpful for understanding where the code has come from: https://docs.djangoproject.com/en/5.0/intro/tutorial01/

First, it will be useful to set up a virtual environment for your project. This will compartmentalize any packages/dependencies of your project and will keep them
separate from your other workspaces.

Install virtualenv (or any other virtual environment tool) with pip. If using virtualenv, run 
```bash
python<version> -m venv <your-env-name-here>
```

To activate your virtual environment, run `source <your-env-name>/bin/activate`. You will need to activate your virtual environment before installing any packages you wish
to use in your project.

Install the django package by running pip install django.

To run this server, use `python manage.py runserver`. 
The port and IP of the server can be changed using a command line argument like so: `python manage.py runserver 8080` or `python manage.py runserver 0.0.0.0:8000`


## Applications

To create an application within this project, run `python manage.py startapp <your-app-name>`. In this template, there is already an application created called `polls` which will
be used as an example.

An application is a web-application that lies within a project. A website can have many applications and creating different applications in your Django project can help
with organization and readability in the future.

Within the `polls` directory, there are several files that are of importance.

The `views.py` file is where you will define all your API endpoints. These will be functions where you can send HTTP Responses back to the client.
This link (https://docs.djangoproject.com/en/5.0/ref/request-response/) has more subclasses of HTTP requests and responses that you can use.

In order for your app to recognize this endpoint, you will need to modify `polls/urls.py`. Under `urlpatterns`, append your new path (e.g. "request_resource/") and the corresponding
view endpoint from `views.py`.

Then, for your project to recognize the app's endpoints, you will need to modify `mysite/urls.py`. Under `urlpatterns`, append your app's path root name (e.g. "polls/") and include
the application's urls. 

Examples for adding API endpoints to your application and your project are both in this template in `polls/urls.py` and `mysite/urls.py`.

## Models
Django also has database support. The guide listed here does a good job of getting you started with using a database in Django: https://docs.djangoproject.com/en/5.0/intro/tutorial02/

