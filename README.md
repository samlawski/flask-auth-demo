# Flask Auth Demo

This is a simple demo to show and explain a very basic flask session authentication setup.

## 🗂 Project Overview

The project is meant to demonstrate very basic authentication and authorization with Flask.

* **app.py**: This is the main project file containing the entire logic of the app and the most relevant code.
* **requirements.txt**: A list of all installed packages and their versions
* **templates/**: All the views. The _base.html is the main layout for all pages.
* **static/**: Contains static assets. So far it's a CSS file, with some basic normalizing styles.

## 🚀 Getting started

### 🖥 Setting up the project environment

First, make sure to have Python 3 installed. Then setup and activate your virtual environment: 

* Install a virtual environment to install Python packages only in your project's environment: `pip3 install virtualenv`
* Create an environemnt folder: `virtualenv env`
* Activate the environment: `source env/bin/activate`

Before you work on your project, make sure that it says `(env)` in your Terminal. This way you know, that you're currently working within the environment you just set up.

### 📦 Installing all relevant packages

Now, let's install all packages that we need: 

```sh
pip3 install flask flask-sqlalchemy flask_login
```

_(Check the requirements.txt file to view the versions of the packages used for this demo.)_

As long as we have set up our environment before, all packages will be installed in the **env** folder.

### 🗄 Setup the database

In order to set up a database, we have to do the following steps:

1. Open the python console: `python3`
2. Import the database from our project: `from app import db`
3. Create the database file: `db.create_all()`
4. Close the console: `exit()`

### 🧨 Run the server

Now, that everything is set up you can start the server:

```sh
python3 app.py
```