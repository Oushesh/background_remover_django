# syntax=docker/dockerfile:1
FROM python:3.8.9
ARG PORT=8000
LABEL maintainer="oushesh"
ENV PYTHONUNBUFFERED 1

WORKDIR /config
COPY requirements.txt /config/

RUN apt update && \
	apt install build-essential && \
	rm -rf /var/cache/apk/* && \
	pip install --upgrade pip && \
	pip install --no-cache-dir -r requirements.txt

COPY . /config/

RUN chmod a+x /config/dev-docker-entrypoint.sh
ENTRYPOINT ["/config/dev-docker-entrypoint.sh"]

