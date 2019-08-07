FROM python:3.6-alpine

LABEL maintainer "yennj12"

ENV PYTHONPATH /app
ENV CELERY_BROKER_URL redis://redis:6379/0
ENV CELERY_RESULT_BACKEND redis://redis:6379/0
ENV C_FORCE_ROOT true
ADD requirements.txt /app/requirements.txt
ADD ./test_celery/ /app/
WORKDIR /app/
RUN pip install -r requirements.txt
ENTRYPOINT celery -A task  worker --loglevel=info  