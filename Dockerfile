FROM python

RUN pip install behave

COPY . /usr/src/app
WORKDIR /usr/src/app/features
