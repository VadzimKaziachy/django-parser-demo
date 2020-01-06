# django-parser-demo

[Русский](docs/ru/README.md) | **English**


The program collects data from the site and creates statistical price changes. 
The application is written in [Django](https://www.djangoproject.com/) 2.2.6.

<img src="docs/img/XKK6EWNMPFY.jpg">

**Contents**

- [Environment variables](#enviroment)
- [Setup with Virtualenv](#setup-with-virtualenv)
- [Setup with Docker](#setup-with-docker)
- [Tests](#tests)


## Environment variables

Part of the project settings is taken from environment variables. 
To define them, create the **.env** file in the docker folder and write the data there in this format: **VARIABLE = value**.

The following variables are available:

- **COMPOSE_PROJECT_NAME** - sets the project name. This value is prepended along with the service name to the container on start up. 
For example, if your project name is **myapp** and it includes two services **db** and **web**, 
then Compose starts containers named **myapp_db_1** and **myapp_web_1** respectively;
- **POSTGRES_DB** - used to define a different name for the default database that is created when the image is first started;
- **POSTGRES_PORT** - port on which the database will work;
- **POSTGRES_HOST** - host on which the database will work;
- **POSTGRES_USER** -  used in conjunction with POSTGRES_PASSWORD to set a user and its password;
- **POSTGRES_PASSWORD** - environment variable sets the superuser password for PostgreSQL;
- **DEBUG** - debug mode. Set to **True** to see debugging information in case of an error. Turned off by **False**;
- **SECRET_KEY** - a secret key for a particular Django installation. 
This is used to provide cryptographic signing, and should be set to a unique, unpredictable value;
- **ADMIN_USER_NAME** - username to login to admin panel;
- **ADMIN_USER_PASSWORD** - admin password.



## Setup with Virtualenv

You can run the gns-backend project locally without installing Docker, and just use Virtualenv,
which is the recommended installation approach for Django itself.

### Dependencies

* [pip3](https://github.com/pypa/pip)
* [Python 3.7](https://www.ics.uci.edu/~pattis/common/handouts/pythoneclipsejava/python.html)
* [Virtualenv](https://virtualenv.pypa.io/en/stable/installation/)

### Installation

First of all, activate the environment. To do this, go to the project root and execute the commands:

    virtualenv --python=python3 venv              
    source venv/bin/activate

Make sure that virtualenv is activated,
otherwise further actions will entail the installation of the globano project in your system.

Next, you need to install all the necessary packages for the application.
To do this, go to the [docker/web](docker/web) folder and install the packages:

    cd docker/web
    pip install -r requirements.txt
    
The next step is to configure our local environment variables. 
You can read how to configure the environment variable file in the section [Environment variables](#enviroment)

After everything has been configured, you can start the project. The first thing you need to do is perform migrations
to set up a database:

    python manage.py migrate

After all the above has been done, you can run our project. To do this, run the command below,
it will allow you to run the project on your machine:

    python manage.py runserver

Now open the project in the [browser](http://localhost:8000).

## Tests

### Dependencies

* [pip3](https://github.com/pypa/pip)
* [Python 3.7](https://www.ics.uci.edu/~pattis/common/handouts/pythoneclipsejava/python.html)
* [Coverage](https://coverage.readthedocs.io/en/coverage-5.0/index.html)

For testing, the Coverage library is used.  To run the tests, run the command in the [web](src/web) folder.

     coverage run --source='.' manage.py test the-app-you-want-to-test

This **command** will fill a **“.coverage”**, located in **COVERAGE_FILE** and then you may see results or report. 
If you need to remove gathered data, execute:

    coverage erase

If you want to show the results in the **command line**, run:

    coverage report

For more readable **reports**:

    coverage html

To know concretely what part of your **code** is covered by **tests**, use:

    coverage annotate -d directory-where-to-put-annotated-files

It will generate same source code file with an additional syntax on it:
* Line with **>** means it was **executed**
* Line beginning with **!** means it was **not executed**
* Line starting with **-** means the line was **excluded** in the **coverage statistics**
