#!/bin/sh

# Stop on error.
set -e

# Define file names.
CRONFILE="/tmp/cronjobs.txt"
APP_DIR="/home/ec2-user/"

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


# Set up cron job to destroy and rebuild entire application infra every hour on the hour.
if crontab -l | grep -q `tear_down`; then
    echo "Cron job already exists."
else
    crontab -l > "$CRONFILE" 2>/dev/null || true
    {
        echo "0 * * * * cd /home/ec2-user/clown-concrete && ./tear_down.sh  && docker-compose up"
    } >> "$CRONFILE"
    crontab "$CRONFILE"
    rm -f "$CRONFILE"
fi

# Start application infra.
cd "$APP_DIR" || exit
docker-compose up -d || true

echo "Installation complete."
