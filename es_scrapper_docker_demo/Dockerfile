FROM python:3.6-alpine

ENV ESLATICSEARCH_URL http://localhost:9200/

ADD requirements.txt /app/requirements.txt
ADD . /app/
WORKDIR /app/
RUN pip install -r requirements.txt
ENTRYPOINT python app.py 