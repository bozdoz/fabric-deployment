FROM python:3.12-alpine3.19

RUN pip install fabric==3.2.2

WORKDIR /app

COPY ./*.py ./

# wrap fab so that we always reference workdir
RUN mv /usr/local/bin/fab /usr/local/bin/_fab \
  && echo -e '#!/bin/sh\n_fab -r /app "$@"' > /usr/local/bin/fab \
  && chmod +x /usr/local/bin/fab
