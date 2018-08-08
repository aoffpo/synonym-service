#!/bin/bash
echo Building image and installing app dependencies...
CONTAINER_NAME=synapp
docker build --no-cache -t $CONTAINER_NAME .
docker run --rm -p 8000:8000 $CONTAINER_NAME