FROM python:3.10.2-buster

WORKDIR /home/app

RUN pip install "Django==4.0.2"

# To make container does not stop (return exits code) itself
CMD tail -f /dev/null