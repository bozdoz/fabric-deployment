FROM python:3.8.0-alpine
RUN apk update \
  && apk add \
  gcc \
  musl-dev \
  linux-headers \
  libffi-dev \
  openssl-dev \
  make \
  bash \
  openssh \
  && pip install fabric==2.5.0 \
  && rm -rf /var/cache/apk/*
WORKDIR /app
COPY ./*.py ./
