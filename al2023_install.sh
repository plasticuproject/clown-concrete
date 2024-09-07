#!/bin/sh

# Stop on error.
set -e

# Define file names.
CRONFILE="/tmp/cronjobs.txt"
APP_DIR="/home/ec2-user"
TEAR_DOWN_SCRIPT="$APP_DIR/clown-concrete/tear_down.sh"

# Ensure the script is run as root
if [ "$(id -u)" -ne 0 ]; then
    echo "This script must ne run as root"
    exit 1
fi

# Install, set up, and start docker servive and docker-compose.
dnf -y update
dnf -y install docker
usermod -a -G docker ec2-user
systemctl enable docker.service
systemctl start docker.service
curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s | tr '[:upper:]' '[:lower:]')-$(uname -m) -o /usr/bin/docker-compose 
chmod 755 /usr/bin/docker-compose 
docker-compose --version

# Install and start crond service.
dnf -y install cronie
systemctl start crond
systemctl enable crond


# Install certbot
dnf -y install python3 augeas-libs
dnf -y remove certbot
python3 -m venv /opt/certbot/
/opt/certbot/bin/pip install --upgrade pip
/opt/certbot/bin/pip install certbot
ln -s /opt/certbot/bin/certbot /usr/bin/certbot
certbot certonly --standalone -m joey@clownconcrete.com --agree-tos -d clownconcrete.plasticuproject.com
echo "cp /etc/letsencrypt/live/clownconcrete.plasticuproject.com/privkey.pem /home/ec2-user/clown-concrete/nginx/certs/private.key" >> "$TEAR_DOWN_SCRIPT"
echo "cp /etc/letsencrypt/live/clownconcrete.plasticuproject.com/cert.pem /home/ec2-user/clown-concrete/nginx/certs/publickey.crt" >> "$TEAR_DOWN_SCRIPT"


# Set up cron job to destroy and rebuild entire application infra every hour on the hour.
if crontab -l | grep -q `tear_down`; then
    echo "Cron job already exists."
else
    crontab -l > "$CRONFILE" 2>/dev/null || true
    {
        echo "0 * * * * cd /home/ec2-user/clown-concrete && ./tear_down.sh  && docker-compose up"
	echo "0 0,12 * * * /opt/certbot/bin/python -c 'import random; import time; time.sleep(random.random() * 3600)' && sudo certbot renew -q"
    } >> "$CRONFILE"
    crontab "$CRONFILE"
    rm -f "$CRONFILE"
fi

# Start application infra.
cd "$APP_DIR"
docker-compose up -d

echo "Installation complete."
