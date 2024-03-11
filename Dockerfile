FROM python:3.9-slim-buster
LABEL org.opencontainers.image.authors="uniquequeue@gmail.com"

ENV LANG ja_JP.UTF-8
ENV LANG C.UTF-8
ENV LANGUAGE en_US:

RUN apt update && apt -y install ghostscript ocrmypdf tesseract-ocr-jpn && rm -rf /var/lib/apt/lists/*

COPY ./app /app

WORKDIR /app