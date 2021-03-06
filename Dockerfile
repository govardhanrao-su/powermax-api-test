# syntax=docker/dockerfile:1

FROM python:3.9.12-slim-buster

RUN useradd -ms /bin/bash appluser
USER appluser
WORKDIR /home/appluser
ENV PATH="/home/appluser/.local/bin:${PATH}"

COPY --chown=appluser:appluser requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip3 install --user -r requirements.txt

COPY --chown=appluser:appluser . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
