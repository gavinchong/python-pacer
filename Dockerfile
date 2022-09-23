# syntax=docker/dockerfile:1
FROM python:3.9
ENV PYTHONUNBUFFERED 1

WORKDIR /src

# Install django and DRF 
COPY requirements.txt /src/

# Prepare virtual env
RUN python3 -m venv venv

# Activate virtual env
RUN . venv/bin/activate

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /src/