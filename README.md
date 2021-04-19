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

First, make sure to have Python 3 installed. **Mac** should come with it preinstalled. If not, you should use something like [Homebrew](https://brew.sh/) to install the latest version. On **Windows 10**, you can install the latest version of Python simply from the Microsoft Store app. For Linux, follow [the instructions here](https://docs.python-guide.org/starting/install3/linux/).

Then setup and activate your virtual environment: 

#### Linux & Mac

* Install a virtual environment to install Python packages only in your project's environment: `pip3 install virtualenv`
* Create an environemnt folder: `virtualenv env`
* Activate the environment: `source env/bin/activate`

Before you work on your project, make sure that it says `(env)` in your Terminal. This way you know, that you're currently working within the environment you just set up.

#### Windows 10

* Install a virtual environment to install Python packages only in your project's environment: `pip3 install virtualenv`
* Create an environemnt folder: `python -m virtualenv .`
* (Optional) Most likely, Windows won't allow you to execute the environment script. So probably you have to run the following line to temporarily grant that permission: `Set-ExecutionPolicy Unrestricted -Scope Proces`
* Now acticate the environment: `.\Script\activate`

Your Command Prompt should now show the name of your project in parentheses. Example: `(flask-auth-demo)`. This is how you know, the environment is active.

### 📦 Installing all relevant packages

Now, let's install all packages that we need: 

```sh
pip3 install -r requirements.txt
```

This will install the main three packages we need:

* `flask`
* `flask-sqlalchemy`
* `flask_login`

_(Check the requirements.txt file to view the versions of the packages used for this demo.)_

As long as we have set up our environment before, all packages will be installed in the **env** folder.

### 🗄 Setup the database

In order to set up a database, we have to do the following steps:

1. Open the python console: `python3` (or just `python` on Windows)
2. Import the database from our project: `from app import db`
3. Create the database file: `db.create_all()`
4. Close the console: `exit()`

### 🧨 Run the server

Now, that everything is set up you can start the server:

#### Linux & Mac

```sh
python3 app.py
```

#### Windows

```sh
python app.py
```

### 🌏 Deployment

This application is not meant to run in production but only meant to demonstrate the use of authentication in flask. 

In fact, it's not even possible to delpoy this application to e.g. Google App Engine. For that, `app.py` should be renamed to `main.py`, SQlite should be replaced with an actual database, and secrets should be stored in environment variables.