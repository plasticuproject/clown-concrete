#!/bin/sh

yum update
yum install docker
usermod -a -G docker ec2-user
systemctl enable docker.service
systemctl start docker.service
curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s | tr '[:upper:]' '[:lower:]')-$(uname -m) -o /usr/bin/docker-compose && sudo chmod 755 /usr/bin/docker-compose && docker-compose --version 
