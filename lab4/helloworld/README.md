Step 1 - Create a Django project
```
django-admin startproject helloworld
python3 manage.py startapp basic
```

Step 2 - Create a docker file inside the project helloworld

```
FROM python:3.9.7-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

Step 3 - Create docker image

```
docker build . -t lab4-img
```

Step 4 - Run the docker image

```
docker run -d -p 8000:8000 -v "E:\SAD\lab4\helloworld:/code" lab4-img
```

Step 5 - Check the running docker container

```
docker ps

```

Step 6 - In the browser go to http://localhost:8000 to check the running system.

