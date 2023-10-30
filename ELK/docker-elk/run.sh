#!/bin/bash

sudo docker-compose stop ; sudo docker-compose rm -f ; sudo docker-compose build ; docker-compose up setup ; sudo docker-compose up

