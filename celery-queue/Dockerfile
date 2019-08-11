#FROM python:3.6-alpine
FROM python:3.6-slim
#FROM continuumio/miniconda3

ENV PYTHONPATH /queue 
ENV CELERY_BROKER_URL redis://redis:6379/0
ENV CELERY_RESULT_BACKEND redis://redis:6379/0
ENV C_FORCE_ROOT true
COPY . /queue
WORKDIR /queue
RUN mkdir -p output logs && pip install -r requirements.txt
ENTRYPOINT celery -A tasks worker --loglevel=info