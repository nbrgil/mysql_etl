################
# Base Development file Development Docker File
################

FROM python:3.6
MAINTAINER Rodrigo Gil

RUN apt-get update && \
  apt-get install -y build-essential \
    libmysqlclient-dev \
    postgresql-server-dev-all \
    mysql-client \
    redis-tools \
    libxml2-dev \
    libxslt-dev \
  && pip install pandas sqlalchemy pymysql mysqlclient \
  && rm -rf $HOME/.cache \
  && apt-get purge -y python.* \
  && apt-get autoremove -y \
  && apt-get clean
