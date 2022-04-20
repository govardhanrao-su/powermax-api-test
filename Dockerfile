# syntax=docker/dockerfile:1

FROM python:3.9.12-slim-buster

RUN pip3 install --upgrade pip3

RUN useradd -u 1234 appluser
USER appluser
WORKDIR /home/appluser

COPY --chown=appluser:appluser requirements.txt requirements.txt
RUN pip3 install --user -r requirements.txt

ENV PATH="/home/appluser/.local/bin:${PATH}"

COPY --chown=appluser:appluser . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
