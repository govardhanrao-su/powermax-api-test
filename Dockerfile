# syntax=docker/dockerfile:1

FROM python:3.9.12-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN adduser -D appluser
USER appluser


CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
