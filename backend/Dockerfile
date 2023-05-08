# pull official base image
FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /requirements.txt
RUN pip install -r ./requirements.txt
COPY . /app

WORKDIR /app
EXPOSE 8000
