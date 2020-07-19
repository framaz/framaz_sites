FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000