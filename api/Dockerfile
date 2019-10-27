FROM python:3.7-alpine

WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

RUN python -m unittest

CMD gunicorn -b 0.0.0.0:5000 --reload app:api