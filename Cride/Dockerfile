FROM python:3.5

ARG DJANGO_ENV

ENV PYTHONUNBUFFERED=1
ENV WEB_DIR=/Cride

RUN mkdir $WEB_DIR

WORKDIR $WEB_DIR

ADD requirements/base.txt $WEB_DIR/  
ADD requirements/$DJANGO_ENV.txt $WEB_DIR/

RUN pip3 install -r $DJANGO_ENV.txt
# create unprivileged user
RUN adduser --disabled-password --gecos '' myuser 

ADD . $WEB_DIR/  
