FROM python:3-alpine
WORKDIR /app
RUN apk update \
  && apk add gcc musl-dev linux-headers \
    libffi-dev openssl-dev make bash \
  && pip install fabric \
  && rm -rf /var/cache/apk/*
COPY ./ ./
ENTRYPOINT ["fab"]