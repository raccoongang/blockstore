# Dockerfile

FROM python:3.5.7-alpine3.9

ENV VIRTUAL_ENV=/blockstore/venv

RUN apk update && apk upgrade
RUN apk add bash bash-completion build-base git perl mariadb-dev libffi-dev

RUN python3.5 -m venv $VIRTUAL_ENV

RUN echo 'cd /blockstore/app/' >> ~/.bashrc
RUN echo 'export PATH=$VIRTUAL_ENV/bin:$PATH' >> ~/.bashrc
