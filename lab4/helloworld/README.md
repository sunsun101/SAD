Step 1 - Create a virtual environment and install Django in it

```
python3 -m venv .venv
source .venv/bin/activate
pip3 install django
```

Step 2 - Collect the requirements to requirement.txt

```
pip3 freeze > requirements.txt
```

Step 3 - Create a Django project and make necessary changes
```
django-admin startproject helloworld
python3 manage.py startapp basic
```

Step 4 - Create a docker file inside the project helloworld and add the following

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

Step 5 - Create docker image

```
docker build . -t lab4-img
```

Step 6 - Run the docker image

```
docker run -d -p 8000:8000 -v "E:\SAD\lab4\helloworld:/code" lab4-img
```

Step 7 - Check the running docker container

```
docker ps

```

Step 8 - In the browser go to http://localhost:8000 to check the running system.

