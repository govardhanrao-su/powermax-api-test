# syntax=docker/dockerfile:1

FROM python:3.9.12-slim-buster

WORKDIR /app

RUN useradd -u 1234 appluser
USER appluser

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .


CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
