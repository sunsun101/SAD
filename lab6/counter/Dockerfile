FROM python:3.10.2-buster

WORKDIR /home/app

RUN pip install "Django==4.0.2"
RUN pip install psycopg2

# CMD tail -f /dev/null
COPY ./counter /home/app
CMD python manage.py runserver 0.0.0.0:8000