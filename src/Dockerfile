# syntax=docker/dockerfile:1.4

FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY . /usr/src/app
RUN pip install -r requirements.txt
