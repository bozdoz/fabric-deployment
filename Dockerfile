FROM python:3-alpine
RUN apk update \
  && apk add gcc musl-dev linux-headers \
    libffi-dev openssl-dev make bash \
  && pip install fabric \
  && rm -rf /var/cache/apk/*
COPY ./fabfile.py ./
