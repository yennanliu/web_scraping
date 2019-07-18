FROM continuumio/miniconda3

LABEL maintainer "yennj12"

ENV HOME /
WORKDIR $HOME
COPY . $HOME

RUN pip install --upgrade pip && \
pip install -r requirements.txt && \ 
pwd && ls && ls home   

RUN /bin/bash -c "python cron_test.py"
