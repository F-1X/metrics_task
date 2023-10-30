ARG ELASTIC_VERSION

FROM elastic/filebeat:${ELASTIC_VERSION:-8.10.2}

USER root

RUN mkdir /app

RUN chmod 777 /app

RUN mkdir /app/nginx

RUN chmod 777 /app/nginx

RUN mkdir /app/mysql

RUN chmod 777 /app/mysql
