#!/bin/sh

docker stop clown-concrete-nginx-proxy-1 clown-concrete-flask-app-1 clown-concrete-pypiserver-authenticated-1
docker rm clown-concrete-nginx-proxy-1 clown-concrete-flask-app-1 clown-concrete-pypiserver-authenticated-1
docker rmi clown-concrete-nginx-proxy clown-concrete-flask-app pypiserver/pypiserver:v1.5.1
docker volume prune -f

#cp /etc/letsencrypt/live/clownconcrete.plasticuproject.com/privkey.pem /home/ec2-user/clown-concrete/nginx/certs/private.key
#cp /etc/letsencrypt/live/clownconcrete.plasticuproject.com/cert.pem /home/ec2-user/clown-concrete/nginx/certs/publickey.crt

