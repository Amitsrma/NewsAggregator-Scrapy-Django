FROM python:3.8

WORKDIR /app

COPY requirements.txt /tmp
COPY . /app

RUN apt-get update && apt-get -y upgrade && \
    pip install --upgrade pip

RUN pip install -r /tmp/requirements.txt --no-cache-dir

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000
