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

# wrap fab so that we always reference workdir
RUN mv /usr/local/bin/fab /usr/local/bin/_fab \
  && echo -e '#!/bin/sh\n_fab -r /app "$@"' > /usr/local/bin/fab \
  && chmod +x /usr/local/bin/fab
