#!/bin/sh

docker rm clown-concrete-nginx-proxy-1 clown-concrete-flask-app-1 clown-concrete-pypiserver-authenticated-1
docker rmi clown-concrete-nginx-proxy clown-concrete-flask-app pypiserver/pypiserver:v1.5.1
