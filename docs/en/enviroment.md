# Environment variables

[Русский](../ru/enviroment.md) | **English**

Part of the project settings is taken from environment variables. 
To define them, create the **.env** file in the docker folder and write the data there in this format: **VARIABLE = value**.

The following variables are available:

- **COMPOSE_PROJECT_NAME** - sets the project name. This value is prepended along with the service name to the container on start up. 
For example, if your project name is **myapp** and it includes two services **db** and **web**, 
then Compose starts containers named **myapp_db_1** and **myapp_web_1** respectively;
- **POSTGRES_DB** - used to define a different name for the default database that is created when the image is first started;
- **POSTGRES_PORT** - port on which the database will work;
- **POSTGRES_HOST** - host on which the database will work;
- **POSTGRES_USER** -  used in conjunction with **POSTGRES_PASSWORD** to set a user and its password;
- **POSTGRES_PASSWORD** - environment variable sets the superuser password for PostgreSQL;
- **DEBUG** - debug mode. Set to **True** to see debugging information in case of an error. Turned off by **False**;
- **SECRET_KEY** - a secret key for a particular Django installation. 
This is used to provide cryptographic signing, and should be set to a unique, unpredictable value;
- **ADMIN_USER_NAME** - username to login to admin panel;
- **ADMIN_USER_PASSWORD** - admin password.