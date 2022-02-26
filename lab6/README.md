Step 1 - Create a Dockerfile
```
FROM python:3.10.2-buster

WORKDIR /home/app

RUN pip install "Django==4.0.2"

CMD tail -f /dev/null
```

Step 2 - Create a docker-compose.yml file
```
version: "3"
services: 
   
    api:
        build:
            context: .
            dockerfile: Dockerfile
  
        ports:
            - "8000:8000"

    postgres:
      image: postgres:14.1
      healthcheck:
        test: [ "CMD", "pg_isready", "-q", "-d", "postgres", "-U", "root" ]
        timeout: 45s
        interval: 10s
        retries: 10
      restart: always
      environment:
        - POSTGRES_USER=root
        - POSTGRES_PASSWORD=password
        - APP_DB_USER=docker
        - APP_DB_PASS=docker
        - APP_DB_NAME=docker
      volumes:
        - postgres-volume:/var/lib/postgresql/data
      ports:
        - 5432:5432
volumes: 
  postgres-volume:

```

Step 4 - Run docker composer
```
docker-compose up
```

Step 3 - Access the Django container

```
docker exec -it lab6-api-1 bash
```

Step 4 - Start a django project 
```
django-admin startproject counter
```

Step 5 - Exit and access the postgresql container
```
docker exec -it lab6-postgres-1 bash
```

Step 6 - Create a database Counter

```
psql -U root
CREATE DATABASE Counter;
```

Step 7 - Alter the Dockerfile
```
FROM python:3.10.2-buster

WORKDIR /home/app

RUN pip install "Django==4.0.2"
RUN pip install psycopg2

# CMD tail -f /dev/null
CMD python manage.py runserver 0.0.0.0:8000
```

Step 8 - Alter the docker compose file
```
version: "3"
services: 
   
    api:
        build:
            context: .
            dockerfile: Dockerfile
  
        ports:
            - "8000:8000"
        volumes:
            - ./counter:/home/app
     

    postgres:
      image: postgres:14.1
      healthcheck:
        test: [ "CMD", "pg_isready", "-q", "-d", "postgres", "-U", "root" ]
        timeout: 45s
        interval: 10s
        retries: 10
      restart: always
      environment:
        - POSTGRES_USER=root
        - POSTGRES_PASSWORD=password
        - APP_DB_USER=docker
        - APP_DB_PASS=docker
        - APP_DB_NAME=docker
      volumes:
        - postgres-volume:/var/lib/postgresql/data
      ports:
        - 5432:5432
volumes: 
  postgres-volume:
```

Step 9 - Change the Database configuration of Django project in settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'counter',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'lab6-postgres-1',
        'PORT': '5432',
    }
}
```

Step 10 - Remove the docker container and docker image the run the docker compose again
```
docker rm lab6-api-1 -f
docker rmi lab6_api
docker-compose up
```

Step 11 - Now go to http://localhost:8000/ you should be able to see Django project up and running

Step 12 - You can access the postgresql database(db name - counter) at localhost:5432 from any GUI application like dbeaver.

Step 13 - Make necessary changes to the Django application.

Step 14 - To run the migrations , get inside django container and run
```
  python manage.py makemigrations
  python manage.py migrate
```

Step 15 - For interactive shell
```
  docker exec -it lab6-api-1 python manage.py shell
```