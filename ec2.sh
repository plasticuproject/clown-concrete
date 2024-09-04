#!/bin/sh

yum update
yum install docker
usermod -a -G docker ec2-user
systemctl enable docker.service
systemctl start docker.service
curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s | tr '[:upper:]' '[:lower:]')-$(uname -m) -o /usr/bin/docker-compose && sudo chmod 755 /usr/bin/docker-compose && docker-compose --version
yum install cronie
sudo systemctl start crond
sudo systemctl enable crond

# Run `crontab -e` and add:
# `0 * * * * cd /home/ec2-user/clown-concrete && ./tear_down.sh  && docker-compose up`
# Then run docker-compose up -d

