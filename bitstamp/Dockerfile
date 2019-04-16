FROM python:3.8.0a3-alpine3.9
MAINTAINER Semen Koretskiy <semenmsu@gmail.com>
RUN mkdir /app && mkdir /data && pip install websocket-client
WORKDIR /app
COPY src /app
ENV APP_ENV "dev"
CMD python3 dump_data.py
