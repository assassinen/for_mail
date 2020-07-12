FROM python:3.7.2

RUN mkdir -p /tests
WORKDIR /tests

COPY ./requirements.txt /tests
RUN pip install --no-cache-dir -r requirements.txt

COPY . /tests